s1=input("enter the string")
charactercount=0
wordcount=1
for i in s1:
    charactercount=charactercount+1
    if(i == ' '):
        wordcount=wordcount+1
print("number of words in the string")
print(wordcount)
print("number of character in the string")
print(charactercount)
