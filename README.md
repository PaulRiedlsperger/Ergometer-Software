# UC Template
## Name und Identifikationsnummer:
UC 1.04 (Alarm bei Leistungsabweichung)

## Beschreibung:
Bei einer zu großen Abweichung der Leistung werden dem/der Diagnostiker:in und dem/der Proband:in auf dem Display ein entsprechender Hinweis angezeigt und ein akustischer Warnton abgespielt. Bei Bedarf wird der Test manuell abgebrochen.

## Beteiligte Akteur:innen:
Diagnostiker:in, Proband:in.

## Status:
In Arbeit

## Verwendete Anwendungsfälle:
UC 1.00

## Auslöser:
Durchführung einer standardisierten Leistungsdiagnose.

## Vorbedingungen:
UC 1.00 - Leistungsdiagnostik,
UC 1.01 (Probandin anlegen),
UC 1.02 (Leistungstest anlegen),

## Invarianten:
Aufzeichnung aller Daten.

## Nachbedingung/Ergebnis:
Der Leistungsinput wird angepasst und der Leistungstest kann ordnungsgemäß fortgeführt werden.

## Standardablauf:
Der/die Proband:in weicht von der geforderten Leistung ab. Daraufhin wird die Warnung angezeigt und die Leistung kann entsprechend gesteigert oder gesenkt werden.

## Alternative Ablaufschritte:
Der Test ist/wird beendet, dadurch tritt der UC 1.04 nicht auf. Der Test muss aus gesundheitlichen Gründen abgebrochen werden. Es tritt ein technischer Defekt auf oder andere Widerstandswerte werden verletzt. In allen Fällen wird die Warnung bei der Leistungsabweichung nicht angezeigt.

## Hinweise:

## Änderungshinweise:
0.02, 14.03.2025, Elias Maier
