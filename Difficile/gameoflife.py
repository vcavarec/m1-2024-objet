import platform
import keyboard
import time
import pyautogui

from src.grid import Grid
from src.game import Game

_OS = platform.system()
if _OS == "Windows":
    import win32api
elif _OS == "Darwin":
    from Quartz import CGEventSourceButtonState, kCGEventSourceStateHIDSystemState, kCGMouseButtonLeft


if __name__ == '__main__':

    # Useful parameters to edit your simulation
    # @cellSize: sets the width and height of each cell in pixels
    # @cellDensity: gives the percentage used for the distribution of initial living cells
    cellSize = 10
    cellDensity = 20
    cycleTime = .05

    grid = Grid(scale=cellSize)
    game = Game(density=cellDensity, nbColumns=grid.nbColumns, nbRows=grid.nbRows)

    def check_mouse_presses():
        if _OS == "Windows":
            return win32api.GetKeyState(0x01) < 0
        elif _OS == "Darwin":
            return CGEventSourceButtonState(kCGEventSourceStateHIDSystemState, kCGMouseButtonLeft) == 1

    def check_keyboard_presses():
        if keyboard.is_pressed('ENTER'):
            game.buildCells(density=cellDensity, nbColumns=grid.nbColumns, nbRows=grid.nbRows)
            grid.drawCells(cells=game.cells)
            time.sleep(0.3)

        if keyboard.is_pressed('BACKSPACE'):
            game.clearCells(nbColumns=grid.nbColumns, nbRows=grid.nbRows)
            grid.drawCells(cells=game.cells)

        if keyboard.is_pressed('SPACE'):
            while keyboard.is_pressed('SPACE'):
                time.sleep(0.01)
            grid.gameStarted = not grid.gameStarted

        if keyboard.is_pressed('ESCAPE'):
            exit()

    while True:
        grid.drawCommands()
        check_keyboard_presses()
        if grid.gameStarted:
            game.cycle()
            time.sleep(cycleTime)
        else:
            if check_mouse_presses():
                game.cells[int(pyautogui.position().x / cellSize)][int(pyautogui.position().y / cellSize)] = 1 - game.cells[int(pyautogui.position().x / cellSize)][int(pyautogui.position().y / cellSize)]
                time.sleep(.1)
        grid.drawCells(game.cells)
