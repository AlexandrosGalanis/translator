#Alexandros Galanis icsd14027
print("Welcome !")
wordlist = {'English':'Agglika'}#we make our word directory as key the english word

fin = open("C:\\Users\\AlexanderDT\\Desktop\\codingfast\\advanced topics pl\\Assignment 2\\dict.txt","a+")#in case that there is no file we make one
fin.close()

fin = open("C:\\Users\\AlexanderDT\\Desktop\\codingfast\\advanced topics pl\\Assignment 2\\dict.txt","r+")#then we read the file

for i in fin:#we add each word of the file to our directory
    word = i.strip().split(",")
    wordlist[word[0]]=word[1]

print (wordlist)
fin.close()

fin = open("C:\\Users\\AlexanderDT\\Desktop\\codingfast\\advanced topics pl\\Assignment 2\\dict.txt","a+")#we are ready to write into the file

inputchoice = input('Press 1 for add a new word or 2 for search of word: ')

if inputchoice == "1":#add
    inputenglishword = input('Write the english word: ')
    inputgreekword = input('Write the translation:')
    wordlist[inputenglishword]=inputgreekword
    fin.write(inputenglishword+","+inputgreekword+"\n")

elif inputchoice == "2":#search

    search = input('Write the english word: ')
    exist ="false"
    for x in wordlist:
        if search == x: 
            exist="true"
            break
        
    if exist == "true":
        print(wordlist[x])
    else:
        print("There is no such word in this dictionary")

fin.close()
