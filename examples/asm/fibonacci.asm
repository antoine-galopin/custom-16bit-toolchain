LOAD R0 0      ; zero register
LOAD R1 0      ; a = 0 (F(0))
LOAD R2 1      ; b = 1 (F(1))
LOAD R3 5      ; n = 5
LOAD R4 1      ; constant 1

loop:
SUB R6 R3 R0   ; check if n == 0
JUMPIF end     ; if n == 0, exit loop

ADD R5 R1 R2   ; temp = a + b
ADD R1 R2 R0   ; a = b
ADD R2 R5 R0   ; b = temp
SUB R3 R3 R4   ; n -= 1
JUMP loop

end:
HALT