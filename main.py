import random 
from termcolor import colored
import os
os.system('cls' if os.name == 'nt' else 'clear')

class Maze:
    def __init__(self, player=[70 , 70 , 'O'] , walls=' ' ,lenght=100):
        '''players position is a [x , y , symbol]  data '''
        
        
        self.maze = []
        self.player = player
        self.lenght = lenght
        self.walls = walls
        
        
        if self.player[0] > self.lenght:
            raise ValueError('OverPosition')
        elif self.player[1] >self.lenght:
            raise ValueError('Overposition')
        
        elif self.player[0] < 0:
            raise ValueError('underposition')
        elif self.player[0] < 0:
            raise ValueError('UnderPosition ! ')
        elif len(self.player[2]) != 1 :
            raise('playerSymbolError ! ')
        else:
            
            self.maze_maker()
            self.draw_maze()
        
        

    def maze_maker(self):       
        for y in range(self.lenght):
            self.maze.append([])
            
            for x in range(0,self.lenght-1):
              
                if x == self.player[0] and y == self.player[1]:  #drawing player's position
                    self.maze[y].append(colored(self.player[2] , 'red'))
                
                
                elif random.randint(0,2) in [0,1]:  #random dot
                    
                    self.maze[y].append('.')
                
                else:
                    self.maze[y].append(' ')
                    
    def draw_maze(self):
        myjoin = ''
        for i in self.maze:
            myjoin = myjoin+'\n'+'  '.join(i)
        os.system('cls' if os.name == 'nt' else 'clear')
        print(myjoin)
         
    def move_up(self,x = 0,y = 0):
        
        if self.player[1] == (self.lenght-1):
            print('order not allowed because of border ! ')


        else :  
            self.player[1] = self.player[1]-1
        
            
            self.draw_maze()
        
   
    def move_right(self):
    
    def move_left(self)
m = Maze(player=[0,0,'O'],lenght=20)

i = input('ask me when happen ')

m.move_up()
