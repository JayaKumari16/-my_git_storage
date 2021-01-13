# -*- coding: utf-8 -*-
"""
Created on Sat Dec 19 19:42:11 2020

@author: Ricky 
"""

import random


def welcome():
    print("###################################################")
    print("\t\tWelcome to the Game")
    print("###################################################")
    
def instruction():
    
    print("############################################################################")
    print("select  1 to 4 for choose any answer ")
    print("if you win the next question display or you choose wrong answer  you are out\n")
    print("In this game there has an 3  level if you clear 1st  only then you will go further\n")
    print("The quiz contains to many  questions and there is no time limit. \n You’ll get 10 point for each correct answer.\n At the end of the quiz, you’ll receive a total score. \n Good luck!")
    
    
    print("############################################################################")
def quiz():
    a=0
    for i in range  (16):
        
    
        ch=random.randint(9,40)
        
        
        if ch==9:
            
            print("How many time zones are there in Russia? \n 1). 10 \t 2). 12\n 3). 22 \t 4). 11")
            
            choose=int(input("Enter your choice..."))
            
            if choose==4:
                
                print("This is Correct answer")
                
                a=( a + 10)
                
                print(a,"you win")
                
            else:
                
                print("This is wrong answer..")
                print("The answer is 11")
                print(a,"your score")
                break
            
        elif ch==10:
            
            print("\nUntil 1923, what was the Turkish city of Istanbul called? \n 1). Boservia       \t 2). Israil  \n 3). Constantinople \t 4). Egypt")
            
            choose=int(input("Enter your choice..."))
            if choose==3:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Constantinople")
                print(a,"your score")
                break
                
        elif ch==11:   
            print("\nWhat’s the smallest country in the world? \n 1). Italy       \t 2). Africa  \n 3). The Vatican \t 4). Pakistan")
            choose=int(input("Enter your choice..."))
            
            if choose==3:
                
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is The vatican")
                print(a,"your score")
                break
        elif ch==12:
            print("\nWhat is the slang name for New York City, used by locals? \n 1).Goza      \t 2). Gotham \n 3). Grozam \t 4). Alcate")
            choose=int(input("Enter your choice..."))
            
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Gotham")
                print(a,"your score")
                break
        elif ch==13: 
            print("\nWho invented the World Wide Web? \n 1).Babylonians \t 2).Tim Berners-Lee \n 3). Rob Delaney \t 4). Josh Brolin ")
            
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else:
                print("This is wrong answer..")
                print("The answer is Tim Berners Lee")
                print(a,"your score")
                break
                
        elif ch==14:        
            print("\nWhich football team is known as ‘The Red Devils’? \n 1). En Fuego CF   \t 2). Rush Hour. \n 3). Thunder     \t 4). Manchester United)")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else:
                print("This is wrong answer..")
                print("The answer is Manchester united" )
                print(a,"your score")
                break
                
        elif ch==15:        
            print("\nWhat was the clothing company Nike originally called? \n 1). Orange Ribbon Sports  \t 2).Red Ribbon Sports  \n 3).Blue Ribbon Sports    \t 4).Cobblers club")
            choose=int(input("Enter your choice..."))
            if choose==3:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Blue Ribbon Sports")
                print(a,"your score")
                break
                
        elif ch==16:        
            print("\nWhen was Netflix founded:\n 1).2001 \t 2). 2009 \n 3). 1997 \t 4). 2015? ")
            choose=int(input("Enter your choice..."))
            if  choose==3:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is 1997")
                print(a,"your score")
                break
                
        elif ch==17:         
            print("\nName Disney’s first film? \n1).Mickey mouse      \t 2). Donald duck \n3).Scooby Dooby Doo  \t 4). Snow White")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Snow White ")
                print(a,"your score")
                break
        elif ch==18:         
            print("\nIf you have cryophobia, what are you afraid of? \n 1). Fire \t 2). Ice\cold \n 3). Dust \t 4). Height")
            choose=int(input("Enter your choice..."))
            if  choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Ice\cold")
                print(a,"your score")
                break
        elif ch==19:
            print("\nHow many permanent teeth does a dog have?  \n 1). 42 \t 2). 43 \n 3). 48 \t 4). 46")
            choose=int(input("Enter your choice..."))
            if choose==1:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is 42")
                print(a,"your score")
                break
        elif ch==20:        
            print("\nWho is the singer of   Hawa banke song ?  \n 1). Aditya narayan \t 2). Arijit singh \n 3). Jubin nautiyal \t 4). Darshan raval")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Darshan raval")
                print(a,"your score")
                break
        elif ch==21:        
                
            print("\nWhich Catastrophe star makes a cameo in Deadpool 2 as Peter?  \n 1).Cris Hemsworth  \t 2). Bruce Banner  \n 3). Rob Delaney     \t 4). Peter Parker")
            choose=int(input("Enter your choice..."))
            if choose==3:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Rob Delaney")
                print(a,"your score")
                break
        elif ch==22:         
            print("\nWhat is the capital city of Australia?  \n 1). Perth    \t 2). Canberra \n 3). Sydney \t 4). Melbourne ")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Canberra")
                print(a,"your score")
                break
        elif ch==23:
            print("\nHow many keys are there on a piano?  \n 1). 68 \t 2). 88 \n 3). 48 \t 4). 98")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is 88")
                print(a,"your score")
                break
        elif ch==24:        
            print("\nWhat is the currency of Vietnam?  \n 1). Vietnamese kong \t 2). Vietnamese pong \n 3). Vietnamese chong  \t 4). Vietnamese dong")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Vietnamese dong")
                print(a,"your score")
                break
        elif ch==25:        
            print("\nWhich star perform Iron Man  & Thanos character in end game?\n 1).Tom holland & John chadwick      \t 2). John chadwick & Josh Brolin  \n 3). Robert downey jr & Tom holland \t 4). Robert downey jr. & Josh Brolin")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Robert downey jr. & Josh Brolin")
                print(a,"your score")
                break
        elif ch==26:        
            print("\nWhich planet has the most moons?  \n 1). Pluto \t 2). Mars \n 3). Saturn \t 4). Jupiter ")
            choose=int(input("Enter your choice..."))
            if choose==3:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Saturn ")
                print(a,"your score")
                break
        elif ch==27:        
            print("\nHow many hearts does an octopus have? \n 1). 6 \t 2). 3 \n 3). 8 \t 4). 4")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is 3")
                print(a,"your score")
                break
        elif ch==28:        
            print("\nIn which year was the Microsoft XP operating system released? \n 1). 2001 \t 2). 1947 \n 3). 2005 \t 4). 2011")
            choose=int(input("Enter your choice..."))
            if choose==1:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is 2001 ")
                print(a,"your score")
                break
        elif ch==29:
                
            print("\nElon Musk is the CEO of which global brand. \n 1). Google \t 2). Yahoo \n 3). MG Hector\t 4). Tesla")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            
            else  :
                print("This is wrong answer..")
                print("The answer is Tesla")
                print(a,"your score")
                break
        elif ch==30:        
            print("\nWhich operating system does a Google Pixel phone use?\n 1). IOS     \t 2). Window \n 3). Android  \t 4). Linux")
            choose=int(input("Enter your choice..."))
            if choose==3:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Android")
                print(a,"your score")
                break
        elif ch==31:        
            print("\nIn which year was the Nintendo 64 released in Europe?\n 1). 2001 \t 2). 1947 \n 3). 1940 \t 4). 1997")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is 1997 ")
                print(a,"your score")
                break
        elif ch==32:
            print("\nHow much parts Twilight saga series has?\n 1). 4 \t 2). 5 \n 3). 6 \t 4). 10 ")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is 5")
                print(a,"your score")
                break
        elif ch==33:         
            print("\nWho killed Tony Stark’s parents? \n 1).Loki            \t  2). Hulk \n 3).The Winter Soldier \t  4).Captain America")
            choose=int(input("Enter your choice..."))
            if choose==3:
                
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is The Winter Soldier")
                print(a,"your score")
                break
        elif ch==34:        
            print("\nWho is known as the father of Free Software Foundation? \n 1). Stanlley     \t 2). Richard Mathew Stallman \n 3). Tim berlley \t 4). Elon mask")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Richard Mathew Stallman ")
                print(a,"your score")
                break
        elif ch==35:
            print("\nWhat is the highest-grossing Marvel movie without the word ‘Avengers’ in the title?\n 1). Thor        \t 2). Captain America \n 3). Spider man \t 4). Black Panther")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Black panther ")
                print(a,"your score")
                break
        elif ch==36:
            print("\nIn which year was computer graphics oringinated?\n 1). 2001 \t 2). 1947 \n 3). 1940 \t 4). 1980")
            
            choose=int(input("Enter your choice..."))
            if choose==3:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is 1940")
                print(a,"your score")
                break
        elif ch==37:
            print("\nWhat is the name of India’s first indigenous supercomputer developed by CDAC named?\n 1). Agni \t 2). Param \n 3). Mark1 \t 4). Insat1")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Param")
                print(a,"your score")
                break
        elif ch==38:
            print("\nNatasha Romanova is the real name of which superhero? \n 1). Valkyire \t 2). Wanda \n 3). Gamoura \t4). Black Widow")
            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Black widow ")
                print(a,"your score")
                break
        elif ch==39:
            print("\nWho invented Computer Mouse?  \n 1). Doughles Engelbert \t 2). Richard Mathew Stallman \n 3). Josh Brolin        \t 4). Robert Downey ")
            choose=int(input("Enter your choice..."))
            if choose==1:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Doughles Engelberth")
                print(a,"your score")
                break
        else :
            print("\n‘WIT’ is the NASDAW code of which Indian IT company?\n 1).Infosys \t 2).Accenture  \n 3).Wipro   \t 4).Flipkart")
            choose=int(input("Enter your choice..."))
            if choose==3:
                
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Wipro ")
                print(a,"your score")
                break
   

