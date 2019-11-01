i={'10.1.24.48':'10:FF:54:65','10.2.56.98':'10:YY:76:UT'}
print("   IP   :   MAC ",end="\n")
for x in i:
        print(x,':',i[x])        
y=input("enter the IP address")
print(y,"the mac is",i[y])

