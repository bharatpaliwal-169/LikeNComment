like = open('likeList.txt','r').read()
like = int(like)
like += 1
storeLike = str(like)
openFile = open('likeList.txt','w')
openFile.write(storeLike)
openFile.close()
like = open('likeList.txt','r').read()
print(like)

