


class Robot:
    SERVO_MIDDLE_STATE = 80
    SERVO_START_STATE = 70
    SERVO_END_STATE = 90

    MOTOR_NUMBER = 6
    SERVO_NUMBER = 6

    SERVO_COMMAND = "s,{servoIndex},{servoPos}"
    MOTOR_COMMAND = "m,{motorIndex},{motorSpeed},{motorDirection}"
    ULTRASONIC_COMMAND = "ultra"
    SPEED_LIMIT = 800


    initMotorState = (0, 0)  # Speed ( 0-1000 ), Direction (0,1)
    initServoState = 0
    servoState = []
    motorState = []
    
    def __init__(self):
        self.commandQueue = []
        self.initServos()
        self.initMotors()
        
    def initServos(self):
        for _ in range(0,self.SERVO_NUMBER):
            self.servoState.append(self.initServoState)
            
    def initMotors(self):
        for _ in range(0, self.MOTOR_NUMBER):
            self.motorState.append(self.initMotorState)
    
    def simpleRotate(self,position):
        if position < self.SERVO_START_STATE or position > self.SERVO_END_STATE : return
        diff = position - self.SERVO_MIDDLE_STATE

        self.setServo(0, self.SERVO_MIDDLE_STATE+diff)
        self.setServo(3, self.SERVO_MIDDLE_STATE+diff)

        self.setServo(1, self.SERVO_MIDDLE_STATE-diff)
        self.setServo(2, self.SERVO_MIDDLE_STATE-diff)

    def setAllMotor(self, speed, direction):
    #    // for index in range(0,self.MOTOR_NUMBER):
       self.setMotor(0, speed, direction)

    def setMotor(self,index,speed,dir):
        speed = int(speed)
        if self.motorState[index] == (speed,dir): return
        # print("prev: "+str(self.motorState[index][0]) + "now: "+str(speed))
        # if self.motorState[index][0]+20 < speed or self.motorState[index][0]-20 > speed:
            # if speed >= self.SPEED_LIMIT:
            #     speed = self.SPEED_LIMIT
        self.motorState[index] = (speed,dir)
        self.createCommand(self.MOTOR_COMMAND.format(motorIndex = index,motorSpeed = speed,motorDirection = dir))

    def setServo(self,index,position):
        position = int(position)
        if self.servoState[index] == position: 
            return
        self.servoState[index] = position
        self.createCommand(self.SERVO_COMMAND.format(servoIndex = index,servoPos = position))

    def createCommand(self,text):
        self.commandQueue.append(text)
