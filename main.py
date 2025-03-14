# Import von Moulen & Bibliotheken
import tkinter as tk

# TKinter Fensterdefinition Klasse
class Tetris_GUI:
    def __init__(self):
        # TKinter Fensterdefinition
        self.window = tk.Tk()
        self.window.title("Tetris Testprogramm")
        self.window.geometry("400x400")
        self.window.resizable(True, True)

        # Fragestellung Label
        self.label = tk.Label(text="Was ist 5 +5?")
        self.label.pack()

        # Eingebautes Eingabefeld
        self.eingabe_feld = tk.Entry(self.window)
        self.eingabe_feld.pack()

        # Ausgabe Label
        self.ausgabe_label = tk.Label(self.window, text="")
        self.ausgabe_label.pack()

        # Button
        self.button = tk.Button(self.window, text="Antwort übernehmen", command=self.eingabe_übernehmen)
        self.button.pack()
        
        # TKinter Fenster starten (Mainloop)
        self.window.mainloop()

    '''Funktion, die die Eingabe übernimmt und ausgibt'''
    def eingabe_übernehmen(self):
        print("Eingabe übernommen")
        eingabe = self.eingabe_feld.get()
        self.ausgabe_label.config(text=eingabe)



'''Hauptfunktion, die das Programm startet'''
def main():
    # Versuche auszuführen
    try:
        # Ausgabe in der Konsole ("Terminal Logging")
        print("Terminal Logging: Starte GUI")
        Tetris_GUI()

    # Fehlerbehandlung (Falls ein Fehler auftritt)
    except Exception as e:
        print(f"Fehler: {e}")

# Starte die Hauptfunktion
if __name__ == "__main__":
    main()