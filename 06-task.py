"""
Create a function that takes a sentence and word and remove the word from the sentence


"""
"""def removeword(sentence):
    words=sentence.split(" ")
    notfon=[]
    for n in words:
        if n in notfon:
            words.replace(n)
        else :
            notfon.append(n)
    print(notfon)            

result=str(input("inter your sentance : "))
removeword(result)    """
s = str(input("inter your sentance :"))
x = str(input("inter the word :"))
sy=s.replace(x,"")
print(sy)