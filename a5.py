#Sam Stinson
#Jan 28 2015

#Unit Three Project-A5 Card Game
#BlackJack 2.0


import random

#function:getShuffle
#@param: length (int), cardsValues(int[])
#@return: cardsValues (int[])
def getShuffle(length, cardsValues):
    for count in range(0,length):
        
        #print "length:",length
        
        endNum=cardsValues[length-1]
        
        #print "endnum:", endNum
             
        randomNumIsIndex=random.randint(0,length-1)
        #print "index:", randomNumIsIndex
            
        randomNum=cardsValues[randomNumIsIndex]#gives number of index position
        #print "num:", randomNum
        
        cardsValues[randomNumIsIndex]=endNum
        cardsValues[length-1]=randomNum
        
        length=length-1
    #print "\n", cardsValues
    return cardsValues

#function:getInput
#@param:
#@return: user(string)
def getInput():
    user=raw_input("\nEnter your name:")
    
    print "\n", user, "v.s the computer!"
    return user

#function:getUsersCard1
#@param: usersCards(int[]), cardsValues(int[]), usersSuits(string[]),cardsSuits(string[])
#@return: usersSuits(string[]), usersCards(int[])
def getUsersCard1(usersCards, cardsValues,usersSuits,cardsSuits):
    usersCards.append(cardsValues[0])
    cardsValues.remove(cardsValues[0])

    card=usersCards[0]
    if card>=1 and card<=13:
        usersSuits.append(cardsSuits[0])
        
    elif card>=101 and card<=113:
        usersSuits.append(cardsSuits[1])
        
    elif card>=1001 and card<=1013:
        usersSuits.append(cardsSuits[2])
        
    elif card>=10001 and card<=10013:
        usersSuits.append(cardsSuits[3])
    
    
    if usersCards[0]>=100 and usersCards[0]<1000:
        new=usersCards[0]-100
        usersCards[0]=new
    elif usersCards[0]>=1000 and usersCards[0]<10000:
        new=usersCards[0]-1000
        usersCards[0]=new
    elif usersCards[0]>=10000 and usersCards[0]<100000:
        new=usersCards[0]-10000
        usersCards[0]=new
        
    return usersSuits, usersCards

#function:getComsCard1
#@param: comCards(int[]), cardsValues(int[]), comSuits(string[]),cardsSuits(string[])
#@return: comSuits(string[]), comCards(int[])
def getComsCard1(comCards,cardsValues,comSuits,cardsSuits):
    comCards.append(cardsValues[0])
    cardsValues.remove(cardsValues[0])

    card=comCards[0]
    if card>=1 and card<=13:
        comSuits.append(cardsSuits[0])
        
    elif card>=101 and card<=113:
        comSuits.append(cardsSuits[1])
        
    elif card>=1001 and card<=1013:
        comSuits.append(cardsSuits[2])
        
    elif card>=10001 and card<=10013:
        comSuits.append(cardsSuits[3])
    
    
    if comCards[0]>=100 and comCards[0]<1000:
        new=comCards[0]-100
        comCards[0]=new
    elif comCards[0]>=1000 and comCards[0]<10000:
        new=comCards[0]-1000
        comCards[0]=new
    elif comCards[0]>=10000 and comCards[0]<100000:
        new=comCards[0]-10000
        comCards[0]=new
    
    #print "com card 1: (not visible to user)", comCards[0],comSuits[0]
    return comSuits,comCards

#function:getUsersCard2
#@param: usersCards(int[]), cardsValues(int[]), usersSuits(string[]),cardsSuits(string[])
#@return: usersSuits(string[]), usersCards(int[])
def getUsersCard2(usersCards,cardsValues,usersSuits,cardsSuits):
    
    usersCards.append(cardsValues[0])
    cardsValues.remove(cardsValues[0])
    
    card=usersCards[1]
    if card>=1 and card<=13:
        usersSuits.append(cardsSuits[0])
        
    elif card>=101 and card<=113:
        usersSuits.append(cardsSuits[1])
        
    elif card>=1001 and card<=1013:
        usersSuits.append(cardsSuits[2])
        
    elif card>=10001 and card<=10013:
        usersSuits.append(cardsSuits[3])
        
    
    if usersCards[1]>=100 and usersCards[1]<1000:
        new=usersCards[1]-100
        usersCards[1]=new
    elif usersCards[1]>=1000 and usersCards[1]<10000:
        new=usersCards[1]-1000
        usersCards[1]=new
    elif usersCards[1]>=10000 and usersCards[1]<100000:
        new=usersCards[1]-10000
        usersCards[1]=new
        
    return usersSuits, usersCards

