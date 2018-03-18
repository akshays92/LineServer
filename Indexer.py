import sys

#print(str(sys.argv[1]))
filename = str(sys.argv[1])
file = open(filename, "r")
lineNumber=0
for line in file:
   print (str(lineNumber)+": "+line)
   lineNumber+=1