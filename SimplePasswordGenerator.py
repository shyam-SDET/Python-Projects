import random,string
def shuffle(string):
    tempList=list(string)
    random.shuffle(tempList)
    return ''.join(tempList)
uppercaseLetter1=chr(random.randint(65,90))
uppercaseLetter2=chr(random.randint(65,90))
lowercaseLetter1=chr(random.randint(97,122))
lowercaseLetter2=chr(random.randint(97,122))
digit1=chr(random.randint(48,57))
digit2=chr(random.randint(48,57))
symbol1=random.choice(string.punctuation)
symbol2=random.choice(string.punctuation)
str=uppercaseLetter1+uppercaseLetter2+lowercaseLetter1+lowercaseLetter2+digit1+digit2+symbol1+symbol2;
print(shuffle(str))
