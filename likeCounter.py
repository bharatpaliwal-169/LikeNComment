# like = open('likeCounter.txt','r').read()
# like = int(like)
# like += 1
# storeLike = str(like)
# openFile = open('likecounter.txt','w')
# openFile.write(storeLike)
# openFile.close()
# like = open('likeCounter.txt','r').read()
# print(like)


#function to increase the like counter...
#1
def likeMe(like):
    like += 1
    return like
#2
def disLikeMe(like):
    like -= 1
    return like
#3
def resetLikeCounter(like):
    like = 0
    return like


#main
print("Press 1 to like,\n")
print("Press 2 to dislike\n")
print("Press 3 to reset likes\n")
print("Press 4 to Display likes\n")
print("Press 0 to Exit\n")

option = int(input("Your Choice here: "))

if option == 1 :
    like = open('./likeCounter.txt','r').read()
    like = int(like)
    like = likeMe(like)
    storeLike = str(like)
    openFile = open('./likecounter.txt','w')
    openFile.write(storeLike)
    openFile.close()

elif option == 2 :
    like = open('./likeCounter.txt','r').read()
    like = int(like)
    like = disLikeMe(like)
    storeLike = str(like)
    openFile = open('./likecounter.txt','w')
    openFile.write(storeLike)
    openFile.close()

elif option == 3 :
    like = open('./likeCounter.txt','r').read()
    like = int(like)
    like = resetLikeCounter(like)
    storeLike = str(like)
    openFile = open('./likecounter.txt','w')
    openFile.write(storeLike)
    openFile.close()
elif option == 4:
    readlike = open('./likeCounter.txt','r').read()
    print("Likes : ",readlike)

#end