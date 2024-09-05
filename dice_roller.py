#!/home/dylan/python/d20_dice/dice_roller.py

import random

colors = [
    "\033[1;31m",
    "\033[1;32m",
    "\033[1;33m",
    "\033[1;34m",
    "\033[1;35m",
    "\033[1;36m",
    "\033[1;37m",
]

reset_color = "\033[0m"

def roll20():
    Rn1 = random.randint(1, 20)
    Rn2 = random.randint(1, 20)
    total = Rn1 + Rn2

    color1 = random.choice(colors)
    color2 = random.choice(colors)

    display_die(Rn1, color1)
    display_die(Rn2, color2)

    print(f"{reset_color}\nTotal of both dice: {total}")

def display_die(Rn, color):
    Rn_str = f"{Rn:>2}"
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
