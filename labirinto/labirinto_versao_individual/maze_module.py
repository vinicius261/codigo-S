"""
Resolução de exercícíos propostos no Bootcamp - Código[s] da Stone
 
Labirinto - Nível 3

Vinicius Miranda Santos

"""

from time import sleep


def maze_create(file) -> list():

    open_file = open(file, "r")
    maze_sketch = list(open_file)

    maze = []
    for line in maze_sketch:
        line = line.strip("\n")
        line = [line[index] for index in range(len(line))]
        maze.append(line)

    for index in range(len(maze)):
        maze[index].insert(0, str(index+1).zfill(2))

    return maze


def maze_print(maze: list) -> None:
    sleep(0.7)
    for line in maze:
        for item in line:
            if item == "#":
                maze[maze.index(line)][line.index(item)] = "###"
            if item == " ":
                maze[maze.index(line)][line.index(item)] = "   "
            if item == "S":
                maze[maze.index(line)][line.index(item)] = " S "

    top_line = ["  "]
    for number in range(1, 21):
        top_line.append(f"{number}".zfill(2))
    top_line_printable = " ".join(top_line)
    print(top_line_printable)

    for line in maze:
        line_printable = "".join(line)
        print(line_printable)
    print(f"\n")


def user_input(maze: list) -> tuple:
    user_choice_l, user_choice_column = tuple(map(int, input(
        "\n\nDigite a posição inicial do robô no formato 'linha,coluna'. ex: 4,12 :").split(",")))
    user_choice_line = user_choice_l - 1

    insert_line_control = []
    insert_column_control = []
    for line in maze:
        line_index_int = int(line[0])
        insert_line_control.append(line_index_int)
    for number in range(1, 21):
        insert_column_control.append(number)

    while (user_choice_l not in insert_line_control) and (user_choice_column not in insert_column_control):
        user_choice_l, user_choice_column = tuple(map(int, input(
            "\n\nO robô só pode partir de espaços vazios existentes no labirinto. \n\nDigite a posição inicial do robô no formato 'linha,coluna'. ex: 4,12 :").split(",")))
        user_choice_line = user_choice_l - 1

    while maze[user_choice_line][user_choice_column] != "   ":
        user_choice_line, user_choice_column = tuple(map(int, input(
            "\n\nO robô só pode partir de espaços vazios existentes no labirinto. \n\nDigite a posição inicial do robô no formato 'linha,coluna'. ex: 4,12 :").split(",")))

    return user_choice_line, user_choice_column


def robot_moviment(initial_line, initial_column: tuple, maze: list):
    line, column = initial_line, initial_column
    maze[initial_line][initial_column] = " X "
    maze_print(maze)
    stop = False
    i, j = line, column
    stack_LIFO = []
    stack_LIFO.append((i, j))
    while stop == False:
        robot_arround = [maze[i-1][j], maze[i]
                         [j+1], maze[i+1][j], maze[i][j-1]]
        for index in robot_arround:
            if robot_arround.index(index) == 0:
                i1 = i-1
                j1 = j
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

            if " S " in robot_arround:
                if robot_arround.index(" S ") == 0:
                    i1 = i-1
                    j1 = j
                elif robot_arround.index(" S ") == 1:
                    i1 = i
                    j1 = j+1
                elif robot_arround.index(" S ") == 2:
                    i1 = i+1
                    j1 = j
                else:
                    i1 = i
                    j1 = j-1
                maze[i1][j1] = " X "
                maze[i][j] = " . "
                maze_print(maze)
                print("\n\nEND")
                stop = True
                break

            if index == "   ":
                maze[i1][j1] = " X "
                stack_LIFO.append((i, j))
                maze[i][j] = " . "
                maze_print(maze)
                i, j = i1, j1
                break

            if (index == " . ") and (("   " not in robot_arround) and (" S " not in robot_arround)):
                if (i1, j1) == stack_LIFO[-1]:
                    maze[i1][j1] = " X "
                    maze[i][j] = " . "
                    maze_print(maze)
                    i, j = i1, j1
                    stack_LIFO.pop()
