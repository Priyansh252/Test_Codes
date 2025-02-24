import random

hexlist = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
# print(len(hexlist))
# subcode=hexlist[random.randint(0,16)]
outlis1=[]
flag1=0
count=0
flag2=0
relist=[]
# flag3=0
outlis2=[]
ask0=input("if decryption: type 1 or encryption type 2: ")
if(ask0=="1"):
    with open('otp.txt','a+') as file:
        ask=input("write : ")
        for x in ask:
            outlis1.append(hexlist[random.randint(0,15)])
            outlis2.append(hexlist[random.randint(0,15)])

        file.write(f"{''.join(outlis1)} {''.join(outlis2)}{ask}\n")
        print(f"Generated Key (Hex): {''.join(outlis1)}\nCiphertext (Hex): {''.join(outlis2)}")
        
elif (ask0=="2"):
    with open('otp.txt','r') as file:
        ask1=input("give Generated Key (Hex): ")  
        ask2=input("Give Ciphertext (Hex): ")
        ask3=ask1+" "+ask2
        
        # print(ask3)
        for x in file.readlines():
            # print(x)
            if(ask3 not in x):
                relist.append(x)

            if(ask3 in x):
            
                print(x[len(ask3):])
                   
            else:
                print("Invalid codes")
            count+=1
    
    with open('otp.txt','w') as file:
        for x in relist:
            file.write(x)
    
else:print("Invalid Input")
           

    
