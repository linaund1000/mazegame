'''
player choose its position in the beginning 

[horizontal position (x) ,vertical position (y)]
moving up and down are checked by


1 means exist
0 means not exist
'''
from abc import abstractmethod
from dataclasses import dataclass
import numpy as np

class NewMap:
    def horizontal_dimension_creation() -> np.array:
        horizontal : list = np.random.choice([' ','_'], size = MapBluePrint.game_size, p=MapBluePrint.block_weights).tolist()
        #todo if statement to fix border
        
        
        return horizontal
    
    def vertical_dimension_creation() -> np.array:
        vertical :np.array = np.random.choice([' ','|'], size = MapBluePrint.game_size, p=MapBluePrint.block_weights).tolist()
        #todo if statement to fix border
        
        return vertical

class MapWorker:
    '''converts the arrays real str information and assambler them'''
    @abstractmethod
    def ceil_assembler() -> str:
        '''is used in ceil and bottom construction'''
        ceil = np.array(['_' for _ in range(MapBluePrint.game_size[1]*2+2)]).tolist()
        ceil = ''.join(ceil)
        return ceil
        
    @abstractmethod
    def columns_assembler(horizontal,vertical) -> str:
        #this line of code for mixing two different array for exampl 
        #a1 = [1,1,1,1,1] ,a2 = [0,0,0,0,0] ->> a_mix = [1,0,1,0,1,0,1,0,1,0]sum_of_blocks = ''
        sum_of_blocks = ''
        for horizontal_part,vertical_part in zip(horizontal,vertical):#vertical control a.k.a. (y)
            adv_list = []
            for item_number in range(len(horizontal_part)):#horizontal control a.k.a. (x)
                
                adv_list.append(horizontal_part[item_number])
                adv_list.append(vertical_part[item_number])
            
            sum_of_blocks = sum_of_blocks + '|'+''.join(adv_list)+'\n'

        return sum_of_blocks
    
    def giant_assembler(horizontal,vertical) -> str:
        maze_str_map = MapWorker.ceil_assembler() +'\n'+ MapWorker.columns_assembler(horizontal,vertical) + MapWorker.ceil_assembler()
        return maze_str_map


@dataclass    
class MapBluePrint:
    '''blueprint of map'''
    game_size: tuple = (50,50)
    block_weights = (0.6,0.4)
    players_position : tuple = (0,0)
    
class Map:
    '''Map of maze game 
    include->>
    *dimension creation
    *blocks in maze
    *information game size
    *assambler
    '''
    def __init__(self):
        
        self.vertical = NewMap.vertical_dimension_creation()
            #be carefull two different variable!
        self.horizontal = NewMap.horizontal_dimension_creation() #for instance a1 = [1,1,1,1,1] ,a2 = [0,0,0,0,0] ->> a_mix = [1,0,1,0,1,0,1,0,1,0]
            #a1,a2 ->> a_mix
        self.assembled_map = MapWorker.giant_assembler(self.horizontal, self.vertical) #=> a_mix
    
    def __str__(self) -> str:
        return self.assembled_map
    
    

    

if __name__ == '__main__':
    x = Map()
    print(x)
    



