#function:getComsCard2
#@param: comCards(int[]), cardsValues(int[]), comSuits(string[]),cardsSuits(string[])
#@return: comSuits(string[]), comCards(int[])
def getComsCard2(comCards,cardsValues,comSuits,cardsSuits):
    #print "new deck", cardsValues
    
    comCards.append(cardsValues[0])
    cardsValues.remove(cardsValues[0])
    #print "com cards", comCards

    card=comCards[1]
    if card>=1 and card<=13:
        comSuits.append(cardsSuits[0])
        
    elif card>=101 and card<=113:
        comSuits.append(cardsSuits[1])
        
    elif card>=1001 and card<=1013:
        comSuits.append(cardsSuits[2])
        
    elif card>=10001 and card<=10013:
        comSuits.append(cardsSuits[3])
        
        
    if comCards[1]>=100 and comCards[1]<1000:
        newCom=comCards[1]-100
        comCards[1]=newCom
    elif comCards[1]>=1000 and comCards[1]<10000:
        newCom=comCards[1]-1000
        comCards[1]=newCom
    elif comCards[1]>=10000 and comCards[1]<100000:
        newCom=comCards[1]-10000
        comCards[1]=newCom
    return comSuits, comCards

#function:getOutput
#@param: user(string), usersCards(int[]),usersSuits(string[]),comCards(int[]), cardsSuits(string[])
#@return: comSuits(string[]), comCards(int[])
def getOutput(user,usersCards,usersSuits,comCards,comSuits):
    num=0
    for count in range(0,1):
        if usersCards[num]==1:
            print "\n", user,"'s 1 card (facedown): Ace of",usersSuits[num]
        elif usersCards[num]==11:
            print "\n", user,"'s 1 card (facedown): Jack of",usersSuits[num]
        elif usersCards[num]==12:
            print "\n", user,"'s 1 card (facedown):Queen of",usersSuits[num]
        elif usersCards[num]==13:
            print "\n", user,"'s 1 card (facedown): King of", usersSuits[num]
        else:
            print "\n", user,"'s 1 card (facedown):", usersCards[num],"of", usersSuits[num]
        
        num=num+1

        if usersCards[num]==1:
            print "\n", user,"'s 2 card: Ace of",usersSuits[num]
        elif usersCards[num]==11:
            print "\n", user,"'s 2 card: Jack of",usersSuits[num]
        elif usersCards[num]==12:
            print "\n", user,"'s 2 card:Queen of",usersSuits[num]
        elif usersCards[num]==13:
            print "\n", user,"'s 2 card: King of", usersSuits[num]
        else:
            print "\n",user,"'s 2 card:", usersCards[num],"of", usersSuits[num]
        

    print "\nThe computer is given a card"

  
    if comCards[1]==1:
        print "\nComputer's 2 card: Ace of",comSuits[1]
    elif comCards[1]==11:
        print "\nComputer's 2 card: Jack of",comSuits[1]
    elif comCards[1]==12:
        print "\nComputer's 2 card:Queen of",comSuits[1]
    elif comCards[1]==13:
        print "\nComputer's 2 card: King of", comSuits[0]
    else:
        print "\nComputer's 2 card:", comCards[1],"of", comSuits[1]
 
#function:getUserTotal
#@param: usersCards(int[]), user(string)
#@return: userTotal(int)  
def getUserTotal(usersCards,user):
    userTotal=0
    num=0
    
    for count in range(0,len(usersCards)):

        card=usersCards[num]
        if card==11 or card==12 or card==13:
            card=10
            
        elif card=="ace" or card=="ACE":
            if userTotal==10:
                card=11
                
            elif userTotal<=21:
                card=11
                
            elif userTotal>21:
                card==1
        
        userTotal=card+userTotal
        num=num+1
        
    print "\n", user,"'s total:", userTotal      
    return userTotal    

