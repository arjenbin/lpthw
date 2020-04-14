#Make array with some standard cars in it
arrayCars = ['merc', 'volvo', 'bmw']

#Get car from array
def getCar(LineRequest):
    CurrentCar = arrayCars[LineRequest]
    print(CurrentCar)
    EnterCommand()
    
#Write car to array
def setCar(LineRequest, NewCar):
    arrayCars[LineRequest] = NewCar
    EnterCommand()
    
#Check if user input was correct    
def CheckCommand(Command,Check):
    return Command.lower() == Check.lower():

#Check if user input was correct    
def CheckLine(Command,Check):
    return int(Command) < Check:
 
#Try again message
def TryAgain():
    print("Try again")
    EnterCommand() 
    
#Get user command    
def EnterCommand():  
    UserCommand = input('Request Car = R, Edit Car = E:')
    
    if CheckCommand(UserCommand,'r'):
        LineRequest = input('enter line request:')
        if CheckLine(LineRequest, len(arrayCars)):
            getCar(int(LineRequest))
        else:
            TryAgain()
    if CheckCommand(UserCommand,'e'):
        LineRequest = input('enter line to edit:')
        if CheckLine(LineRequest, len(arrayCars)):
            NewCar = input('enter new Car brand:')
            setCar(int(LineRequest),NewCar)
        else:
            TryAgain()
    else:
        TryAgain()
        
#Main    
EnterCommand()
