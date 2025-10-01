# Educational Marine Biology Chatbot 🌊🐠

Welcome to the Educational Chatbot repository! This project is an interactive terminal chatbot designed to answer questions about marine biology clearly and didactically, using the power of Large Language Models (LLMs) running locally with Ollama.

This project was developed as part of an Artificial Intelligence course.

## Demo 🖥️

Here is an example of an interaction with the chatbot:

```
--- Educational Biology Chatbot ---
Hello! Ask a question about biology or type 'exit' to quit.

You: what is echolocation?
Chatbot: Thinking...
Chatbot: Echolocation is a method used by animals like dolphins and some whales. They produce sounds that bounce off objects, which helps them find food or navigate through dark waters.

You: how are sharks different from other fish?
Chatbot: Thinking...
Chatbot: Sharks and rays are special because their skeletons are made of cartilage instead of bone, which makes them lighter and more flexible.

You: exit
Chatbot: Goodbye!
```

## Features 🌟

  * **Interactive Chat:** Converse with the bot directly from your terminal.
  * **100% Local:** Uses [Ollama](https://ollama.com/) to run the AI models locally, ensuring privacy with no API costs.
  * **Fact-Based Answers:** Implements the **RAG (Retrieval-Augmented Generation)** architecture to ensure answers are based on a provided text (`biology.txt`), preventing hallucinations.
  * **Flexible Knowledge Base:** It's easy to change or expand the chatbot's knowledge by simply editing the text file.

## Technologies Used 🛠️

  * **Language:** Python 3
  * **LLM Runner:** [Ollama](https://ollama.com/)
  * **Embedding Model:** `nomic-embed-text` (to vectorize the text)
  * **Generative Model:** `gemma:2b` (to generate the answers)
  * **Libraries:** `ollama-python`, `numpy`

## How It Works (RAG Architecture) 🧠

The chatbot doesn't "know" marine biology on its own. It uses a smart technique to answer questions based on your study material:

1.  **📚 Preprocessing:** On startup, the script reads the `biology.txt` file, splits it into paragraphs (chunks), and uses `nomic-embed-text` to turn each chunk into a numerical representation (a vector).
2.  **❓ User Question:** When you ask a question, it is also converted into a vector.
3.  **🔍 Search (Retrieval):** The system compares your question's vector with the chunk vectors to find the most relevant paragraphs from the original text.
4.  **✍️ Generation:** The chatbot sends the relevant paragraphs along with your original question to the `gemma:2b` model, with the instruction: "Use this context to formulate a simple and didactic answer."

This ensures the chatbot is an expert on the content *you* provided\!

## Setup and Installation 🚀

Follow the steps below to run the project on your machine.

### 1\. Prerequisites

  * [Python 3.8+](https://www.python.org/downloads/)
  * [Ollama](https://ollama.com/) installed and running.

### 2\. Clone the Repository

```bash
git clone https://github.com/carol-lanzu/chatbot_educacional.git
cd chatbot_educacional
```

### 3\. Install Dependencies

It's recommended to use a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the required libraries:

```bash
pip install ollama numpy
```

### 4\. Download the Ollama Models

Run the following commands in your terminal to download the necessary models:

```bash
ollama pull nomic-embed-text
ollama pull gemma:2b
```

## How to Use ▶️

1.  **Make sure the Ollama application is running** in the background.
2.  Run the main chatbot script:
    ```bash
    python chatbot.py
    ```
3.  Start asking questions\! To quit, type `exit`.

## Knowledge Base 📖

All of the chatbot's "knowledge" is in the `biology.txt` file. You can:

  * **Add more information:** Simply edit the file and add new paragraphs.
  * **Change the Topic:** Replace the content with a text about History, Physics, or any other subject\!

**Important:** Separate paragraphs with a **blank line** to ensure the system chunks them correctly.

-----

Made with ❤️ by **Carol**


# Chatbot Educacional sobre Biologia Marinha 🌊🐠

Bem-vindo(a) ao repositório do Chatbot Educacional! Este projeto é um chatbot interativo de terminal projetado para responder perguntas sobre biologia marinha de forma clara e didática, utilizando o poder dos Modelos de Linguagem (LLMs) rodando localmente com Ollama.

Este projeto foi desenvolvido como parte da disciplina de Inteligência Artificial.

## Demonstração 🖥️

Veja como é a interação com o chatbot:

```

--- Educational Biology Chatbot ---
Hello\! Ask a question about biology or type 'exit' to quit.

You: what is echolocation?
Chatbot: Thinking...
Chatbot: Echolocation is a method used by animals like dolphins and some whales. They produce sounds that bounce off objects, which helps them find food or navigate through dark waters.

You: how are sharks different from other fish?
Chatbot: Thinking...
Chatbot: Sharks and rays are special because their skeletons are made of cartilage instead of bone, which makes them lighter and more flexible.

You: exit
Chatbot: Goodbye!

```

## Funcionalidades 🌟

* **Chat Interativo:** Converse com o bot diretamente do seu terminal.
* **100% Local:** Utiliza o [Ollama](https://ollama.com/) para rodar os modelos de IA localmente, garantindo privacidade e sem custos de API.
* **Respostas Baseadas em Fatos:** Implementa a arquitetura **RAG (Retrieval-Augmented Generation)** para garantir que as respostas sejam baseadas em um texto de apoio (`biology.txt`), evitando alucinações.
* **Base de Conhecimento Flexível:** É fácil alterar ou expandir o conhecimento do chatbot simplesmente editando o arquivo de texto.

## Tecnologias Utilizadas 🛠️

* **Linguagem:** Python 3
* **LLM Runner:** [Ollama](https://ollama.com/)
* **Modelo de Embedding:** `nomic-embed-text` (para vetorizar o texto)
* **Modelo Generativo:** `gemma:2b` (para gerar as respostas)
* **Biblioteca:** `ollama-python`, `numpy`

## Como Funciona? (Arquitetura RAG) 🧠

O chatbot não "sabe" sobre biologia marinha por si só. Ele usa uma técnica inteligente para responder com base no seu material de estudo:

1.  **📚 Pré-processamento:** Ao iniciar, o script lê o arquivo `biology.txt`, divide-o em parágrafos (chunks) e usa o `nomic-embed-text` para transformar cada chunk em uma representação numérica (vetor).
2.  **❓ Pergunta do Usuário:** Quando você faz uma pergunta, ela também é transformada em um vetor.
3.  **🔍 Busca (Retrieval):** O sistema compara o vetor da sua pergunta com os vetores dos chunks e encontra os parágrafos mais relevantes do texto original.
4.  **✍️ Geração (Generation):** O chatbot envia os parágrafos encontrados junto com a sua pergunta original para o modelo `gemma:2b`, com a instrução: "Use este contexto para formular uma resposta simples e didática".

Isso garante que o chatbot seja um especialista no conteúdo que *você* forneceu!

## Configuração e Instalação 🚀

Siga os passos abaixo para rodar o projeto na sua máquina.

### 1. Pré-requisitos
* [Python 3.8+](https://www.python.org/downloads/)
* [Ollama](https://ollama.com/) instalado e em execução.

### 2. Clone o Repositório
```bash
git clone https://github.com/carol-lanzu/chatbot_educacional.git
cd chatbot_educacional
````

### 3\. Instale as Dependências

Instale as bibliotecas necessárias:

```bash
pip install ollama numpy
```

### 4\. Baixe os Modelos do Ollama

Execute os seguintes comandos no seu terminal para baixar os modelos necessários:

```bash
ollama pull nomic-embed-text
ollama pull gemma:2b
```

## Como Usar ▶️

1.  **Certifique-se de que o Ollama está rodando** em segundo plano.
2.  Execute o script principal do chatbot:
    ```bash
    python chatbot.py
    ```
3.  Comece a fazer perguntas\! Para sair, digite `exit`.

## Base de Conhecimento 📖

Todo o "conhecimento" do chatbot está no arquivo `biology.txt`. Você pode:

  * **Adicionar mais informações:** Simplesmente edite o arquivo, adicionando novos parágrafos.
  * **Mudar o Tópico:** Substitua o conteúdo por um texto sobre História, Física, ou qualquer outro assunto\!

**Importante:** Separe os parágrafos com uma **linha em branco** para garantir que o sistema os divida corretamente.

-----

Feito com ❤️ por **Carol**

```
```
