"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Labirinto - Nível 3

Vinicius Miranda Santos

"""
from maze_module import maze_create, maze_print, robot_moviment, user_input

print("\n\nBem vindo ao Labirinto!\n\nNesse script você escolhe uma posição inicial para o robô e observa ele sair do labirinto usando um algotimo criado por mim.\n")

maze = maze_create("labirinto_2.txt")

maze_print(maze)

insert_line, insert_column = user_input(maze)

robot_moviment(insert_line, insert_column, maze)
