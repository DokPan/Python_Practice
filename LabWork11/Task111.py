import re

text= "Я люблю котиков!А КОТИКИ ЛЮБЯТ МЕНЯ?Абсолютно.А вы что думали…"

for s in re.split(r'(?<=[.!?…])',text):
    if s:
     print(s)