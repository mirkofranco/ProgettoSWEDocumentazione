from tika import parser

testo = "ciao, sono un tavolo. Sono fatto di legno. ciao, sono un tavolo; Sono fatto di legno. ciao, sono un tavolo. Sono fatto di legno. ciao, sono un tavolo. Sono fatto di legno."
import re

punti = len(re.findall(r'[.]+\s', testo)) + len(re.findall(r'[;]+\s', testo)) - len(re.findall(r'[.]+\s+[.]', testo))

print(punti)