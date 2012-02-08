import re

file = raw_input("Enter the expression: ")

sms = file.lower()

newstring = ''
num = ''


newsms = ''

list = re.split(' ',sms)                   #create a word list using regex split funtion
           

flag = ''

for word in list:                     #iterate through list
    backup = ''
    for ch in word:                   #remove double letter
        if ch == backup:
            word = re.sub(ch,"",word,count = 1)            #replace double letter with an empty space
        backup = ch
        
                   
    if re.search(word[-2],"'"):       #if the word is apostrophe'd - take it out (next line)
         word = re.sub(word[-2],"",word,count = 1)
        #word = word[0:-2] + word[-1]
    if re.search(word[-1],'?.,!;'):   #if there is a punctuation mark at end of word: chop it off   [problem -compiler cant deal with ?-mark]
        newword = word[:-1]
        #newword = re.sub(word[-1],'',ch, count = 1)
        flag = ''
        if len(newword) <= 2:             #we dont edit words not longer than 2 characters, apart from the punctuation marks we've removed.
             newsms += newword + ' ' 
             #print '1.',newsms
             flag = 'true'
    else:
        newword = word
        
    if flag <> 'true':                    #we dont want to add the same word twice
         if len(newword) <= 2:
             newsms += newword + ' '
             #print '2' ,newsms         
    
         else:          
             for ch in newword[:-1]:       #leave last char value out because we dont chop vowels off the end of words
        
                 #if ch not in ['a','e','o','i','u']:
                 if re.search(ch,"aeoiu") == None:     # if the character value is not a vowel
                      newsms += ch                     # we can add it to the string           
        
             newsms += newword[-1] + ' '            # add the last value whether it is a vowel or not.
         #print '3', newsms

print newsms



"""
#possible shorter method, though incomplete, could possibly solve with one very complex regular expression:
import re

string = " Hello,? how are you doing! i'd like.."
sms = string.lower()
nsms = re.sub("[.!?,:;'aouie]",'',sms)

print nsms

"""
