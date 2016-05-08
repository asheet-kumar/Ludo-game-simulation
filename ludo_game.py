import pygame,sys
from pygame.locals import *
from random import randint

pygame.init()

BoardWidth = 1000
BoardHeight = 700
BPadding = 10
outlineWidth = 5

title = 'Ludo Board'

boxwidth = 50
boxheight = 50

WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
PURPLE = (255,20,255)

dispsurf = pygame.display.set_mode((BoardWidth,BoardHeight))
pygame.display.set_caption(title)

FPS = 10
fpsClock = pygame.time.Clock()

def renderText(string,(cx,cy),fontSize,color):
    fontObj = pygame.font.Font('freesansbold.ttf',fontSize)
    textSurfObj = fontObj.render(string,True,color)
    textRectObj = textSurfObj.get_rect()
    textRectObj.center = (cx,cy)
    dispsurf.blit(textSurfObj,textRectObj)

def showButtonRoll():
    pygame.draw.rect(dispsurf,BLACK,(750,500,200,40))
    renderText("Roll",(850,520),32,WHITE)

def showButtonMove():
    pygame.draw.rect(dispsurf,BLACK,(750,600,200,40))
    renderText("Move",(850,620),32,WHITE)

def showDiceBox(n):
    pygame.draw.rect(dispsurf,BLACK,(750,450,200,40),3)
    renderText(str(n),(850,470),32,BLACK)

def showTurnBox(n):
    pygame.draw.rect(dispsurf,BLACK,(750,10,200,40))
    pygame.draw.rect(dispsurf,WHITE,(750,10,200,40),1)
    pygame.draw.line(dispsurf,WHITE,(870,10),(870,50),1)
    renderText("Turn",(810,30),32,WHITE)
    renderText("P"+str(n),(910,30),32,WHITE)

def showLudoButtons():
    pygame.draw.rect(dispsurf,BLACK,(750,550,40,40),3)
    renderText(str(1),(770,570),32,BLACK)

    pygame.draw.rect(dispsurf,BLACK,(800,550,40,40),3)
    renderText(str(2),(820,570),32,BLACK)

    pygame.draw.rect(dispsurf,BLACK,(850,550,40,40),3)
    renderText(str(3),(870,570),32,BLACK)

    pygame.draw.rect(dispsurf,BLACK,(900,550,40,40),3)
    renderText(str(4),(920,570),32,BLACK)


def drawBoard():
    # draw outline
    pygame.draw.line(dispsurf,BLACK,(0,0),(1000,0))
    pygame.draw.line(dispsurf,BLACK,(701,0),(701,700))
    # draw home
    C = (350,350)
    TL = (275,275)
    BL = (275,425)
    BR = (425,425)
    TR = (425,275)
    pygame.draw.polygon(dispsurf,RED,(C,BR,BL),0)
    pygame.draw.polygon(dispsurf,GREEN,(C,BL,TL),0)
    pygame.draw.polygon(dispsurf,YELLOW,(C,TL,TR),0)
    pygame.draw.polygon(dispsurf,BLUE,(C,TR,BR),0)

    # draw grid
    # bottom boxes
    list1 = [(275, 425,WHITE), (275, 481,WHITE), (275, 537,WHITE), (275, 593,RED), (275, 649,WHITE),
(325, 425,RED), (325, 481,RED), (325, 537,RED), (325, 593,RED), (325, 649,WHITE),
(375, 425,WHITE), (375, 481,WHITE), (375, 537,WHITE), (375, 593,WHITE), (375, 649,WHITE)]
    for item in list1:
        if(item[2] == RED):
            pygame.draw.rect(dispsurf,item[2],(item[0],item[1],49,54),0)
        else:
            pygame.draw.rect(dispsurf,BLACK,(item[0],item[1],50,54),1)

    # left boxes
    list2 = [(275, 275,WHITE), (219, 275,WHITE), (163, 275,WHITE), (107, 275,GREEN), (51, 275,WHITE),
(275, 325,GREEN), (219, 325,GREEN), (163, 325,GREEN), (107, 325,GREEN), (51, 325,WHITE,GREEN),
(275, 375,WHITE), (219, 375,WHITE), (163, 375,WHITE), (107, 375,WHITE), (51, 375,WHITE)]
    for item in list2:
        #pygame.draw.rect(dispsurf,BLACK,(item[0],item[1],-52,48),1)
        if(item[2] == GREEN):
            pygame.draw.rect(dispsurf,item[2],(item[0],item[1],-52,48),0)
        else:
            pygame.draw.rect(dispsurf,BLACK,(item[0],item[1],-52,48),1)

    # top boxes
    list3 = [(425, 275,WHITE), (425, 219,WHITE), (425, 163,WHITE), (425, 107,YELLOW), (425, 51,WHITE),
(375, 275,YELLOW), (375, 219,YELLOW), (375, 163,YELLOW), (375, 107,YELLOW), (375, 51,WHITE),
(325, 275,WHITE), (325, 219,WHITE), (325, 163,WHITE), (325, 107,WHITE), (325, 51,WHITE)]
    for item in list3:
        #pygame.draw.rect(dispsurf,BLACK,(item[0],item[1],-46,-52),1)
        if(item[2] == YELLOW):
            pygame.draw.rect(dispsurf,item[2],(item[0],item[1],-46,-52),0)
        else:
            pygame.draw.rect(dispsurf,BLACK,(item[0],item[1],-46,-52),1)


    # right boxes
    list4 = [(425, 425,WHITE), (481, 425,WHITE), (537, 425,WHITE), (593, 425,BLUE), (649, 425,WHITE),
(425, 375,BLUE), (481, 375,BLUE), (537, 375,BLUE), (593, 375,BLUE), (649,375,WHITE),
(425, 325,WHITE), (481, 325,WHITE), (537, 325,WHITE), (593, 325,WHITE), (649, 325,WHITE)]
    for item in list4:
        #pygame.draw.rect(dispsurf,BLACK,(item[0],item[1],54,-46),1)
        if(item[2] == BLUE):
            pygame.draw.rect(dispsurf,item[2],(item[0],item[1],54,-46),0)
        else:
            pygame.draw.rect(dispsurf,BLACK,(item[0],item[1],54,-46),1)


    '''
    no_of_lines = 4
    diff = 0
    tracklist = [(0,0)]
    for i in range(1, no_of_lines):
        x = BL[0] + diff
        y = BL[1]
        pygame.draw.line(dispsurf, BLACK, (x, y), (x, 700))
        for j in range(1, 6):
            pygame.draw.line(dispsurf, BLACK, (x, y), (x + 50, y))
            tracklist.append((x,y))

            y += 56

        diff += 50
    diff = 0
    for i in range(1,no_of_lines):
        x = TL[0]
        y = TL[1] + diff
        pygame.draw.line(dispsurf, BLACK, (x, y), (0, y))
        for j in range(1, 6):
            pygame.draw.line(dispsurf, BLACK, (x, y), (x, y + 50))
            tracklist.append((x,y))
            x -= 56

        diff += 50

    diff = 0
    for i in range(1,no_of_lines):
        x = TR[0] - diff
        y = TR[1]
        pygame.draw.line(dispsurf,BLACK,(x,y),(x,0))
        for j in range(1,6):
            pygame.draw.line(dispsurf,BLACK,(x,y),(x-50,y))
            tracklist.append((x,y))
            y-=56

        diff +=50

    diff = 0
    for i in range(1,no_of_lines):
        x = BR[0]
        y = BR[1] - diff
        pygame.draw.line(dispsurf,BLACK,(x,y),(700,y))
        for j in range(1,6):
            pygame.draw.line(dispsurf,BLACK,(x,y),(x,y-50))
            tracklist.append((x,y))
            x+=56

        diff +=50
    #print len(tracklist)
    #print tracklist
    '''

    # draw player home
    colors = [RED,GREEN,YELLOW,BLUE]
    p_home = [(0,425),(0,0),(425,0),BR,]

    for i in range(1,5):
        pygame.draw.rect(dispsurf,colors[i-1],(p_home[i-1][0]+1,p_home[i-1][1]+1,275,275))
        pygame.draw.rect(dispsurf,WHITE,(p_home[i-1][0]+41,p_home[i-1][1]+41,193,193))
        xx = p_home[i-1][0]+41
        yy = p_home[i-1][1]+41
        #print xx
        #print yy
        pygame.draw.rect(dispsurf,colors[i-1],(xx+15,yy+15,70,70))
        pygame.draw.rect(dispsurf,colors[i-1],(xx+105,yy+15,70,70))
        pygame.draw.rect(dispsurf,colors[i-1],(xx+15,yy+105,70,70))
        pygame.draw.rect(dispsurf,colors[i-1],(xx+105,yy+105,70,70))


