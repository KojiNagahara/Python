#x = -25
x = 25
epsilon = 0.01
numGuesses = 0
if x > 0 :
    low = 0.0
    high = max(1.0, x)
else :
    low = min(-1.0, x)
    high = 0.0

ans = (high + low)/2.0
while abs(ans**3 - x) >= epsilon :
    print('low =', low, 'high =', high, 'ans =', ans)
    numGuesses += 1
    if ans**3 < x :
        low = ans
    else : 
        high = ans
    ans = (high + low)/2.0
print('numGuesses =', numGuesses)
print(ans, 'is close to cube root of', x)