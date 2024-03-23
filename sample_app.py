import chainlit as cl

@cl.on_chat_start
async def on_chat_start():
  await cl.Message(content="Hello, I am a sample app. How can I help you?").send()

@cl.on_message
async def on_message(input_message):
  print("Received message: ", input_message)
  await cl.Message(content="You said: " + input_message).send()
