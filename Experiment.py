# packages laden
from   psychopy import visual, gui, core, event
import random
import os
import glob
import time
import pandas as pd

# Bilder importieren
img_dir     = os.path.join(os.getcwd(), "images")             # Verzeichnis anpassen
img_all     = glob.glob(os.path.join(img_dir, "*.png"))
img_human   = glob.glob(os.path.join(img_dir, "Mensch*"))
img_primate = glob.glob(os.path.join(img_dir, "Affe*"))

# Daten aufnehmen mit Systemdialog
vp_info = {                              # Dataframe für Daten, die aufgenommen werden sollen
    "age"   : [],                        # durch leere Liste ist freie Eingabe möglich
    "gender": ["---","m", "w", "d"],     # Auswahlmöglichkeiten
    "vp_id" : []
}
vp_data = gui.DlgFromDict(vp_info, title = "Probandendaten",                    # Titel der Dialogbox
                          labels = ["Alter", "Geschlecht", "Probanden-ID"])     # Dialogbox anzeigen und labels definieren
age    = vp_info["age"]                                                         # Variablen für die aufgenommenen Daten definieren und aus dict nehmen
gender = vp_info["gender"]
vp_id  = vp_info["vp_id"]


# Outputordner definieren
output_path = os.path.join(os.getcwd(), f'vp_{vp_id}')          # separat für VP wird Ordner definiert
if not os.path.exists(output_path):                             # wenn Output-Ordner für VP nicht existiert, erstellen
    os.makedirs(output_path)

file_path = os.path.join(output_path, f'vp_{vp_id}_find-human.csv')


# dict für behav_Daten
behav_data = {'vp_id' : [],                    # für jede erfasste Variable eine leere Liste erstellen
                'age' : [],
                'gender' : [],
                'block' : [],
                'trial' : [],
                'correct_key' : [],
                'reaction_time' : [],
                'target' : [],                 
                'key' : [],
                'size' : [] 
                          }

# Fenster erstellen
win = visual.Window(
    color='grey',
    size=[1366, 768],                      # Display anpassen, mac = 2560, 1440
    fullscr = True                         # kann bei Mac nun geschlossen an, mac = true
    )                        

win.mouseVisible = False


# Instruktionen definieren
welcome_stim = visual.TextStim(win)
welcome_stim.setText(
"Herzlich willkommen! \n\n" "In diesem Experiment geht es darum ein Menschengesicht zwischen mehreren Affengesichtern zu finden.") #Je nach dem wann die Anzeigetafel angezeigt wird?
welcome_stim.draw()
win.flip()
event.waitKeys(maxWait=30.0, keyList=["space"])

instruct_stim = visual.TextStim(win) 
instruct_stim.setText(
"Das Experimenten besteht aus 8 Blöcken mit 45 trials. \n\n" \
"Drücken Sie bitte die Taste [A] wenn ein Menschengesicht da ist und [L] wenn kein Menschengesicht da ist. \n\n" \
"Legen Sie nun bitte die Finger auf die entsprechenden Tasten. \n\n"\
"Drücken Sie die Leertaste für [weiter].")
instruct_stim.draw()
win.flip()
event.waitKeys(maxWait=30.0, keyList=["space"])

instruct_stim_2 = visual.TextStim(win) 
instruct_stim_2.setText("Zunächst starten wir mit einem kurzen Training. \n\n " \
"Nach erfolgreichem Training startet das eigentliche Experiment. \n\n" \
"Drücken Sie die Leertaste, um das Experiment zu starten. \n\n" \
"Viel Erfolg!")   
instruct_stim_2.draw()
win.flip() 
event.waitKeys(maxWait=30.0, keyList=["space"])   


