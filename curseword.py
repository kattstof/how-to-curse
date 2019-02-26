import random
curses = open("curses.txt",).readlines()
sentences = open("sentences.txt").readlines()
print(random.choice(sentences),(random.choice(curses))) 
new = input("Please type a new curseword/enter to exit.:")
if new != "":
    with open("curses.txt", "a") as f:
        f.write(new)
elif new == "":
    print("Goodbye, Twatwaffle")
    exit()