def displayScoreBoard(scores):
    pygame.draw.rect(dispsurf,BLACK,(750,50,200,40))
    renderText("Scores",(850,70),32,WHITE)

    pygame.draw.rect(dispsurf, BLACK, (750, 90, 200, 60))
    renderText("1", (775, 100), 20, WHITE)
    renderText("2", (825, 100), 20, WHITE)
    renderText("3", (875, 100), 20, WHITE)
    renderText("4", (925, 100), 20, WHITE)

    pygame.draw.line(dispsurf, WHITE, (750, 110), (950, 110), 1)
    pygame.draw.line(dispsurf, WHITE, (800, 110), (800, 150), 1)
    pygame.draw.line(dispsurf, WHITE, (850, 110), (850, 150), 1)
    pygame.draw.line(dispsurf, WHITE, (900, 110), (900, 150), 1)
    pygame.draw.line(dispsurf, WHITE, (950, 110), (950, 150), 1)

    renderText(str(scores[1]), (775, 130), 28, WHITE)
    renderText(str(scores[1]), (825, 130), 28, WHITE)
    renderText(str(scores[1]), (875, 130), 28, WHITE)
    renderText(str(scores[1]), (925, 130), 28, WHITE)

    '''
    pygame.draw.rect(dispsurf,BLACK,(750,150,200,40))
    pygame.draw.rect(dispsurf,WHITE,(750,150,200,40),1)
    pygame.draw.line(dispsurf,WHITE,(870,150),(870,190),1)
    renderText("Player1",(810,170),32,WHITE)
    renderText(str(scores[0]),(910,170),32,WHITE)

    pygame.draw.rect(dispsurf,BLACK,(750,200,200,40))
    pygame.draw.rect(dispsurf,WHITE,(750,200,200,40),1)
    pygame.draw.line(dispsurf,WHITE,(870,200),(870,240),1)
    renderText("Player2",(810,220),32,WHITE)
    renderText(str(scores[1]),(910,220),32,WHITE)

    pygame.draw.rect(dispsurf,BLACK,(750,250,200,40))
    pygame.draw.rect(dispsurf,WHITE,(750,250,200,40),1)
    pygame.draw.line(dispsurf,WHITE,(870,250),(870,290),1)
    renderText("Player3",(810,270),32,WHITE)
    renderText(str(scores[2]),(910,270),32,WHITE)

    pygame.draw.rect(dispsurf,BLACK,(750,300,200,40))
    pygame.draw.rect(dispsurf,WHITE,(750,300,200,40),1)
    pygame.draw.line(dispsurf,WHITE,(870,300),(870,340),1)
    renderText("Player4",(810,320),32,WHITE)
    renderText(str(scores[3]),(910,320),32,WHITE)
    '''
