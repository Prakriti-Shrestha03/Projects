import time
import random 

PET_FILE="petfile.txt"

def save_to_file(i,new_data1,new_data2,new_data3):
     with open(PET_FILE,'r') as File:
        data=File.read()
        data=data.split() 
        if new_data1>100:
             data[i+1]=100
        elif new_data1<0:
             data[i+1]=0
        else:
             data[i+1]=new_data1
        if new_data2>100:
             data[i+2]=100
        elif new_data2<0:
             data[i+2]=0
        else:
             data[i+2]=new_data2
        if new_data3>100:
             data[i+3]=100
        elif new_data3<0:
             data[i+3]=0
        else:
             data[i+3]=new_data3

        new_data=""
        for x in data:
            new_data=new_data+" "+str(x)

     with open(PET_FILE,'w') as File:
          File.write(new_data)

     print(f"the stats: \n Hunger={data[i+1]}  Happiness={data[i+2]}  Energy={data[i+3]}")
     
     
     

def feed_pet(pet_name):
    """To feed the pet to increase hunger"""
    
    print("You can feed your pet the following foods:")
    print("1.Burger (+10 hunger +0 happiness)")
    print("2.Pizza (+10 hunger +0 happiness)")
    print("3.Ice Cream (+5 hunger +5 happiness)")
    print("4.Medicine (+20 hunger -5 happiness)")
    choice=input("Enter your choice (1/2/3/4):")
    with open(PET_FILE,"r") as File:
             data=File.read()
             data=data.split()
             i=0
             for index,elements in enumerate(data):
                  if elements==pet_name:
                       i=index
    data[i+1]=int(data[i+1])
    data[i+2]=int(data[i+2])
    data[i+3]=int(data[i+3])
             
    if choice=="1":
            data[i+2]+=0
            data[i+1]+=10
    elif choice=="2":
            data[i+2]+=0
            data[i+1]+=10
    elif choice=="3":
           data[i+2]+=5
           data[i+1]+=5
    elif choice=="4":
            data[i+2]-=5
            data[i+1]+=20
    else:
            print("No such choice exists")
    x=input("do you want to save?").lower()
    if x=="yes":
         save_to_file(i,data[i+1],data[i+2],data[i+3])
    


def play_time(pet_name):
    """Energy decrease and Happiness Increase""" 
    print("Let's play with a ball")
    randoms=["toy","no toy"]
    while True:
        choice=input("Throw the ball to your pet(yes/no)").lower()
        if choice=="yes":
            print("The pet fetches it and brings it back to you(+5 Happiness -5 Energy)")
            with open(PET_FILE,"r") as File:
             data=File.read()
             data=data.split()
             i=0
             for index,elements in enumerate(data):
                  if elements==pet_name:
                       i=index
             data[i+1]=int(data[i+1])
             data[i+2]=int(data[i+2])
             data[i+3]=int(data[i+3])
             data[i+2]+=5
             data[i+3]-=5
             x=random.choice(randoms)
             if x=="toy":
                  data[i+2]+=5
                  print("Your pet found a toy +5 happiness")
        elif choice=="no":
            print("I guess enough playing for today")
            break
        x=input("do you want to save?").lower()
        if x=="yes":
            save_to_file(i,data[i+1],data[i+2],data[i+3])

def nap_time(pet_name):
    """Energy increase  Happiness Decrease and Happiness Decrese""" 
    print("Let's take a nap. Your pet shall nap until it is fully rested")
    while True:
         time.sleep(2)
         print("+10 Energy -2 Happiness -2 Hunger ")
         with open(PET_FILE,"r") as File:
             data=File.read()
             data=data.split()
             i=0
             for index,elements in enumerate(data):
                  if elements==pet_name:
                       i=index
             data[i+1]=int(data[i+1])
             data[i+2]=int(data[i+2])
             data[i+3]=int(data[i+3])
             data[i+1]-=2
             data[i+2]-=2
             data[i+3]+=10
             
         x=input("do you want to save?").lower()
         if x=="yes":
            save_to_file(i,data[i+1],data[i+2],data[i+3]) 

         if(data[i+3]==100):
             print("Fully rested")
             break


def gameplay():
    """The main game play """
    print("Let's meet your pet")
    pet_name=input("Enter your pet's name:").strip()

    with open(PET_FILE,"a") as File:
        pass 
    
    with open(PET_FILE,"r") as File:
        data=File.read()
        data=data.split()
        
    if pet_name in data:
         print("Welcome Back")
    else:
        print("Congrats on adopting a new pet..")
        with open(PET_FILE,'a') as File:
            Hunger=50
            Happiness=50
            Energy=50
            File.write("\n" + pet_name )
            File.write(" " + str(Hunger))
            File.write(" " + str(Happiness))
            File.write(" " + str(Energy))
    
    with open(PET_FILE,"r") as File:
             data=File.read()
             data=data.split()
             i=0
             for index,elements in enumerate(data):
                  if elements==pet_name:
                       i=index
             data[i+1]=int(data[i+1])
             data[i+2]=int(data[i+2])
             data[i+3]=int(data[i+3])
    
    while True:
        starting_time=time.time()
        endTime=starting_time+10
        print("What would you like to do with your pet:")
        print("1.Feed your pet")
        print("2.Play with your pet")
        print("3.It's Nap Time")
        print("4.Exit")
        
        with open(PET_FILE,"r") as File:
             data=File.read()
             data=data.split()
             i=0
             for index,elements in enumerate(data):
                  if elements==pet_name:
                       i=index
             data[i+1]=int(data[i+1])
             data[i+2]=int(data[i+2])
             data[i+3]=int(data[i+3])
             if (data[i+1]==0 or  data[i+2]==0 or  data[i+3]==0):
                print("Your pet died of negligence. Game Over")
                break
    
             elif( data[i+1]>80 and  data[i+2]>80 and  data[i+3]>80):
                print("Your pet is satisfied. You win")
                break

        choice=input("Enter your choice (1/2/3/4):").strip()

        if time.time()>endTime:
            print("Too Slow")
            break

        if choice=="1":
            feed_pet(pet_name)
        elif choice =="2":
            play_time(pet_name)
        elif choice=="3":
            nap_time(pet_name)
        elif choice=="4":
            print("Thank you for playing")
            break
        else:
            print("No such choice exists")


def display_pet_stat():
    with open(PET_FILE,"r") as File:
             data=File.read()
             data=data.split()

             for i in range(0,len(data),4):
                  if i+3<len(data):
                       print(f"\n Pet Name={data[i]} Hunger={data[i+1]} Happiness={data[i+2]} Energy={data[i+3]}")

def main():
    print("Welcome, Come inside to meet your virtual pet")
    while True:
        print("==Game Menu==")
        print("1.Adopt/Return to your pet")
        print("2.Check your pet's stats")
        print("3.Exit")
        choice=input("Enter your choice (1/2/3):").strip()

        if choice =="1":
            gameplay()
        elif choice=="2":
            display_pet_stat()
        elif choice =="3":
            print("Thank you for playing")
            break
        else:
            print("No such choice exists")

        
if __name__=="__main__":
    main()
