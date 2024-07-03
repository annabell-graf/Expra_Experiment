# packages laden

from   psychopy import visual, gui, core, event
import random
import os
import glob
import time
import pandas as pd

# Bilder importieren

img_dir = os.getcwd() + "images"                                                                # Arbeitsverzeichnis definieren!

stim_list      = glob.glob(os.path.join(img_dir, "*.jpeg"))
primate_img_list   = glob.glob(os.path.join(img_dir, "primate*"))
human_img_list = glob.glob(os.path.join(img_dir, "human*"))

# Outputordner definieren

# ...

# Abbruchkriterium für Training

# ...

# Anzahl von Trials und Blöcken

# ...

# keyboard input

trial_keys = ['a', 'l']
continue_key = 'space'


# Daten aufnehmen

vp_info = {
    "age"   : [],
    "gender": ["---","m", "w", "d"],            # vorauswählbare Antworten
    "vp_id" : []
}

vp_data = gui.DlgFromDict(vp_info, title = "Probandendaten",                    # Titel der Dialogbox
                          labels = ["Alter", "Geschlecht", "Probanden-ID"],     # Labels der Kästchen
                          alwaysOnTop = True)                                   # Dialogbox anzeigen

print(vp_info)                                                                  # Antworten werden automatisch in dict übernommen

age = vp_info["age"]
gender = vp_info["gender"]
vp_id = vp_info["vp_id"]
print(age, gender, vp_id)



# stuff specific to our experiment
win = visual.Window(
    color='grey',
    size=[1366, 768],                      # Display anpassen
    fullscr = False)                        # kann bei Mac nun geschlossen an


# Anzahl der Stimuli randomisieren

display_sizes = [9,18,36]

random.choice(display_sizes)


# Instruktionen (als dict?) definieren
welcome_stim = visual.TextStim(win)
welcome_stim.setText("Willkommen zu unserem Experiment \n\n Bitte geben Sie Ihre Daten in folgende Anzeigetafel ein.") #Je nach dem wann die Anzeigetafel angezeigt wird?
welcome_stim.draw()
win.flip()
core.wait(5) #Zeit evtl. anpassen

instruct_stim = visual.TextStim(win) 
instruct_stim.setText("In diesem Experiment geht es darum ein Menschengesicht zwischen mehreren Affengesichtern zu finden. \n\n "\
"Auf diese Weise wollen wir untersuchen, wie gut zwischen Menschen- und Affengesichtern unterschieden werden kann. \n\n "\
"Das Experimenten besteht aus x Blöcken mit y trials. \n\n" \
"Ihre Aufgabe besteht darin, (1) in jedem Display das Menschengesicht zu suchen und (2) zu entscheiden, ob das Display ein Menschengesicht enthält. \n\n "\
"Drücken Sie bitte die Taste (A) für  Menschengesicht und (L) für kein Menschengesicht. \n\n" \
"Legen Sie nun bitte die Finger auf die entsprechenden Tasten. \n\n"\
"Drücken Sie die Leertaste für [weiter].")
instruct_stim.draw()
win.flip()
event.waitKeys(maxWait=30.0, keyList=["space"])

instruct_stim_2 = visual.TextStim(win) 
instruct_stim_2.setText("Zunächst starten wir mit einem kurzen Training. \n\n " \
"Nach erfolgreiche Trainig startet das eigentliche Experiment. \n\n" \
"Drücken Sie die Leertaste, um das Experiment zu starten \n\n" \
"Viel Erfolg!")   
instruct_stim_2.draw()
win.flip() 
event.waitKeys(maxWait=30.0, keyList=["space"])#Anzeigedauer noch anpassen.



# Experiment-Funktion


# end experiment
core.quit()
