from RobotArm import RobotArm

robotArm = RobotArm('exercise 8')

# Jouw python instructies zet je vanaf hier:

#for x in range():
robotArm.moveRight();
robotArm.drop();
robotArm.grab();
for i in range(7):
    for x in range(8):
        robotArm.moveRight();
    robotArm.drop();
    for i in range(8):
        robotArm.moveLeft();
    robotArm.drop();
    robotArm.grab();


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()