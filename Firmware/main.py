import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners.keypad import PinsScanner

keyboard = KMKKeyboard()


keyboard.matrix = PinsScanner(
    [board.D10, board.D9, board.D8],
    value_when_pressed=False
)

# czech keyboard mapping
keyboard.keymap = [
    [
        KC.LALT(KC.X),
        # alt + x         
        KC.LSHIFT(KC.GRAVE), 
        ## ;  
        KC.LWIN(KC.LSHIFT(KC.S)), 
        ## win + shift + s
    ]
]

if __name__ == "__main__":
    keyboard.go()