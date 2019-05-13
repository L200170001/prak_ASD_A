#Nama  : Riza Frisnanda
#Nim   : L200170001 / A
#Modul : 7

#----N0.1----#
import re
f = open('test.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'me[\w]+'
tampil = re.findall(pola,teks)
print(tampil, "\n")

#----N0.2----#
f = open('test.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'di[\w]+'
tampil = re.findall(pola,teks)
print(tampil, "\n")

#----N0.3----#
f = open('test.txt', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'di [\w]+'
tampil = re.findall(pola,teks)
print(tampil, "\n")

#----N0.4a----#
f = open('KEI.html', 'r', encoding = 'latin1')
teks = f.read()
f.close()
pola = r'(\w+)</a></td>'
tampil = re.findall(pola,teks)
print(tampil)

pola = r'(\d+)</a></td><td>'
tampil = re.findall(pola,teks)
print(tampil)

#----N0.4b----#
f = open('KEI.html','r', encoding='latin1')
teks = f.read()
f.close()
tampil = re.findall(r'title="([\w+]+)">',teks)
tampil = re.findall(r'">([\w+]+)</a></td>\n<td>([0-9.]+)</td>',teks)
a = []
for i in tampil :
    a.append((i[0], float(i[1])))
print(a)

