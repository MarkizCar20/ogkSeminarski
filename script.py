#Script for comparing two arrays of words written in files
import array as arr

file1 = open("logatomiGrupa3.txt", encoding='utf-8',mode = 'r')
file2 = open("logatomiGrupa4.txt", encoding='utf-8',mode = 'r')
file3 = open("logatomiGrupa5.txt", encoding='utf-8',mode = 'r')
file4 = open("./logatomiSlusalaca/slusalac9Grupa3.txt", encoding='utf-8', mode= 'r')
file5 = open("./logatomiSlusalaca/slusalac9Grupa4.txt", encoding='utf-8', mode= 'r')
file6 = open("./logatomiSlusalaca/slusalac9Grupa5.txt", encoding='utf-8', mode= 'r')

file1.seek(0)
file2.seek(0)
file3.seek(0)
file4.seek(0)
file5.seek(0)
file6.seek(0)

logGrupa3 = []
logGrupa4 = []
logGrupa5 = []
slusalac3Grupa3 = []
slusalac3Grupa4 = []
slusalac3Grupa5 = []


errCount = 0

for line in file1:
    logGrupa3.append(line)
    logGrupa4.append(file2.readline())
    logGrupa5.append(file3.readline())
    slusalac3Grupa3.append(file4.readline()) 
    slusalac3Grupa4.append(file5.readline())
    slusalac3Grupa5.append(file6.readline())

wordCount = len(logGrupa3)

for i in range(len(logGrupa3)):
    if(logGrupa5[i] != slusalac3Grupa5[i]):
        errCount += 1

succRate = ((wordCount-errCount)/wordCount)*100

print(str(errCount) + " " + str(succRate))        

file1.close()
file2.close()
file3.close()
file4.close()
file5.close()