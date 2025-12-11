#!/usr/bin/env pybricks-micropython
# Projekt: Wächter-Roboter (Security Bot)
# Teammitglieder: Joshua, Benno, Patrik
# Verwendete Ports:
#   - Port S4: Ultraschallsensor (Abstandsmessung)
#   - Lautsprecher und Display: EV3Brick integriert
# Starthinweise:
#   1. Sensor an Port S4 anschliessen.
#   2. EV3 einschalten und dieses Programm starten.
#   3. Der Roboter zeigt den erkannten Abstand an und gibt je nach Nähe einen Warnton aus.
#   4. Bei Entfernungen unter 10 cm ertönt ein Alarm und eine Warnmeldung wird angezeigt.
#
# Kurzbeschreibung:
# Dieses Programm steuert einen einfachen Wächter-Roboter. Der Ultraschallsensor misst kontinuierlich die Entfernung zu einem Hindernis.
# Je nach Distanz gibt der EV3 unterschiedliche Töne aus (Sicher, Warnung, Alarm) und zeigt Textmeldungen auf dem Display an.
# Ziel: Einen Bereich überwachen und akustisch sowie visuell auf zu nahe Annäherungen reagieren.
#
# Hinweis auf KI-Einsatz:
# Teilweise KI-gestützte Code-Kommentierung und Strukturierung (z. B. zur besseren Dokumentation).
#
# Bibliotheken:
# pybricks.hubs, pybricks.ev3devices, pybricks.parameters, pybricks.tools
#
# Programmdatei: waechter_robot.py
# Version: 1.1


from pybricks.hubs import EV3Brick
from pybricks.ev3devices import UltrasonicSensor
from pybricks.parameters import Port
from pybricks.tools import wait

# Initialisierung
ev3   = EV3Brick()
ultra = UltrasonicSensor(Port.S4)   # Ultraschallsensor an Port 4

# Endlosschleife: Überwachung mit Anzeige und Warnton
while True:
    distance_mm = ultra.distance()      # Entfernung in Millimetern
    distance_cm = distance_mm // 10     # grobe cm-Anzeige

    # Display aktualisieren
    ev3.screen.clear()
    ev3.screen.print("Abstand: {} cm".format(distance_cm))

    # Distanzabhängiger Warnton
    if distance_mm < 100:               # < 10 cm = Alarm
        ev3.speaker.beep(frequency=1000, duration=100)
        wait(100)
        ev3.screen.print("ALARM!")
    elif distance_mm < 300:             # 10–30 cm = Warnung
        ev3.speaker.beep(frequency=500, duration=100)
        wait(300)
        ev3.screen.print("WARNUNG!")
    else:                               # > 30 cm = Sicher
        ev3.speaker.beep(frequency=250, duration=100)
        wait(700)
        ev3.screen.print("SICHER")
