'''
Froggier.py
@author Kyle Wisecarver
@license This software is free - http://www.gnu.org/licenses/gpl.html'''
'Maybe we can code as a list of to do items'

''''''
# Path: Actor.py
import sys  # The sys module (the sys module)
from random import choice, randrange  # The random module (the random module)

import g2d  # The g2d module (the g2d module) G2D is a module that allows you to create games with Python Generate to detect collisions and collisions
from g2d import *

sprites = g2d.load_image("Froggier_sprites.png") # Load the sprites
background = g2d.load_image("Froggier_bg.png") # Load the background
global arena_w, arena_h, framecount, lives, score, framecount2
arena_w, arena_h, framecount, lives, score, framecount2 = 720, 480, 0, 3, 0, 0
##   ##   ##  ##  ##
def save_score(): # Save the score
    global score
    with open("scores.txt", "w") as file:
        file.write(str(score))


def read_score(): # Read the score
    with open("scores.txt", "r") as file:
        max_score = 0
        max_score = int(file.readline())
        return max_score


class Arena(): # The arena class
    def __init__(self, w, h): # Initialize the arena class
        global framecount # Global framecount
        self._w = w # Width
        self._h = h # Height
        self._actors = [] # List of actors
        g2d.init_canvas((w - 80, h)) # Init the canvas

    def check_all_collisions(self): # Check all collisions in the arena
        for i in range(len(self._actors) - 6):
            check_collision(self._actors[0], self._actors[i])
        if not arena._actors[0]._clipped:
            for i in range(6):
                check_collision(self._actors[0], self._actors[-i-1])
                check_collision(self._actors[0], self._actors[-i-2])

        for i in range(len(self._actors) - 6):
            check_collision(self._actors[1], self._actors[i])
        if not arena._actors[1]._clipped:
            for i in range(6):
                check_collision(self._actors[1], self._actors[-i-1])
                check_collision(self._actors[1], self._actors[-i-2])

    def check_frog_position(self): # Check the frog position
        xf, yf, wf, hf = self._actors[0].get_position()
        if not - 25 < xf < arena_w - 80 or not 0 < yf < arena_h:
            dead(0)
        xf, yf, wf, hf = self._actors[1].get_position()
        if not - 25 < xf < arena_w - 80 or not 0 < yf < arena_h:
            dead(1)

    def move_all(self): # Move all the actors in the arena by one step in their direction
        for i in range(len(self._actors)):
            self._actors[i].move()

    def print_actors(self): # Print all the actors in the arena to the screen
        global lives
        for i in reversed(self._actors):
            g2d.draw_image_clip(sprites, i.get_position(), i.get_symbol())
        for i in range(lives):
            g2d.draw_image_clip(
                sprites, (550 + i * 28, 6, 25, 33), (337, 172, 25, 33))

    def add_actors(self): # Add the actors to the arena
        frog = Frog(320, 440, 0)
        self._actors.append(frog)
        frog2 = Frog(144, 440, 1)
        self._actors.append(frog2)
        raft1 = Raft(-30, 82, 0)
        self._actors.append(raft1)
        raft2 = Raft(670, 114, 1)
        self._actors.append(raft2)
        raft3 = Raft(0, 146, 0)
        self._actors.append(raft3)
        croc = Croc(600, 178, 2)
        self._actors.append(croc)
        raft5 = Raft(300, 210, 0)
        self._actors.append(raft5)
        raft6 = Raft(110, 82, 0)
        self._actors.append(raft6)
        raft7 = Raft(200, 114, 1)
        self._actors.append(raft7)
        raft8 = Raft(670, 146, 0)
        self._actors.append(raft8)
        turtle1 = Turtle(150, 178, 0)
        self._actors.append(turtle1)
        turtle2 = Turtle(0, 178, 0)
        self._actors.append(turtle2)
        turtle3 = Turtle(187, 178, 0)
        self._actors.append(turtle3)
        turtle4 = Turtle(113, 178, 0)
        self._actors.append(turtle4)
        raft10 = Raft(-20, 210, 0)
        self._actors.append(raft10)
        raft11 = Raft(300, 146, 0)
        self._actors.append(raft11)
        car1 = Car(635, 271, 0)
        self._actors.append(car1)
        car2 = Car(670, 303, 1)
        self._actors.append(car2)
        car3 = Car(0, 335, 0)
        self._actors.append(car3)
        car4 = Car(600, 367, 2)
        self._actors.append(car4)
        car5 = Car(300, 399, 0)
        self._actors.append(car5)
        car6 = Car(110, 271, 0)
        self._actors.append(car6)
        car7 = Car(200, 303, 1)
        self._actors.append(car7)
        car8 = Car(670, 335, 0)
        self._actors.append(car8)
        car9 = Car(150, 367, 2)
        self._actors.append(car9)
        car10 = Car(-20, 399, 0)
        self._actors.append(car10)
        car11 = Car(300, 335, 0)
        self._actors.append(car11)
        endline = EndLine(0, 34, 0)
        self._actors.append(endline)
        trophy = Trophy()
        self._actors.append(trophy)
        river = River(0, 80, 0)
        self._actors.append(river)
        river2 = River(48, 48, 1)
        self._actors.append(river2)
        river3 = River(176, 48, 1)
        self._actors.append(river3)
        river4 = River(304, 48, 1)
        self._actors.append(river4)
        river5 = River(432, 48, 1)
        self._actors.append(river5)
        river6 = River(560, 48, 1)
        self._actors.append(river6)

    def actors(self) -> list: # Return the list of actors in the arena
        return list(self._actors)

    def frog_goes_up(self, frog_n): # The frog goes up in the arena
        self._actors[frog_n]._dir = 'u'

    def frog_goes_down(self, frog_n): # The frog goes down
        self._actors[frog_n]._dir = 'd'

    def frog_goes_left(self, frog_n): # The frog goes left
        self._actors[frog_n]._dir = 'l'

    def frog_goes_right(self, frog_n): # The frog goes right
        self._actors[frog_n]._dir = 'r'

    def frog_stays(self, frog_n): # The frog stays still
        self._actors[frog_n]._dir = 's'

    def unclip_frog(self, frog_n): # Unclip the frog from the river
        self._actors[frog_n]._clipped = False

    def reset_frog(self, frog_n): # Reset the frog position
        if frog_n == 0:
            self._actors[0] = Frog(320, 440, 0)
        else:
            self._actors[1] = Frog(144, 440, 1)


