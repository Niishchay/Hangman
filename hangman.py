import random


def find(str, ch):
    for i, ltr in enumerate(str):
        if ltr == ch:
            yield i


def hangman():
    words = ['rainbow', 'computer', 'science', 'programming', 'python',
             'mathematics', 'player', 'condition', 'reverse',
             'water', 'board', 'geeks']
    word = random.choice(words)
    copyWord = list(word)
    lis = ['-'] * len(word)
    used = set()
    lives = 6
    while len(copyWord) != 0:
        print("".join(lis) + " | Already used letters:", *used)
        userInput = input("guess the alphabet: ")
        if userInput in word:
            if userInput in used:
                print("you have already used this letter")
                continue
            else:
                used.add(userInput)
                findlis = list(find(word, userInput))
                for i in findlis:
                    lis[i] = userInput
                    copyWord.remove(userInput)
        else:
            lives -= 1
            print(f"wrong guess, you have {lives} lives left")
        if lives == 0:
            print("you lost the match!")
            break
    if len(copyWord) == 0:
        print(f"You won the match Hooray! and the correct word is {word}")

hangman()
