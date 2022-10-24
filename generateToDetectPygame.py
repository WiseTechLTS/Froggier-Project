'''
Froggier.py
@author Kyle Wisecarver
@license This software is free - http://www.gnu.org/licenses/gpl.html'''
'Maybe we can code as a list of to do items'

''''''

try:
    import pygame  # , pygame.gfxdraw
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


def init_canvas(size: (int, int)):   # function to initialize the canvas (width, height) (width, height) (width, height) (width, height) (width, height) 
    '''Set size of first CANVAS and return it'''
    global _canvas
    pygame.init()
    _canvas = pygame.display.set_mode(size)
    _canvas.fill((255, 255, 255))


def fill_canvas(color: (int, int, int)) -> None: # function to fill the canvas with a color (r, g, b) (r, g, b) (r, g, b) (r, g, b) (r, g, b)
    _canvas.fill(color)


def update_canvas() -> None: # function to update the canvas and handle events (must be called every frame)
    pygame.display.update()


def draw_line(color: (int, int, int), pt1: (int, int), pt2: (int, int)) -> None: # function to draw a line to the canvas
    pygame.draw.line(_canvas, color, pt1, pt2)


def draw_circle(color: (int, int, int), center: (int, int), radius: int) -> None: # function to draw a circle to the canvas
    pygame.draw.circle(_canvas, color, center, radius)


def draw_rect(color: (int, int, int), rectangle: (int, int, int, int)) -> None: # function to draw a rectangle to the canvas
    pygame.draw.rect(_canvas, color, rectangle)


def draw_text(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None: # function to draw text to the canvas
    font = pygame.font.SysFont('freesansbold', size)
    surface = font.render(txt, True, color)  # , (255, 255, 255))
    _canvas.blit(surface, pos)


def draw_text_centered(txt: str, color: (int, int, int), pos: (int, int), size: int) -> None: # function to draw text centered on the canvas
    font = pygame.font.SysFont('freesansbold', size)
    surface = font.render(txt, True, color)  # , (255, 255, 255))
    w, h = surface.get_size()
    _canvas.blit(surface, (pos[0] - w // 2, pos[1] - h // 2))


def load_image(url: str) -> pygame.Surface: # function to load images into the program
    return pygame.image.load(url)


def draw_image(image: pygame.Surface, pos: (int, int)) -> None: # function to draw an image to the canvas (x, y) (x, y) (x, y) (x, y) (x, y)
    _canvas.blit(image, pos)


def draw_image_clip(image: pygame.Surface, rect: (int, int, int, int), area: (int, int, int, int)) -> None: # function to draw a clipped image to the canvas (for animation) (x, y, width, height) (x, y, width, height) (x, y, width, height) (x, y, width, height) (x, y, width, height)
    x0, y0, w0, h0 = area
    x1, y1, w1, h1 = rect
    if w0 == w1 and h0 == h1:
        _canvas.blit(image, rect, area=area)
    else:
        cropped = pygame.Surface((w0, h0), pygame.SRCALPHA)
        cropped.blit(image, (0, 0), area=area)
        scaled = pygame.transform.smoothscale(cropped, (w1, h1))
        _canvas.blit(scaled, (x1, y1))


def load_audio(url: str) -> pygame.mixer.Sound: # function to load audio files into the program
    return pygame.mixer.Sound(url)


def play_audio(audio: pygame.mixer.Sound, loop=False) -> None: # function to play audio playback
    audio.play(-1 if loop else 0)


def pause_audio(audio: pygame.mixer.Sound) -> None: # function to pause audio playback
    audio.stop()


def alert(message: str) -> None: # function to alert the user with a message box
    messagebox.showinfo(" ", message)


def confirm(message: str) -> bool: # function to confirm with the user
    return messagebox.askokcancel(" ", message)


def prompt(message: str) -> str: # function to prompt the user for input
    return simpledialog.askstring(" ", message, parent=_tkmain)


def handle_keyboard(keydown, keyup): # function to handle keyboard events
    global _keydown, _keyup
    _keydown, _keyup = keydown, keyup


def handle_mouse(mousedown, mouseup): # function to handle mouse events
    global _mousedown, _mouseup
    _mousedown, _mouseup = mousedown, mouseup


def web_key(key: int) -> str: # function to convert pygame keys to web keys
    word = pygame.key.name(key)
    word = word[0].upper() + word[1:]
    if len(word) == 1 and word.isalpha():
        word = "Key" + word
    elif len(word) == 1 and word.isdigit():
        word = "Digit" + word
    elif word in ("Up", "Down", "Right", "Left"):
        word = "Arrow" + word
    return word


def main_loop(update=None, millis=100) -> None: # function to run the main loop of the program and update the screen every 100 milliseconds
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


def exit() -> None: # function to exit the program
    pygame.quit()
    sys.exit()
