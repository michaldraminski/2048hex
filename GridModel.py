import random
import xml.etree.ElementTree as ET
import re


# Zamienia stringa na listę list
def convert(string):
    sets = re.findall(r'(?<=\[)[0-9,\,\w\'\s]*?(?=\])', string)
    converted = []
    for set in sets:
        x_coord = int(set[0])
        y_coord = int(set[3])
        value_coord = re.findall(r'(?<=\')[0-9\s]*?(?=\')', set)[0]
        changed = bool(re.findall(r'[a-z|A-Z]+', set)[0])
        converted.append([x_coord, y_coord, value_coord, changed])
    return converted


emptyChar = ""


debug = False


# Klasa zawierająca kody kolorów do kolorowej konsoli
class Colors:
    BLACK = ['\u001b[30m',"<font color=\"Black\">"]
    RED = ['\u001b[31m',"<font color=\"Red\">"]
    GREEN = ['\u001b[32m',"<font color=\"Green\">"]
    YELLOW = ['\u001b[33m',"<font color=\"Yellow\">"]
    BLUE = ['\u001b[34m',"<font color=\"Blue\">"]
    MAGENTA = ['\u001b[35m',"<font color=\"Magenta\">"]
    CYAN= ['\u001b[36m',"<font color=\"Cyan\">"]
    WHITE = ['\u001b[37m',"<font color=\"White\">"]
    ENDC = ['\033[0m',"<font color=\"Endc\">"]


