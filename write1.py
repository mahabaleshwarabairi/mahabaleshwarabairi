file1=open('writefile.txt','w')
file2=open('for2.py','r')
data=file2.read()
file1.write(data)
print(data)
file1.close()
file2.close