def quiz2():
    a=160
    for i in range  (8):
        
    
        ch=random.randint(1,8)
        
        
        if ch==1:
            
            print("When does India celebrate Independence Day? \n 1). 15th August \t 2). 2nd October \n  3). 26th January \t4. 4th July")
	
            choose=int(input("Enter your choice..."))
            
            if choose==1:
                
                print("This is Correct answer")
                
                a=( a + 10)
                
                print(a,"you win")
                
            else:
                
                print("This is wrong answer..")
                print("The answer is 15th August")
                print(a,"your score")
                break
            
        elif ch==2:
            
            print("Nobel prize is awarded for which of the following disciplines? \n 1. Literature, peace and economics\t 2. Medicine or Physiology \n 3. Chemistry and Physics \t 4. All the above")

            choose=int(input("Enter your choice..."))
            if choose==4:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is all of the above")
                print(a,"your score")
                break
                
        elif ch==3:   
            print("\nWhich state has Introduced new kin technology? \n 1). Assam       \t 2). Delhi  \n 3). Haryana \t 4). Punjab")
            choose=int(input("Enter your choice..."))
            
            if choose==4:
                
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is punjab")
                print(a,"your score")
                break
        elif ch==4:
            print("\nWho has won pro Kabadi League this season? \n 1).Dabang Delhi   \t 2). Bengal Warriors \n 3).Puneri paltan \t 4). U Mumba")
            choose=int(input("Enter your choice..."))
            
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Bengal Warriors ")
                print(a,"your score")
                break
        elif ch==5: 
            print("\nFirst private train in India run between which of the two cities? \n 1).Delhi-Lucknow\t 2).Delhi-Ahmedabad\n 3).Both of the above route \t 4). None of the above")
            
            choose=int(input("Enter your choice..."))
            if choose==1:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else:
                print("This is wrong answer..")
                print("The answer is Delhi-Lucknow")
                print(a,"your score")
                break
                
        elif ch==6:        
            print("\nAs per a latest report by Brand Finance 2019, which is the India's most valuable brand? \n 1). Reliance   \t 2). Tata Group \n 3). State bank of india    \t 4).Flipkart")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else:
                print("This is wrong answer..")
                print("The answer is Tata Group" )
                print(a,"your score")
                break
                
        elif ch==7:        
            print("\nAt the end of March 2019, what was the amount of India's external debt? \n 1).US $ 540 billion  \t 2).US $ 543 billion \n 3).US $ 547 billion    \t 4).US $ 541 billion")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is US $ 543 billion")
                print(a,"your score")
                break
                
        else:        
            print("\n'LIBRA' an alternative of existing cryptocurrency like bitcoin is being developed by?\n 1).Facebook \t 2). Google \n 3).Microsoft \t 4). None of the above ")
            choose=int(input("Enter your choice..."))
            if  choose==1:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Facebook")
                print(a,"your score")
                break
                