#function:getComTotal
#@param: comCards(int[])
#@return: comTotal(int)  
def getComTotal(comCards):
    comTotal=0
    num=0

    for count in range(0,len(comCards)):
        
        card=comCards[num]    
        if card==11 or card==12 or card==13:
            card=10
        
        elif card=="ace" or card=="ACE":
            if comTotal<=21:
                card=11
            elif comTotal>21:
                card==1
            
        comTotal=card+comTotal
        num=num+1
    
    #print "computer's total (not visible to user):", comTotal    
    return comTotal

#function:getUserMove
#@param: choice(boolean), userTotal(int), usersCards(int[]), cardsValues(int[]), usersSutis(string[]), cardsSuits(string[]), user(string)
#@return: usersCards(int[]), usersSuits(string[]), UsersTotal(int)  
def getUserMove(choice,userTotal,usersCards,cardsValues,usersSuits,cardsSuits,user):
    num=2
    while choice==True:
        
        if userTotal>=21:
            choice=False
            break
        
        move=raw_input("\nEnter your move, hit (add another card) or stay (add no card):")
        if move=="hit" or move=="Hit" or move=="HIT":
            
            usersCards.append(cardsValues[0])
            cardsValues.remove(cardsValues[0])
            
            card=usersCards[num]
            if card>=1 and card<=13:
                usersSuits.append(cardsSuits[0])
            elif card>=101 and card<=113:
                usersSuits.append(cardsSuits[1])
            elif card>=1001 and card<=1013:
                usersSuits.append(cardsSuits[2])
            elif card>=10001 and card<=10013:
                usersSuits.append(cardsSuits[3])
                
            
            if usersCards[num]>=100 and usersCards[num]<1000:
                new=usersCards[num]-100
                usersCards[num]=new
            elif usersCards[num]>=1000 and usersCards[num]<10000:
                new=usersCards[num]-1000
                usersCards[num]=new
            elif usersCards[num]>=10000 and usersCards[num]<100000:
                new=usersCards[num]-10000
                usersCards[num]=new
            
            if usersCards[num]==1:
                print "\n", user,"'s 3 card: Ace of",usersSuits[num]
            elif usersCards[num]==11:
                print "\n", user,"'s 3 card: Jack of",usersSuits[num]
            elif usersCards[num]==12:
                print "\n", user,"'s 3 card:Queen of",usersSuits[num]
            elif usersCards[num]==13:
                print "\n", user,"'s 3 card: King of", usersSuits[num]
            else:
                print "\n", user,"'s 3 card:", usersCards[num],"of", usersSuits[num]
            
            userTotal=userTotal+usersCards[num]
            print "\n",user,"'s new total:", userTotal  
            
            num=num+1
  
        elif move=="stay" or move=="Stay" or move=="STAY":
            choice==False
            break
        
        else:
            print "\n Sorry, that is not a proper move"
    
    return usersCards, usersSuits, userTotal

#function:getComMove
#@param: comCards(int[]), comSuits(string[]), cardsValues(int[])
#@return: comCards(int[]), comSuits(string[]), comTotal(int)
def getComMove(comTotal,comCards,comSuits,cardsValues,cardsSuits):
    choice=True
    move=True
    if move==True:
        if comTotal>=17:
            comMove="Stay"
            move=False
            
        elif comTotal<17:
            comMove="Hit"
            move=True

            num=2
            while choice==True:
                
                if comTotal>=21:
                    choice=False
                    break
                
                elif comMove=="Hit":
                        comCards.append(cardsValues[0])
                        cardsValues.remove(cardsValues[0])
                        
                        #print "com cards", comCards
                        
                        card=comCards[num]
                        if card>=1 and card<=13:
                            comSuits.append(cardsSuits[0])
                        elif card>=101 and card<=113:
                            comSuits.append(cardsSuits[1])
                        elif card>=1001 and card<=1013:
                            comSuits.append(cardsSuits[2])
                        elif card>=10001 and card<=10013:
                            comSuits.append(cardsSuits[3])
    
                        if comCards[num]>=100 and comCards[num]<1000:
                            new=comCards[num]-100
                            comCards[num]=new
                        elif comCards[num]>=1000 and comCards[num]<10000:
                            new=comCards[num]-1000
                            comCards[num]=new
                        elif comCards[num]>=10000 and comCards[num]<100000:
                            new=comCards[num]-10000
                            comCards[num]=new
    
                        comTotal=comTotal+comCards[num]
                        
                        num=num+1
                
                elif comMove=="Stay":
                    choice==False

    return comMove, comCards, comSuits, comTotal