wo = 1
winOrder = [0,0,0,0]
def winingOrder(scores):
    global wo
    global winOrder
    for i in range(4):
        if(winOrder[i] == 0 and scores [i] == 1):
            winOrder[i] = wo
            wo += 1
    y = 170
    for i in range(4):
        if(winOrder[i] != 0):
            #renderText(str(winOrder[i]),(975,y),32,GREEN)
            y+=50



# Ludo button class

class LudoButton:
    radius = 15
    center_x = 0
    center_y = 0

    def drawLudoButton(self,color,(center_x,center_y)):
        self.center_x = center_x
        self.center_y = center_y
        pygame.draw.circle(dispsurf,color,(self.center_x,self.center_y),self.radius,0)

# class player
class Player (LudoButton):
    score = 0    # score of each player
    def __init__(self,color,track):
        self.color = color    # color assigned to player
        self.LudobuttonList = [LudoButton() for i in range(1,5)]   # list having four ludo buttons for a player
        self.finalstatus = [0,0,0,0]                               # final status of ludo buttons of a player
        self.initialstatus = [0,0,0,0]                             # initial status of ludo buttons of a player
        self.track = track                                         # track on which ludo buttons will move
        self.currentposition = [-1,-1,-1,-1]        # current position of each of the ludo button in  track

    def placeLudoButtons(self,position,initiated):
        '''
        method to place ludo buttons in respective positions
        position is a list having co-ordinates as tuple for each of four button
        count is an integer variable tells how many ludo buttons are to be initiated
        '''
        for i in range(4):
            if(initiated[i] == position[i]):
                kkk=32
                 #print " This ludo buttons has initiated"
            else:
                pygame.draw.circle(dispsurf,PURPLE,position[i-1],17,0)
                self.drawLudoButton(self.color,position[i-1])

    def makeAMove(self,current):
        '''
        method to move a ludo button
        current is the current position of the ludo button
        '''
        pygame.draw.circle(dispsurf,self.color,self.track[current + 1],self.radius,0)

    def InitiateStart(self, btn_no):
        '''
        method to initiate ludo buttons from the starting positions
        btn_no tells about which button to be initiated
        '''
        pygame.draw.circle(dispsurf,self.color,self.track[0],self.radius,0)


    def isInHome(self):
        '''
        method to check how many ludo buttons have reached to the home
        '''
        for i in range (4):
            if(self.currentposition[i] == 47 and self.finalstatus[i] != 1):
                self.score +=1
                self.finalstatus[i] = 1
                print 'final status'
                print self.finalstatus


    def displayTransitButtons(self):
        for i in range(4):
            #print i
            #print self.currentposition[i]
            if(self.currentposition[i] != -1):
                pygame.draw.circle(dispsurf,PURPLE,self.track[self.currentposition[i]],17,0)
                self.drawLudoButton(self.color,self.track[self.currentposition[i]])




'''
 Track for player1 (red)
'''
track1 = [(300,621),(300,565),(300,509),(300,453),(247,400),(191,400),(135,400),(79,400),(23,400), (23,350),
(23,300),(79,300),(135,300),(191,300),(247,300),(300,247),(300,191),(300,135),(300,79),(300,23),(350,23),
(400,23),(400,79),(400,135),(400,191),(400,247),(453,300),(509,300),(565,300),(621,300),(677,300),(677,350),
(677,400),(621,400),(565,400),(509,400),(453,400),(400,453),(400,509),(400,565),(400, 621),(400,677),(350,677),
(350, 621),(350,565),(350,509),(350,453),(350,350)]

'''
 Track for player2 (green)
'''

track2 = [(79,300),(135,300),(191,300),(247,300),(300,247),(300,191),(300,135),(300,79),(300,23),
(350,23),(400,23),(400,79),(400,135),(400,191),(400,247),(453,300),(509,300),(565,300),(621,300),
(677,300),(677,350),(677,400),(621,400),(565,400),(509,400),(453,400),(400,453),(400,509),(400,565),
(400, 621),(400,677),(350,677),(300,677),(300,621),(300,565),(300,509),(300,453),(247,400),(191,400),(135,400),
(79,400),(23,400), (23,350),(79,350),(135,350),(191,350),(247,350),(350,350)]

'''
 Track for player3 (yellow)
'''

track3 = [(400,79),(400,135),(400,191),(400,247),(453,300),(509,300),(565,300),(621,300),(677,300),
(677,350),(677,400),(621,400),(565,400),(509,400),(453,400),(400,453),(400,509),(400,565),(400, 621),
(400,677),(350,677),(300,677),(300,621),(300,565),(300,509),(300,453),(247,400),(191,400),(135,400),
(79,400),(23,400),(23,350),(23,300),(79,300),(135,300),(191,300),(247,300),(300,247),(300,191),(300,135),
(300,79),(300,23),(350,23),(350,79),(350,135),(350,191),(350,247),(350,350)]

'''
 Track for player4 (blue)
'''

track4 = [(621, 400), (565, 400), (509, 400), (453, 400), (400, 453), (400, 509), (400, 565), (400,  621),
(400, 677),(350, 677), (300,677),(300, 621), (300, 565), (300, 509), (300, 453), (247, 400), (191, 400),
(135, 400), (79, 400),(23, 400), (23, 350), (23, 300), (79, 300), (135, 300), (191, 300),
(247, 300), (300, 247),(300, 191), (300, 135), (300, 79), (300, 23), (350, 23), (400, 23), (400, 79),
(400, 135), (400, 191),(400, 247), (453, 300), (509, 300), (565, 300), (621, 300), (677, 300), (677, 350),
(621, 350), (565, 350),(509, 350), (453, 350),(350,350)]

