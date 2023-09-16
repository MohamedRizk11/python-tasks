"""
 Create a function that takes a sentence and prints the sentence without duplicated words

"""

def removeduplicate(sentence):
    words=sentence.split(" ")
    notfon=[]
    for n in words:
        if n not in notfon:
            notfon.append(n)

    print(" ".join(notfon))

result=str(input("inter your sentance : "))
removeduplicate(result)    