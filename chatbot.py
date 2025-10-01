import ollama
import numpy as np

# --- INITIAL SETUP ---
# Define the models to be used
EMBEDDING_MODEL = 'nomic-embed-text:v1.5'
LLM_MODEL = 'gemma:2b'

# Name of the knowledge base file
KNOWLEDGE_BASE_FILE = 'biology.txt'

# Global variable to store the processed data
processed_chunks = []

def process_knowledge_base():
    """
    Reads the text file, splits it into chunks, generates embeddings for each,
    and stores them in memory. This is a pre-processing step.
    """
    global processed_chunks
    try:
        with open(KNOWLEDGE_BASE_FILE, 'r', encoding='utf-8') as f:
            # Reads the file content
            content = f.read()
            # Splits the text by new lines, treating each line as a "document"
            chunks = content.strip().split('\n')

            print(f"Processing {len(chunks)} chunks from the document...")

            for chunk in chunks:
                if chunk.strip(): # Ignore empty lines
                    # Generate the embedding for the text chunk
                    embedding = ollama.embeddings(
                        model=EMBEDDING_MODEL,
                        prompt=chunk
                    )['embedding']
                    
                    # Store the original text and its corresponding embedding
                    processed_chunks.append({
                        'text': chunk,
                        'embedding': np.array(embedding)
                    })
            print("Knowledge base processed successfully!")

    except FileNotFoundError:
        print(f"Error: File '{KNOWLEDGE_BASE_FILE}' not found.")
        exit()


def find_relevant_context(user_question, top_k=2):
    """
    Finds the 'top_k' most relevant chunks for the user's question.
    """
    if not processed_chunks:
        return ""

    # 1. Generate the embedding for the user's question
    question_embedding = np.array(ollama.embeddings(
        model=EMBEDDING_MODEL,
        prompt=user_question
    )['embedding'])

    # 2. Calculate the cosine similarity between the question and all chunks
    # Cosine similarity is a good metric to compare vectors
    similarities = []
    for chunk in processed_chunks:
        # The dot product of normalized vectors is the cosine similarity
        sim = np.dot(question_embedding, chunk['embedding']) / (np.linalg.norm(question_embedding) * np.linalg.norm(chunk['embedding']))
        similarities.append(sim)

    # 3. Find the indices of the most similar chunks
    most_relevant_indices = np.argsort(similarities)[-top_k:][::-1]

    # 4. Join the texts of the most relevant chunks to form the context
    context = "\n".join([processed_chunks[i]['text'] for i in most_relevant_indices])
    return context


def chatbot():
    """
    Main function that runs the user interaction loop.
    """
    print("--- Educational Marine Biology Chatbot ---")
    print("Hello! Ask a question about marine biology or type 'exit' to quit.")

    while True:
        # Allows interaction in the terminal
        question = input("\nYou: ").strip()

        # Allows the user to end the conversation
        if question.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break

        # Step 1: Find the relevant context in the knowledge base
        relevant_context = find_relevant_context(question)

        # Step 2: Build the prompt for the generative 
        system_prompt = f"""
        You are an educational assistant. Use ONLY the context provided below to answer the user's question.
        Your answer should be short, simple, didactic, and objective, ideal for a learner and **always use emoji**.
        If the answer is not in the context, say "Sorry, I do not have information about that in the provided material."."""
        
        final_prompt = f"""**Context:**
        {relevant_context}

        **Question:**
        {question}

        **Answer:**
        """

        # Step 3: Call the generative model (LLM) to get the final answer
        print("Chatbot: Thinking...")
        
        # Using ollama.chat for a conversational format
        response = ollama.chat(
            model=LLM_MODEL,
            messages=[
                {'role': 'system', 'content': system_prompt},
                {'role': 'user', 'content': final_prompt}
            ]
        )
        
        # Print the chatbot's answer
        print(f"Chatbot: {response['message']['content']}")


if __name__ == "__main__":
    # Pre-process the knowledge base once at the start
    process_knowledge_base()
    # Start the chatbot
    chatbot()