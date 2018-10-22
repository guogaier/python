import random
secret = random.randint(1,99)
guess = 0
tries = 0
print ("AH! i'm guogeier, and i have a secret! ")
print ("It is a number from 1 to 99. i'll give you 6 tries. ")
while guess != secret and tries < 6:
    guess = int(input ("what's your guess? "))
    if guess < secret:
        print ("Too low, ye scurvy dog! ")
    elif guess > secret:
        print ("Too high, landlubber! ")

    tries = tries + 1

if guess == secret:
    print ("Wow! you got it! found my secret, you did!")
else:
    print ("No more guesses! better luck next time, matey!")
    print ("The secret number was",secret)
