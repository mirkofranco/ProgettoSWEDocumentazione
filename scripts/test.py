from tika import parser

raw = parser.from_file('../Esterni/PianoDiQualifica/PianoDiQualifica.pdf')
print(raw['content'])