from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from prompt import get_rag_prompt
from dotenv import load_dotenv
load_dotenv()

def get_rag_review(user_code:str) -> str:
    vectorstore = Chroma(
        persist_directory="chroma_index",
        embedding_function=OpenAIEmbeddings()
    )

    retriever = vectorstore.as_retriever(search_kwags={"k":4})
    retrieved_docs = retriever.get_relevant_documents(user_code)

    context = "\n---\n".join(doc.page_content for doc in retrieved_docs)
    
    final_prompt = get_rag_prompt(context=context, code = user_code)

    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)
    response = llm.invoke(final_prompt)

    return {
        "review":response.content,
        "sources":[doc.page_content for doc in retrieved_docs]
    }
    