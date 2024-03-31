import openai

response = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "私は優秀なシステムエンジニアです。"},
    {"role": "user", "content": "オブジェクト指向について説明してください。"}
  ]
)

print(response)
