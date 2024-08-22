#!/usr/bin/python

import random

def roll20():
    # Roll the first die
    Rn1 = random.randint(1, 20)
    # Roll the second die
    Rn2 = random.randint(1, 20)
    total = Rn1 + Rn2

    # Display the first die
    display_die(Rn1)

    # Display the second die
    display_die(Rn2)

    # Print the total
    print("\nTotal of both dice: {}".format(total))

def display_die(Rn):
    if Rn > 9:
        print("""\033[1;32m
            ,:::,
       ,,,:;  :  ;:,,,
   ,,,:       :       :,,,
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;   {}    ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''
       ''':;;   ;;:'''
            ':::' 
        """.format(Rn))
    else:
        print("""\033[1;32m
            ,:::,
       ,,,:;  :  ;:,,,
   ,,,:       :       :,,,
,,;...........:...........;,,
; ;          ;';          ; ;
;  ;        ;   ;        ;  ;
;   ;      ;     ;      ;   ;
;    ;    ;       ;    ;    ;
;     ;  ;    {}    ;  ;     ;
;      ;:...........:;      ;
;     , ;           ; ,     ;
;   ,'   ;         ;   ',   ;
'';'      ;       ;      ';''
   ''';    ;     ;    ;'''         
       ''':;;   ;;:'''
            ':::'
        """.format(Rn))

if __name__ == "__main__":
    roll20()
