<h2>Document-Based Question Answering with Chat Models</h2>

This project focuses on implementing a pipeline for answering questions based on documents using chat models and retrieval techniques. The code loads PDF files, converts them into text fragments, and creates vector representations using OpenAI's embeddings. It then performs similarity searches and uses a chat model (GPT-3.5-turbo) to answer questions.

The main steps of the pipeline are:

1. Loading PDF files and converting them into text fragments.
2. Creating vector representations of the text fragments.
3. Performing a similarity search to retrieve relevant documents.
4. Utilizing a chat model for question-answering, both with and without context from retrieved documents.
5. Implementing a memory component to store previous conversations.

The project leverages OpenAI's chat models and vector representations to provide concise and accurate answers to questions, demonstrating the integration of AI language models into real-world applications.
