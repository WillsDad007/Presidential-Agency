import time

username = input("Hello, Welcome to Presidential Agency. To get started, please enter a username: ")
password = input("Please enter a password: ")

print("Processing.....")
time.sleep(2)
print("Account Created")
time.sleep(3)

print("Please login to Presidential Agency")
time.sleep(1)
if username == (input("Hello, please enter a username: ")):
    if password == (input("Please enter a password: ")):
        print("Processing.....")
        time.sleep(2)
        print("Access Granted")
        
    else:
        print("Processing.....")
        time.sleep(2)
        print("Access Denied, Launching Nuclear Attack")
        quit()
else:
    print("Processing.....")
    time.sleep(2)
    print("Access Denied, Launching Nuclear Attack")
    quit()
    
Action = input("Launch Missiles, Request Supplies, Open Digital Library or Log Out? ")

if Action == "Launch Missiles":
    print("Processing.....")
    time.sleep(2)
    Target = input("Choose a Target ")
    print("Processing.....")
    time.sleep(2)
    print("Deploying Missiles, Please Wait")
    time.sleep(3)
    print(Target + " Destroyed")
    

elif Action == "Request Supplies":
    print("no")
    time.sleep(1)
    print("Self Destructing In")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Goodbye...")
    quit()
    
    
elif Action == "Log Out":
    print("Processing.....")
    time.sleep(2)
    print("Logging Out")
    time.sleep(1)
    print("they are coming for you")
    print("Processing.....")
    time.sleep(2)
    quit()
    
elif Action == "Open Digital Library":
    time.sleep(1)
    print("Read a Real Book")
    
else:
    print("ERROR CRITICAL ERROR ERASING ALL DATA")
    quit()
   
time.sleep(2)

Continue = input("Would you like to continue, Yes or No? ")

if Continue == "No":
    quit()

else:
    print("ERROR CRITICAL ERROR ERASING ALL DATA")
    time.sleep(1)
    quit
    
Action = input("Launch Missiles, Request Supplies, Open Digital Library or Log Out? ")

if Action == "Launch Missiles":
    print("Processing.....")
    time.sleep(2)
    Target = input("Choose a Target ")
    print("Processing.....")
    time.sleep(2)
    print("Deploying Missiles, Please Wait")
    time.sleep(3)
    print(Target + " Destroyed")
    

elif Action == "Request Supplies":
    print("no")
    time.sleep(1)
    print("Self Destructing In")
    print(3)
    time.sleep(1)
    print(2)
    time.sleep(1)
    print("1")
    time.sleep(1)
    print("Goodbye...")
    quit()
        
        
elif Action == "Log Out":
    print("Processing.....")
    time.sleep(2)
    print("Logging Out")
    time.sleep(1)
    print("they are coming for you")
    print("Processing.....")
    time.sleep(2)
    quit()
        
elif Action == "Open Digital Library":
    time.sleep(1)
    print("Read a Real Book")
        
else:
    print("ERROR CRITICAL ERROR ERASING ALL DATA")
    quit()
       
    time.sleep(2)