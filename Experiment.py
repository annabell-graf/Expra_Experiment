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






# Daten aufnehmen
vp_info = {
    "age"   : [],
    "gender": ["---","m", "w", "d"],            # vorauswählbare Antworten
    "vp_id" : []
}

vp_data = gui.DlgFromDict(vp_info, title = "Probandendaten",                    # Titel der Dialogbox
                          labels = ["Alter", "Geschlecht", "Probanden-ID"])                                   # Dialogbox anzeigen

print(vp_info)                                                                  # Antworten werden automatisch in dict übernommen

age = vp_info["age"]
gender = vp_info["gender"]
vp_id = vp_info["vp_id"]
print(age, gender, vp_id)


# Outputordner definieren
output_path = os.path.join(os.getcwd(), f'vp{vp_id}')
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

file_path = os.path.join(output_path, f'vp{"vp_id"}_find-human.csv')


# stuff specific to our experiment
win = visual.Window(
    color='grey',
    size=[1366, 768],                      # Display anpassen, mac = 2560, 1440
    fullscr = True)                        # kann bei Mac nun geschlossen an, mac = true


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
"Drücken Sie bitte die Taste (a) wenn ein Menschengesicht da ist und (l) wenn kein Menschengesicht da ist. \n\n" \
"Legen Sie nun bitte die Finger auf die entsprechenden Tasten. \n\n"\
"Drücken Sie die Leertaste für [weiter].")
instruct_stim.draw()
win.flip()
event.waitKeys(maxWait=30.0, keyList=["space"])

instruct_stim_2 = visual.TextStim(win) 
instruct_stim_2.setText("Zunächst starten wir mit einem kurzen Training. \n\n " \
"Nach erfolgreichem Training startet das eigentliche Experiment. \n\n" \
"Drücken Sie die Leertaste, um das Experiment zu starten \n\n" \
"Viel Erfolg!")   
instruct_stim_2.draw()
win.flip() 
event.waitKeys(maxWait=30.0, keyList=["space"])   


def show_display(blocks = 2, trials = 3):
     # Seitenverhältnis Fenster
    aspect_ratio = win.size[0] / win.size[1]              # Anpassung: damit Bilder nicht in Breite gezogen werden
    scale_factor = min(win.size) / 768                    # Anpassung: Faktor, der Suchdisplay an unterschiedliche Bildschirmgrößen anpasst

    # Anpassungen für Stimuli
    rect_width = 0.15 * scale_factor                      # [auf meinem Bildschirm geeignete] Höhe wird an Bildschirmhöhe angepasst
    rect_height = 0.15 * aspect_ratio * scale_factor      # Breite des Bilds wird zusätzlich an Breite angepasst


    #trials = 5     # Experiment= 45  (müssen wir mal gucken)
    #blocks = 2     # Experiment = 8

    # loop für Trials erstellen
    for m in range(blocks):
        
        

        block_text = visual.TextStim(win, text = f"Block {m+1} \n\n" \
                                     "Drücke [a] für Mensch und [l] für kein Mensch \n\n" \
                                        "Drücke die Leertaste, um weiter zu machen")
        block_text.draw()
        win.flip()
        event.waitKeys(keyList =["space"])
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


            # Inter Trial Intervall (ITI)

            iti = visual.TextStim(win, height = 0.3)         
            iti.setText("")
            iti.draw()
            win.flip()
            core.wait(.5)

            # Fixatioskreuz anzeigen
            fix_cross = visual.TextStim(win, height = 0.3)         # Fixationskreuz erstellen
            fix_cross.setText("+")
            fix_cross.draw()
            win.flip()
            core.wait(1.)
            
            

            # Zeichnen der Rechtecke

            for i in range(size-1):

                # Ablenker zufällig auswählen
                flanker = random.choice(img_primate)                #Liste anpassen (alle Bilder brauchen .jpeg)
                target_list = random.choice(["img_human", "img_primate"]) #im dict festhalten, aus welcher Liste Target
                if target_list == "img_human":
                    target = random.choice(img_human)
                elif target_list == "img_primate":
                    target = random.choice(img_primate)
                print(target_list)
                print(target)

                pos = random.choice(pos_list)
                print(pos)
                pos_list.remove(pos)
                img_stim = visual.ImageStim(win, image = flanker, size=[rect_width, rect_height],
                                pos = pos)                 #default rectangle plotten
                img_stim.draw()

            


            pos = random.choice(pos_list)                  #graue fenster als Platz für Traget, Target fehltnoch
            pos_list.remove(pos)
            img_stim = visual.ImageStim(win, image = target, size=[rect_width, rect_height],
                                pos = pos)
            img_stim.draw()
            win.flip()

            # zufällig auswählen ob target anwesend oder nicht

            
            reaction_times = {}
           
            # Startzeit messen
            start_time = time.time()

            # auf Antwort warten und Experiment abbrechen
            while True:
                keys = event.getKeys(keyList=["a", "l", "space", "escape"])
                if keys:
                    if 'escape' in keys:
                        win.close()
                        core.quit()
                    else:
                        response = keys[0]
                        break


            # Endzeit messen
            if response:
                end_time = time.time()
                reaction_time = end_time - start_time  # Reaktionszeit berechnen

            # Reaktionszeit speichern
                reaction_times[f'block_{m}_trial_{n}'] = {
                'response': response[0],
                'reaction_time': reaction_time
            }
                print(f"Response: {response}, Reaction Time: {reaction_time:.4f} seconds") #4 Nachkommastellen

# Training

training_answer = "y"

while training_answer == "y":
    show_display(blocks=1, trials=1)    # ändern: 5
    training_stim = visual.TextStim(win)
    training_stim.setText("Möchtest du das Training wiederholen? \n\n "
                      "Ja [y]      Nein [n]")
    training_stim.draw()
    win.flip()
    training_answer = event.waitKeys(keyList=["y", "n"])[0]
    print(f"Training answer: {training_answer}")



# Experiment durchführen
text_stim = visual.TextStim(win)
text_stim.setText("Jetzt beginnt das Experiment  \n\n" \
                    "Drücke die Leertaste, um zu beginnen")
text_stim.draw()
win.flip()
event.waitKeys(keyList = ["space"])
show_display(blocks = 2, trials = 1)


win.close()