#function:getComOutput
#@param: comMove(string), comCards(int[]), cosmSuits(string[])
#@return:
def getComOutput(comMove,comCards,comSuits):
    print "\nComputer's move:",comMove
    
    if comMove=="Hit":
        print "computer's cards", comCards
            
        if comCards[2]==1:
            print "\n computer's 3 card: Ace of",comSuits[2]
        elif comCards[2]==11:
            print "\n computer's 3 card: Jack of",comSuits[2]
        elif comCards[2]==12:
            print "\n computer's 3 card:Queen of",comSuits[2]
        elif comCards[2]==13:
            print "\n computer's 3 card: King of",comSuits[2]
        else:
            print "\n computer's 3 card:", comCards[2],"of", comSuits[2]

#function:getWinner
#@param: user(string), comTotal(int), userTotal(int)
#@return: 
def getWinner(user,comTotal,userTotal):
    print "\nComputer's final total:", comTotal
    print "\n", user, "'s final total", userTotal
    
    if comTotal==userTotal:
        print "\n Computer Wins! Sorry YOU lose!"
    
    elif comTotal==21 and userTotal!=21:
        print "\n Computer Wins! Sorry YOU lose!"
    
    elif userTotal==21 and comTotal!=21:
        print "\n", user," wins!"
        
    elif (abs(comTotal-21))<(abs(userTotal-21)):
        print "\n Computer Wins! Sorry YOU lose!"
        
    elif (abs(comTotal-21))>(abs(userTotal-21)):
        print "\n", user," wins!"
        
    elif (abs(comTotal-21))==(abs(userTotal-21)):
        print "\n Computer Wins! Sorry YOU lose!"
    
    print "\n \n The end! Thanks for playing!\n \n \n"

#function:main
#@param:
#@return:
def main():
    #instructions
    instructions= " BlackJack 2.0 \n \n The goal of the game is to beat the dealer's hand (i.e. the computer) \n by scoring 21, or as close to 21 as you can get without going over. \n To start, you and computer will be dealt 1 face down card each,\n then 1 face up card each.\n You will have two moves: hit or stay.\n If the dealer scores closest to 21 or equal to, you will lose.\n Good Luck!\n "
    print instructions
    
    #global values
    choice=True
    cardsValues=[1,2,3,4,5,6,7,8,9,10,11,12,13,101,102,103,104,105,106,107,108,109,110,111,112,113,1001,1002,1003,1004,1005,1006,1007,1008,1009,1010,1011,1012,1013,10001,10002,10003,10004,10005,10006,10007,10008,10009,10010,10011,10012,10013]
    #print "start:", cardsValues, "\n"
    cardsSuits=["hearts", "diamonds", "clubs", "spades"]
    length=len(cardsValues)
    usersCards=[]
    usersSuits=[]
    comCards=[]
    comSuits=[]

    #functions
    deck=getShuffle(length, cardsValues)
    user=getInput()
    usersSuits, usersCards=getUsersCard1(usersCards, cardsValues,usersSuits,cardsSuits)
    comSuits, comCards=getComsCard1(comCards,cardsValues,comSuits,cardsSuits)    
    usersSuits, usersCards=getUsersCard2(usersCards,cardsValues,usersSuits,cardsSuits)
    comSuits, comCards=getComsCard2(comCards,cardsValues,comSuits,cardsSuits)
    getOutput(user,usersCards,usersSuits,comCards,comSuits)
    userTotal=getUserTotal(usersCards,user)
    comTotal=getComTotal(comCards)
    usersCards,usersSuits,userTotal=getUserMove(choice,userTotal,usersCards,cardsValues,usersSuits,cardsSuits,user)
    comMove, comCards,comSuits, comTotal=getComMove(comTotal,comCards,comSuits,cardsValues, cardsSuits)
    getComOutput(comMove,comCards, comSuits)
    getWinner(user,comTotal,userTotal)

main()