def quiz3():
    a=240
    for i in range  (10):
        
    
        ch=random.randint(1,10)
        
        
        if ch==1:
            
            print("In which year was Sports Authority of India established?\n 1). 1952 \t 2). 1967 \n  3). 1993 \t 4).1982")
	
            choose=int(input("Enter your choice..."))
            
            if choose==4:
                
                print("This is Correct answer")
                
                a=( a + 10)
                
                print(a,"you win")
                
            else:
                
                print("This is wrong answer..")
                print("The answer is 1982")
                print(a,"your score")
                break
            
        elif ch==2:
            
            print("Headquater of International Olympic Committee is situated at? \n 1. Athens\t 2. Lausanne \n 3. Dubai \t 4. All the above")

            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Lausanne")
                print(a,"your score")
                break
                
        elif ch==3:   
            print("\nThe Coalition Years' is the autobiography of? \n 1). L.K Advani      \t 2). Pranab Mukherjee \n 3). Atal Behari Vajpayee \t 4). Sonia Gandhi")
            choose=int(input("Enter your choice..."))
            
            if choose==2:
                
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Pranab Mukherjee")
                print(a,"your score")
                break
        elif ch==4:
            print("\nWhich Indian revolutionary leader is known as 'Bagha Jatin'?\n 1).Jatindranath Mukherjee   \t 2). Jatindranath Bannerjee \n 3).atindranath das \t 4).atindranath bose")
            choose=int(input("Enter your choice..."))
            
            if choose==1:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Jatindranath Mukherjee")
                print(a,"your score")
                break
        elif ch==5: 
            print("\nGarampani Sanctuary is locate in which of the following places? \n 1).Junagarh, Gujarat\t 2).Diphu, Assamn \n3).Both of the above route \t 4). None of the above")
            
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else:
                print("This is wrong answer..")
                print("The answer is Diphu, Assam")
                print(a,"your score")
                break
                
        elif ch==6:        
            print("\nEntomology studies what?\n 1). Behavior of human beings  \t 2). Insects \n 3). The formation of rocks    \t 4).The origin and history of technical and scientific terms")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else:
                print("This is wrong answer..")
                print("The answer is Insects" )
                print(a,"your score")
                break
                
        elif ch==7:        
            print("\nGalileo was an astronomer who \n 1).Developed the telescope  \t 2).Discovered four satellites of Jupiter \n 3).  All the above  \t 4).discovered that the movement of pendulum produces a regular time measurement")
            choose=int(input("Enter your choice..."))
            if choose==2:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Discovered four satellites of Jupiter")
                print(a,"your score")
                break
        elif ch==8:        
            print("\nWho is the father of geometry? \n 1). Aristotle \t 2).Pythagoras\n 3).Euclid   \t 4).Kepler")
            choose=int(input("Enter your choice..."))
            if choose==3:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Euclid")
                print(a,"your score")
                break
        elif ch==9:        
            print("\nThe Government of which state has instituted the 'Tansen Samman'? \n 1).Madhya Pradesh  \t 2).Bihar \n 3). Gujrat    \t 4).West Bengal")
            choose=int(input("Enter your choice..."))
            if choose==1:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else :
                print("This is wrong answer..")
                print("The answer is Madhya Pradesh")
                print(a,"your score")
                break
                                
        else:        
            print("\n'Madhya Pradesh Chief Minister Kamal Nath has declared that Bhopal metro will be known as?\n 1).Bhoj Metro \t 2). Khoj Metro \n 3).Bhopal Metro \t 4). Auranga Metro ")
            choose=int(input("Enter your choice..."))
            if  choose==1:
                print("This is Correct answer")
                a=( a + 10)
                print(a,"you win")
            else  :
                print("This is wrong answer..")
                print("The answer is Bhoj Metro")
                print(a,"your score")
                break
                
