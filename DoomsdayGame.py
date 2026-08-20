from ast import While
import time
from time import sleep
import os
import sys

print('Scrivi "exit" Per Uscire Dal Gioco')

while True:
         time.sleep(1)
         print('-------------------------------------------')
         print('|   Benvenuto al Gioco Della Apocalisse   |')
         print('-------------------------------------------')

         time.sleep(1)

         Anno = (input('Inserisci l\'anno : '))
         if Anno == "exit":
             print('Alla Prossima!')
             time.sleep(0.5)
             sys.exit()
         time.sleep(0.5)
         Mese = input('Inserisci il mese : ')
         if Mese == "exit":
             print('Alla Prossima!')
             time.sleep(0.5)
             sys.exit()
         time.sleep(0.5)
         Giorno = (input('Inserisci il giorno : '))
         if Giorno == "exit":
             print('Alla Prossima')
             time.sleep(0.5)
             sys.exit()
         time.sleep(0.5)

         if not Anno.isdigit() or not Giorno.isdigit():
             print("Errore: L'anno e il giorno devono essere numeri interi.")
             continue

         if int(Anno) < 1 or int(Giorno) < 1 or int(Giorno) > 31:
             print("Errore: L'anno deve essere maggiore di 0 e il giorno deve essere compreso tra 1 e 31.")
             continue

         if Mese not in ["Gennaio", "Febbraio", "Marzo", "Aprile", "Maggio", "Giugno", "Luglio", "Agosto", "Settembre", "Ottobre", "Novembre", "Dicembre"]:
             print("Errore: Il mese deve essere uno dei seguenti: Gennaio, Febbraio, Marzo, Aprile, Maggio, Giugno, Luglio, Agosto, Settembre, Ottobre, Novembre, Dicembre.")
             continue

         if Mese == "Febbraio" and int(Giorno) > 29:
             print("Errore: Febbraio ha al massimo 29 giorni.")
             continue

         if Mese in ["Aprile", "Giugno", "Settembre", "Novembre"] and int(Giorno) > 30:
             print(f"Errore: {Mese} ha al massimo 30 giorni.")
             continue

         if Mese in ["Gennaio", "Marzo", "Maggio", "Luglio", "Agosto", "Ottobre", "Dicembre"] and int(Giorno) > 31:
             print(f"Errore: {Mese} ha al massimo 31 giorni.")
             continue

         if int(Anno) < 1583:
             print("Errore: L'anno deve essere maggiore o uguale a 1583 (inizio del calendario gregoriano).")
             continue   

         if int(Anno) > 9999:
             print("Errore: L'anno deve essere minore o uguale a 9999.")
             continue

         #CENTURY ANCHOR

         Secolo = int(Anno) // 100

         if Secolo % 4 == 0:
           SecoloAnchor = 2

         elif Secolo % 4 == 1:
             SecoloAnchor = 0

         elif Secolo % 4 == 2:
             SecoloAnchor = 5

         elif Secolo % 4 == 3:
             SecoloAnchor = 3

         #YEAR SHIFT

         YearShift = (int(Anno) % 100 + (int(Anno) % 100 // 4)) % 7

         #MONTHS

         MonthCode = {"Gennaio": 3, "Febbraio": 0, "Marzo": 0, "Aprile": 3, "Maggio": 5, "Giugno": 1, "Luglio": 3, "Agosto": 6, "Settembre": 2, "Ottobre": 4, "Novembre": 0, "Dicembre": 2}

         #WEEKDAYS

         Days = ["Domenica", "Lunedi", "Martedi", "Mercoledi", "Giovedi", "Venerdi", "Sabato"]

         Domenica = 0
         Lunedi = 1
         Martedi = 2
         Mercoledi = 3
         Giovedi = 4
         Venerdi = 5
         Sabato = 6

         #WEEKDAY CALCULATION

         GiornoSettimana = (int(Giorno) + MonthCode[Mese] + YearShift + SecoloAnchor) % 7

         time.sleep(1)

         print("Il giorno della settimana è: ", Days[GiornoSettimana])
         time.sleep(3)
         