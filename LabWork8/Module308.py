def split_sentences(text):
    for s in text.split("."):
        if s:
            print(s+".")