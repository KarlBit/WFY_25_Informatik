import logging

# Importieren der YAML-Bibliothek ("pip install pyyaml")
import yaml

# Laden der YAML-Konfigurationsdatei#
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Konfiguration des Loggers
#logging.basicConfig(level=logging.DEBUG, format="%(asctime)s - %(levelname)s - %(message)s")
logging.basicConfig(level=config["LOGGING_LEVEL"], format=config["LOGGING_FORMAT"])

# Variablen
a = 1
b = 2

def main():
    # Versuche auszuführen
    try:
        logging.info(f"Starte Berechnung: {a} + {b}")
        logging.info(f"Ergebnis: {a} + {b} = {(a + b)}")

    # Fehlerbehandlung (Falls ein Fehler auftritt)
    except Exception as e:
        # Logge den Fehler
        logging.error(f"Fehler: {e}")


# Starte die Hauptfunktion
if __name__ == "__main__":
    main()