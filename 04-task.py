"""
 Create a function that takes a sentence and prints the sentence without duplicated words

"""

"""def removeduplicated( sentence):
    words=sentence.split('')
    s=[]
   
    for n in words:
        if n not in s:
            s.append(n)
    print(''. join(s))
ss =input("Ffdfdf'd")
removeduplicated(ss)  
s = input("enter sentence:")
w =[]
for x in      
"""
from collections import Counter 
def remove_duplicate(s):

    s = s.split(" ")
    word_dic = Counter(s)
    result = " ".join(word_dic.keys())
    print (result)
 
st = 'There are two  d d d d d d children children playing in the park'
remove_duplicate(st)