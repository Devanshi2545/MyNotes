#short circuiting - an be done when using 'or' and 'and' as well
is_friend=True
is_user=True

if is_friend or is_user:
    print('best friend forever')


#By short-circuiting, we mean the stoppage of execution of boolean operation if the truth value of expression has been determined already. The evaluation of expression takes place from left to right. In python, short-circuiting is supported by various boolean operators and functions.

#or: When the Python interpreter scans or expression, it takes the first statement and checks to see if it is true. If the first statement is true, then Python returns that object’s value without checking the second statement. The program does not bother with the second statement. If the first value is false, only then Python check the second value, and then the result is based on the second half. 

#and: For an and expression, Python uses a short circuit technique to check if the first statement is false then the whole statement must be false, so it returns that value. Only if the first value is true, does it check the second statement and return the value. 

#An expression containing and or stops execution when the truth value of expression has been achieved. Evaluation takes place from left to right.
