import random
count=0
while(count<=100):
	n=input("enter r to roll a dice")
	if(n=='r'):
		a=random.randint(1,6)
		count=count+a
		print("my position",count)
		print("your random value",a)
	if(count==8):
		count=37
		print("hiphip ladder")
	elif(count==11):
		count=2
		print("uff snake bite")
	elif(count==13):
		count=34
		print("hiphip ladder")
	elif(count==25):
		count=4
		print("uff sanke bite")
	elif(count==38):
		count=9
		print("uff snake bite")
	elif(count==40):
		count=68
		print("hiphip ladder")
	elif(count==52):
		count=81
		print("hiphip ladder")
	elif(count==65):
		count=46
		print("uf snake bite")
	elif(count==76):
		count=97
		print("hiphip ladder")
	elif(count==89):
	    count=89
	    print("uff snake bite")
	elif(count==93):
	    count=64
	    print("uff snake bite")
	elif(count>100):
		count=count-a
		print("you cant go beyond 100")
	elif(count==100):
	  	print("congrats, won the game")
	  	break
            OUTPUT 
enter r to roll a dicer
my position 2
your random value 2
enter r to roll a dicer
my position 6
your random value 4
enter r to roll a dicer
my position 11
your random value 5
uff snake bite
enter r to roll a dicer
my position 4
your random value 2
enter r to roll a dicer
my position 8
your random value 4
hiphip ladder
enter r to roll a dicer
my position 41
your random value 4
enter r to roll a dicer
my position 44
your random value 3
enter r to roll a dicer
my position 50
your random value 6
enter r to roll a dicer
my position 51
your random value 1
enter r to roll a dicer
my position 56
your random value 5
enter r to roll a dicer
my position 60
your random value 4
enter r to roll a dicer
my position 61
your random value 1
enter r to roll a dicer
my position 65
your random value 4
uf snake bite
enter r to roll a dicer
my position 50
your random value 4
enter r to roll a dicer
my position 55
your random value 5
enter r to roll a dicer
my position 58
your random value 3
enter r to roll a dicer
my position 64
your random value 6
enter r to roll a dicer
my position 68
your random value 4
enter r to roll a dicer
my position 69
your random value 1
enter r to roll a dicer
my position 70
your random value 1
enter r to roll a dicer
my position 75
your random value 5
enter r to roll a dicer
my position 77
your random value 2
enter r to roll a dicer
my position 78
your random value 1
enter r to roll a dicer
my position 83
your random value 5
enter r to roll a dicer
my position 88
your random value 5
enter r to roll a dicer
my position 90
your random value 2
enter r to roll a dicer
my position 96
your random value 6
enter r to roll a dicer
my position 98
your random value 2
enter r to roll a dicer
my position 101
your random value 3
you cant go beyond 100
enter r to roll a dicer
my position 100
your random value 2
congrats, won the game
