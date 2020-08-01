#FIRST INSTALL PYTHON AND PYGAME USING COMMANED
#pip install pygame

#import pygame for gui 
#import sys for exit method 
#import time to count time 
import pygame, sys, time
from pygame.locals import *

#init of windows size 
WINDOWWIDTH = 1100
WINDOWHEIGHT = 600

#colors
#            R    G    B
GRAY     = (100, 100, 100)
NAVYBLUE = ( 60,  60, 100)
WHITE    = (255, 255, 255)
RED      = (255,   0,   0)
GREEN    = (  0, 255,   0)
BLUE     = (  0,   0, 255)
YELLOW   = (255, 255,   0)
ORANGE   = (255, 128,   0)
PURPLE   = (255,   0, 255)
CYAN     = (  0, 255, 255)

#this backround color 
BGCOLOR = NAVYBLUE

#all colors for prgrms in MC
ALLCOLORS = (RED, BLUE, YELLOW, ORANGE, PURPLE, CYAN)  
 

# memoire central class
class Mc():
    """MC : 'memoire central',  class for similltion about gui dynamique MC 
        that can show tha main three algo first fit , best fit and worst fit 
        it can help to affect this this algo in gui way
    """
    
# car of the MC 
    def __init__(self, size=1200):
        self.width = 900
        self.height = 200
        #X and Y cord point for the MC rectangle
        self.TopLeftX = 100
        self.TopLeftY = 100
        #size (in mg)
        self.size = size
        #this to affect value of time whene the space is free in MC we choose 0
        #u can change it to -1
        self.Non = 0
        #list of prgrms in MC , we init it 
        self.MC = list([{'name':'free', 'size':size, 'start':0, 'time':self.Non}])
        #the pile that help us keep prgrms we enter 
        self.pile = list()
        #sec we wont to wait betwine very 1 sec in the prgrms
        self.sec = 1

#enter prgrms in the pile (name, size and time in sec)
    def enter(self, n):
        for i in range(n):
            name = input('enter name : ')
            size = int(input('enter size  (MC_size >= size > 0): '))
            time = int(input('enter time  (> 0): '))
            self.pile.append({'name': name, 'size': size, 'time': time})
            
#find space for prgrm in the MC return True else False
    def find_space(self):
        if not self.pile:
            return False
        
        size = self.pile[0]['size']
        
        for pgm in self.MC:
            if pgm['name'] == 'free' and pgm['size'] >= size:
                return True
        return False

# First Fit algo in MC 
    def FirstFit(self):
        if not self.find_space():
            return False

        pgm = self.pile.pop(0)
        
        for index in range(len(self.MC)):
            if self.MC[index]['name'] == 'free' and self.MC[index]['size'] >= pgm['size']:
                if self.MC[index]['size'] != pgm['size']:
                    self.MC.insert(index, {'name': 'free', 'size': self.MC[index]['size'] - pgm['size'], 'time': self.Non, 'start': pgm['size']+ self.MC[index]['start']})
                    index += 1
                self.MC[index]['name'] = pgm['name']
                self.MC[index]['time'] = pgm['time']
                self.MC[index]['size'] = pgm['size']
                return True

# Best fit aLgo
    def BestFit(self):
        if not self.find_space():
            return False
            
        pgm = self.pile.pop(0)
        
        index = self.Non
        size = self.size
        for i in range(len(self.MC)):
            if self.MC[i]['name'] == 'free' and self.MC[i]['size'] >= pgm['size'] and self.MC[i]['size'] < size:
                index = i
                size = self.MC[i, 'size']
                
        if self.MC[index]['size'] != pgm['size']:
            self.MC.insert(index, {'name': 'free', 'size': self.MC[index]['size'] - pgm['size'], 'time': self.Non, 'start': pgm['size'] + self.MC[index]['start']})
            index += 1
            
        self.MC[index]['name'] = pgm['name']
        self.MC[index]['time'] = pgm['time']
        self.MC[index]['size'] = pgm['size']
        
        return True

# worst fit algo
    def WorstFit(self):
        if not self.find_space():
            return False

        pgm = self.pile.pop(0)
        
        index = self.Non
        size = self.size
        for i in range(len(self.MC)):
            if self.MC[i]['name'] == 'free' and self.MC[i]['size'] >= pgm['size'] and self.MC[i]['size'] > size:
                index = i
                size = self.MC[i]['size']
                
        if self.MC[index, 'size'] != pgm['size']:
            self.MC.insert(index, {'name': 'free', 'size': self.MC[index]['size'] - pgm['size'], 'time': self.Non, 'start': pgm['size'] + self.MC[index]['start']})
            index += 1
            
        self.MC[index]['name'] = pgm['name']
        self.MC[index]['time'] = pgm['time']
        self.MC[index]['size'] = pgm['size']
        
        return True

