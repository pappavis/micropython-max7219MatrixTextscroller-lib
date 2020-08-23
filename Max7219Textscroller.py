import max7219
from machine import Pin, SPI
import time

class MatrixTextscroller:
    def __init__(self, SPIpin=15, screens=4):
        'afhankelijkheid: https://github.com/mcauser/micropython-max7219'
        
        self.spi = SPI(1, baudrate=10000000, polarity=0, phase=0)
        self.display = max7219.Matrix8x8(self.spi, Pin(SPIpin), screens)
        self.display.brightness(0)
        self.display.fill(0)
        self.display.show()
        self.__debug = False

        self.display.text('----',0,0,1)
        self.display.show()
        time.sleep(0.05)
        self.display.fill(0)
        self.display.show()
        time.sleep(0.05)


    def scrollText(self, textToScroll=''):        
        str123 = '12345678'
        #strabc1 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZAaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz '
        if(textToScroll == ''):
            strabc1 = '****Micropython lichtkrant door Easylab4kids.'
            textToScroll = strabc1
        else:
            strabc1 = textToScroll

        
        leeg1 = '*'

        for spa1 in (0, 100):
            leeg1 += '*'

        strabc1 = leeg1 + strabc1  #debug textjes
        #self.display.text(strabc1,0,0,1)
        
        self.display.text(textToScroll[0:4],0,0,1)
        self.display.show()
        time.sleep(2.5)

        for teller1 in range(0, len(textToScroll)):
            if(teller1 >= 1 ):
                teLatenzien = textToScroll[teller1:]
                if(self.debug):
                    print(teller1, 'volgende letter:', teLatenzien)
                self.display.text(teLatenzien,0,0,1)

            self.display.scroll(-1,0)
            self.display.show()
            time.sleep(0.1)
            self.display.fill(0)
            self.display.show()

    @property
    def debug(self):
        return self.__debug

    @debug.setter
    def debug(self, value):
        self.__debug = value

