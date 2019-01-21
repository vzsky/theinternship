import os, sys, tty
from random import randint
from man import stickman
from pick import pick
from glob import glob

tty.setcbreak(sys.stdin)  

mistake = 0
point = 0
guessed = []

class Word ():
    def __init__ (self, text):
        self.value = text.lower()
        self.size = len(text) -1
        self.result = text
        self.guessed = []
        self.result = ["_" if _letter.isalpha() else _letter for _letter in self.result]
    def __str__ (self):
        return self.value
    def guess (self, char):
        global point
        _append = _correct = 0
        for _index ,_letter in enumerate(self.value):
            if char == _letter and not char in self.guessed:
                self.result[_index] = char
                _correct = 1
                point += 10
                _append = 1
        if _correct == 0:
            global mistake
            mistake+=1
            point -= 5
        if not char in self.guessed or _append == 1 :
            _append = 0
            self.guessed.append(char)
    def display (self):
        for _letter in self.result:
            print(_letter, end=' ')
    def more (self):
        _more = 0
        for _letter in self.result:
            if _letter == '_':
                _more += 1
        return _more

def printhangman(m):
    for row in stickman[m]:
        print(row)

def select (topic):
    words_set  = open("words/"+topic+".txt", "r")
    words = words_set.readlines()
    random = randint(0, len(words)-1)
    text = words[random].split(' ')[0]
    hint = words[random].split(' ')[1]
    word = Word(text)
    return word, hint

def choose ():
    title = 'pick the topic of words'
    options = [file.replace("./words/", "").replace(".txt","") for file in glob("./words/*.txt")]
    option, index = pick(options, title)
    return option

def play (topic):
    global point
    word, hint = select(topic)
    global mistake
    mistake = 0

    while True :
        os.system('clear')
        print("hint :", hint)
        printhangman(mistake)
        if mistake == 5 :
            raise Exception("MistakeReached")
            break
        left = word.more()
        if left == 0 :
            os.system('clear')
            print(word, end='')
            print("you got", point, "points")
            break

        word.display()
        print()

        print("Guessed letters :", end=' ')
        for letter in word.guessed:
            print(letter, end=' ')
        print()

        print("points :", point)

        print("Character : ")
        g = chr(ord(sys.stdin.read(1)))
        word.guess(g.lower())

if __name__ == "__main__":
    topic = choose()
    while True:
        try :
            play(topic)
        except Exception as e:
            print("Gameover", e)
            print("You got", point, "point")
            break
        print("space to continue, r to reselect topic, q to quit")
        while True:
            cmd = ord(sys.stdin.read(1))
            if cmd == ord('r'):
                topic = choose()
            elif cmd == ord(' '):
                break
            elif cmd == ord('q'):
                quit()
        guessed = []
        
#TODO make shell cmd
#TODO somehow test on windows linux? since lib are diff?