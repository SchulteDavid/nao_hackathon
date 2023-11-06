# HTWK-Robots Hackathon

Dieses Repo ist für Challenges-Dateien, vorgefertigte Skripte etc. gedacht. Hier kann jeder seine Challenges pushen.
YAY!  

Willkommen willkommen zum 1. HTWK Robots Hackathon!  
Hier findet ihr einige nützliche Infos zum Event.  

### Vorträge am Samstag:
* 14:30 Uhr: Willkommen & Vorstellung der Challenges
* 15:30 Uhr: Projekt - Deep Loca
* 16:30 Uhr: Projekt - Automatische Erkennung der Jerseynummer
* 17:30 Uhr: Projekt - Whistle Detection/Sound
   

### Bedienen des Roboters über Button Interface:
* Roboter einschalten: Knopf in der Mittekürz drücken (Einschalten dauert ca. 30s warten)
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
   Passwort: Todesmaschine
3. Auf Nao Start der Firmware: `fw_sydney -p`
4. Auf Nao Programm zum manuellen steuern: `presentation`

### Start von NaoControl (Software für Live Kamerabilder, Lokalisierungsinfos Nao etc):
1. Mit SSH auf Nao verbinden
2. Überschreibe die vorhandene IP mit deiner IP in *etc/deploy/infocast_debug.pc*
3. Start NaoControl: `./NaoControl/run.sh`
4. Starte die Firmware auf Roboter

### WLAN:
* Name: NaoHTWK_5G
* Passwort: 
