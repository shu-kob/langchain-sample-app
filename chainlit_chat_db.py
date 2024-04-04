import chainlit as cl
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain.prompts import PromptTemplate
from langchain.schema import HumanMessage
from langchain_community.vectorstores import Chroma

embeddings = OpenAIEmbeddings(
  model="text-embedding-ada-002"
)

chat = ChatOpenAI(model="gpt-3.5-turbo")

prompt = PromptTemplate(template="""文章を元に質問に答えてください。

文章:
{document}

質問: {query}
""", input_variables=["document", "query"])

database = Chroma(
  persist_directory="./.data",
  embedding_function=embeddings
)

@cl.on_chat_start
async def on_chat_start():
  await cl.Message(content="準備ができました！メッセージを入力してください！").send()

@cl.on_message
async def on_message(input_message: cl.Message):
  print("入力されたメッセージ: " + input_message.content)
  documents = database.similarity_search(input_message.content)

  documents_string = ""

  for document in documents:
    documents_string += f"""
  -------------------------
  {document.page_content}
  """

  result = chat([
    HumanMessage(content=prompt.format(document=documents_string, query=input_message.content))
  ])
  await cl.Message(content=result.content).send()
