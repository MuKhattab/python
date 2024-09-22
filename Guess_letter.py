from hangman_word_list import word_list
import random
chosen_word=random.choice(word_list)
#print (chosen_word)
word_length= len(chosen_word)
#print(word_length)
empty=0
under_scores=[]
for empty in range(empty, word_length):
    under_scores.append("_")
    empty+=1

#print(under_scores)
while '_' in under_scores:
    guess=input("Guess a letter: ").lower()
    i=0
    for i in range(i, word_length):
        letter = chosen_word[i]
        if letter==guess:
            under_scores[i]=letter
        i+1
    print(under_scores)
print(f"You win, thw word is: {chosen_word}")