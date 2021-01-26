import random

def computerGuess(lowval, highval, randnum, count=0):
    if highval >= lowval:
        guess = lowval + (highval - lowval)//2
        # if guess is in the middle, it is found
        if guess == randnum:
            return count

        #if guess > number, it mus be found in the lower half betweent
        # the lower value and the gusss
        elif guess > randnum:
            count = count +1 
            return computerGuess(lowval, guess-1, randnum, count)
        else:
            count = count + 1 
            return computerGuess(guess + 1, highval, randnum, count)
    else: 
        #numbet not found
        return -1
 #end of function

#generate a random number between 1 and 100
randnum = random.randint(1,101)
#print (randnum)
count = 0
guess = -99

while (guess != randnum):
    # Get the user's guess
    guess = (int) (input("Enter your guess between 1 and 100: "))

    if guess < randnum:
            print ("Higher")
    elif guess > randnum:
            print ('Lower')
    else:
            print ("You get it")
            break
    count = count + 1

#end of while loop

print ('You took ' + str(count) + ' steps to guess the number')

print ('Computer took ' + str(computerGuess(0,100, randnum))+ ' steps to guess the number')