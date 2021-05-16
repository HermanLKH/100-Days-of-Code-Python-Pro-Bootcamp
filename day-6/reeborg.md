# Day 6
Source: https://reeborg.ca/
## Hurdle Challenge
```
def turn_right():
    turn_left()
    turn_left()
    turn_left()

def jump():
    turn_left()
    while not right_is_clear():
        move()
    turn_right()
    move()
    turn_right()
    while not wall_in_front():
        move()
    else:
        turn_left()
    
def race():
    while not at_goal():
        if not front_is_clear():
            jump()
        else:
            move()
```

## Maze Challenge
```
def left_is_clear():
    turn_left()
    result = front_is_clear()
    turn_right()
    return result

def maze1():
    last_right_is_clear = right_is_clear()
    while not at_goal():
        if left_is_clear() and right_is_clear() and front_is_clear() and last_right_is_clear:
            last_right_is_clear = right_is_clear()
            move()
        elif wall_on_right() and front_is_clear():
            last_right_is_clear = right_is_clear()
            move()
        elif right_is_clear():
            last_right_is_clear = right_is_clear()
            turn_right()
            move()
        else:
            last_right_is_clear = right_is_clear()
            turn_left()
            
def maze2():
    while front_is_clear():
        move()
    turn_left()
    while not at_goal():
        if right_is_clear():
            turn_right()
            move()
        elif front_is_clear():
            move()
        else:
            turn_left()
```