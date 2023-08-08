
  <h1>Conversational QA with Contextual Memory using langchain</h1>
  <p>This repository contains code for performing conversational question answering using contextual memory and advanced language models. The code utilizes the langchain library to process PDF documents, split them into chunks, and create embeddings for efficient similarity search. It then employs OpenAI's GPT-3.5 Turbo for generating responses and maintaining conversational context.</p>

  <h2>Features:</h2>
  <ul>
      <li>Load PDF documents and split them into chunks for processing.</li>
      <li>Generate vector embeddings using OpenAI's GPT-3.5 Turbo.</li>
      <li>Conduct similarity search to retrieve relevant chunks for a given question.</li>
      <li>Utilize a prompt template to guide answers based on contextual information.</li>
      <li>Maintain conversational memory for more coherent and context-aware responses.</li>
  </ul>

  <h2>Usage:</h2>
  <ol>
      <li>Set your OpenAI API key by assigning it to the 'OPENAI_API_KEY' environment variable.</li>
      <li>Specify the path to the PDF file using the 'pdffilepath' variable.</li>
      <li>Load PDF files and split them into smaller documents.</li>
      <li>Create vector embeddings using Chroma and OpenAI Embeddings.</li>
      <li>Perform a similarity search to retrieve relevant document chunks for a given question.</li>
      <li>Generate answers using the retrieval-based QA model and GPT-3.5 Turbo.</li>
      <li>Maintain conversation history using the 'ConversationBufferMemory' class.</li>
      <li>Conduct conversational QA with context using 'ConversationalRetrievalChain'.</li>
  </ol>

  <p><strong>Note:</strong></p>
  <ul>
      <li>Replace 'INSERTKEYHERE' with your actual OpenAI API key.</li>
      <li>Replace 'INSERTPDFFILEPATH' with the path to your PDF file.</li>
      <li>Modify the 'question' variable to the desired question for QA.</li>
  </ul>

  <p>Feel free to customize and extend the code for your specific use case. Enjoy contextually rich conversational QA with the power of langchain and advanced language models!</p>
</html>
