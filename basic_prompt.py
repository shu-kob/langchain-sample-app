from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
  model="gpt-3.5-turbo",
)

result = chat(
  [
    HumanMessage(content="マグロを漢字に直してください。"),
  ]
)
print(result.content)
