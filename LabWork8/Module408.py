def cesar(s,k=3):
    alf ="абвгдеёжзийклмнопрстуфхцчшщъыьэюя"
    out =""
    for char in s:
        if char in alf:
            index= alf.find(char)
            new_index =(index +k)%33
            out += alf[new_index]
        else:
            out += char
    return out
