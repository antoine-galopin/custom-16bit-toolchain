; Compute factorial(5) using repeated addition for multiplication.
; Result will be stored in R2.
;
; Algorithm:
;   result = 1
;   n = 5
;   while n != 0:
;       product = 0
;       multiplier = n
;       multiplicand = result
;       while multiplier != 0:
;           product += multiplicand
;           multiplier -= 1
;       result = product
;       n -= 1
;   halt
;
; This tests:
; - nested loops
; - repeated addition-based multiplication
; - zero-flag conditional branching
; - register and label usage

LOAD R1 5      ; n = 5
LOAD R2 1      ; result = 1
LOAD R6 1      ; constant 1
LOAD R0 0      ; zero register

outer:
SUB R7 R1 R0   ; set zero_flag if n == 0
JUMPIF end     ; if n == 0, end

ADD R4 R1 R0   ; multiplier = n (copy R1)
LOAD R5 0      ; product = 0
ADD R3 R2 R0   ; multiplicand = result (copy R2)

inner:
SUB R7 R4 R0   ; set zero_flag if multiplier == 0
JUMPIF after_inner
ADD R5 R5 R3   ; product += multiplicand
SUB R4 R4 R6   ; multiplier -= 1
JUMP inner

after_inner:
ADD R2 R5 R0   ; result = product
SUB R1 R1 R6   ; n -= 1
JUMP outer

end:
HALT
