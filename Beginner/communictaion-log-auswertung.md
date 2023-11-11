# Beginner Aufgabe: Analysiere den Communication Log der Spiele


Währen der Wettkämpfe kommunizieren alle Roboter mit einem zentralen Game Controller.
Die Roboter senden dabei in regelmäßigen Abständen unter anderem ihre erkannte Position, die erkannte Position des Balles und ihre Spielernummer. Die Daten aller Roboter werden in einem Log erfasst.

Einen der Logs findest du als csv-Datei im Ordner data/game_statistics

### Aufgabe:
Analysiere die Log-Datei mithilfe eines Python Scripts.
Du kannst dabei zum Beispiel:
 - Analysieren welche Roboter besonders oft Fallen
 - Auswerten welche Roboter sehr oft eine Zeitstrafe bekommen
 - Eine Heatmap der Positionen der Roboter erstellen
 - Dir weitere sinnvolle Auswertungen überlegen

### Hinweis:
Die Spalten der Tabelle haben folgende Bedeutungen:

- Timestamp: Zeit in Millisekunden, die seit dem Start des Game Controllers vergangen sind
- Game State: Gibt an, in welcher Spielphase die Daten aufgenommen wurden
    - R - Ready
    - P - Playing
    - S - Set
    - I - Initial
    - F - Finished
- Player: Gibt die Spielernummer an
- Penalized: Zeigt an, ob gegen den Roboter eine Zeitstrafe läuft
    - U - keine Zeitstrafe
    - P - Zeitstrafe läuft
- Pose X: X-Position des Roboters auf dem Spielfeld
- Pose Y: Y-Position des Roboters auf dem Spielfeld
- Pose A: Rotation des Roboters
- isFallen: Hat den Wert true wenn der am Boden liegt, oder sich in der Aufstehbewegung befindet
- Ball Age: Zeit in Millisekunden, seit der Roboter den Ball zuletzt erkannt hat
- Ball X: X-Position der Balls auf dem Spielfeld
- Ball Y: Y-Position der Balls auf dem Spielfeld


