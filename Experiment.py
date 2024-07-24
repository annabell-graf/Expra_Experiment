# packages laden
from   psychopy import visual, gui, core, event
import random
import os
import glob
import time
import pandas as pd

# Bilder importieren

img_dir     = os.path.join(os.getcwd(), "images")             # Verzeichnis anpassen
img_all     = glob.glob(os.path.join(img_dir, "*.jpeg"))
img_human   = glob.glob(os.path.join(img_dir, "human*"))
img_primate = glob.glob(os.path.join(img_dir, "primate*"))


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
                           'target' : [],                    #zur Erfassung ob Zielreiz gezeigt wurde ja/nein
                          })

file_path = os.path.join(output_path, f' vp{"vp_id"}_find-human.csv')


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

#_____________________________________________________________________bis hierher läuft es___________________________________________________________________________________________


# Abbruchkriterium für Training

# for-loop mit displays noch erstellen
true_answers = 0
response = event.waitKeys(maxWait = 60.0, keyList = ["a", "l"])                 # response musste definiert werden (geht es ohne maxWait -> wir wollen ja open trial)
while true_answers < 5:
    if response == ["a"] and "human" in display: #displays müssen noch definiert werden
            true_answers += 1
    elif response == ["l"] and "no human" in display:  
            true_answers += 1
    elif response == ["a"] and "no human" in display:
            true_answers += 0
    elif response == ["l"] and "human" in display:  
            true_answers += 0 
# Experiment-Funktion



#---------------------------------------------

# Seitenverhältnis Fenster
aspect_ratio = win.size[0] / win.size[1]              # Anpassung: damit Bilder nicht in Breite gezogen werden
scale_factor = min(win.size) / 768                    # Anpassung: Faktor, der Suchdisplay an unterschiedliche Bildschirmgrößen anpasst

# Anpassungen für Stimuli
rect_width = 0.15 * scale_factor                      # [auf meinem Bildschirm geeignete] Höhe wird an Bildschirmhöhe angepasst
rect_height = 0.15 * aspect_ratio * scale_factor      # Breite des Bilds wird zusätzlich an Breite angepasst


trials = 3
blocks = 2

# loop für Trials erstellen

for m in range(blocks):
    for n in range(trials):

        # Erstellen einer Liste mit Positionen
        pos_list = []


        n_row   = 6
        n_col   = 6
        spacing =  .18                                 # Abstand zwischen Elementen
        for i in range(n_row):
            for j in range(n_col):
                x_pos = (j - (n_col - 1) / 2) * spacing * scale_factor
                y_pos = (i - (n_row - 1) / 2) * spacing * aspect_ratio * scale_factor
                pos_list.append((x_pos, y_pos))


        # Größe der Displays + zufällig generieren

        display_size = [8, 16, 36]

        size = random.choice(display_size)




        # Zeichnen der Rechtecke

        for i in range(size-1):

            # Ablenker zufällig auswählen
            flanker = random.choice(img_primate)         # Liste anpassen

            pos = random.choice(pos_list)
            pos_list.remove(pos)
            img_stim = visual.ImageStim(win, image = flanker, size=[rect_width, rect_height],
                            pos = pos)                 # Bilder plotten plotten
            img_stim.draw()
                                              # Problem!

        # zufällig auswählen ob target anwesend oder nicht
        target_list = random.choice(["human", "primate"])    # im dict festhalten, aus welcher Liste Target
        if target_list == "human":
            target = random.choice(img_human)
        elif target_list == "primate":
            target = random.choice(img_primate)
        
        pos = random.choice(pos_list)                  #graue fenster als Platz für Target, Target fehltnoch
        pos_list.remove(pos)
        img_stim = visual.ImageStim(win, image = target, size=[rect_width, rect_height],
                            pos = pos)



        # auf Antwort warten
        response = event.waitKeys(maxWait = 10., keyList = ["a", "l"])
    win.flip() 
win.close()