def rating():
    print("give us a  rating on a basis of  1 to 5....")
    rate=int(input("enter rating==="))
    if rate==1:
        print("sorry for inconvinence")
        print("we will try our best to full fill your requirements..")
    elif rate==2:
        print("sorry for inconvinence")
        print("we will try our best to full fill your requirements..")
    elif rate==3:
        print("sorry for inconvinence")
        print("we will try our best to full fill your requirements..")
    elif rate==4:
        print("thanxs for giving us  your valuable time")
        print("we will try our best to full fill your requirements..")
    elif rate==5:
        print("thanxs for giving us  your valuable time")
        print("we will try our best to full fill your requirements..")
    
def developer():
    
    print("To see the developer details  press 1 \n else press 2.....\n ")
    d=int(input("Do you want to see details of developer......... "))
    if d==1:
        print("PROJECT ASSIGN BY PROF. SHWETA JOSHI ...... ")
        print("RITIK KUMAR  has developed this game ...")
        print("Gmail= rk2398419@gmail.com   \n")
        print("Any details about game  and code send your queries on above mails..... ")
        print("Thanxs for using")
    else :
        print("Thanxs for using")
    
welcome()
instruction()
a=0
quiz()

if a==160:
    print("welcome to level 2...")
    a+=10
    quiz2()
   
if a==240:    
    print("welcome to level 3...")
    a+=10
    quiz3() 

else:
    print("better luck next time....")
print("________________") 
print("thanxs for playing ")
rating()
print("we hope u enjoy this game")
print("________________")

developer()

print("________________")