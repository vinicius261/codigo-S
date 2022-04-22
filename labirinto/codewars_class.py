"""
LABIRINTO
 
Nível 3

Vinicius Miranda Santos

"""
from maze_class import Maze

print("\n\nBem vindo ao Labirinto!\n\nNesse script você escolhe uma posição inicial para o robô e observa ele sair do labirinto usando um algotimo criado por mim.\n")

maze = Maze("labirinto_2.txt")

maze.maze_create()

maze.maze_print()

user_choice_l, user_choice_column = tuple(map(int,input("\n\nDigite a posição inicial do robô no formato 'linha,coluna'. ex: 4,12 :").split(",")))
user_choice_line = user_choice_l - 1

maze = Maze("labirinto_2.txt", user_choice_line, user_choice_column)
    
maze.user_input_validation()

maze.robot_moviment()