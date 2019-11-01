i={'10.1.24.48':'10:FF:54:65','10.2.56.98':'10:YY:76:UT'}
print("   IP   :   MAC ",end="\n")
for x in i:
        print(x,':',i[x])
z=input("enter the mac")
for x in i:
        if z==i[x]:
                print(z,"the ip is",x)

