# Calcolare l'indice di Leggibilita' di un PDF
# aimriccardop & atk23 (aka AnnaP) x TEAM_N0

#import sys
import textract

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

import os

import re
def gulpease(pdf_file):
    testo = textract.process(pdf_file, method='pdftotext')
    result = ''
    parole  = len(re.findall(r'\w+', testo))
    lettere = len(re.findall(r'\w', testo))
    punti = len(re.findall(r'[.]+\s', testo)) + len(re.findall(r'[;]+\s', testo)) - len(re.findall(r'[.]+\s+[.]', testo))
    indiceG=89+((300*punti)-(10*lettere))/parole
    if parole!=0:
        if indiceG>100:
            indiceG=100

    return result


pdf_files = ['../Esterni/PianoDiQualifica/PianoDiQualifica.pdf',
    '../Esterni/PianoDiProgetto/PianoDiProgetto.pdf',
    '../Esterni/AnalisiDeiRequisiti/AnalisiDeiRequisiti.pdf',
    '../Interni/NormeDiProgetto/NormeDiProgetto.pdf']

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('ZeroSevenDocuments').sheet1

pp = pprint.PrettyPrinter()
result = sheet.get_all_records()
pp.pprint(result)


gulpease_arr = []
for file in pdf_files:
    if os.path.isfile(file):
        gulpease_arr.append(gulpease(file))
    else:
        gulpease_arr.append(-1)

sheet.insert_row(gulpease_arr, 1)
