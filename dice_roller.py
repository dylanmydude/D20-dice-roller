#!/home/dylan/python/d20_dice/dice_roller.py

import random

# Define ANSI color codes
colors = [
    "\033[1;31m",  # Red
    "\033[1;32m",  # Green
    "\033[1;33m",  # Yellow
    "\033[1;34m",  # Blue
    "\033[1;35m",  # Magenta
    "\033[1;36m",  # Cyan
    "\033[1;37m",  # White
]

# Reset color
reset_color = "\033[0m"

def roll20():
    # Roll the first die
    Rn1 = random.randint(1, 20)
    # Roll the second die
    Rn2 = random.randint(1, 20)
    total = Rn1 + Rn2

    # Random colours
    color1 = random.choice(colors)
    color2 = random.choice(colors)

    # Display the first die
    display_die(Rn1, color1)

    # Display the second die
    display_die(Rn2, color2)

    # Total
    print(f"{reset_color}\nTotal of both dice: {total}")

def display_die(Rn, color):
    # Format the number to always occupy two spaces
    Rn_str = f"{Rn:>2}"  # Right-align with two character spaces
    print(f"""{color}
            ,:::,
       ,,,:;  :  ;:,,,
   ,,,:       :       :,,,
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;  {Rn_str}   ;    ;    ;
;     ;  ;         ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''
       ''':;;   ;;:'''
            ':::'
        {reset_color}""")

if __name__ == "__main__":
    roll20()