class Actor(): # The actor class (parent class)
    def move(self):
        raise NotImplementedError("Abstract method")

    def collide(self, frog_n):
        raise NotImplementedError("Abstract method")

    def get_position(self):
        raise NotImplementedError("Abstract method")

    def get_symbol(self):
        raise NotImplementedError("Abstract method") # The symbol of the actor


class Frog(Actor):  # The frog class
    def __init__(self, x, y, istance_type):
        self._x = x
        self._y = y
        self._w = 31
        self._h = 23
        self._istance_type = istance_type
        if self._istance_type == 0:
            self._imagex = 8
            self._imagey = 367
        elif self._istance_type == 1:
            self._imagex = 267
            self._imagey = 377
        self._dir = 's'
        self._speed = 0
        self._clipped = False

    def move(self):
        global framecount, framecount2
        if self._istance_type == 0:
            if framecount >= 10:
                self.set_symbol(8, 367, 31, 23)
                self._dir = 's'
                framecount = 0
            if self._dir == 's':
                self._speed = 0
                self.set_symbol(8, 367, 31, 23)
            if self._dir == 'u':
                self._speed = 6.5
                self.set_symbol(41, 365, 29, 23)
                self._y -= self._speed
                framecount += 1
                arena.check_frog_position()
            if self._dir == 'd':
                self._speed = 6.5
                self.set_symbol(110, 365, 29, 23)
                self._y += self._speed
                framecount += 1
                arena.check_frog_position()
            if self._dir == 'l':
                self._speed = 5
                self.set_symbol(110, 335, 29, 23)
                self._x -= self._speed
                framecount += 1
                arena.check_frog_position()
            if self._dir == 'r':
                self._speed = 5
                self.set_symbol(39, 335, 29, 23)
                self._x += self._speed
                framecount += 1
                arena.check_frog_position()
        else:
            if framecount2 >= 10:
                self.set_symbol(367, 377, 29, 23)
                self._dir = 's'
                framecount2 = 0
            if self._dir == 's':
                self._speed = 0
                self.set_symbol(267, 377, 29, 23)
            if self._dir == 'u':
                self._speed = 6.5
                self.set_symbol(342, 371, 29, 23)
                self._y -= self._speed
                framecount2 += 1
                arena.check_frog_position()
            if self._dir == 'd':
                self._speed = 6.5
                self.set_symbol(311, 334, 29, 23)
                self._y += self._speed
                framecount2 += 1
                arena.check_frog_position()
            if self._dir == 'l':
                self._speed = 5
                self.set_symbol(344, 405, 29, 23)
                self._x -= self._speed
                framecount2 += 1
                arena.check_frog_position()
            if self._dir == 'r':
                self._speed = 5
                self.set_symbol(266, 407, 29, 23)
                self._x += self._speed
                framecount2 += 1
                arena.check_frog_position()

    def clip(self, raft_dx, raft_dir):
        self._clipped = True
        if raft_dir == 'l':
            self._x -= raft_dx
        if raft_dir == 'r':
            self._x += raft_dx
        arena.check_frog_position()

    def collide(self, frog_n):
        pass

    def get_position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def set_symbol(self, x, y, w, h):
        self._imagex = x
        self._imagey = y
        self._w = w
        self._h = h

    def get_symbol(self) -> (int, int, int, int):
        return self._imagex, self._imagey, self._w, self._h


