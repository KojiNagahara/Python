# ニュートン-ラフソン法の実装
# x**2 -25 = 0 で誤差がepsilon以下になるxを求める
epsilon = 0.01
k = 25.0
guess = k/2.0
numGuesses = 0
while abs(guess*guess - k) >= epsilon:
    numGuesses += 1
    print('guess =', guess)
    guess = guess - (((guess**2) - k)/(2*guess))
print('numGuesses =', numGuesses)
print('Square root of', k, 'is about', guess)