from my_functions import build_person
from my_functions import build_experiment

if __name__ == "__main__":
    # Erstellen eines Sportlers
    subject = build_person("Max", "Musterfrau", "male", 30)
    
    # Erstellen einer Versuchsleitung
    supervisor = build_person("Paul", "Riedlsperger", "male", 23)
    
    # Erstellen eines Experiments
    experiment = build_experiment("Herzfrequenz-Studie", "2025-03-22", supervisor, subject)
    
    # Ausgabe des Experiment-Dictionaries
    print(experiment)
