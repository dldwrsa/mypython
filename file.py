
import string, re
from time import time

t1 = time()
filename = raw_input("Please enter the filename: ")
file = open(filename,'r')
f = open('outputfile.txt','w')

string = ''
d = {}

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

         
         d[nword] = new_word
         
     
     string += '\n'

f.write(string)
#print string
f.close()



input = ''
fullfile = ''
rebuilt = ''
newfile = open('outputfile.txt','r')

for l2 in newfile:
     l4 = l2.split()
     for w in l4:
          
          input = d.get(w,None)
          #print input + ' ',
          rebuilt += str(input) + " "

writtenfile = open("finaloutput.txt",'w')
writtenfile.write(rebuilt)
writtenfile.close()
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
