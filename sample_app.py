import chainlit as cl
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage

chat = ChatOpenAI(
  model="gpt-3.5-turbo",
)

@cl.on_chat_start
async def on_chat_start():
  await cl.Message(content="こんにちは。私はAIです。質問をしてください。").send()

@cl.on_message
async def on_message(input_message):
  print("Received message: ", input_message)

  result = chat([
    HumanMessage(content=input_message),
  ])
  await cl.Message(content=result.content).send()
