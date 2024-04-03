from langchain_openai import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat = ChatOpenAI(
  model="gpt-3.5-turbo",
)

result = chat.invoke(
  [
    SystemMessage(content="私は優秀なソフトウェアエンジニアです。"),
    HumanMessage(content="Langchainについて説明してください。"),
  ]
)
print(result.content)
