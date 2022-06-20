import random
import os

'''
Doc

this is a maze game consist of dots and space

player is supposed to go to the other door which is little bit far



the whole maze information will be saved in self.maze list
coordinate of (x,y) ==> self.maze[y][x]


[[][][]] = has three coloumn

[['.','.']] = has two row


'''


class Maze:
    def __init__(self, player=[70 , 70 , 'O'] ,lenght=100):
        '''
        
        players position is a [x , y , symbol]  data 
        
        '''

        self.maze = []
        self.player = player
        self.lenght = lenght


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

            self.new_maze_maker()
            self.draw_maze()


    def new_maze_maker(self):       
        for y in range(self.lenght):
            self.maze.append([])

            for x in range(0,self.lenght-1):

                if x == self.player[0] and y == self.player[1]:  #drawing player's position
                    self.maze[y].append(self.player[2])


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


    def position_check(self,x = None , y = None):
        '''
        use this function for checking before moving around
        
        
        Function returns 
        TRUE if given position is available which is '.' ,
        FALSE if given position is not available which is 'x' or ' ' (space) or '|', 
        'lose' if given position is 'x' because it shows user touched that position before
        '''
        try:
            given_position = self.maze[y][x]
        
        except:
            print('that move is not possible')
            return False


        if given_position == '.':
            return True

        elif given_position == ' ':
            return False
        elif given_position == 'x':
            return 'lose'
        else:
            print('order is not allowed // // // position CHECK_ERROR')
            return False        


    def move_up(self):
        x = self.player[0]
        y = (self.player[1]-1)
        
        new_position_allowed  = self.position_check(x,y)
        if new_position_allowed == True:
            
            self.maze[self.player[1]][self.player[0]] = 'x'
            self.player[1] = y
            self.maze[self.player[1]][self.player[0]] = 'O'
            
            self.draw_maze()
        
        elif new_position_allowed == False:
            pass
        elif new_position_allowed == 'lose':
        
            self.lose()


    def move_down(self):
        x = self.player[0]
        y = (self.player[1]+1)
        
        new_position_allowed  = self.position_check(x,y)
        if new_position_allowed == True:
                
            self.maze[self.player[1]][self.player[0]] = 'x'
            self.player[1] = y
            self.maze[self.player[1]][self.player[0]] = 'O'
            
            self.draw_maze()

        elif new_position_allowed == False:
            pass

        elif new_position_allowed == 'lose':
            self.lose()
    def move_left(self):
        x = (self.player[0]-1)
        y = self.player[1]
        print(x)
        new_position_allowed  = self.position_check(x,y)
        if new_position_allowed == True:
                
            self.maze[self.player[1]][self.player[0]] = 'x'
            self.player[0] = x
            self.maze[self.player[1]][self.player[0]] = 'O'
            
            self.draw_maze()

        elif new_position_allowed == False:
            pass

        elif new_position_allowed == 'lose':
            self.lose()
    
    def move_right(self):
        x = (self.player[0]+1)
        y = self.player[1]
        print(y)
        new_position_allowed  = self.position_check(x,y)
        if new_position_allowed == True:
                
            self.maze[self.player[1]][self.player[0]] = 'x'
            self.player[0] = x
            self.maze[self.player[1]][self.player[0]] = 'O'
            
            self.draw_maze()

        elif new_position_allowed == False:
            pass

        elif new_position_allowed == 'lose':
            self.lose()
            
    
    
    def lose(self):
        os.system('cls' if os.name == 'nt' else 'clear')
        mssg = 'YOU LOST DUDE !!'
        mssg = '-'*(len(mssg)+2) + '\n|'+mssg+'|\n' + '-'*(len(mssg)+2)
        print(mssg)
        
                


m = Maze(player=[0,0,'O'],lenght=20)

for a in range(0,m.lenght**2):

    i = input('move around : ')
    if i =='s':
        m.move_down()
        print("s")

    elif i == "w":
        m.move_up()
        print("w")
    elif i == "d":
        m.move_right()
        print("d")
    elif i == "a":
        m.move_left()
        print("a")
m.lose()







