import os
from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain



# Set path and openAI-Key
os.environ['OPENAI_API_KEY'] = "INSERTKEYHERE"
pdffilepath = "INSERTPDFFILEPATH"

# Load pdf-files
loader = PyPDFDirectoryLoader(pdffilepath)
data = loader.load()

# Convert pdf files to splitted documents
text_splitter = RecursiveCharacterTextSplitter(chunk_size = 500, chunk_overlap = 0)
all_splits = text_splitter.split_documents(data)

# Create vectorstore
vectorstore = Chroma.from_documents(documents=all_splits, embedding=OpenAIEmbeddings())

question = "QUESTION"

# Do similarity search for the vectorstore
docs = vectorstore.similarity_search(question)
print(docs)

# Answer question without prompt template
llm = ChatOpenAI(model_name = "gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(llm, retriever = vectorstore.as_retriever())
qa_chain = ({"query": question})

print(qa_chain)

# Create the prompt template with context retrived from the vectorstore
template = """Use the following pieces of context to answer the question at the end. 
If you don't know the answer, just say that you don't know, don't try to make up an answer. 
Use three sentences maximum and keep the answer as concise as possible. Always answer in German.
{context}
Question: {question}
Helpful Answer:"""
QA_CHAIN_PROMPT = PromptTemplate.from_template(template)

# Define the chat model
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0)
qa_chain = RetrievalQA.from_chain_type(
    llm,
    retriever=vectorstore.as_retriever(),
    chain_type_kwargs={"prompt": QA_CHAIN_PROMPT}
)

# Just the answer (without memory)
result = qa_chain({"query": question})
result["result"]

# Answer with memory of the previous conversation
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

retriever = vectorstore.as_retriever()
chat = ConversationalRetrievalChain.from_llm(llm, retriever=retriever, memory=memory)

result = chat({"question": question})
result['answer']