class Turtle(Actor): # The turtle class
    def __init__(self, x, y, istance_type):
        self._x = x
        self._y = y
        self._w = 50
        self._h = 25
        self._imagex = 13
        self._imagey = 408
        self._speed = 3
        self._dir = 'l'
        self._istance_type = istance_type
        self._timer = 0

    def move(self):
        self._x -= self._speed
        if self._x < -110:
            self._x += (arena_w + 100)
            self._timer = 0
        if self._x > 650:
            self._timer = 0
            self._x -= (arena_w + 100)

    def collide(self, frog_n):
        arena._actors[frog_n].clip(self._speed, self._dir)
        self._timer += 1
        if self._timer >= 150:
            dead(frog_n)

    def get_position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def get_symbol(self) -> (int, int, int, int):
        if self._timer == 0:
            self._imagex, self._imagey = 13, 408
        if self._timer >= 1:
            self._timer += 1
        if 90 <= self._timer <= 150:
            self._imagex, self._imagey = 130, 407
        if self._timer > 150:
            self._imagex, self._imagey = 175, 408
        return self._imagex, self._imagey, self._w - 13, self._h


class Croc(Actor): # The crocodile class
    def __init__(self, x, y, istance_type):
        self._x = x
        self._y = y
        self._istance_type = istance_type
        self._speed = 3
        self._w = 99
        self._h = 28
        self._imagex = 151
        self._imagey = 369
        self._dir = 'l'

    def move(self):
        self._x -= self._speed
        if self._x < -110:
            self._x += (arena_w + 100)
        if self._x > 650:
            self._x -= (arena_w + 100)

    def collide(self, frog_n):
        arena._actors[frog_n].clip(self._speed, self._dir)

    def get_position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def get_symbol(self) -> (int, int, int, int):
        return self._imagex, self._imagey, self._w, self._h


class Trophy(Actor): # The trophy class (the goal) (the end)
    def __init__(self):
        self._position = randrange(1, 5)
        self._y = 48
        self._imagex = 134
        self._imagey = 233
        self._w = 35
        self._h = 35
        if self._position == 1:
            self._x = 109
        elif self._position == 2:
            self._x = 240
        elif self._position == 3:
            self._x = 368
        elif self._position == 4:
            self._x = 496

    def move(self):
        pass

    def collide(self, frog_n):
        global score
        score += 150
        self._last_position = self._position
        self._position = randrange(1, 5)
        while self._position == self._last_position:
            self._position = randrange(1, 5)
        if self._position == 1:
            self._x = 109
        elif self._position == 2:
            self._x = 240
        elif self._position == 3:
            self._x = 368
        elif self._position == 4:
            self._x = 496

    def get_position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def get_symbol(self) -> (int, int, int, int):
        return self._imagex, self._imagey, self._w, self._h


