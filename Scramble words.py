from random import randint

def Main() :
    userSentence = input("Enter a string (or blank to quit):")
    while userSentence != "" :
        print(scramble(userSentence))
        userSentence = input("Enter a string (or blank to quit):")

def scramble(word) :
   if len(word) <= 3 :
       return word
   # smart
   first = randint(1, len(word) - 3)
   second = randint(first + 1, len(word) - 2)

   return word[0: first] + word[second] + word[first + 1 : second] + word[first] + word[second + 1 : len(word)]

Main()

