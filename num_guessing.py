# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 10:46:35 2020

@author: Ricky
"""
# import random
# correct_num=random.randint(1,100)
# abc=int(input("guess number:\t"))
# print("answer is:\t",correct_num)
# score=10
# while abc!=correct_num  :
    
    
     
#     if abc>correct_num:
#         # print("guess is gr then  number-")
#         abc=int(input("guess a sm number "))
#         score=score-1
#     if abc<correct_num:
#         # print("guess is sm then number")
#         abc=int(input("guess a gr number"))
#         score=score-1
#     # else: 
#     #     print("your guess is equal to number")    
#     #     print(correct_num,"=",abc,"u win ")
# print("your score -",score)
import random 
num=random.randint(1,100)
abc=int(input("guess number:\t"))
print("answer is:\t",num)
score=10
while abc!=num:
    
     
    if abc>num:
        abc=int(input("guess smaller num:\t"))
        score=score-1
      
    elif abc<num: 
        abc1=int(input("guess greater num:\t"))
        score=score-1
    else:
        print("correct guessed")
        
print("Final score:\t:",score)               