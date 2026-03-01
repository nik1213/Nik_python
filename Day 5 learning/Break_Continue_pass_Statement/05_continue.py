for i in range(1, 20):
    if i == 10:
        continue #the continue statement says to bypass the print and go and execute for the next value of i
# continue the loop for the next iteration here itself
    print(i)

'''
continue
🎯 Purpose:

Skip the current iteration and move to the next one.

When Python sees continue:

It ignores remaining statements in that iteration.

Goes directly to the next loop cycle.
=================------------===========
ey Points:

Does NOT stop the loop.

Only skips current iteration.

Useful when filtering values.
'''