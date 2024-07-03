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
output_path = os.getcwd() + f'vp{vp_id}'
if not os.path.exists(output_path):
    os.makedirs(output_path)

# dict für behav_Daten
behav_data = pd.DataFrame({'vp_id' : [],
                           'age' : [],
                           'gender' : [],
                           'block' : [],
                           'trial' : [],
                           'correct_key' : [],
                           'reaction_time' : [],
                           'target : [],             # wir wollen erfassen, ob Zielreiz anwesend ist -> ja/nein
                          })

file_path = os.path.join(output_path, f' vp{vp_id}_find-human.csv')



# Abbruchkriterium für Training

# for-loop mit displays noch erstellen
true_answers = 0
while true_answers < 5:
    if response == ["a"] and "human" in display: #displays müssen noch definiert werden
            true_answers += 1
    elif response == ["l"] and "no human" in display:  
            true_answers += 1
    elif response == ["a"] and "no human" in display:
            true_answers += 0
    elif response == ["l"] and "human" in display:  
            true_answers += 0 

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
    size=[1366, 768],                      # Display anpassen, mac = 2560, 1440
    fullscr = False)                        # kann bei Mac nun geschlossen an, mac = true


# Anzahl der Stimuli randomisieren

display_sizes = [9,18,36]

random.choice(display_sizes)


# Instruktionen definieren
welcome_stim = visual.TextStim(win)
welcome_stim.setText(
"Herzlich willkommen! \n\n" "In diesem Experiment geht es darum ein Menschengesicht zwischen mehreren Affengesichtern zu finden.") #Je nach dem wann die Anzeigetafel angezeigt wird?
welcome_stim.draw()
win.flip()
event.waitKeys(maxWait=30.0, keyList=["space"])

instruct_stim = visual.TextStim(win) 
instruct_stim.setText(
"Das Experimenten besteht aus x Blöcken mit y trials. \n\n" \
"Drücken Sie bitte die Taste (A) wenn ein Menschengesicht da ist und (L) wenn kein Menschengesicht da ist. \n\n" \
"Legen Sie nun bitte die Finger auf die entsprechenden Tasten. \n\n"\
"Drücken Sie die Leertaste für [weiter].")
instruct_stim.draw()
win.flip()
event.waitKeys(maxWait=30.0, keyList=["space"])

instruct_stim_2 = visual.TextStim(win) 
instruct_stim_2.setText("Zunächst starten wir mit einem kurzen Training. \n\n " \
"Nach erfolgreichem Trainig startet das eigentliche Experiment. \n\n" \
"Drücken Sie die Leertaste, um das Experiment zu starten \n\n" \
"Viel Erfolg!")   
instruct_stim_2.draw()
win.flip() 
event.waitKeys(maxWait=30.0, keyList=["space"])                                    



# Experiment-Funktion


# end experiment
core.quit()