#print the gui MC in the window and prgrms with name and time
    def showMC(self, DISPLAYSURF, fontObj):
        pygame.draw.rect(DISPLAYSURF, WHITE, (self.TopLeftX, self.TopLeftY, self.width, self.height))
        pygame.draw.rect(DISPLAYSURF, GRAY, (self.TopLeftX, self.TopLeftY, self.width, self.height), 5)
        self.showTxt(DISPLAYSURF, fontObj, str(self.size), ORANGE, BGCOLOR, TopLeft=(self.width+80, self.TopLeftY-40))
        if self.MC:
            i = 0
            for pgm in self.MC:
                pointA = (pgm['start'] * self.width / self.size) + self.TopLeftX
                pointB = pgm['size'] * self.width / self.size
                self.showTxt(DISPLAYSURF, fontObj, str(pgm['start']), ORANGE, BGCOLOR, TopLeft=(pointA-20, 60))
                if pgm['name'] != 'free':
                    Rect = pygame.Rect(pointA, self.TopLeftY+3, pointB-3, self.height-6)
                    pygame.draw.rect(DISPLAYSURF, ALLCOLORS[i], Rect)
                    
                    self.showTxt(DISPLAYSURF, fontObj, pgm['name'], GREEN, ALLCOLORS[i], (Rect.centerx, Rect.centery-50))
                    self.showTxt(DISPLAYSURF, fontObj, str(pgm['time']), GREEN, ALLCOLORS[i], (Rect.centerx, Rect.centery))
                    i+=1
                    if i > len(ALLCOLORS):
                        i = 0

#print gui text in the MC (time and name of MC)                 
    def showTxt(self, DISPLAYSURF, fontObj, string, color, bgcolor, center=0, TopLeft=0):
        textSurfaceObj = fontObj.render(string, True, color, bgcolor)
        textRectObj = textSurfaceObj.get_rect()
        if TopLeft == 0:
            textRectObj.center = center
        else:
            textRectObj.topleft = TopLeft
        DISPLAYSURF.blit(textSurfaceObj, textRectObj)

#update time every sec pass  
    def update_time(self):
        if not self.MC:
            return False
        
        for i in range(len(self.MC)):
            if self.MC[i]['name'] != 'free':
                self.MC[i]['time'] -= 1

# put togther spaces that are bsides  if they are free space in the MC whene time is 0       
    def togther(self):
        if not self.MC and len(self.MC) > 1:
            return False
        i = 0
        while i < len(self.MC) - 1:
            if self.MC[i]['name'] == self.MC[i+1]['name'] == 'free':
                self.MC[i]['size'] += self.MC[i+1]['size']
                del self.MC[i+1]
            else:
                i += 1
        
        if len(self.MC) == 1:
            self.MC[i]['start'] = 0
        
#delay 1  sec every time to simulate time in MC      
    def delay(self):
        time.sleep(self.sec)
        
    def choose(self, name):
        if name == 'FirstFit':
            while self.FirstFit():
                pass
        elif name == 'BestFit':
            while self.BestFit():
                pass
        elif name == 'WorstFit':
            while self.WorstFit():
                pass

#check if the time 0 in MC to change it to free in MC 
    def check_0_time(self):
        
        for i in range(len(self.MC)):
            if self.MC[i]['name'] != 'free' and self.MC[i]['time'] == 0:
                self.MC[i]['name'] = 'free'
            

# the main func for the gui 
def main():    
    pygame.init()
    
    # disp black surface of the MC and name and init size of the text in gui  
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    pygame.display.set_caption('MC game')
    fontObj = pygame.font.Font('freesansbold.ttf', 32)
    
    #disp back round color
    DISPLAYSURF.fill(BGCOLOR)
    
    #enter size of MC
    size = int(input('enter size of MC : ))
    #neter numb of prgrms that will be run
    n = int(input('enter number of prgrms : '))
    # choose type of algo to be run in dynamique MC
    typ = input('engter FisrtFit , BestFit or WorstFit')
    #create instince of the MC classe
    mc = Mc(size)
    #call enter method to fill the pile woth detailes of prgrms to be run in 
    #the MC
    mc.enter(n)
    
    #tha main loop for the MC gui to print
    while True: # main game loop
        DISPLAYSURF.fill(BGCOLOR) # drawing the window
        
        mc.choose(typ)
            
        mc.showMC(DISPLAYSURF, fontObj)
        
        #loop to exit prgrm by click QUIT key
        for event in pygame.event.get():
            if event.type == QUIT:
                print(mc.MC)
                pygame.quit()
                sys.exit()
        mc.delay()
        mc.update_time()
        mc.check_0_time()
        mc.togther()
        pygame.display.update()
        



# call main func
if __name__ == '__main__':
    main()
