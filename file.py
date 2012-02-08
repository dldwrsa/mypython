
import string, re
from time import time

t1 = time()
filename = raw_input("Please enter the filename: ")
file = open(filename,'r')

string = ''
for line in file:
    
#input_data = "This is? some hello ditto samp324le i'nput Ha;llo."       #just give input first, didn't have to prompt user
     input_data = line
     input = input_data.lower()
     l = input.split()

     for word in l:
         new_word = re.sub(r'([^A-Za-z0-9])','',word)      #for punctuation
    

         nnword = re.sub(r'([a-z])\1+',r'\1',new_word)     #for double characters
   

         nword = re.sub(r'\B[aeiou]\B','',nnword)
         string += nword + ' '
     string += '\n'

print string

t2 = time()
print 'time taken is ',(t2 - t1) ,' seconds'
'''
for word in input_data.split():
    newWord = ''
    for letter in word:
        if letter in string.ascii_letters + "0123456789":
            newWord += letter

    newnewWord = newWord[0]
    for letter in newWord[1:-1]:
        if not letter in "aeiouAEIOU":
            newnewWord += letter
    newnewWord += newWord[-1]

    finalWord = newnewWord[0]
    previousChar = newnewWord[0]
    for letter in newnewWord[1:]:
        if not letter == previousChar:
            finalWord += letter
        previousChar = letter

    print finalWord,
'''
