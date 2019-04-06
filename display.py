from displayelements import TextPrint, InputBox

class Display:
    WINDOW_TITLE = "LegoMaM Controller 2018"
    size = [640, 480]

    def __init__(self,pygame):
        self.screen = pygame.display.set_mode(self.size)
        pygame.display.set_caption(self.WINDOW_TITLE)
        self.textPrint = TextPrint(pygame)
        
    def showRobotStatus(self,robot):
        self.textPrint.print(self.screen, "Servo: ")
        self.textPrint.indent()
        for index, servoPos in enumerate(robot.servoState):
            self.textPrint.print(self.screen, "[{}] Pos: {}".format(index,servoPos))
        self.textPrint.unindent()

        self.textPrint.print(self.screen, "Motor: ")
        self.textPrint.indent()
        for index,(speed,dir) in enumerate(robot.motorState):
             self.textPrint.print(self.screen, "[{}] Speed: {}, Dir: {}".format(index, speed,dir))
        self.textPrint.unindent()
       
    def showBaseInfo(self,joystick):
        # Get the name from the OS for the controller/joystick
        name = joystick.get_name()
        self.textPrint.print(self.screen, "Joystick name: {}".format(name))

        # Usually axis run in pairs, up/down for one, and left/right for
        # the other.
        axes = joystick.get_numaxes()
        self.textPrint.print(self.screen, "Number of axes: {}".format(axes))
        self.textPrint.indent()

        for i in range(axes):
            axis = joystick.get_axis(i)
            self.textPrint.print(self.screen, "Axis {} value: {:>6.3f}".format(i, axis))
        self.textPrint.unindent()

        # buttons = joystick.get_numbuttons()
        # self.textPrint.print(self.screen, "Number of buttons: {}".format(buttons))
        # self.textPrint.indent()

        # for i in range(buttons):
        #     button = joystick.get_button(i)
        #     self.textPrint.print(
        #         self.screen, "Button {:>2} value: {}".format(i, button))
        # self.textPrint.unindent()

        # Hat switch. All or nothing for direction, not like joysticks.
        # Value comes back in an array.
        # hats = joystick.get_numhats()
        # self.textPrint.print(self.screen, "Number of hats: {}".format(hats))
        # self.textPrint.indent()

        # for i in range(hats):
        #     hat = joystick.get_hat(i)
        #     self.textPrint.print(
        #         self.screen, "Hat {} value: {}".format(i, str(hat)))
        # self.textPrint.unindent()
        # self.textPrint.unindent()

    def draw(self):
    # def draw(self,joystick):
        self.screen.fill(self.textPrint.getcolor("WHITE"))
        self.textPrint.reset()
        # self.showBaseInfo(joystick)
