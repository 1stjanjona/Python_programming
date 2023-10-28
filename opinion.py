#!/usr/bin/env python3
answer = input("Are you brave enough to watch Horror movies?\nPlease type Yes, No, or Maybe: \n")
if answer.upper() == "YES":
    print(f"You typed {answer}, that's great you are too brave")
elif answer.upper() == "NO":
    print(f"You typed {answer}, you missed a lot of good movies")
elif answer.upper() == "MAYBE":
    print(f"You typed {answer}, OH come on let's watch one now")
else:
    print(f"You typed {answer}, which is not an option\nplease stick on the options")
