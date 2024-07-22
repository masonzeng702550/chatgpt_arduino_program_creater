from openai import OpenAI
from dotenv import load_dotenv
import os
import time

load_dotenv()
#api_key = os.environ["OPENAI_API_KEY"]
client = OpenAI()
#p=str(input(""))
completion = client.chat.completions.create(
  model="gpt-4o",
  messages=[
    {"role": "system", "content": "你是一個 Arduino 程式專家，以下是使用者的需求："+str(input("請輸入prompt: "))+"，請根據使用者需求給我 Arduino 程式碼，只回傳c語言程式碼部分，不需要任何說明，不要任何解釋，程式碼不要任何註解，開頭不要有任何c 或 cpp 或 arduino字眼出現。"}
  ]
)
message = completion.choices[0].message.content
print(message)
patha = str(time.time())
os.mkdir(patha)
with open(patha+"/"+patha+".ino","w")as f:
    f.write(message)
f.close
os.system("arduino-cli compile --fqbn arduino:avr:uno  "+str(patha))
os.system("arduino-cli upload --port COM3 --fqbn  arduino:avr:uno "+str(patha))
