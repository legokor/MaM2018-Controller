import pygame
from displayelements import TextPrint, InputBox
from display import Display
from robot import Robot
from joystick import Joystick
from tcpclient import TCPClient
import asyncore
from threading import Thread,Lock,currentThread



def communication(commands,lock):
    tcpClient = TCPClient()
    queue = []
    
    t = currentThread()
    # tcpClient.send("init")
    print("thread started")
    data = tcpClient.recv()
    print(data)
    while getattr(t, "do_run", True):
        lock.acquire()
        if len(commands) > 0:
            for command in commands:
                queue.append(command)
            commands.clear()
        lock.release()
        
        if len(queue) > 0:
            for command in queue:
                tcpClient.send(command)
                data = tcpClient.recv()
                print(data)
            queue.clear()
 

    tcpClient.close()

def main(commands,lock):
    
    robot = Robot()

    #Loop until the user clicks the close button.
    done = False

    # Used to manage how fast the screen updates
    clock = pygame.time.Clock()

    display = Display(pygame)

    # joystick = Joystick(pygame)
    # Get ready to print
    pressedButtons = [0,0,0,0]
    servoPos = 100

    # input_box2 = InputBox(pygame,100, 300, 140, 32)
    queue = []
    # -------- Main Program Loop -----------
    while done==False:
        # EVENT PROCESSING STEP
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT: # If user clicked close
                done=True # Flag that we are done so we exit this loop
            
            # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
            if event.type == pygame.JOYBUTTONDOWN:
                print("Joystick button pressed.")
                # robot.setAllMotor(500,1)
                # robot.simpleRotate(Robot.SERVO_MIDDLE_STATE+5)
                # print(robot.motorState[0]);
                
            if event.type == pygame.JOYBUTTONUP:
                print("Joystick button released.")

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    pressedButtons[0] = 1
                if event.key == pygame.K_DOWN:
                    pressedButtons[1] = 1
                if event.key == pygame.K_RIGHT:
                    pressedButtons[2] = 1
                if event.key == pygame.K_LEFT:
                    pressedButtons[3] = 1
                if event.key == pygame.K_a:
                    robot.setServo(5,40)
                if event.key == pygame.K_s:
                    robot.setServo(5,75)
                if event.key == pygame.K_d:
                    robot.setServo(5,110)
                    
                
        
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    pressedButtons[0] = 0
                if event.key == pygame.K_DOWN:
                    pressedButtons[1] = 0
                if event.key == pygame.K_RIGHT:
                    pressedButtons[2] = 0
                if event.key == pygame.K_LEFT:
                    pressedButtons[3] = 0

            if pressedButtons[0] == 1:
                robot.setAllMotor(800,1)
            elif pressedButtons[1] == 1:
                robot.setAllMotor(800,0)
            else:
                robot.setAllMotor(0,0)

            if pressedButtons[2] == 1:
                robot.simpleRotate(Robot.SERVO_END_STATE)
            elif pressedButtons[3] == 1:
                robot.simpleRotate(Robot.SERVO_START_STATE)
            else:
                robot.simpleRotate(Robot.SERVO_MIDDLE_STATE)

        # joystick.control(robot)
       

        # DRAWING STEP 
        #display.draw(joystick.getPyJoystick())
        display.draw()
        display.showRobotStatus(robot)
        # ALL CODE TO DRAW SHOULD GO ABOVE THIS COMMENT
        
        if len(robot.commandQueue) > 0:
            for command in robot.commandQueue:
                queue.append(command)
            robot.commandQueue.clear()

        if len(queue) > 0:
            lock.acquire()
            for command in queue:
                commands.append(command)
            lock.release()
            queue.clear()
            

        # Go ahead and update the screen with what we've drawn.
        pygame.display.flip()

        # Limit to 20 frames per second
        clock.tick(8)

if __name__ == '__main__':
    
   
   
    commands = []
    lock = Lock()

    com = Thread(target=communication,args=(commands,lock,))
    com.start()
   
    pygame.init()
    main(commands,lock)
    pygame.quit()

    com.do_run = False
    com.join()
