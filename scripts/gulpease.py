import textract
import requests
import os
import re
import datetime

NOW = datetime.datetime.now()
URL = "https://hooks.zapier.com/hooks/catch/4637877/n9hvza/"

def gulpease(pdf_file):
    testo = textract.process(pdf_file, method='pdftotext')
    parole  = len(re.findall(r'\w+', testo))
    lettere = len(re.findall(r'\w', testo))
    punti = len(re.findall(r'[.]+\s', testo)) + len(re.findall(r'[;]+\s', testo)) - len(re.findall(r'[.]+\s+[.]', testo))
    indiceG=89+((300*punti)-(10*lettere))/parole
    if parole!=0:
        if indiceG>100:
            indiceG=100

    return indiceG


pdf_files = ['../Esterni/PianoDiQualifica/PianoDiQualifica.pdf',
    '../Esterni/PianoDiProgetto/PianoDiProgetto.pdf',
    '../Esterni/AnalisiDeiRequisiti/AnalisiDeiRequisiti.pdf',
    '../Interni/NormeDiProgetto/NormeDiProgetto.pdf']

params = {'date' : NOW.strftime("%Y-%m-%d")}

for file in pdf_files:
    if os.path.isfile(file):
        print(file + ":"+ str(gulpease(file)))
        params[file] = str(gulpease(file)) 
    else:
        print(file +" not found")

r = requests.get(url = URL, params = params)