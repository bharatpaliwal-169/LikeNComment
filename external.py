#Writing into a  file
newText = 'Hello from the external.py!\n'
saveFile = open('sample.txt','w')
saveFile.write(newText)
saveFile.close()
#appending new info
appendText = 'add this info to the pre-existing data'
appendFile = open('sample.txt','a')
appendFile.write(appendText)
appendFile.close()

#read
readMe = open('sample.txt','r').read()
print(readMe)