'''
print len(track1)
print len(track2)
print len(track3)
print len(track4)
'''

'''
 Instances of class player
'''
Player1 = Player(RED, track1)
Player2 = Player(GREEN, track2)
Player3 = Player(YELLOW, track3)
Player4 = Player(BLUE, track4)

'''
initial positions of ludo buttons for each player
'''
position1 = [(91,516), (181,516), (91,606), (181,606)]
position2 = [(91,91), (181,91), (91,181), (181,181)]
position3 = [(516,91), (606,91), (516,181), (606,181)]
position4 = [(516,516), (606,516), (516,606), (606,606)]


'''
lists about initiated buttons of a particular player
'''

initiated1 = [(0,0),(0,0),(0,0),(0,0)]
initiated2 = [(0,0),(0,0),(0,0),(0,0)]
initiated3 = [(0,0),(0,0),(0,0),(0,0)]
initiated4 = [(0,0),(0,0),(0,0),(0,0)]







mousex=0              # x co-ordinate of the point where mouse is clicked
mousey=0              # y co-ordinate of the point where mouse is clicked
mouseclicked = False  # variable holds the status whether mouse is clicked or not
mc = 0
movebutton = 0        # which button out of (1,2,3,4) is to be moved
p_id = 1              # variable to hold the turn of the player
i=1                   # variable helps in animating the movement of ludo button
n=0                   # variable tells about number that turned up while rolling the dice
flagIMP = 0







def diceroll(n,c,b,tick,In):
    kkk = 1;
    location = (710, 140)
    while kkk<15 :
        print 'dice rollssss'
        print b
        print In
        if In < 15 and n == 1 and b == 1:
            filename = str(In) + ".gif"  # ensure filename is correct
            img = pygame.image.load(filename)
            dispsurf.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img1.gif"  # ensure filename is correct
                img = pygame.image.load(filename)
                dispsurf.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 2 and b == 1:
            filename = str(In) + ".gif"  # ensure filename is correct
            img = pygame.image.load(filename)
            dispsurf.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img2.gif"  # ensure filename is correct
                img = pygame.image.load(filename)
                dispsurf.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 3 and b == 1:
            filename = str(In) + ".gif"  # ensure filename is correct
            img = pygame.image.load(filename)
            dispsurf.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img3.gif"  # ensure filename is correct
                img = pygame.image.load(filename)
                dispsurf.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 4 and b == 1:
            filename = str(In) + ".gif"  # ensure filename is correct
            img = pygame.image.load(filename)
            dispsurf.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img4.gif"  # ensure filename is correct
                img = pygame.image.load(filename)
                dispsurf.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 5 and b == 1:
            filename = str(In) + ".gif"  # ensure filename is correct
            img = pygame.image.load(filename)
            dispsurf.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img5.gif"  # ensure filename is correct
                img = pygame.image.load(filename)
                dispsurf.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        if In < 15 and n == 6 and b == 1:
            filename = str(In) + ".gif"  # ensure filename is correct
            img = pygame.image.load(filename)
            dispsurf.blit(img, location)
            c.tick(tick)
            In += 1
            if In == 14:
                filename = "img6.gif"  # ensure filename is correct
                img = pygame.image.load(filename)
                dispsurf.blit(img, location)
                c.tick(tick)
                b = 0
                In = 1
        pygame.display.flip()
        kkk+=1

def dispdiceroll(n):
    location = (710,140)
    if n == 1:
        filename = "img1.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        dispsurf.blit(img, location)
    elif n == 2:
        filename = "img2.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        dispsurf.blit(img, location)
    elif n == 3:
        filename = "img3.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        dispsurf.blit(img, location)
    elif n == 4:
        filename = "img4.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        dispsurf.blit(img, location)
    elif n == 5:
        filename = "img5.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        dispsurf.blit(img, location)
    elif n == 6:
        filename = "img6.gif"  # ensure filename is correct
        img = pygame.image.load(filename)
        dispsurf.blit(img, location)

'''
  Main Game Loop
'''

c = pygame.time.Clock() # create a clock object for timing
b=0
tick = 20
In=1

