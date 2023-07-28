command = ""
started = False
while True:                          #using while command True mean as far as the command below is true then continue
    command = input("> ").upper()
    if command == "HELP":
        print("""
start - to start the car
stop  - t0 stop the car
quit  - t0 exit  
         """)
    elif command == "START":
        if started:
            print("car already started")
        else:
            started = True
            print("Car start")

    elif command == "STOP":
        if not started:
            print("car is already stopped")
        else:
            started = False
            print("car stopped")

    elif command == "QUIT":
        break
    else:
        print("Invalid command")
