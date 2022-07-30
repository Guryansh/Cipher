#This version can do infinite comination of two keys
print("Welcome to Cryptobuild By GS")
start=input("What do you wanna do?")

def e():
    lock=input("Please put Cipher lock:")
    print('Rule:Only numeric and lower case letters are allowed')
    value=input("Please put value to encrypt:")
    value.lower()
    lock=[x for x in lock]
    for i in lock:
        if int(i)==0:
            value=lock0(value)
        elif int(i)==1:
            value=lock1(value)
        elif int(i)==2:
            value=lock2(value)
        elif int(i)==3:
            value=lock3(value)
        elif int(i)==4:
            value=lock4(value)
        elif int(i)==5:
            value=lock5(value)
        elif int(i)==6:
            value=lock6(value)
        elif int(i)==7:
            value=lock7(value)
        elif int(i)==8:
            value=lock8(value)
        elif int(i)==9:
            value=lock9(value)
    return value

def lock1(value):
    list1=[x for x in value]
    for i in list1:
         snake={'a':'0','b':'1','c':'2','d':'3','e':'4','f':'5','g':'6','h':'7','i':'8','j':'9'}
         key_snake = list(snake.keys())
         val_snake = list(snake.values())
         if str(i) in val_snake:
             j=int(i)
             pS = val_snake.index(str(j))
             p=list1.index(i)
             list1[p]=key_snake[pS]+'&'
    list1=''.join([str(elem) for elem in list1])
    return list1

def lock2(value):
    list3=[x for x in value]
    for i in range(len(list3)):
        index=int(i+i)
        from random import randint
        x=randint(0,9)
        list3.insert(index,x)
    list3=''.join([str(elem) for elem in list3])
    return list3

def d():
    key=input("Please put Cipher key:")
    value=input("Please put value to decrypt:")
    key=[x for x in key]
    key.reverse()
    for i in key:
        if int(i)==0:
            value=key0(value)
        elif int(i)==1:
            value=key1(value)
        elif int(i)==2:
            value=key2(value)
        elif int(i)==3:
            value=key3(value)
        elif int(i)==4:
            value=key4(value)
        elif int(i)==5:
            value=key5(value)
        elif int(i)==6:
            value=key6(value)
        elif int(i)==7:
            value=key7(value)
        elif int(i)==8:
            value=key8(value)
        elif int(i)==9:
            value=key9(value)
    return value

def key1(value):
    list1=[x for x in enumerate(value)]
    nlist1=[]
    for i in list1:
         snake={'0':'a','1':'b','2':'c','3':'d','4':'e','5':'f','6':'g','7':'h','8':'i','9':'j'}
         key_snake = list(snake.keys())
         val_snake = list(snake.values())
         (a,b)=i
         p=list1.index(i)
         if str(b) in val_snake and p+1<len(list1) and list1[p+1]==(int(a+1),'&'):                                   
             pS = val_snake.index(b)
             nlist1.insert(int(a),int(key_snake[pS]))
             list1.pop(p+1)
         else:
             nlist1.insert(int(a),b)
    list1=''.join([str(elem) for elem in nlist1])
    return list1
    
def key2(value):
    import numpy as np
    list3=[x for x in value]
    x=len(list3)
    x=x/2
    for i in np.arange(0,x,1):
        j=int(i)
        del list3[j]
    list3=''.join([str(elem) for elem in list3])
    return list3 

if start=='d':
    print('Launching program to decrypt')
    decrypted=d()
    print(decrypted)
    
elif start=='e':
    print('Launching program to encrypt')
    encrypted=e()
    print(encrypted)

elif start=='exit':
    exit()
