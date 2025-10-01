import ollama
import numpy as np

# --- CONFIGURAÇÃO INICIAL ---
# Define os modelos que serão usados
MODELO_EMBEDDING = 'nomic-embed-text'
MODELO_LLM = 'gemma:2b'

# Nome do arquivo da base de conhecimento
ARQUIVO_CONHECIMENTO = 'biology.txt'

# Variáveis globais para armazenar os dados processados
chunks_processados = []

def processar_base_conhecimento():
    """
    Lê o arquivo de texto, divide em "chunks" (partes), gera embeddings para cada um
    e armazena em memória. Este é um passo de pré-processamento.
    """
    global chunks_processados
    try:
        with open(ARQUIVO_CONHECIMENTO, 'r', encoding='utf-8') as f:
            # Divide o texto por linhas, tratando cada linha como um "documento"
            conteudo = f.read()
            # Dividindo por parágrafos (duas quebras de linha) ou linhas
            chunks = conteudo.strip().split('\n')

            print(f"Processando {len(chunks)} trechos do documento...")

            for chunk in chunks:
                if chunk.strip(): # Ignora linhas vazias
                    # Gera o embedding para o chunk de texto
                    embedding = ollama.embeddings(
                        model=MODELO_EMBEDDING,
                        prompt=chunk
                    )['embedding']
                    
                    # Armazena o texto original e seu embedding correspondente
                    chunks_processados.append({
                        'texto': chunk,
                        'embedding': np.array(embedding)
                    })
            print("Base de conhecimento processada com sucesso!")

    except FileNotFoundError:
        print(f"Erro: Arquivo '{ARQUIVO_CONHECIMENTO}' não encontrado.")
        exit()


def encontrar_contexto_relevante(pergunta_usuario, top_k=2):
    """
    Encontra os 'top_k' chunks mais relevantes para a pergunta do usuário.
    """
    if not chunks_processados:
        return ""

    # 1. Gera o embedding para a pergunta do usuário
    embedding_pergunta = np.array(ollama.embeddings(
        model=MODELO_EMBEDDING,
        prompt=pergunta_usuario
    )['embedding'])

    # 2. Calcula a similaridade de cossenos entre a pergunta e todos os chunks
    # A similaridade de cossenos é uma boa métrica para comparar vetores
    similaridades = []
    for chunk in chunks_processados:
        # Produto escalar entre vetores normalizados é a similaridade de cossenos
        sim = np.dot(embedding_pergunta, chunk['embedding']) / (np.linalg.norm(embedding_pergunta) * np.linalg.norm(chunk['embedding']))
        similaridades.append(sim)

    # 3. Encontra os índices dos chunks mais similares
    indices_mais_relevantes = np.argsort(similaridades)[-top_k:][::-1]

    # 4. Concatena os textos dos chunks mais relevantes para formar o contexto
    contexto = "\n".join([chunks_processados[i]['texto'] for i in indices_mais_relevantes])
    return contexto


def chatbot():
    """
    Função principal que executa o loop de interação com o usuário.
    """
    print("--- Chatbot Educacional de Biologia ---")
    print("Olá! Faça uma pergunta sobre biologia ou digite 'sair' para encerrar.")

    while True:
        # Permite a interação no terminal
        pergunta = input("\nVocê: ").strip()

        # Permite que o usuário encerre a conversa
        if pergunta.lower() == 'sair':
            print("Chatbot: Até a próxima!")
            break

        # Passo 1: Encontrar o contexto relevante na base de conhecimento
        contexto_relevante = encontrar_contexto_relevante(pergunta)

        # Passo 2: Montar o prompt para o modelo generativo
        prompt_final = f"""
        Você é um assistente educacional. Use APENAS o contexto fornecido abaixo para responder à pergunta do usuário.
        Se a resposta não estiver no contexto, diga "Desculpe, não tenho informações sobre isso no meu material.".
        Sua resposta deve ser curta, simples, didática e objetiva, ideal para quem está aprendendo.

        **Contexto:**
        {contexto_relevante}

        **Pergunta:**
        {pergunta}

        **Resposta:**
        """

        # Passo 3: Chamar o modelo generativo (LLM) para obter a resposta final
        print("Chatbot: Pensando...")
        
        # Usando o ollama.chat para um formato de conversação
        response = ollama.chat(
            model=MODELO_LLM,
            messages=[
                {'role': 'user', 'content': prompt_final}
            ]
        )
        
        # Respostas coerentes com o contexto definido
        print(f"Chatbot: {response['message']['content']}")


if __name__ == "__main__":
    # Pré-processa a base de conhecimento uma vez no início
    processar_base_conhecimento()
    # Inicia o chatbot
    chatbot()