while True:
    dispsurf.fill(WHITE)    # fills the background color on the board
    drawBoard()             # function call to draw ludo board
    showButtonRoll()        # function call to  display Roll button
    showButtonMove()        # function call to display Move button
    dispdiceroll(n)
    #diceroll(1,c,b,tick,In)
    if(mc == 0):            # condition to maintain the display of number that turned up while rolling the dice
        showDiceBox(0)
    else:
        showDiceBox(n)
    # function call to display four numbered buttons for movement of a particular ludo button
    showLudoButtons()
    showTurnBox(p_id)       # function call to display the turn of the player


    # instances of class player is calling to place four ludo buttons on initial positions

    Player1.placeLudoButtons(position1,initiated1)         # Player 1
    Player2.placeLudoButtons(position2,initiated2)         # Player 2
    Player3.placeLudoButtons(position3,initiated3)         # Player 3
    Player4.placeLudoButtons(position4,initiated4)         # Player 4

    # Displaying buttons in transitions

    Player1.displayTransitButtons()                        # Player 1
    Player2.displayTransitButtons()                        # Player 2
    Player3.displayTransitButtons()                        # Player 3
    Player4.displayTransitButtons()                        # Player 4


    # List to store scores of each player

    scores = [Player1.score,Player2.score,Player3.score,Player4.score]
    #displayScoreBoard(scores)         # Function call to display score board

    #winingOrder(scores)               # Function call to show winning orders near scoreboard

    for event in pygame.event.get():  # event loop
        #print event
        if event.type == QUIT:        # if type of event is quit
            pygame.quit()
            sys.exit()
        elif event.type == MOUSEBUTTONUP:    # if type of event is mouse button up
            (mousex,mousey) = event.pos      # co-ordinates of point where mouse is clicked
            mouseclicked = True              # variable to hold status of mouse click event


    '''
    If Roll Button is clicked
    '''
    if(mouseclicked == True and mousex >= 750 and mousex <= 950 and mousey >= 500 and mousey <= 540):
        print "Roll is clicked"
        mc = 1
        n = randint(1,6)       # returns a random number from 1 to 6
        print 'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
        print n
        b=1

        showDiceBox(n)         # Function call to display number that turned up on dice
        mouseclicked = False  # change the status of mouse clicked event
        ''' dice roll starts'''
        diceroll(n, c, b, tick, In)
        print 'dice roll ends'
        ''' dice roll ends'''





    elif(mouseclicked == True and mousey >= 550 and mousey <= 590):  # to select button number by a player
        if(mousex >= 750 and mousex <= 790):
            print "1 is clicked"                        # 1st button is selected
            movebutton = 1
        elif(mousex >= 800 and mousex <= 840):
            print "2 is clicked"                        # 2nd button is selected
            movebutton = 2
        elif(mousex >= 850 and mousex <= 890):
            print "3 is clicked"
            movebutton = 3                              # 3rd button is clicked
        elif(mousex >= 900 and mousex <= 940):
            print "4 is clicked"
            movebutton = 4                              # 4th button is clicked

        mouseclicked = False             # change the status of mouse clicked event

    # If Move button is clicked
    elif(mouseclicked == True and mousex >= 750 and mousex <= 950 and mousey >= 600 and mousey <= 640):
        print "Move is clicked"
        if(p_id == 1):      # corresponding to player 1
            if(Player1.finalstatus[0] == 1 and Player1.finalstatus[1] == 1 and  Player1.finalstatus[2] == 1 and Player1.finalstatus[3] == 1):
                p_id = 2    # If all the buttons have reached home, then change player id
            else:
                if(movebutton ==1):      # If 1st button was selected
                    if(flagIMP == 0):
                        diff = (47 - Player1.currentposition[0])
                        flagIMP = 1

                    print 'move button1, Player 1'
                    if(Player1.initialstatus[0] == 0):
                        if(n == 6 or n == 1):     # If 1 or 6 turned up on dice

                            Player1.initialstatus[0] = 1    # change the status of button 1 for player 1
                            initiated1[0] = position1[0]    # set the button which has been initiated
                            Player1.InitiateStart(1)        # Function call to initiate the start of button1
                            mouseclicked = False            # Change the status of the event
                            Player1.currentposition[0] = 0  # set the current position of button 1
                            print "button1 initialized"
                            '''
                            print Player1.initialstatus
                            print Player2.initialstatus
                            print Player3.initialstatus
                            print Player4.initialstatus
                            print p_id
                            '''
                        else:
                            p_id = 2                        # change the player-id if number is not 1 or 6
                            print 'This button cannot be initialized'
                            mouseclicked =False             # change the status of mouse  clicked event
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player1.finalstatus[0] !=1):
                                if(Player1.currentposition[0] >= 41 and n <= diff):
                                    Player1.makeAMove(Player1.currentposition[0])
                                    Player1.currentposition[0] +=1
                                    i+=1
                                elif(Player1.currentposition[0] < 41):
                                    Player1.makeAMove(Player1.currentposition[0])
                                    Player1.currentposition[0] +=1
                                    i+=1
                                else:
                                    p_id = 2
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"


                        elif(i > n):
                            p_id = 2
                            i=1
                            mouseclicked = False
                if(movebutton ==2):
                    if(flagIMP == 0):
                        diff = (47 - Player1.currentposition[1])
                        flagIMP = 1

                    print 'move button2, Player 1'
                    if(Player1.initialstatus[1] == 0):
                        if(n == 6 or n == 1):

                            Player1.initialstatus[1] = 1
                            initiated1[1] = position1[1]
                            Player1.InitiateStart(2)
                            mouseclicked = False
                            Player1.currentposition[1] = 0
                            print "button1 initialized"

                            print p_id
                        else:
                            p_id = 2
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player1.finalstatus[1] !=1):
                                if(Player1.currentposition[1] >= 41 and n <= diff):
                                    Player1.makeAMove(Player1.currentposition[1])
                                    Player1.currentposition[1] +=1
                                    i+=1
                                elif(Player1.currentposition[1] < 41):
                                    Player1.makeAMove(Player1.currentposition[1])
                                    Player1.currentposition[1] +=1
                                    i+=1
                                else:
                                    p_id = 2
                                    i=1
                                    mouseclicked = False


                            else:
                                print "This button has been to home already"


                        elif(i > n):
                            p_id = 2
                            i=1
                            mouseclicked = False
                if(movebutton ==3):
                    if(flagIMP == 0):
                        diff = (47 - Player1.currentposition[2])
                        flagIMP = 1
                    print 'move button3, Player 1'
                    print diff
                    print Player1.currentposition[2]

                    if(Player1.initialstatus[2] == 0):
                        if(n == 6 or n == 1):

                            Player1.initialstatus[2] = 1
                            initiated1[2] = position1[2]
                            Player1.InitiateStart(3)
                            mouseclicked = False
                            Player1.currentposition[2] = 0
                            print "button1 initialized"
                            print Player1.initialstatus
                            print p_id
                        else:
                            p_id = 2
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player1.finalstatus[2] !=1):



                                if(Player1.currentposition[2] >= 41 and n <= diff):
                                    print 'one'
                                    print diff
                                    Player1.makeAMove(Player1.currentposition[2])
                                    Player1.currentposition[2] +=1
                                    i+=1

                                elif(Player1.currentposition[2] < 41):
                                    #print 'two'
                                    Player1.makeAMove(Player1.currentposition[2])
                                    Player1.currentposition[2] +=1
                                    i+=1
                                else:
                                    print 'three'
                                    p_id = 2
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"


                        elif(i > n):
                            p_id = 2
                            i=1
                            mouseclicked = False
                if(movebutton ==4):
                    if(flagIMP == 0):
                        diff = (47 - Player1.currentposition[3])
                        flagIMP = 1

                    print 'move button4, Player 1'
                    if(Player1.initialstatus[3] == 0):
                        if(n == 6 or n == 1):

                            Player1.initialstatus[3] = 1
                            initiated1[3] = position1[3]
                            Player1.InitiateStart(4)
                            mouseclicked = False
                            Player1.currentposition[3] = 0
                            print "button1 initialized"
                            print Player1.initialstatus
                            print p_id
                        else:
                            p_id = 2
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player1.finalstatus[3] !=1):
                                if(Player1.currentposition[3] >= 41 and n <= diff):
                                    Player1.makeAMove(Player1.currentposition[3])
                                    Player1.currentposition[3] +=1
                                    i+=1
                                elif(Player1.currentposition[3] < 41):
                                    Player1.makeAMove(Player1.currentposition[3])
                                    Player1.currentposition[3] +=1
                                    i+=1
                                else:
                                    p_id = 2
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"


                        elif(i > n):
                            p_id = 2
                            i=1
                            mouseclicked = False



        elif(p_id == 2):
            if(Player2.finalstatus[0] == 1 and Player2.finalstatus[1] == 1 and Player2.finalstatus[2] == 1 and Player2.finalstatus[3] == 1):
                p_id = 3
            else:
                if(movebutton ==1):
                    if(flagIMP == 0):
                        diff = (47 - Player2.currentposition[0])
                        flagIMP = 1

                    print 'move button1, Player 2'
                    if(Player2.initialstatus[0] == 0):
                        if(n == 6 or n == 1):

                            Player2.initialstatus[0] = 1
                            initiated2[0] = position2[0]
                            Player2.InitiateStart(1)
                            mouseclicked = False
                            Player2.currentposition[0] = 0
                            print "button1 initialized"

                            print Player2.initialstatus
                            print Player2.initialstatus
                            print Player3.initialstatus
                            print Player4.initialstatus
                            print p_id
                        else:
                            p_id = 3
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player2.finalstatus[0] !=1):
                                if(Player2.currentposition[0] >= 41 and n <= diff):
                                    Player2.makeAMove(Player2.currentposition[0])
                                    Player2.currentposition[0] +=1
                                    i+=1
                                elif(Player2.currentposition[0] < 41):
                                    Player2.makeAMove(Player2.currentposition[0])
                                    Player2.currentposition[0] +=1
                                    i+=1
                                else:
                                    p_id = 3
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"


                        elif(i > n):
                            p_id = 3
                            i=1
                            mouseclicked = False
                if(movebutton ==2):

                    if(flagIMP == 0):
                        diff = (47 - Player2.currentposition[1])
                        flagIMP = 1

                    print 'move button 2, Player 2'
                    if(Player2.initialstatus[1] == 0):
                        if(n == 6 or n == 1):

                            Player2.initialstatus[1] = 1
                            initiated2[1] = position2[1]
                            Player2.InitiateStart(2)
                            mouseclicked = False
                            Player2.currentposition[1] = 0
                            print "button1 initialized"

                            print p_id
                        else:
                            p_id = 3
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player2.finalstatus[1] !=1):
                                if(Player2.currentposition[1] >= 41 and n <= diff):
                                    Player2.makeAMove(Player2.currentposition[1])
                                    Player2.currentposition[1] +=1
                                    i+=1
                                elif(Player2.currentposition[1] < 41):
                                    Player2.makeAMove(Player2.currentposition[1])
                                    Player2.currentposition[1] +=1
                                    i+=1
                                else:
                                    p_id = 3
                                    i=1
                                    mouseclicked = False


                            else:
                                print "This button has been to home already"


                        elif(i > n):
                            p_id = 3
                            i=1
                            mouseclicked = False
                if(movebutton ==3):
                    if(flagIMP == 0):
                        diff = (47 - Player2.currentposition[2])
                        flagIMP = 1
                    print 'move button3, Player 2'
                    print diff
                    print Player2.currentposition[2]

                    if(Player2.initialstatus[2] == 0):
                        if(n == 6 or n == 1):

                            Player2.initialstatus[2] = 1
                            initiated2[2] = position2[2]
                            Player2.InitiateStart(3)
                            mouseclicked = False
                            Player2.currentposition[2] = 0
                            print "button1 initialized"
                            print Player2.initialstatus
                            print p_id
                        else:
                            p_id = 3
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player2.finalstatus[2] !=1):



                                if(Player2.currentposition[2] >= 41 and n <= diff):
                                    print 'one'
                                    print diff
                                    Player2.makeAMove(Player2.currentposition[2])
                                    Player2.currentposition[2] +=1
                                    i+=1

                                elif(Player2.currentposition[2] < 41):
                                    #print 'two'
                                    Player2.makeAMove(Player2.currentposition[2])
                                    Player2.currentposition[2] +=1
                                    i+=1
                                else:
                                    print 'three'
                                    p_id = 3
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"


                        elif(i > n):
                            p_id = 3
                            i=1
                            mouseclicked = False
                if(movebutton ==4):
                    if(flagIMP == 0):
                        diff = (47 - Player2.currentposition[3])
                        flagIMP = 1

                    print 'move button 4, Player 2'
                    if(Player2.initialstatus[3] == 0):
                        if(n == 6 or n == 1):

                            Player2.initialstatus[3] = 1
                            initiated2[3] = position2[3]
                            Player2.InitiateStart(4)
                            mouseclicked = False
                            Player2.currentposition[3] = 0
                            print "button1 initialized"
                            print Player2.initialstatus
                            print p_id
                        else:
                            p_id = 1
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player2.finalstatus[3] !=1):
                                if(Player2.currentposition[3] >= 41 and n <= diff):
                                    Player2.makeAMove(Player2.currentposition[3])
                                    Player2.currentposition[3] +=1
                                    i+=1
                                elif(Player2.currentposition[3] < 41):
                                    Player2.makeAMove(Player2.currentposition[3])
                                    Player2.currentposition[3] +=1
                                    i+=1
                                else:
                                    p_id = 3
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"


                        elif(i > n):
                            p_id = 3
                            i=1
                            mouseclicked = False




        elif(p_id == 3):
            if(Player3.finalstatus[0] == 1 and Player3.finalstatus[1] == 1 and Player3.finalstatus[2] == 1 and Player3.finalstatus[3] == 1):
                p_id = 4
            else:
                if(movebutton ==1):
                    if(flagIMP == 0):
                        diff = (47 - Player3.currentposition[0])
                        flagIMP = 1

                    print 'move button1, Player 3'
                    if(Player3.initialstatus[0] == 0):
                        if(n == 6 or n == 1):

                            Player3.initialstatus[0] = 1
                            initiated3[0] = position3[0]
                            Player3.InitiateStart(1)
                            mouseclicked = False
                            Player3.currentposition[0] = 0
                            print "button1 initialized"

                            print Player3.initialstatus
                            print Player3.initialstatus
                            print Player3.initialstatus
                            print Player4.initialstatus
                            print p_id
                        else:
                            p_id = 4
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player3.finalstatus[0] !=1):
                                if(Player3.currentposition[0] >= 41 and n <= diff):
                                    Player3.makeAMove(Player3.currentposition[0])
                                    Player3.currentposition[0] +=1
                                    i+=1
                                elif(Player3.currentposition[0] < 41):
                                    Player3.makeAMove(Player3.currentposition[0])
                                    Player3.currentposition[0] +=1
                                    i+=1
                                else:
                                    p_id = 4
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"

                        elif(i > n):
                            p_id = 4
                            i=1
                            mouseclicked = False
                if(movebutton ==2):

                    if(flagIMP == 0):
                        diff = (47 - Player3.currentposition[1])
                        flagIMP = 1

                    print 'move button 2, Player 3'
                    if(Player3.initialstatus[1] == 0):
                        if(n == 6 or n == 1):

                            Player3.initialstatus[1] = 1
                            initiated3[1] = position3[1]
                            Player3.InitiateStart(2)
                            mouseclicked = False
                            Player3.currentposition[1] = 0
                            print "button1 initialized"

                            print p_id
                        else:
                            p_id = 4
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player3.finalstatus[1] !=1):
                                if(Player3.currentposition[1] >= 41 and n <= diff):
                                    Player3.makeAMove(Player3.currentposition[1])
                                    Player3.currentposition[1] +=1
                                    i+=1
                                elif(Player3.currentposition[1] < 41):
                                    Player3.makeAMove(Player3.currentposition[1])
                                    Player3.currentposition[1] +=1
                                    i+=1
                                else:
                                    p_id = 4
                                    i=1
                                    mouseclicked = False


                            else:
                                print "This button has been to home already"

                        elif(i > n):
                            p_id = 4
                            i=1
                            mouseclicked = False
                if(movebutton ==3):
                    if(flagIMP == 0):
                        diff = (47 - Player3.currentposition[2])
                        flagIMP = 1
                    print 'move button3, Player 3'
                    print diff
                    print Player3.currentposition[2]

                    if(Player3.initialstatus[2] == 0):
                        if(n == 6 or n == 1):

                            Player3.initialstatus[2] = 1
                            initiated3[2] = position3[2]
                            Player3.InitiateStart(3)
                            mouseclicked = False
                            Player3.currentposition[2] = 0
                            print "button1 initialized"
                            print Player3.initialstatus
                            print p_id
                        else:
                            p_id = 4
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player3.finalstatus[2] !=1):



                                if(Player3.currentposition[2] >= 41 and n <= diff):
                                    print 'one'
                                    print diff
                                    Player3.makeAMove(Player3.currentposition[2])
                                    Player3.currentposition[2] +=1
                                    i+=1

                                elif(Player3.currentposition[2] < 41):
                                    #print 'two'
                                    Player3.makeAMove(Player3.currentposition[2])
                                    Player3.currentposition[2] +=1
                                    i+=1
                                else:
                                    print 'three'
                                    p_id = 4
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"

                        elif(i > n):
                            p_id = 4
                            i=1
                            mouseclicked = False
                if(movebutton ==4):
                    if(flagIMP == 0):
                        diff = (47 - Player3.currentposition[3])
                        flagIMP = 1

                    print 'move button 4, Player 3'
                    if(Player3.initialstatus[3] == 0):
                        if(n == 6 or n == 1):

                            Player3.initialstatus[3] = 1
                            initiated3[3] = position3[3]
                            Player3.InitiateStart(4)
                            mouseclicked = False
                            Player3.currentposition[3] = 0
                            print "button1 initialized"
                            print Player3.initialstatus
                            print p_id
                        else:
                            p_id = 4
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player3.finalstatus[3] !=1):
                                if(Player3.currentposition[3] >= 41 and n <= diff):
                                    Player3.makeAMove(Player3.currentposition[3])
                                    Player3.currentposition[3] +=1
                                    i+=1
                                elif(Player3.currentposition[3] < 41):
                                    Player3.makeAMove(Player3.currentposition[3])
                                    Player3.currentposition[3] +=1
                                    i+=1
                                else:
                                    p_id = 4
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"

                        elif(i > n):
                            p_id = 4
                            i=1
                            mouseclicked = False



        elif(p_id == 4):
            if(Player2.finalstatus[0] == 1 and Player2.finalstatus[1] == 1 and Player2.finalstatus[2] == 1 and Player2.finalstatus[3] == 1):
                p_id = 1
            else:
                if(movebutton ==1):
                    if(flagIMP == 0):
                        diff = (47 - Player4.currentposition[0])
                        flagIMP = 1

                    print 'move button1, Player 4'
                    if(Player4.initialstatus[0] == 0):
                        if(n == 6 or n == 1):

                            Player4.initialstatus[0] = 1
                            initiated4[0] = position4[0]
                            Player4.InitiateStart(1)
                            mouseclicked = False
                            Player4.currentposition[0] = 0
                            print "button1 initialized"

                            print Player4.initialstatus
                            print Player4.initialstatus
                            print Player4.initialstatus
                            print Player4.initialstatus
                            print p_id
                        else:
                            p_id = 1
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player4.finalstatus[0] !=1):
                                if(Player4.currentposition[0] >= 41 and n <= diff):
                                    Player4.makeAMove(Player4.currentposition[0])
                                    Player4.currentposition[0] +=1
                                    i+=1
                                elif(Player4.currentposition[0] < 41):
                                    Player4.makeAMove(Player4.currentposition[0])
                                    Player4.currentposition[0] +=1
                                    i+=1
                                else:
                                    p_id = 1
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"

                        elif(i > n):
                            p_id = 1
                            i=1
                            mouseclicked = False
                if(movebutton ==2):

                    if(flagIMP == 0):
                        diff = (47 - Player4.currentposition[1])
                        flagIMP = 1

                    print 'move button 2, Player 4'
                    if(Player4.initialstatus[1] == 0):
                        if(n == 6 or n == 1):

                            Player4.initialstatus[1] = 1
                            initiated4[1] = position4[1]
                            Player4.InitiateStart(2)
                            mouseclicked = False
                            Player4.currentposition[1] = 0
                            print "button1 initialized"

                            print p_id
                        else:
                            p_id = 1
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player4.finalstatus[1] !=1):
                                if(Player4.currentposition[1] >= 41 and n <= diff):
                                    Player4.makeAMove(Player4.currentposition[1])
                                    Player4.currentposition[1] +=1
                                    i+=1
                                elif(Player4.currentposition[1] < 41):
                                    Player4.makeAMove(Player4.currentposition[1])
                                    Player4.currentposition[1] +=1
                                    i+=1
                                else:
                                    p_id = 1
                                    i=1
                                    mouseclicked = False


                            else:
                                print "This button has been to home already"

                        elif(i > n):
                            p_id = 1
                            i=1
                            mouseclicked = False
                if(movebutton ==3):
                    if(flagIMP == 0):
                        diff = (47 - Player4.currentposition[2])
                        flagIMP = 1
                    print 'move button3, Player 4'
                    print diff
                    print Player4.currentposition[2]

                    if(Player4.initialstatus[2] == 0):
                        if(n == 6 or n == 1):

                            Player4.initialstatus[2] = 1
                            initiated4[2] = position4[2]
                            Player4.InitiateStart(3)
                            mouseclicked = False
                            Player4.currentposition[2] = 0
                            print "button1 initialized"
                            print Player4.initialstatus
                            print p_id
                        else:
                            p_id = 1
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player4.finalstatus[2] !=1):



                                if(Player4.currentposition[2] >= 41 and n <= diff):
                                    print 'one'
                                    print diff
                                    Player4.makeAMove(Player4.currentposition[2])
                                    Player4.currentposition[2] +=1
                                    i+=1

                                elif(Player4.currentposition[2] < 41):
                                    #print 'two'
                                    Player4.makeAMove(Player4.currentposition[2])
                                    Player4.currentposition[2] +=1
                                    i+=1
                                else:
                                    print 'three'
                                    p_id = 1
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"

                        elif(i > n):
                            p_id = 1
                            i=1
                            mouseclicked = False
                if(movebutton ==4):
                    if(flagIMP == 0):
                        diff = (47 - Player4.currentposition[3])
                        flagIMP = 1

                    print 'move button 4, Player 4'
                    if(Player4.initialstatus[3] == 0):
                        if(n == 6 or n == 1):

                            Player4.initialstatus[3] = 1
                            initiated4[3] = position4[3]
                            Player4.InitiateStart(4)
                            mouseclicked = False
                            Player4.currentposition[3] = 0
                            print "button1 initialized"
                            print Player4.initialstatus
                            print p_id
                        else:
                            p_id = 1
                            print 'This button cannot be initialized'
                            mouseclicked =False
                    else:

                        if(i<=n):
                            if(i==n):
                                flagIMP = 0

                            if(Player4.finalstatus[3] !=1):
                                if(Player4.currentposition[3] >= 41 and n <= diff):
                                    Player4.makeAMove(Player4.currentposition[3])
                                    Player4.currentposition[3] +=1
                                    i+=1
                                elif(Player4.currentposition[3] < 41):
                                    Player4.makeAMove(Player4.currentposition[3])
                                    Player4.currentposition[3] +=1
                                    i+=1
                                else:
                                    p_id = 1
                                    i=1
                                    mouseclicked = False

                            else:
                                print "This button has been to home already"

                        elif(i > n):
                            p_id = 1
                            i=1
                            mouseclicked = False





    Player1.isInHome()
    Player2.isInHome()
    Player3.isInHome()
    Player4.isInHome()



    pygame.display.update()
    fpsClock.tick(FPS)

