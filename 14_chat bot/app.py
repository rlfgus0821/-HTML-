import openai
import os
from pprint import pprint

client = openai.OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
model ='gpt-3.5-turbo'
response = client.chat.completions.create(model=model,
                               messages=[{'role':'user',
                                          'content':'Hi'}]).model_dump()
pprint(response)