import tkinter as tk

# TKinter Fensterdefinition

class Tetris_GUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Tetris Testprogramm")
        self.window.geometry("400x400")
        self.window.resizable(True, True)
        
        self.label = tk.Label(text="Tetris Beispiel")
        self.label.pack()
 
        self.window.mainloop()

# Hauptfunktion
def main():
    try:
        print("Terminal Logging: Starte GUI")
        gui = Tetris_GUI()

    except Exception as e:
        print(f"Fehler: {e}")

if __name__ == "__main__":
    main()