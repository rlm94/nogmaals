from RobotArm import RobotArm

robotArm = RobotArm('exercise 10')

# Jouw python instructies zet je vanaf hier:
for a in range(1,6):
    robotArm.grab()

    for x in range(2,13-(a*2)):
        robotArm.moveRight()
        
    robotArm.drop()

    for y in range(9):
        robotArm.moveLeft()

    for i in range(a):
        robotArm.moveRight()
# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()