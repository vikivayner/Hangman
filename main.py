
from random_word import RandomWords


r = RandomWords()



game_dif = str(input("Hello Welcome to Hangman! " "\n" "Please state your difficulty (hard, medium, easy): "))


if game_dif == "easy": 
   word_easy = r.get_random_word(hasDictionaryDef="true", minCorpusCount=100000, minLength =3, maxLength=5)
   wordChoice = word_easy.lower()
if game_dif == "medium": 
    word_medium = r.get_random_word(hasDictionaryDef="true", minCorpusCount = 100, minLength=6, maxLength=10)
    wordChoice = word_medium.lower()
if game_dif == "hard": 
    word_hard = r.get_random_word(hasDictionaryDef="true", minCorpusCount = 3, minLength=11)
    wordChoice = word_hard.lower()

# wordChoice = str(input("Word: "))

new_wording = list(set(wordChoice.lower()))
new_wording2 = list(wordChoice.lower())

guesses = len(wordChoice) + 2
print("Number of Letters:", len(wordChoice))
lst = []

for char in wordChoice: 
     lst.append("_")
     
print(lst)
rejects = []

while guesses != 0: 
    
    letter1 = input("Guess Letter:" )
    
    if letter1 in new_wording: 
         print("True! Your letter is" , letter1,  "Keep guessing other letters.", guesses, "guesses left.") 
         new_wording.remove(letter1)
     
         
         index = [index for index, value in enumerate(new_wording2) if value == letter1]
         for ind in index: 
              lst[ind] = letter1
         print(lst)
         
    if  new_wording == []:  
          
          break
    
    elif letter1 not in new_wording2: 

         rejects.append(letter1)
         guesses = guesses  - 1 
         print("False! Try again! Number of guesses left:", guesses, '\n' "Rejected letters: ", rejects)

print("The word was", wordChoice)
