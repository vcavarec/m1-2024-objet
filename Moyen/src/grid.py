import keyboard as keyboard
import pygame
import time
import keyboard

class Grid:
    def __init__(self, scale):
        self.cellSize = scale  # Size of one cell

        self.gameStarted = False  # Game state
        self.monitorDisplay = None  # PyGame window
        self.monitorSpecs = None  # PyGame display information
        self.nbColumns = None
        self.nbRows = None

        # Build GUI
        self.buildGrid()

    def buildGrid(self):
        pygame.init()
        pygame.display.set_caption("Conway's Game of Life")
        self.monitorSpecs = pygame.display.Info()
        # Sets the size of the window according to the screen resolution
        self.monitorDisplay = pygame.display.set_mode([self.monitorSpecs.current_w, self.monitorSpecs.current_h])
        # Compute the number of columns and rows according to screen resolution and cell size
        self.nbColumns = int(self.monitorSpecs.current_w / self.cellSize)
        self.nbRows = int(self.monitorSpecs.current_h / self.cellSize)

    def drawCommands(self):
        pygame.event.get()
        if not self.gameStarted:
            font = pygame.font.SysFont('arial', 20)
            space = font.render('Press <SPACE> to start the game', False, (180, 180, 180))
            spacePos = (self.monitorSpecs.current_w * 0.05, self.monitorSpecs.current_h * 0.01)
            enter = font.render('Press <ENTER> to generate random seed', False, (180, 180, 180))
            enterPos = (self.monitorSpecs.current_w * 0.05, self.monitorSpecs.current_h * 0.04)
            click = font.render('Press <LEFTCLICK> to add a cell', False, (180, 180, 180))
            clickPos = (self.monitorSpecs.current_w * 0.05, self.monitorSpecs.current_h * 0.07)
            clear = font.render('Press <RETURN> to clear the grid', False, (180, 180, 180))
            clearPos = (self.monitorSpecs.current_w * 0.05, self.monitorSpecs.current_h * 0.1)
            self.monitorDisplay.blit(space, spacePos)
            self.monitorDisplay.blit(enter, enterPos)
            self.monitorDisplay.blit(click, clickPos)
            self.monitorDisplay.blit(clear, clearPos)
        else:
            pygame.event.get()
            font = pygame.font.SysFont('arial', 20)
            space = font.render('Press <SPACE> to pause the game', False, (180, 180, 180))
            spacePos = (self.monitorSpecs.current_w * 0.05, self.monitorSpecs.current_h * 0.01)
            self.monitorDisplay.blit(space, spacePos)
            pygame.display.update()
            if keyboard.is_pressed('SPACE'):
                while keyboard.is_pressed('SPACE'):
                    time.sleep(0.01)
                self.gameStarted = not self.gameStarted
        pygame.display.update()

    def drawCells(self, cells):
        # Iterate through the whole board (2D matrix)
        for x in range(len(cells)):
            for y in range(len(cells[0])):
                # pygame.draw.rect takes a rect as an argument: (posX, posY, width, height)
                rect = [x * self.cellSize, y * self.cellSize, self.cellSize, self.cellSize]
                # Draws a cell on the display, blue if the cell is living, black if the cell is dead
                if cells[x][y] == 1:
                    pygame.draw.rect(self.monitorDisplay, (14, 72, 143), rect)
                else:
                    pygame.draw.rect(self.monitorDisplay, (0, 0, 0), rect)
                    pygame.draw.rect(self.monitorDisplay, (5, 5, 5), rect, 1)
        pygame.display.update()
