from decouple import config
import openai

#pass api key from enviroment variables to variable API_KEY
API_KEY = config('OPENAI_KEY')

#stablish connection with openAI client
client = openai.OpenAI(api_key=API_KEY)

#wait for user message prompt
message = input ("Enter Your Message : ")

#send instance to chat completion api
response = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": message}
  ]
)
print(response.choices[0].message.content)
