

import string, re
from time import time


t1 = time()          #timer starts

d = {}
dict = file("dictionary.txt",'r')              #you want to open your external dictionary

for line in dict:              #recreates dictionary
      l = line.split()          #create list of words
      count = 0
      for word in l:
                   
          if count == 0:             #if it is the first word
               backup = word        #store it in backup variable
          else:
               d[backup] = word             #assigns word to key to recreate dictionary
          count += 1                        #increment count variable, so we now refer to the second word and the 'else' bracket.
      count = 0                                #the next loop we count from 0 to 1 again.
          
dict.close()








#fname = raw_input("Enter the filename: ")
newfile = open(raw_input("Enter the filename: "),'r')        #Enter file to be converted

t = time()  #start another timer

input = ''

rebuilt = ''

for l2 in newfile:
     l4 = l2.split()
     for w in l4:
       
          input = d.get(w,None)                       #search the word in the imported exported dictionary          
          rebuilt += str(input) + " "              #recreate file with correct words
     rebuilt += '\n'         
#print rebuilt
newfile.close()

writtenfile = open("finaloutput2.txt",'w')               #write to outputfile
writtenfile.write(rebuilt)
writtenfile.close()

t2 = time()         #final timer
print 'time taken since the program started is ',(t2 - t1) ,' seconds'            #calculate time taken by subtracting the end time from the start time.

print 'time taken since the filename was entered is ', (t2 - t) ,' seconds'

