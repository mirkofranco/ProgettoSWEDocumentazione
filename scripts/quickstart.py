import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

# Calcolare l'indice di Leggibilita' di un PDF
# aimriccardop & atk23 (aka AnnaP) x TEAM_N0
import sys

nomeScript, nomeFile = sys.argv

import textract

#nf = raw_input("Digita il nome del PDF di cui vuoi calcolare l'indice di leggibilita': ")
testo = textract.process(nomeFile, method='pdftotext')
#print(testo)

import re
parole  = len(re.findall(r'\w+', testo))
lettere = len(re.findall(r'\w', testo))
punti = len(re.findall('[.]+\s', testo))+len(re.findall('[;]+\s', testo)) - len(re.findall('[.]+\s+[.]', testo))

indiceG=89+((300*punti)-(10*lettere))/parole
print("numero di parole presenti nei doc :   " + str(parole))
print("numero di lettere presenti nei doc :  " + str(lettere))
print("numero di frasi presenti nei doc :    " + str(punti))
print("")
if parole!=0:
    if indiceG>100:
        indiceG=100

    print("indice di Gulpease restrittivo : " + str(indiceG))
    punti = len(re.findall('[.]', testo)) + len(re.findall('[;]', testo))
    indiceG = 89 + ((300 * punti) - (10 * lettere)) / parole
    if indiceG>100:
        indiceG=100

    print("indice di Gulpease non restrittivo : " + str(indiceG))
    print("")
    print("Nel primo indice non viene considerato delimitatore di frase:")
    print("- la punteggiatura spazio punteggiatura come delimitatore di frasi")
    print("- la punteggiatura che non e' seguita da un carattere di spaziatura")
else:
    print("Errore nel calcolo dell'indice Gulpease")




scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('ZeroSevenDocuments').sheet1

pp = pprint.PrettyPrinter()
result = sheet.get_all_records()
pp.pprint(result)

new_row = ["ndp",70]
index = 2
sheet.insert_row(new_row, index)

