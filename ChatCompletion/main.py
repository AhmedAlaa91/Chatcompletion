from decouple import config
import openai

API_KEY = config('OPENAI_KEY')

client = openai.OpenAI(api_key=API_KEY)

message = input ("Enter Your Message : ")

response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": message}
  ]
)
print(response.choices[0].message.content)