class GridModel:
    def __init__(self, print_prefix, grid_size, callbackObject):
        super().__init__()
        self.print_prefix = print_prefix
        self.pola = []
        self.callbackObject = callbackObject
        middle = grid_size - 1
        start_idx = 0
        end_idx = (grid_size * 2 - 1) * 2

        self.firstx = middle
        self.lastx = middle + middle * 2
        self.lasty = middle * 2
        for i in range(grid_size):
            for j in range(start_idx, end_idx, 2):
                if i > 0:
                    self.pola.append([j, middle - i, "", False])
                self.pola.append([j, middle + i, "", False])
            start_idx += 1
            end_idx -= 1
        self.new_number()

    def logFunction(self, logMsg, color=None):
        self.callbackObject.print(color, logMsg)
        
    def new_number(self):
        newx = random.randint(0, len(self.pola)-1)
        occupied = [newx]
        while self.pola[newx][2] != emptyChar:
            newx = random.randint(0, len(self.pola) - 1)
            occupied.append(newx)
            if len(occupied) == len(self.pola):
                return
        self.pola[newx][2] = "2"


    def update_hex_text(self, x, y, new_label, combinedValue = False):
        for pole in self.pola:
            if pole[0] == x and pole[1] == y:
                pole[2] = new_label
                pole[3] = combinedValue
                break

    def get_cell_value(self, x, y):
        for pole in self.pola:
            if pole[0] == x and pole[1] == y:
                return str(pole[2]),pole[3]
        return "0", False

    def get_pola_copy(self):
        newPola = []
        for pole in self.pola:
            newPola.append(pole.copy())
        return newPola

    def set_pola_copy(self, polaSource):
        self.pola = []
        for pole in polaSource:
            self.pola.append(pole.copy())

    def move_element(self, startx, starty, endx, endy):
        end_label, endAlreadyCombined = self.get_cell_value(endx, endy)
        start_label, startAlreadyCombined = self.get_cell_value(startx, starty)
        # self.logFunction(self.print_prefix+startx, ",", starty, "do ", endx, ",", endy, "labele: ", start_label,end_label)
        if start_label == end_label and start_label != emptyChar and not startAlreadyCombined and not endAlreadyCombined:
            self.update_hex_text(endx, endy, str(int(start_label)+int(end_label)), True)
            self.update_hex_text(startx, starty, emptyChar)
            return True
        elif start_label != emptyChar and end_label == emptyChar:
            self.update_hex_text(endx, endy, start_label, startAlreadyCombined)
            self.update_hex_text(startx, starty, emptyChar)
            return True
        else:
            return False

    def moveW(self):
        retVal = False
        startx = self.firstx
        stopx = self.lastx
        stepx = -1

        for y in range(self.lasty + 1):
            x = startx + 2
            while x <= stopx:
                if self.move_element(x, y, x - 2, y):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
            startx += stepx
            stopx -= stepx
        return retVal

    def moveE(self):
        retVal = False
        startx = self.firstx
        stopx = self.lastx
        stepx = -1
        for y in range(self.lasty + 1):
            x = stopx - 2
            while x >= startx:
                if self.move_element(x, y, x + 2, y) :
                    retVal = True
                x -= 2
            if startx == 0:
                stepx = - stepx
            startx += stepx
            stopx -= stepx
        return retVal

    def moveNE(self):
        retVal = False
        startx = self.firstx - 1
        stopx = self.lastx + 1
        stepx = -1
        offset = -2
        for y in range(1, self.lasty + 1):
            x = startx
            while x <= stopx + offset:
                if debug:
                    self.logFunction(self.print_prefix+"startx: " + str(startx) + " stepx: " + str(stepx) + "," + str(x) + ":" + str(y))
                if self.move_element(x, y, x + 1, y-1):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
                offset = 0
            startx += stepx
            stopx -= stepx
        return retVal

    def moveNW(self):
        retVal = False
        startx = self.firstx - 1
        stopx = self.lastx + 1
        stepx = -1
        offsetx = 2
        for y in range(1, self.lasty + 1):
            x = startx + offsetx
            while x <= stopx:
                if debug:
                    self.logFunction(self.print_prefix + "startx: " + str(startx) + " stepx: " + str(stepx) + "," + str(x) + ":" + str(y))
                if self.move_element(x, y, x - 1, y - 1):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
                offsetx = 0
            startx += stepx
            stopx -= stepx
        return retVal

    def moveSW(self):
        retVal = False
        startx = self.firstx - 1
        stopx = self.lastx + 1
        stepx = -1
        offsetx = 2
        for y in range(self.lasty - 1, -1, -1):
            x = startx + offsetx
            while x <= stopx:
                if debug:
                    self.logFunction(self.print_prefix + "startx: "+str(startx)+" stepx: "+str(stepx)+","+str(x)+":"+str(y))
                if self.move_element(x, y, x - 1, y + 1):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
                offsetx = 0
            startx += stepx
            stopx -= stepx
        return retVal

    def moveSE(self):
        retVal = False
        startx = self.firstx - 1
        stopx = self.lastx + 1
        xoffset = 2
        stepx = -1
        for y in range(self.lasty - 1, -1, -1):
            x = startx
            while x <= stopx - xoffset:
                if debug:
                    self.logFunction(self.print_prefix + "startx: "+str(startx)+" stepx: "+str(stepx)+","+str(x)+":"+str(y))
                if self.move_element(x, y, x + 1, y + 1):
                    retVal = True
                x += 2
            if startx == 0:
                stepx = - stepx
                xoffset = 0
            startx += stepx
            stopx -= stepx
        return retVal

    def clearCombinedFields(self):
        for pole in self.pola:
            pole[3] = False


    def moveWFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveW():
            moved = True
            continue
        if moved:
            self.logFunction(self.print_prefix + " lewo (a)", Colors.GREEN )
            self.new_number()
        return moved

    def moveEFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveE():
            moved = True
            continue
        if moved:
            self.logFunction( self.print_prefix + " prawo (d)", Colors.CYAN)
            self.new_number()
        return moved

    def moveNEFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveNE():
            moved = True
            continue
        if moved:
            self.logFunction(self.print_prefix + " góra-prawo (e)", Colors.RED)
            self.new_number()
        return moved

    def moveNWFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveNW():
            moved = True
            continue
        if moved:
            self.logFunction(self.print_prefix + " góra-lewo (q)", Colors.BLUE)
            self.new_number()
        return moved

    def moveSWFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveSW():
            moved = True
            continue
        if moved:
            self.logFunction(self.print_prefix + " dół-lewo (z)", Colors.MAGENTA)
            self.new_number()
        return moved

    def moveSEFull(self):
        self.clearCombinedFields()
        moved = False
        while self.moveSE():
            moved = True
            continue
        if moved:
            self.logFunction(self.print_prefix + " dół-prawo (c)", Colors.YELLOW )
            self.new_number()
        return moved