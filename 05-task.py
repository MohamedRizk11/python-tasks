"""

Create a function that takes a sentence and prints how many words in the sentence (do not count the
spaces)

"""
def countwords(sentence):
    words=sentence.split(" ")
    notfon=[]
    sss=sum(len(n) for n in words )

    print(sss)

result=str(input("inter your sentance : "))
countwords(result)  