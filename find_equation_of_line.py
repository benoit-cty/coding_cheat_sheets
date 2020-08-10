import sys
import math

# Auto-generated code below aims at helping you parse
# the standard input according to the problem statement.

x_1, y_1 = [int(i) for i in input().split()]
x_2, y_2 = [int(i) for i in input().split()]

# Write an answer using print
# To debug: print("Debug messages...", file=sys.stderr, flush=True)


slope = (y_2-y_1)/(x_2-x_1)
intercept = y_2-x_2*slope
if intercept>=0:
    intercept = f'+{int(intercept)}'
else:
    intercept = f'{int(intercept)}'
print(f'{int(slope)}*x{intercept}')
