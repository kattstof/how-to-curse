import random
curses = open("curses.txt").readlines()
sentences = open("sentences.txt").readlines()
print(random.choice(sentences),(random.choice(curses))) 
