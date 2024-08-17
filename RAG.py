
import os
from langchain_chroma import Chroma
from langchain_community.embeddings import HuggingFaceBgeEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.retrievers.merger_retriever import MergerRetriever
from llms import llm

with open('/Users/nirbhaysedha/Desktop/walert/email_content.txt','r') as w:
        USER_QUERY=w.read()

def Inference(llm,USER_QUERY):
    model_name = "BAAI/bge-large-en"
    model_kwargs = {'device': 'cpu'}
    encode_kwargs = {'normalize_embeddings': False}

    hf = HuggingFaceBgeEmbeddings(
        model_name=model_name,
        model_kwargs=model_kwargs,
        encode_kwargs=encode_kwargs
    )
    print("Embedding Model Loaded..........")

    loader_un_sdg = PyPDFLoader("data.pdf")
    documents_un_sdg = loader_un_sdg.load()


    text_splitter_un_sdg = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    texts_un_sdg = text_splitter_un_sdg.split_documents(documents_un_sdg)

    un_sdg_store = Chroma.from_documents(texts_un_sdg, hf, collection_metadata={"hnsw:space": "cosine"}, persist_directory="store/un_sdg_chroma_cosine")

    load_un_sdg_store = Chroma(persist_directory="store/un_sdg_chroma_cosine", embedding_function=hf)

    retriever_un_sdg = load_un_sdg_store.as_retriever(search_type="similarity", search_kwargs={"k": 3})


    lotr = MergerRetriever(retrievers=[retriever_un_sdg])
    query=USER_QUERY
    retrived_docs=lotr.get_relevant_documents(query)

    context = "\n".join([doc.page_content for doc in retrived_docs])


    context=f"based on the provided context create a efficient and eror free content in a email format :- ( Email writing instructions :- as data is provided to you use email footer as **RMIT Univerity\n STUDENT CONNECT \n 0410885184\n email.com) and email header strats with Dear applicant name(catch applicant name from the context and fill that ), additionally make the email straightforward and reduce your halllucinations  {context}"
    message = llm(context)
    return message


message=Inference(llm,USER_QUERY)








