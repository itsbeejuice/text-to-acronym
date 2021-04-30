words=input("please enter your words that you want to make into an acronym here: ")

def acronym(words):
    words=words.split()
    string=""
    for word in words:
        if words!="and":
            string+=str(word[0])
    return string.upper()
result=acronym(words)
print(result)
