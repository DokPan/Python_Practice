import Module108
from Module208 import perevod
from Module308 import split_sentences
from Module408 import cesar
from Module508 import bit_operations

Module108.hello()
Module108.hello("Полина")

print(perevod(10,2))
print(perevod(10,8))
print(perevod(10,16))

print(split_sentences("Я люблю котиков.Котики любят меня.Весь мир любит котиков."))

print(cesar("привет"))
print(cesar("привет",5))

bit_operations(5,3)