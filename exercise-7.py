from RobotArm import RobotArm

robotArm = RobotArm('exercise 7')

# Jouw python instructies zet je vanaf hier:

robotArm.moveRight();
for x in range(1, 10, 2):
    for i in range(6):
        robotArm.grab();
        robotArm.moveLeft();
        robotArm.drop();
        robotArm.moveRight();
    robotArm.moveRight();
    robotArm.moveRight();


# Na jouw code wachten tot het sluiten van de window:
robotArm.wait()