class Raft(Actor): # The raft class (the moving platform) (the middle)  (the bridge)
    def __init__(self, x, y, istance_type):
        self._x = x
        self._y = y
        self._istance_type = istance_type
        if istance_type == 0:
            self._speed = 3
            self._dir = 'r'
            self._w = 91
            self._h = 25
            self._imagex = 4
            self._imagey = 227
        if istance_type == 1:
            self._speed = 2
            self._dir = 'l'
            self._w = 122
            self._h = 25
            self._imagex = 4
            self._imagey = 196
        if istance_type == 2:
            self._speed = 4
            self._dir = 'l'
            self._w = 91
            self._h = 25
            self._imagex = 4
            self._imagey = 227

    def move(self):
        if self._dir == 'l':
            self._x -= self._speed
        if self._dir == 'r':
            self._x += self._speed
        if self._x < -110:
            self._x += (arena_w + 100)
        if self._x > 650:
            self._x -= (arena_w + 100)

    def collide(self, frog_n):
        arena._actors[frog_n].clip(self._speed, self._dir)

    def get_position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def get_symbol(self) -> (int, int, int, int):
        return self._imagex, self._imagey, self._w, self._h


class Car(Actor): # The car class (the enemy) (the bad) (the obstacle) (the danger) (the death)
    def __init__(self, x, y, istance_type):
        self._x = x
        self._y = y
        self._istance_type = istance_type
        if istance_type == 0:
            self._speed = 5
            self._dir = 'r'
            self._w = 31
            self._h = 31
            self._imagex = 79
            self._imagey = 261
        if istance_type == 1:
            self._speed = 5
            self._dir = 'l'
            self._w = 31
            self._h = 31
            self._imagex = 43
            self._imagey = 262
        if istance_type == 2:
            self._speed = 10
            self._dir = 'l'
            self._w = 31
            self._h = 31
            self._imagex = 8
            self._imagey = 262

    def move(self):
        if self._dir == 'l':
            self._x -= self._speed
        if self._dir == 'r':
            self._x += self._speed
        if self._x < -110:
            self._x += (arena_w + 100)
        if self._x > 650:
            self._x -= (arena_w + 100)

    def collide(self, frog_n):
        dead(frog_n)

    def get_position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def get_symbol(self) -> (int, int, int, int):
        return self._imagex, self._imagey, self._w, self._h


class River(Actor): # The river class (the water) (the middle) (the bridge) (the goal) (the end)  (the death)
    def __init__(self, x, y, istance_type):
        self._x = x
        self._y = y
        if istance_type == 0:
            self._w = 640
            self._h = 160
        elif istance_type == 1:
            self._w = 31
            self._h = 45
        self._imagex = 0
        self._imagey = 474

    def move(self):
        pass

    def collide(self, frog_n):
        dead(frog_n)

    def get_position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def get_symbol(self) -> (int, int, int, int):
        return self._imagex, self._imagey, self._w, self._h

# It's a class that represents the end line of the game


class EndLine(Actor): # The end line class (the goal) (the end) (the death)
    def __init__(self, x, y, istance_type):
        self._x = x
        self._y = y
        self._w = 640
        self._h = 20
        self._imagex = 0
        self._imagey = 474

    def move(self):
        """
        It returns the position of the frog.
        """
        pass

    def collide(self, frog_n):
        won(frog_n)

    def get_position(self) -> (int, int, int, int):
        return self._x, self._y, self._w, self._h

    def get_symbol(self) -> (int, int, int, int):
        return self._imagex, self._imagey, self._w, self._h


