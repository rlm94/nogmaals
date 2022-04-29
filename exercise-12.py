from RobotArm import RobotArm

robotArm = RobotArm('exercise 12')

# Jouw python instructies zet je vanaf hier:
c = 0

for i in range(9):
    robotArm.grab()
    scanResult = robotArm.scan()
    
    if scanResult != 'red':
        robotArm.drop()
        
    else:
        for i in range(9):
            robotArm.moveRight()
        robotArm.drop()
        for y in range(9-c):
            robotArm.moveLeft()

    robotArm.moveRight()

    c += 1 
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()