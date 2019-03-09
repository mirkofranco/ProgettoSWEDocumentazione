# Calcolare l'indice di Leggibilita' di un PDF
# aimriccardop & atk23 (aka AnnaP) x TEAM_N0
import sys
import textract

import re
def gulpease(pdf_file):
    testo = textract.process("scripts/PianoDiQualifica.pdf", method='pdftotext')
    result = ''
    parole  = len(re.findall(r'\w+', testo))
    lettere = len(re.findall(r'\w', testo))
    punti = len(re.findall('[.]+\s', testo))+len(re.findall('[;]+\s', testo)) - len(re.findall('[.]+\s+[.]', testo))
    indiceG=89+((300*punti)-(10*lettere))/parole
    result += "numero di parole presenti nei doc :   " + str(parole) + '\n'
    result += "numero di lettere presenti nei doc :  " + str(lettere) + '\n'
    result += "numero di frasi presenti nei doc :    " + str(punti) + '\n'
    if parole!=0:
        if indiceG>100:
            indiceG=100

        result += "indice di Gulpease restrittivo : " + str(indiceG) + '\n'
        punti = len(re.findall('[.]', testo)) + len(re.findall('[;]', testo))
        indiceG = 89 + ((300 * punti) - (10 * lettere)) / parole
        if indiceG>100:
            indiceG=100

        result += "indice di Gulpease non restrittivo : " + str(indiceG) + '\n'
        result += "Nel primo indice non viene considerato delimitatore di frase:" + '\n'
        result += "- la punteggiatura spazio punteggiatura come delimitatore di frasi" + '\n'
        result += "- la punteggiatura che non e' seguita da un carattere di spaziatura" + '\n'
    else:
        result += "Errore nel calcolo dell'indice Gulpease" + '\n'
    return result


pdf_files = ["scripts/PianoDiQualifica.pdf"]
print(gulpease(pdf_files[0]))