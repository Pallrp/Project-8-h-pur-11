# These lines you can keep as is
print("Think of a number between 1 and 100 (inclusive)")
print("I am going to guess what it is")
input("Press enter when you are ready to play")

# Here you might want to initialize some variables
cheater = False
quitter = False
cmd = 0
# Then start a while loop

high = 100
low = 0
test_case = 0
while test_case <= 7 or cmd != "q":
    # These lines you can keep as is
    guess = (high+low) // 2
    print("Is the number", guess, "?")
    print("Type one of the following letters and press enter:")
    print("h: if the guess is too (h)igh")
    print("l: if the guess is too (l)ow")
    print("c: if the guess is (c)orrect")
    print("q: to (q)uit the game")
    cmd = input()
    if cmd == "l":
        low = guess
        high = low * 2
        if high > 100:
            high = 100
    elif cmd == "h":
        high = guess
        
    elif cmd == "c":
        print("I AM VICTORIOUS")
        
        break

    test_case += 1
    if test_case > 7:
        print("Tsk, tsk, don't try to cheat me")
        cheater = True
        break
    elif cmd == "q":
        print("Quitter")
        quitter = True
        break


    # Now it's up to you to check the command and take appropriate action


# If you detect that the user h5as not been truthful, you should print the following
