print("INPUT VALIDATION")
while True:
	try:
	       age=int(input("Please enter age:"))
	except ValueError:
	       print("Please enter valid input")
	       continue
	       
	else:
	       break
	
if age > 20:		
        print("Entered age is : ",str(age)+" more than 18")
