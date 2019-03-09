import gspread
from oauth2client.service_account import ServiceAccountCredentials
import os


pdf_files = ['../Esterni/PianoDiQualifica/PianoDiQualifica.pdf',
    '../Esterni/PianoDiProgetto/PianoDiProgetto.pdf',
    '../Esterni/AnalisiDeiRequisiti/AnalisiDeiRequisiti.pdf',
    '../Interni/NormeDiProgetto/NormeDiProgetto.pdf']

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(creds)

sheet = client.open('ZeroSevenDocuments').sheet1

gulpease_arr = []
for file in pdf_files:
    if os.path.isfile(file):
        gulpease_arr.append(file)
    else:
        gulpease_arr.append(-1)

print(gulpease_arr)
sheet.insert_row(gulpease_arr, 2)

records = sheet.get_all_records()
print(records)