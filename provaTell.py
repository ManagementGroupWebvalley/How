#!\usr/bin/python

f=open('toTell.txt','r+')       #r+ cosi' posso sia scrivere che leggere

print f.readline()
print
print f.tell()
print
print f.readline()
print
f.write('aggiunto')
f.close