def check_collision(frog: Actor, other: Actor): # The collision function
    """
    If the frog is within the other actor's bounding box, then the other actor collides with the frog

    :param frog: Actor
    :type frog: Actor
    :param other: the object that the frog is colliding with
    :type other: Actor
    :return: the result of the collision.
    """
    xf, yf, wf, hf = frog.get_position()
    xo, yo, wo, ho = other.get_position()
    if (xo <= xf + wf - 1 <= xo + wo) and (yo <= yf + hf - 1 <= yo + ho):
        other.collide(frog._istance_type)
    else:
        return


def finished(): # The function that checks if the game is finished
    """
    It checks if the frog has reached the top of the screen, and if so, it adds 100 to the score and
    resets the frog to the bottom of the screen
    """
    ""
    global score
    highest = read_score()
    if score >= int(highest):
        save_score()
        highest = score
    s = ''
    g2d.alert(s.join(("Game Over!\nYour score: ", str(
        score), "\nHighest score is: ", str(highest))))
    exit()


def won(frog_n): # The function that checks if the frog has won
    """
    `won` is called when a frog reaches the top of the screen, and `dead` is called when a frog is hit
    by a car

    :param frog_n: the frog number (0-3)
    """
    global score
    score += 100
    arena.reset_frog(frog_n)


def dead(frog_n): # The function that checks if the frog has died
    global lives
    lives -= 1
    arena.reset_frog(frog_n)


def update(): # The update function
    """
    It updates the game
    """
    global framecount, lives, framecount2
    arena.check_all_collisions()
    g2d.fill_canvas((255, 255, 255))
    g2d.draw_image(background, (0, 0))
    arena.move_all()
    arena.print_actors()
    if framecount > 0:
        framecount += 1
    if framecount == 0:
        arena.unclip_frog(0)
    if framecount2 > 0:
        framecount2 += 1
    if framecount2 == 0:
        arena.unclip_frog(1)
    if lives < 0:
        finished()
    g2d.draw_text(str(score), (255, 255, 255), (6, 17), 21)


def keydown(code): # The keydown function
    """
    The function keydown() is called when a key is pressed.

    :param code: the key that was pressed
    """
    # print(code)
    if code == "ArrowUp":
        if framecount == 0:
            arena.frog_goes_up(0)
    if code == "ArrowDown":
        if framecount == 0:
            arena.frog_goes_down(0)
    if code == "ArrowLeft":
        if framecount == 0:
            arena.frog_goes_left(0)
    if code == "ArrowRight":
        if framecount == 0:
            arena.frog_goes_right(0)
    if code == 'KeyW':
        if framecount2 == 0:
            arena.frog_goes_up(1)
    if code == 'KeyS':
        if framecount2 == 0:
            arena.frog_goes_down(1)
    if code == 'KeyA':
        if framecount2 == 0:
            arena.frog_goes_left(1)
    if code == 'KeyD':
        if framecount2 == 0:
            arena.frog_goes_right(1)
    if code == "Space":
        x, y, w, h = arena._actors[0].get_position()
        if (x <= 570 + 20 - 1 <= x + w) and (y <= 245 + 20 - 1 <= y + h):
            g2d.alert("Credits:\nCoded by: Kyle Wisecarver ")


def keyup(code): # The keyup function
    """
    "When the keyup event is triggered, do nothing."

    Now let's add some code to the keyup function

    :param code: The key code of the key that was released
    """
    pass


def main(): # The main function (the function that runs the game) (the function that runs the game)
    """
    It creates an arena, adds actors to it, and then starts the main loop
    """
    global arena, framecount, framecount2 # The global variables that are used in the game (the global variables that are used in the game)
    g2d.alert("Welcome in Froggier! \nReach the other shore, to collect bonus trophies! Don't get hit by the cars!")
    arena = Arena(arena_w, arena_h) # The arena (the arena)
    arena.add_actors() # The actors (the actors)
    framecount, framecount2 = 0, 0 # The framecount (the framecount)
    g2d.handle_keyboard(keydown, keyup) # The keyboard (the keyboard)
    g2d.main_loop(update, 1000//30) # The main loop (the main loop)


main()
