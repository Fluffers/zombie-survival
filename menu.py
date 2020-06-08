import pygame as pg

class button():
    def __init__(self, color, x, y, width, height, text=''):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text

    def draw(self, win, outline=None):
        # Call this method to draw the button on the screen
        if outline:
            pg.draw.rect(win, outline, (self.x - 2, self.y - 2, self.width + 4, self.height + 4), 0)

        pg.draw.rect(win, self.color, (self.x, self.y, self.width, self.height), 0)

        if self.text != '':
            font = pg.font.SysFont('comicsans', 60)
            text = font.render(self.text, 1, (0, 0, 0))
            win.blit(text, (
            self.x + (self.width / 2 - text.get_width() / 2), self.y + (self.height / 2 - text.get_height() / 2)))

    def isOver(self, pos):
        # Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True

        return False

def draw_text(self, text, font_name, size, color, x, y, align="top-left"):
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    if align == "top-left":
        text_rect.topleft = (x, y)
    if align == "top-right":
        text_rect.topright = (x, y)
    if align == "bottom-left":
        text_rect.bottomleft = (x, y)
    if align == "bottom-right":
        text_rect.bottomright = (x, y)
    if align == "top":
        text_rect.midtop = (x, y)
    if align == "bottom":
        text_rect.midbottom = (x, y)
    if align == "right":
        text_rect.midright = (x, y)
    if align == "left":
        text_rect.midleft = (x, y)
    if align == "center":
        text_rect.center = (x, y)
    self.screen.blit(text_surface, text_rect)

def draw_button(self, x, y, width, height, color, thickness=0):
    button = pg.Rect(x - width / 2, y - height / 2, width, height)
    pg.draw.rect(self.screen, color, button, thickness)
    return button