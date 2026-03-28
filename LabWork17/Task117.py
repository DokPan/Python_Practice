import clr
import os
clr.AddReference(r"C:\Temp\!_ispp3445\LibraryPython\LibraryPython\bin\Debug\LibraryPython.dll")

from LibraryPython import LibraryClass

fw = LibraryClass()

fw.CreateFile("test.txt", "Привет из Python!")

content = fw.ReadFile("test.txt")
print("Содержимое:", content)

fw.AppendFile("test.txt", " Добавлено через C#.")

content = fw.ReadFile("test.txt")
print("После добавления:", content)

fw.DeleteFile("test.txt")
