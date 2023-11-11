# HTWK-Robots Hackathon

### Willkommen willkommen zum 1. HTWK Robots Hackathon!  
Hier findet ihr einige nützliche Infos zum Event.    
      
Um euch einen Einblick in unsere Arbeite zu geben könnt ihr heute Challenges bei uns machen.
Dies sind verschiedene Aufgaben und Probleme die euch auch so bei uns im Team über den Weg laufen könnten.
Dabei haben wir Aufgaben für alle, egal ob du schonmal etwas programmiert hast oder nicht. Dafür sind die Challenges in verschiedene
Schwierigkeitsabstufungen eingeteilt.
Die Beginner-Challenges sind für Leute die selbst noch keine oder nicht so viel Programmiererfahrung haben. Die Intermediate Challenges sind für Leute die schon programmieren können
und erste Erfahungen mit weiterführenden Themen, wie z.B. Bilderkennung machen wollen. Die Advanced Challenges sind für Leute die schon gut programmieren können und bereites
erste Erfahrungen mit Themen wie z.B. Bildanalyse oder neuronalen Netzen gemacht haben.

| Schwierigkeit | Challenge | Kuzbeschreibung |
|---------------|-----------|-----------------|
| Beginner | | |  
| | mic-plot | In dieser Challenge sollen Audiodaten in einem Graphen dargestellt werden und anschließend überlegt, woran ein defekt erkannt werden kann. |
| | slalom | Für diese Challenge muss eine einfache Fernsteuerung für den Roboter in Python implementiert werden. Anschließend soll damit ein Slalom-Lauf absolviert werden. |
| | Schussbewegung | Bringt dem Roboter in zweierteams bei, einen Schuss auszuführen! |
| | reel | Leute die sich nicht nur fürs coden interressieren, können in dieser Challenge ein Reel machen. Die besten werden (nur mit eurer Zustimmung) auf unserem Instagram hochgeladen. |
| Intermediate | | |
| | mic-defects | Diese Challenge ist eine Weiterführung der mic-plot Challenge. Hier soll die ausgedachte erkennung automatisiert werden. |
| | slalom2 | Hier wird die Beginner-Slalom-Challenge weitergeführt. Dafür wird die Steuerung etwas erschwierigt. |
| | red-ball | In dieser Challenge soll ein roter Ball in einem Bild erkannt werden. |
| | Aufstehbewegung | Bringt dem Roboter in Zweierteams bei aufzustehen! |
| Advanced | | |
| | black-white-ball | Diese Challenge ist eine Weiterführung der red-ball Challenge. Dafür soll nun ein schwarz-weißer Ball mithilfe eines neuronalen Netzes erkannt werden. |
| | field-lines | In dieser Challenge sollen die Feldlinien auf Bildern erkannt werden. |
| | samplerate | Hier sollen die Daten eines Mikrofons, dass eine bestimmte Samplerate eingestellt hat zu Daten mit einer anderen Samplerate kovertiert werden. |

    
### Bedienen des Roboters über Button Interface:
* Roboter einschalten: Knopf in der Mitte kurz drücken (Einschalten dauert ca. 30s warten)
* Roboter ausschalten: Knopf in der Mitte lange drücken
* Firmware starten: Knopf in der Mitte kurz drücken, wenn Roboter an ist
* Firmware ausschalten: Knopf in der Mitte kurz drücken, wenn Firmware an ist
* IP Adresse ansagen: vorderster der 3 Knöpfe auf Kopf des Naos und Knopf vorne an linkem Fuß gleichzeitig drücken
   

### Bedeutung LEDs:
* Grünes Auge: Roboter wird geladen
* Blaue LEDs am Ohr: Akkustand (100% bei geschlossenem Kreis)
 

### Start der Firmware via SSH:
1. Mit WLAN NaoHTWK_5G verbinden
2. Mit Nao verbinden via `ssh nao@10.0.13.XX` (XX ist die Nummer auf Kopf des Naos)
   Passwort: Hackathon2023
3. Auf Nao Start der Firmware: `fw_sydney -p`
4. Auf Nao Programm zum manuellen steuern: `presentation`

### Start von NaoControl (Software für Live Kamerabilder, Lokalisierungsinfos Nao etc):
1. Mit SSH auf Nao verbinden
2. Überschreibe die vorhandene IP mit deiner IP in *etc/deploy/infocast_debug.pc*
3. Start NaoControl: `./NaoControl/run.sh`
4. Starte die Firmware auf Roboter

### WLAN:
* Name: NaoHTWK_5G
* Passwort: Hackathon2023
