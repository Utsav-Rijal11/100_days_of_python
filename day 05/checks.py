def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    while front_is_clear():
        move()
        
while not at_goal():
    if front _is_clear():
        move()
    else:
        jump()
        
    
