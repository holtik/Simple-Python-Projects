import tkinter
import random

# List of words
words = ['penultimate', 'diminutive', 'confluence', 'granular', 'parlance', 'pithy', 'despondent', 'lucid',
         'effervescent', 'abate', 'bespoke', 'resplendent', 'erudite', 'fortnight', 'ennui', 'diatribe', 'vitriolic',
         'pusillanimous', 'bloviate', 'rococo', 'aplomb', 'pervicacious', 'obfuscate', 'fastidious', 'sycophant',
         'articulate', 'accolade', 'brevity', 'anomaly', 'adulation', 'cacophony', 'aquiver', 'glib', 'umbrage',
         'sequitur', 'vamoose', 'ubiquitous', 'nefarious', 'capricous', 'boondoggle', 'sycophant', 'mellifluous',
         'brogue', 'perfunctory', 'tryst', 'obtuse', 'quagmire', 'flummoxed', 'cajole', 'caustic', 'gregarious',
         'fastidious', 'maudlin', 'flabbergasted', 'teetotaler', 'empathy']

score = 0

timeleft = 60

def startGame(event):
    if timeleft == 60:
        countdown()  # start countdown

    nextWord()  # run function to choose next word

# Choose and display next word
def nextWord():
    global score
    global timeleft

    # If game is in play
    if timeleft > 0:
        e.focus_set()

        if e.get().lower() == words[0].lower():
            score += 1

        e.delete(0, tkinter.END)

        random.shuffle(words)

        label.config(text=str(words[0]))

        scoreLabel.config(text="Score: " + str(score))
    else:
        endgame()

def countdown():
    global timeleft

    # If game is in play
    if timeleft > 0:
        timeleft -= 1
        timeLabel.config(text="Time left: " + str(timeleft))
        timeLabel.after(1000, countdown)
    else:
        endgame()

def endtimer():
    global timeleft
    timeleft = 0

def endgame():
    global timeleft
    global score
    timeleft = 60
    label.config(text="")
    timeLabel.config(text="Press enter to start again")
    scoreLabel.config(text="Your score was: " + str(score))
    score = 0

# Create GUI
root = tkinter.Tk()

root.title("Typing Test Game")
root.geometry("375x200")

# Add labels

reset = tkinter.Button(root, text='End game', width=25, command=endtimer)
reset.pack()

instructions = tkinter.Label(root,text="Type in the words that appear, as fast as you can.", font=('Helvetica', 12))
instructions.pack()

scoreLabel = tkinter.Label(root, text="Press enter to start", font=('Helvetica', 12))
scoreLabel.pack()

timeLabel = tkinter.Label(root, text="Time left: "+ str(timeleft), font=('Helvetica', 12))
timeLabel.pack()

label = tkinter.Label(root, font=('Helvetica', 35))
label.pack()


# Add text entry box
e = tkinter.Entry(root)

# Start game when enter is pressed
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
