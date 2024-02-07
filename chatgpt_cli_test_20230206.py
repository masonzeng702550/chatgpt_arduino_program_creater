import os
from tkinter import N
import time
import openai

openai.api_key = "YOUR CHATGPT API KEY"
model_engine = "text-davinci-003"
prompt =str(input("請輸入prompt: "))+"只回傳程式碼部分"

completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

response = completion.choices[0].text
print(response)

patha = str(time.time())
os.mkdir(patha)
with open(patha+"/"+patha+".ino","w")as f:
    f.write(response)

os.system("arduino-cli compile --fqbn arduino:avr:uno  "+str(patha))
os.system("arduino-cli upload --port COM4 --fqbn  arduino:avr:uno "+str(patha))

#arduino程式，讓腳位13的LED閃爍，每隔0.3秒明滅1次
#arduino程式接在腳位9的喇叭發出la音調1秒，暫停2秒，無限循環
#Arduino code, the ultrasonic sensor tri is connected to pin 5, and the echo is connected to pin 4. Only when the ultrasonic detects that the distance is less than 10 cm, the buzzer at pin 9 will continue to emit tone La the following program: 0.3 seconds, Pause for 0.3 seconds,and reapt.
