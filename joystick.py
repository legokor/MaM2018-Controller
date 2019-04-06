from robot import Robot

class Joystick:
    JOYSTICK_INDEX = 0

    def __init__(self,pygame):
        
        pygame.joystick.init()

        joystick = pygame.joystick.Joystick(self.JOYSTICK_INDEX)
        joystick.init()
        self.joystick = joystick

    def getPyJoystick(self):
        return self.joystick

    def convertAxisValue(self):
        throttle = self.calculateThrottle(self.joystick.get_axis(1))
        steering = self.calculateSteering(self.joystick.get_axis(0))
        return (throttle,steering)

    def calculateThrottle(self,joyValue):
        #-1 to 1
        return joyValue*-300

    def calculateSteering(self,joyValue):
        joyValue += 1  # 0 - 2
        servoRange = Robot.SERVO_END_STATE - Robot.SERVO_START_STATE
        joyValue *= servoRange/2
        joyValue += Robot.SERVO_MIDDLE_STATE-servoRange/2
        return joyValue

    def control(self,robot):
        (throttle,steering) = self.convertAxisValue()
        direction = 1 if throttle > 0 else 0
        
        robot.setAllMotor(abs(throttle),direction)
        robot.simpleRotate(steering)
        robot.setServo(4,self.calculateSteering(self.joystick.get_axis(2)))
        robot.setServo(5, self.calculateSteering(self.joystick.get_axis(3)))
