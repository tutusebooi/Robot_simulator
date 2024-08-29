robot_name = input("what do you want to name me: ")
#name = robot_name()
robot_limit = (100,100)
current_position = (0,0)
movement = input()

def foward(new_position, current_position):
    new_position = (current_position[0] + 5 ,current_position[1])
    current_position = new_position
    print(current_position)
    return current_position

def back(new_position,current_position):
    new_position = (current_position[0] - 1,current_position[1])
    current_position = new_position
    print(current_position)
    return current_position

while movement != "exit":
    movement = input(f"{robot_name} : how would you like me to move: ")
    if movement == "foward":
        foward()
    elif movement == "back":
        back()
    elif movement == "exit":
        break
    else:
        print("no such command")

