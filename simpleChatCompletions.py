import os
from openai import OpenAI

client = OpenAI(
  # This is the default and can be omitted
  api_key=os.environ.get("OPENAI_API_KEY"),
)

chat_completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "私は優秀なソフトウェアエンジニアです。"},
    {"role": "user", "content": "kubernetesについて説明してください。"}
  ]
)

print(chat_completion.choices[0].message.content)
