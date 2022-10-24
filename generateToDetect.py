try:
    import pygame
except:
    import subprocess
    import sys
    subprocess.call([sys.executable, "-m", "pip", "install", "pygame"])
    import pygame

import sys
from tkinter import Tk, messagebox, simpledialog

_tkmain = Tk()
_tkmain.wm_withdraw()  # to hide the main window

_canvas = None
_keydown, _keyup = None, None
_mousedown, _mouseup = None, None


def init_canvas(size: (int, int)):
    '''Set size of first CANVAS and return it'''
    global _canvas
    pygame.init()
    _canvas = pygame.display.set_mode(size)
    _canvas.fill((255, 255, 255))


def fill_canvas(color: (int, int, int)) -> None:
    _canvas.fill(color)


def update_canvas() -> None: # update the canvas (display the changes)
    pygame.display.update()


def draw_line(color: (int, int, int), pt1: (int, int), pt2: (int, int)) -> None: # draw a line from pt1 to pt2 with a color (pt1 and pt2 are tuples of (x, y) coordinates)
    pygame.draw.line(_canvas, color, pt1, pt2)


def draw_circle(color: (int, int, int), center: (int, int), radius: int) -> None: # draw a circle with a color (center is a tuple of (x, y) coordinates) and a radius (int)
    pygame.draw.circle(_canvas, color, center, radius)


def draw_rect(color: (int, int, int), rectangle: (int, int, int, int)) -> None: # draw a rectangle with a color (rectangle is a tuple of (x, y, width, height) coordinates)   
    pygame.draw.rect(_canvas, color, rectangle)


def draw_text(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None: # draw text at a position (pos) on the canvas (pos is a tuple of (x, y) coordinates)
    font = pygame.font.SysFont('freesansbold', size)
    surface = font.render(txt, True, color)  # , (255, 255, 255))
    _canvas.blit(surface, pos)


def draw_text_centered(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None: # draw text centered at a position (pos) on the canvas (pos is a tuple of (x, y) coordinates)
    font = pygame.font.SysFont('freesansbold', size)
    surface = font.render(txt, True, color)  # , (255, 255, 255))
    w, h = surface.get_size()
    _canvas.blit(surface, (pos[0] - w // 2, pos[1] - h // 2))


def load_image(url: str) -> pygame.Surface: # load an image file and return it as a pygame.Surface object (https://www.pygame.org/docs/ref/surface.html#pygame.Surface)
    return pygame.image.load(url)


def draw_image(image: pygame.Surface, pos: (int, int)) -> None: # draw an image at a position (pos) on the canvas (pos is a tuple of (x, y) coordinates)
    _canvas.blit(image, pos)


def draw_image_clip(image: pygame.Surface, rect: (int, int, int, int), area: (int, int, int, int)) -> None: # draw a clip of an image
    x0, y0, w0, h0 = area
    x1, y1, w1, h1 = rect
    if w0 == w1 and h0 == h1:
        _canvas.blit(image, rect, area=area)
    else:
        cropped = pygame.Surface((w0, h0), pygame.SRCALPHA)
        cropped.blit(image, (0, 0), area=area)
        scaled = pygame.transform.smoothscale(cropped, (w1, h1))
        _canvas.blit(scaled, (x1, y1))


def load_audio(url: str) -> pygame.mixer.Sound: # load an audio file and return it as a pygame.mixer.Sound object (https://www.pygame.org/docs/ref/mixer.html#pygame.mixer.Sound)
    return pygame.mixer.Sound(url)


def play_audio(audio: pygame.mixer.Sound, loop=False) -> None: # play the audio (if it is not playing) and pause it if it is playing
    audio.play(-1 if loop else 0)


def pause_audio(audio: pygame.mixer.Sound) -> None: # pause the audio (if it is playing) and resume it if it is paused
    audio.stop()


def alert(message: str) -> None: # display an alert message to the user (no input) and continue execution
    messagebox.showinfo(" ", message)


def confirm(message: str) -> bool: # prompt the user for confirmation (yes/no) and return True if yes, False if no (or if the user closes the window)
    return messagebox.askokcancel(" ", message)


def prompt(message: str) -> str: # prompt the user for input
    return simpledialog.askstring(" ", message)

def handle_keyboard(keydown, keyup): # handle keyboard events (keydown, keyup) with (key) as parameters (key is the key pressed)
    global _keydown, _keyup
    _keydown, _keyup = keydown, keyup


def handle_mouse(mousedown, mouseup): # handle mouse events (mousedown, mouseup) with (x, y) as parameters (x, y are the position of the mouse)
    global _mousedown, _mouseup
    _mousedown, _mouseup = mousedown, mouseup


def web_key(key: int) -> str: # convert pygame key to web key (https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values)
    word = pygame.key.name(key)
    word = word[0].upper() + word[1:]
    if len(word) == 1 and word.isalpha():
        word = "Key" + word
    elif len(word) == 1 and word.isdigit():
        word = "Digit" + word
    elif word in ("Up", "Down", "Right", "Left"):
        word = "Arrow" + word
    return word


def main_loop(update=None, millis=100) -> None: # main loop of the program (update is called every millis milliseconds)
    clock = pygame.time.Clock()
    while True:
        for e in pygame.event.get():
            # print(e)
            if e.type == pygame.QUIT:
                exit()
            elif e.type == pygame.KEYDOWN and _keydown:
                _keydown(web_key(e.key))
            elif e.type == pygame.KEYUP and _keyup:
                _keyup(web_key(e.key))
            elif e.type == pygame.MOUSEBUTTONDOWN and _mousedown:
                _mousedown(e.pos, e.button - 1)
            elif e.type == pygame.MOUSEBUTTONUP and _mouseup:
                _mouseup(e.pos, e.button - 1)
        if update:
            update()
        pygame.display.flip()
        clock.tick(1000/millis)
    exit()


def exit() -> None: # exit the program
    pygame.quit()
    sys.exit()