# Funktion für Experiment erstellen
def show_display(blocks = 8, trials = 45, dict_for_data = None):
     # Seitenverhältnis Fenster
    aspect_ratio = win.size[0] / win.size[1]              # Anpassung: damit Bilder nicht in Breite gezogen werden
    scale_factor = min(win.size) / 768                    # Anpassung: Faktor, der Suchdisplay an unterschiedliche Bildschirmgrößen anpasst

    # Anpassungen für Stimuli
    rect_width = 0.19 * scale_factor                      # [auf meinem Bildschirm geeignete] Höhe wird an Bildschirmhöhe angepasst (sollte so bleiben, damit Code korrekt funktioniert)
    rect_height = 0.15 * aspect_ratio * scale_factor      # Breite des Bilds wird zusätzlich an Breite angepasst

    # loop für Trials erstellen
    for m in range(blocks):
        # zu Beginn jedes Blocks Instruktionen zeigen
        block_text = visual.TextStim(win, text = f"Block {m+1} \n\n" \
                                     "Drücken Sie [A] für Mensch und [L] für kein Mensch. \n\n" \
                                        "Drücken Sie die Leertaste, um fortzufahren.")
        block_text.draw()
        win.flip()
        event.waitKeys(keyList =["space"])

        for n in range(trials):

            # Erstellen einer Liste mit Positionen auf dem Display
            pos_list = []
            n_row   = 6                                    # Anzahl der Zeilen
            n_col   = 6                                    # Anzahl der Spalten
            spacing =  .18                                 # Abstand zwischen Elementen
            # Liste mit allen möglichen Kombinationen von Koordinaten auf dem Suchdisplay
            for i in range(n_row):
                for j in range(n_col):
                    x_pos = (j - (n_col - 1) / 2) * spacing * scale_factor
                    y_pos = (i - (n_row - 1) / 2) * spacing * aspect_ratio * scale_factor
                    pos_list.append((x_pos, y_pos))


            # Größe der Displays + zufällig aus Liste ziehen
            display_sizes = [8, 16, 36]
            size = random.choice(display_sizes)


            # Inter Trial Intervall (ITI)
            iti = visual.TextStim(win, height = 0.3)         
            iti.setText("")
            iti.draw()
            win.flip()
            event.waitKeys(maxWait = .5, keyList = None)             # Es soll kein Tastendruck aufgezeichnet werden


            # Fixationskreuz anzeigen
            fix_cross = visual.TextStim(win, height = 0.3)         
            fix_cross.setText("+")
            fix_cross.draw()
            win.flip()
            event.waitKeys(maxWait = 1., keyList = None)
            
            
            # Zeichnen der Bilder
            for i in range(size-1):

                # Ablenker zufällig auswählen
                flanker = random.choice(img_primate)                
                pos = random.choice(pos_list)
                pos_list.remove(pos)
                img_stim = visual.ImageStim(win, image = flanker, size=[rect_width, rect_height],
                                pos = pos)                 
                img_stim.draw()
            # Zufällig auswählen, ob target primate angezeigt wird
            target_list = random.choice(["human", "primate"])   
            if target_list == "human":
                target = random.choice(img_human)
            elif target_list == "primate":
                target = random.choice(img_primate)
            pos = random.choice(pos_list)                 
            pos_list.remove(pos)
            img_stim = visual.ImageStim(win, image = target, size=[rect_width, rect_height],
                                pos = pos)
            img_stim.draw()

            win.flip()

            
            reaction_times = {}             # ?
           

            # Startzeit messen
            start_time = time.time()


            # auf Antwort warten und Experiment abbrechen
            
            while True:
                keys = event.getKeys(keyList=["a", "l", "escape"])           # diese Tasten werden kontinuierlich während Suchdisplay "beobachtet"
                if keys:
                    # Abbruch ist möglich, wenn Suchdisplay gezeigt wird
                    if 'escape' in keys:
                        text_stim = visual.TextStim(win)
                        text_stim.setText("Wollen Sie das Experiment beenden?\n\nja [j]   nein [n]\n\n Bestätigen Sie Ihre Eingabe mit der Leertaste")
                        text_stim.draw()
                        win.flip()
                        event.clearEvents()
                        response = event.waitKeys(keyList = ["j", "n"])
                        if response[0] == "j":
                            df = pd.DataFrame.from_dict(behav_data)  # gesammelte Daten in einen DataFrame umwandeln
                            df.to_csv(file_path, sep=",", index=False, header=True)  # Daten als CSV speichern
                            print(f"Zwischengespeicherte Daten bis Block {m+1}, Trial {n+1}")
                            win.close()
                            core.quit()
                        elif response[0] == "n":
                            event.clearEvents()
                            continue
                    else:
                        response = keys[0]
                        break

            # Endzeit messen
            if response:
                end_time = time.time()
                reaction_time = round(end_time - start_time, 4)  # Reaktionszeit berechnen


            # Reaktionszeit speichern
                reaction_times[f'block_{m}_trial_{n}'] = {
                'response': response[0],
                'reaction_time': reaction_time
            }


            # correct key ermitteln
            if response[0] == "a" and target_list == "human":
                correct_key = True
            elif response[0] == "l" and target_list == "primate":
                correct_key = True
            else:
                correct_key = False

            # Dictionary befüllen mit gemessenen Daten
            if dict_for_data:
                dict_for_data["vp_id"].append(vp_id)
                dict_for_data["age"].append(age)
                dict_for_data["gender"].append(gender)
                dict_for_data["block"].append(m+1)
                dict_for_data["trial"].append(n+1)
                dict_for_data["correct_key"].append(correct_key)
                dict_for_data["reaction_time"].append(reaction_time)
                dict_for_data["target"].append(target_list)
                dict_for_data["key"].append(response[0])
                dict_for_data["size"].append(size)


                # Ende der Funktion

# Training
training_dict = {'vp_id' : [],                    # gesondertes dict erstellen für Trainingsdaten
                'age' : [],
                'gender' : [],
                'block' : [],
                'trial' : [],
                'correct_key' : [],
                'reaction_time' : [],
                'target' : [],                    
                'key' : [],
                'size' : [] 
                          }
training_answer = 0
while training_answer <= 8:      # 8/10 trials sollen korrekt beantwortet werden
    training_answer = 0
    show_display(blocks = 1, trials = 10, dict_for_data = training_dict)
    for i in training_dict["correct_key"]:
        if i == True:
            training_answer = training_answer + 1
    if training_answer <= 8:
        text_stim = visual.TextStim(win)
        text_stim.setText("Hier ist ein weiterer Übungsblock. \n\n" \
                    "Drücken Sie die Leertaste, um fortzufahren.")
        text_stim.draw()
        win.flip()
        event.waitKeys(keyList = ["space"])

# Experiment durchführen
text_stim = visual.TextStim(win)
text_stim.setText("Jetzt beginnt das Experiment.  \n\n" \
                    "Drücken Sie die Leertaste, um zu beginnen.")
text_stim.draw()
win.flip()
event.waitKeys(keyList = ["space"])
show_display(blocks = 8, trials = 45, dict_for_data = behav_data)


# Abschlussdisplay
text_stim = visual.TextStim(win)
text_stim.setText("Das Experiment ist beendet. \n\n  Vielen Dank für Ihre Teilnahme!")
text_stim.draw()
win.flip()
event.waitKeys(keyList = ["space"])


win.close()


# befülltes dict in Konsole ausgeben
for key in behav_data:
    print(key, ":", behav_data[key])


# Dataframe speichern
try:
    df = pd.DataFrame.from_dict(behav_data)                       # dict in pandas Dataframe umwandeln
    df.to_csv(file_path, sep = ",", index=False, header=True)
except:
    print(f"Fehler beim Speichern der Datei {file_path}")
