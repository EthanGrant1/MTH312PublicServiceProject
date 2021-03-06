# Gamer moment
import pygame as p

# Pygame local variables like QUIT
# from pygame.locals import *

# Initialize pygame to our system
p.init()


# Text boxes are simply rendered Rect(s) that allow for text to be held inside them
# (which is rendered using pygame.font.Font information)
class textbox:

    # Constructor
    def __init__(self, box=p.Rect(0, 0, 0, 0), lineWeight=0, boxColor=p.Color('white'), text='Placeholder',
                 font=None, fontSize=32, fontColor=p.Color('white')):

        # Box is a pygame.Rect() object. It has a color and a line weight.
        self.box = box
        self.boxColor = p.Color(str(boxColor))
        self.lineWeight = lineWeight

        # Text to be rendered inside the box. It has a font, a font size,
        # and a font color.
        self.text = text
        self.fontSize = fontSize

        if font is not None:
            self.font = p.font.Font(str(font), self.fontSize)
        else:
            self.font = p.font.Font(None, self.fontSize)

        self.fontColor = p.Color(str(fontColor))

    # Getters #
    def getBox(self):
        return self.box

    def getLineWeight(self):
        return self.lineWeight

    def getBoxColor(self):
        return self.boxColor

    def getText(self):
        return self.text

    def getFont(self):
        return self.font

    def getFontSize(self):
        return self.fontSize

    def getFontColor(self):
        return self.fontColor

    # Setters #
    def setBox(self, box):
        self.box = box

    def setLineWeight(self, lineWeight):
        self.lineWeight = lineWeight

    def setBoxColor(self, boxColor):
        self.boxColor = boxColor

    def setText(self, text):
        self.text = text

    def setFont(self, font):
        self.font = font

    def setFontSize(self, fontSize):
        self.fontSize = fontSize

    def setFontColor(self, fontColor):
        self.fontColor = fontColor

    # drawBox will use the draw.rect() method to draw the box to the screen.
    # The method will require a screen object which will be defined in the main
    # program.
    # def drawBox(self, screen):
    #   p.draw.rect(screen, self.boxColor, self.box, self.lineWeight)

    # createRender will use the font.render() method to render the text as a
    # surface. It simply uses the variables that we defined previously.
    # def createRender(self):
    #   return self.font.render(self.text, True, self.fontColor)

    # blit will use the Surface.blit() method to draw an object on the
    # screen. In this case it will be our text surface that we defined
    # in createRender. We will blit the surface with some padding, so
    # that it fits snugly in the box.
    # def blit(self, screen, render):
    # 	screen.blit(render, (self.box.x + 5, self.box.y + 5))

    # drawText splits the string into multiple lines (if they exist)
    # each line is in turn rendered in the font as a surface and then
    # blit-ed to the screen
    def drawText(self, screen):

        rect = self.box
        surface = p.Surface((rect.w, rect.h))
        surface.fill(self.boxColor)
        txt = self.text
        y = rect.top
        lineSpacing = -2

        screen.blit(surface, (self.box.x, self.box.y))

        # https://www.pygame.org/wiki/TextWrap
        while txt:
            i = 1

            # determine if the row of text will be outside our area
            if y + self.fontSize > rect.bottom:
                break

            # determine maximum width of line
            while (self.font.size(txt[:i])[0] + 5) < rect.width and i < len(txt):
                i += 1

            # if we've wrapped the text, add some ellipses
            if i < len(txt):
                txt = txt[:i-5] + " ... " + txt[i:]

            image = self.font.render(txt[:i], True, self.fontColor)
            screen.blit(image, (rect.left + 5, y + 5))
            y += self.fontSize + lineSpacing

            txt = txt[i:]

        return txt
