"""
</>
Programmer: Mehroj Majidov
Github: https://github.com/MehrojOfficial
Title: "Password Generator"
</>
"""
import random

numbers = ['0','1','2','3','4','5','6','7','8','9']
letters_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
letters_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
symbols = ['!','@','#','$','%','^','&','*','(',')','_','+','=','-',"|",'`','~','<','>','/','{','}','[',']','?',':',';']

result = []

def number():
    global result
    result.append(random.choice(numbers))

def letter_up():
    global result
    result.append(random.choice(letters_upper))

def letter_low():
    global result
    result.append(random.choice(letters_lower))

def symbol():
    global result
    result.append(random.choice(symbols))

def listToString(s): 
    str1 = ""  
    return (str1.join(s))

def mixture(numberv,symbolv,letter_lowv,letter_upv,lent):
    global result
    result=[]
    limit = int(lent)
    while True:
        if numberv:
            if len(result) < limit:
                number()
            else:
                break

        if symbolv:
            if len(result) < limit:
                symbol()
            else:
                break
            
        if letter_upv:
            if len(result) < limit:
                letter_up()
            else:
                break
            
        if letter_lowv:
            if len(result) < limit:
                letter_low()
            else:
                break
            
    random.shuffle(result)
    return listToString(result)