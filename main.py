class Car(object):
    def __init__(self, name, colour, company):
        self.name: name
        self.colour: colour
        self.company: company
    
    def Start(self):
        print("The car is starting now")
    
    def Stop(self):
        print("The car is stopping now")
    
    def Accelerate(self):
        print("The car is speeding up")

    def Decelerate(self):
        print("The car is slowing down")

    def Gear(self):
        print("The car is going to change gear")
        gear = input("Enter the gear you want your car to change to")
        if(gear == "1"):
            print("Gear changed to 1")
        elif(gear == "2"):
            print("Gear changed to 2")
        elif(gear == "3"):
            print("Gear changed to 3")
        elif(gear == "4"):
            print("Gear changed to 4")
        elif(gear == "5"):
            print("Gear changed to 5")
        elif(gear == "6"):
            print("Gear changed to 6")
        else:
            print("Invalid gear number")
    
    def TellName(self, Name):
        return self.name 

Jeep = Car("JEEP COMPASS", "WHITE AND BLACK", "JEEP")
Jeep.Start()
Jeep.Accelerate()
Jeep.Gear()
Jeep.Decelerate()
Jeep.Stop()