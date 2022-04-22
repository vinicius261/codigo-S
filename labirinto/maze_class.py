"""
LABIRINTO
 
Nível 3

Vinicius Miranda Santos
"""

from time import sleep

class Maze:
    def __init__(self, file: str, initial_line = 0, initial_column = 0, maze =[]) -> None:
        self.file = file
        self.line = initial_line
        self.column = initial_column
        self.maze = maze

    def maze_create(self):
        
        open_file = open(self.file, "r")
        maze_sketch = list(open_file)
        
        for line in maze_sketch:
            line = line.strip("\n")
            line = [line[index] for index in range(len(line))]
            self.maze.append(line)
    
        for index in range(len(self.maze)):
            self.maze[index].insert(0,str(index+1).zfill(2))


    def maze_print(self) -> None:
        sleep(0.7)
        for line in self.maze:
            for item in line:
                if item == "#" :
                    self.maze[self.maze.index(line)][line.index(item)] = "###"
                if item == " ":
                    self.maze[self.maze.index(line)][line.index(item)] = "   "
                if item == "S":
                    self.maze[self.maze.index(line)][line.index(item)] = " S "

        top_line = ["  "]
        for number in range(1,21):
            top_line.append(f"{number}".zfill(2))
        top_line_printable = " ".join(top_line)    
        print(top_line_printable)
    
        for line in self.maze:
            line_printable = "".join(line)
            print(line_printable)
        print(f"\n")

    def user_input_validation (self) -> tuple:
        insert_line_control = []
        insert_column_control = []
        for line in self.maze:
            line_index_int = int(line[0])
            insert_line_control.append(line_index_int)
        for number in range(1,21):
            insert_column_control.append(number)

        while ((self.line+1) not in insert_line_control) and (self.column not in insert_column_control):
            user_choice_l, self.column = tuple(map(int,input("\n\nO robô só pode partir de espaços vazios existentes no labirinto. \n\nDigite a posição inicial do robô no formato 'linha,coluna'. ex: 4,12 :").split(",")))
            self.line = user_choice_l - 1

        while self.maze[self.line][self.column] != "   ":
                self.line, self.column =  tuple(map(int,input("\n\nO robô só pode partir de espaços vazios existentes no labirinto. \n\nDigite a posição inicial do robô no formato 'linha,coluna'. ex: 4,12 :").split(",")))


    def robot_moviment (self):
        line, column = self.line, self.column
        self.maze[self.line][self.column] = " X "
        self.maze_print()
        stop = False
        i, j = line, column       
        stack_LIFO = []
        stack_LIFO.append((i,j))
        while stop == False:        
            robot_arround = [self.maze[i-1][j],self.maze[i][j+1],self.maze[i+1][j], self.maze[i][j-1]]                   
            for index in robot_arround:
                if robot_arround.index(index) == 0:
                    i1 = i-1
                    j1 =  j   
                    robot_arround[0] = "Next repeated item"             
                elif robot_arround.index(index) == 1:
                    i1 = i
                    j1 = j+1
                    robot_arround[1] = "Next repeated item"       
                elif robot_arround.index(index) == 2:
                    i1 = i+1
                    j1 = j
                    robot_arround[2] = "Next repeated item"       
                else:
                    i1 = i
                    j1 = j-1
                
                if  " S " in robot_arround:
                    if robot_arround.index(" S ") == 0:
                        i1 = i-1
                        j1 =  j                              
                    elif robot_arround.index(" S ") == 1:
                        i1 = i
                        j1 = j+1                
                    elif robot_arround.index(" S ") == 2:
                        i1 = i+1
                        j1 = j                   
                    else:
                        i1 = i
                        j1 = j-1            
                    self.maze[i1][j1] = " X "
                    self.maze[i][j] = " . "
                    self.maze_print()
                    print("\n\nEND")
                    stop = True
                    break
                
                if index == "   ":                
                    self.maze[i1][j1] = " X "
                    stack_LIFO.append((i,j))
                    self.maze[i][j] = " . "
                    self.maze_print()
                    i,j = i1,j1 
                    break

                        
                if (index == " . ") and (("   " not in robot_arround) and (" S " not in robot_arround)) :               
                    if (i1,j1) == stack_LIFO[-1]:
                        self.maze[i1][j1] = " X "
                        self.maze[i][j] = " . "
                        self.maze_print()
                        i,j = i1,j1
                        stack_LIFO.pop()  