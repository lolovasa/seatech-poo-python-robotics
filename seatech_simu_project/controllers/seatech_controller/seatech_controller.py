from time import sleep
import os

from controller import Robot, Motor, Keyboard, Camera, CameraRecognitionObject


class RobotCamera(Camera):
    def __init__(self):
        super().__init__('camera')
        self.enable(samplingPeriod=50)
        self.recognitionEnable(samplingPeriod=100)
        
    def detect_red(self):
        objs =self.getRecognitionObjects()
        for obj in objs:
            if obj.get_colors()== [1, 0, 0]:
                return True
        return False
    
    def detect_green(self):
        objs =self.getRecognitionObjects()
        for obj in objs:
            if (obj.get_colors()== [0, 1, 0]):
                return True
        return False
    
    

            

    

class RobotMotor(Motor):
    def __init__(self, name):
        super().__init__(name)
        self.setPosition(float('inf'))
        self.setVelocity(0)
        

    
class SeatechRobot(Robot):
    def __init__(self):
        super().__init__() 
        self.camera=RobotCamera()
        self.leftMotor = RobotMotor('left wheel motor')
        self.rightMotor = RobotMotor('right wheel motor')    

    def run(self):
        self.leftMotor.setVelocity(MAX_SPEED)
        self.rightMotor.setVelocity(MAX_SPEED)
    
    def right(self):
        self.leftMotor.setVelocity(MAX_SPEED)
        self.rightMotor.setVelocity(LOW_SPEED)
    
    def left(self):
        self.leftMotor.setVelocity(LOW_SPEED)
        self.rightMotor.setVelocity(MAX_SPEED)

    def stop(self):
        self.leftMotor.setVelocity(LOW_SPEED)
        self.rightMotor.setVelocity(LOW_SPEED)
    
    def fuit(self):
        self.leftMotor.setVelocity(-0.5*MAX_SPEED)
        self.rightMotor.setVelocity(-MAX_SPEED)

    


    def check_environnement(self):
        if self.camera.detect_red():
            print("cours poto fuiiiittt")
            robot.fuit()
           
            

        elif self.camera.detect_green():
            print("nique le")
            robot.run()
        
        else :
            print("tranquille mon reuf")
            robot.right()
            

if __name__=='__main__':
    TIME_STEP = 64
    MAX_SPEED = 6.28 
    LOW_SPEED = 0

    

# create the Robot instance.
robot = SeatechRobot()
print('hello')
print('some more keyboard')
keyboard= Keyboard()
keyboard.enable(samplingPeriod=100)
#robot.run()
while robot.step(TIME_STEP) != -1:
    robot.check_environnement()
    
    key=keyboard.getKey()
    if key == keyboard.UP:
        robot.run()
        print("avance")
        
    elif key == keyboard.LEFT:
        robot.left()
        print("tourne a gauche ")
        
    elif key==keyboard.RIGHT:
        robot.right()
        print("tourne a droite")

    elif key==keyboard.DOWN:
        robot.stop()
        print("arrete toi paysans")
          
pass
