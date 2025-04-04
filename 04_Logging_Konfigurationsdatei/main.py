''' Testprogramm für die Verwendung einer Konfigurationsdatei mit Logging'''
# Imports
# Standardbibliotheken
import os
import logging

# Dritte Bibliotheken
# Zum finder der Bibliotheken nutze zum Beispiel "pypi.org"
# YAML MODUL ("install pyyaml")
import yaml

# Config Datei Überprüfung
if not os.path.exists("config.yaml"):
    print("Konfigurationsdatei nicht gefunden!")
    exit(1)
else:
    print("Konfigurationsdatei gefunden!")

# Einlesen der Konfigurationsdatei
with open("config.yaml", "r", encoding="utf-8") as f:
    config = yaml.safe_load(f)

# Überprüfen, ob die Logging Datei existiert
if not os.path.exists(config["LOGGING_PATH"]):
    print("Log Datei nicht gefunden!")
    exit(1)
else:
    print("Log Datei gefunden!")

# Logging Konfiguration
logging.basicConfig(
    level=config["LOGGING_LEVEL"],
    format=config["LOGGING_FORMAT"],
    handlers=[
        # Datei Logging
        logging.FileHandler(config["LOGGING_PATH"], encoding="utf-8"),
        # Konsolen Logging
        logging.StreamHandler()
    ]
)

# Setzen der Variablen
VARIABLE_A = float(config["VARIABLE_1"])
VARIABLE_B = float(config["VARIABLE_2"])

''' Hautpfunktion für das Modultesting'''
def main():
    logging.info("Starte das Programm...")
    # Versuche auszuführen
    try:
        logging.debug("Starte die try Anweisung...")
        logging.warning("Das ist eine warning...")
        logging.error("Berechnung erfolgreich")

        logging.critical("Ergebnis: %d + %d = %d", VARIABLE_A, VARIABLE_B, VARIABLE_A + VARIABLE_B)
        logging.info("Das Programm läuft erfolgreich.")

    # Exception und Fehlerbehandlung
    except Exception as e:
               # Logge den Fehler
        logging.error("Fehler: %s", e)
        logging.debug("Irgendwas ist schiefgelaufen")

# Starte die Hauptfunktion
if __name__ == "__main__":
    main()
