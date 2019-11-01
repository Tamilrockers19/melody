import random
def main():
    arr=[]
    n=int(input("Enter the Frame size"))
    for i in range(0,n):
        x=int(input("Enter the Frame Element\t"))
        arr.append(x)
    y=int(input("Enter the Window size"))
    ran=random.randint(0,y)
    print("\nWindow Frames\n")
    for i in range(0,y):
        if(i!=ran):
            print("Frame :",arr[i],"received")
            print("Acknowledgement received for Frame",arr[i],"\n")
        else:
            print("Frame :",arr[ran],"not received")
            print("Acknowledgement not received for Frame",arr[ran],"\n")
    number=ran+y
    print("\nWindow Frames\n")
    for i in range(ran,number):
            print("Frame :",arr[i],"revceived")
            print("Acknowledgement received for Frame",arr[i],"\n")
    final=number+y
    print("\nWindow Frames\n")
    for i in range(number,final):
        print("Frame :",arr[i],"received")
        print("Acknoweledgement received for Frame",arr[i],"\n")
    print("\nWindow Frames\n ")
    if(final!=n):
        for i in range(final,n):
            if (i!=(final+y)):
                print("Frame :",arr[i],"received")
                print("Acknoweledgement received for Frame",arr[i],"\n")
            else:
                print("\nWindow Frames\n")
                print("Frame :",arr[i],"received")
                print("Acknoweledgement received for Frame",arr[i],"\n")   
if __name__ == '__main__':
    main()
