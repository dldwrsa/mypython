

import string, re
from time import time              

t1 = time()                                          #timer commences
filename = raw_input("Please enter the filename: ")
t = time()  #after input timer

file = open(filename,'r')           #open the file to read from
f = open('outputfile.txt','w')      #open the outputfile to write to

string = ''
#d = {}                           #create dictionary

for line in file:                #iterate through file
        
     input_data = line
     input = input_data.lower()  #display input file in lowercase
     l = input.split()           #split into list of words
     
     for word in l:

         new_word = re.sub(r'([^A-Za-z0-9])','',word)      #for punctuation
    
         nnword = re.sub(r'([a-z])\1+',r'\1',new_word)     #for double characters
   

         nword = re.sub(r'\B[aeiou]\B','',nnword)    #for inner vowels
         string += nword + ' '

         
         #d[nword] = new_word     #create a dictionary with the words [though here we already have a dictionary]
         
     
     string += '\n'

f.write(string)

f.close()                    #file converted to sms speak



t2 = time()         #final timer
print 'time taken since the program started is ',(t2 - t1) ,' seconds'            #calculate time taken by subtracting the end time from the start time.

print 'time taken since the filename was entered is ', (t2 - t) ,' seconds'

'''
#fname = raw_input("Enter the filename: ")
#newfile = open(raw_input("Enter the filename: "),'r')

input = ''
fullfile = ''
rebuilt = ''
newfile = open('outputfile.txt','r')    #open output file

for l2 in newfile:
     l4 = l2.split()                    #create list of words to eliminate whitespace
     for w in l4:
          
          input = d.get(w,None)           #look up word
          #print input + ' ',
          rebuilt += str(input) + " "      #rebuild the original file (minus the punctiation and extra whitespace)

writtenfile = open("finaloutput.txt",'w')      
writtenfile.write(rebuilt)
writtenfile.close()
t2 = time()
print 'time taken is ',(t2 - t1) ,' seconds'



#This is used to print the dictionary to a file

dictionary = open("dictionary.txt",'w')        #open dictionary file
string = ''
for key in d:                              #iterate through dictionary
     string += key + " " + d[key] + '\n'         #build a file to write the dictionary to an other file

dictionary.write(string)                    #write to the file the dictionary for external use
dictionary.close()
'''

