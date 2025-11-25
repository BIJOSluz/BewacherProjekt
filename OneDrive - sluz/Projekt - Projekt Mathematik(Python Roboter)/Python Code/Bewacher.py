#Projektanforderung: 
#Wächter-Roboter (Security Bot): Entwickeln Sie einen Roboter, der wie ein Wachposten funktioniert. 
# Aufgabe: Der Roboter soll einen Bereich überwachen und einen Alarm auslösen, wenn jemand zu nahe kommt. 
# Nutzen Sie den Ultraschall- oder IR-Sensor, um Bewegungen/Annäherungen zu erkennen. 
# Zum Beispiel kann der Roboter patrouillieren (hin- und herfahren) und bei einem erkannten Eindringling anhalten, 
# laut Geräusche machen und auf seinem Display eine Warnung anzeigen. Bonus-Idee: Mit dem Gyrosensor könnte der Roboter 
# immer wieder seine Ausgangsrichtung einnehmen (wie ein Wächter, der sich nach einer Drehung wieder nach vorn ausrichtet).

#Abgabe des Projekts:
#Bitte gebt bei der Abgabe eures EV3 Pybricks–MicroPython–Codes Folgendes mit ab:
#Programmdatei: eure .py-Datei mit allen Funktionen und der Hauptroutine
#Kurzbeschreibung im Code: kurze Erklärung, was das Programm macht und wie es aufgebaut ist
#Hinweis auf KI-Einsatz: im Kommentar markieren, ob und wie KI (oder ähnliche Tools) verwendet wurden
#Installationshinweise im Code: verwendete EV3-Ports und benötigte Bibliotheken dokumentieren
#Teilnehmer am Projekt: Namen in Zeile 2 (nach <code>#!/usr/bin/env pybricks-micropython</code>)


#!/usr/bin/env pybricks-micropython
# Programm 8: Ultraschallsensor – Distanzabhängiger Warnton

from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialisierung
ev3   = EV3Brick()
ultra = UltrasonicSensor(Port.S4)   # Ultraschallsensor an Port 4

# Endlosschleife
while True:
    distance_mm = ultra.distance()      # Entfernung in Millimetern
    distance_cm = distance_mm // 10     # grobe cm-Anzeige

    # Display aktualisieren
    ev3.screen.clear()
    ev3.screen.print("Abstand: {} cm".format(distance_cm))

    # Distanzabhängiger Warnton
    if distance_mm < 100:               # < 10 cm
        ev3.speaker.beep(frequency=1000, duration=100)
        wait(100)
        ev3.screen.print("ALARM!")
    elif distance_mm < 300:             # 10–30 cm
        ev3.speaker.beep(frequency=500, duration=100)
        wait(300)
        ev3.screen.print("WARNUNG!")
    else:                               # > 30 cm
        ev3.speaker.beep(frequency=250, duration=100)
        wait(700)
        ev3.screen.print("SICHER")
