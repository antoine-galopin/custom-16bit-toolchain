; Multiply 4 by 5 using repeated addition
; Result will be stored in R3

start:
LOAD R1 4      ; multiplicand
LOAD R2 5      ; multiplier
LOAD R3 0      ; result
LOAD R4 1      ; constant 1

loop:
ADD R3 R3 R1   ; result = result + multiplicand
SUB R2 R2 R4   ; multiplier = multiplier - 1
JUMPIF end     ; if multiplier == 0, stop
JUMP loop      ; otherwise continue

end:
HALT