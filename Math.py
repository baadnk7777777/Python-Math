import random
import time
from playsound import playsound
import winsound

Correct = 0
Problem = 0
time = 60

print("====== Select Menu ======")
print("1: Addition")
print("2: Subtraction")
print("3: Multiplication")
print("4: Division")
print("5: Exponentiation")
print("====== =========== ======")
menu = input()
print("=========================")

if menu == '1':
    print("====== Select Addition Level ======")
    print("1: Easy Even")
    print("2: Easy Odd")
    print("3: Medium Even")
    print("4: Medium Odd")
    print("5: Hard Even")
    print("6: Hard Odd")
    print("====== =========== ======")
    level = input()
    print("=========================")

    if level == '1':
        print("Easy Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 8, 2)
            y = random.randrange(1, 8, 2)
            Problem += 1
            print(x, "+", y)
            z = (input())
            print("-------------------------")
            if z == str(x+y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x+y)
                print("=========================")
    elif level == '2':
        print("Easy Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 8+1, 2)
            y = random.randrange(1, 8+1, 2)
            Problem += 1
            print(x, "+", y)
            z = (input())
            print("-------------------------")
            if z == str(x+y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x+y)
                print("=========================")
    elif level == '3':
        print("Medium Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 98, 2)
            y = random.randrange(1, 98, 2)
            Problem += 1
            print(x, "+", y)
            z = (input())
            print("-------------------------")
            if z == str(x+y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x+y)
                print("=========================")
    elif level == '4':
        print("Medium Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 98+1, 2)
            y = random.randrange(1, 98+1, 2)
            Problem += 1
            print(x, "+", y)
            z = (input())
            print("-------------------------")
            if z == str(x+y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x+y)
                print("=========================")
    elif level == '5':
        print("Hard Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 998, 2)
            y = random.randrange(1, 998, 2)
            Problem += 1
            print(x, "+", y)
            z = (input())
            print("-------------------------")
            if z == str(x+y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x+y)
                print("=========================")
    elif level == '6':
        print("Hard Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 998+1, 2)
            y = random.randrange(1, 998+1, 2)
            Problem += 1
            print(x, "+", y)
            z = (input())
            print("-------------------------")
            if z == str(x+y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x+y)
                print("=========================")

    else:
        print("Error!!!")

elif menu == '2':
    print("====== Select Subtraction Level ======")
    print("1: Easy Even")
    print("2: Easy Odd")
    print("3: Medium Even")
    print("4: Medium Odd")
    print("5: Hard Even")
    print("6: Hard Odd")
    print("====== =========== ======")
    level = input()
    print("=========================")

    if level == '1':
        print("Easy Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 8, 2)
            y = random.randrange(1, 8, 2)
            if x > y:
                Problem += 1
                print(x, "-", y)
                z = (input())
                print("-------------------------")

                if z == str(x-y):
                    Correct += 1
                    e = int(time.time() - start_time)
                    print("Correct !!!")
                    print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                    print("=========================")
                elif z == 'q':
                    totaltime = int(time.time() - start_totaltime)
                    print("Total Problem: ", Problem)
                    print("Your Score:", Correct, "!!!")
                    print('Total Time: {:02d}:{:02d}'.format(
                        (totaltime % 3600 // 60), totaltime % 60))
                    playsound('Source/wow.mp3')
                    break
                else:
                    print("Answer: ", x-y)
                    print("=========================")
    elif level == '2':
        print("Easy Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 8+1, 2)
            y = random.randrange(1, 8+1, 2)
            if x > y:
                Problem += 1
                print(x, "-", y)
                z = (input())
                print("-------------------------")
                if z == str(x-y):
                    Correct += 1
                    e = int(time.time() - start_time)
                    print("Correct !!!")
                    print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                    print("=========================")
                elif z == 'q':
                    totaltime = int(time.time() - start_totaltime)
                    print("Total Problem: ", Problem)
                    print("Your Score:", Correct, "!!!")
                    print('Total Time: {:02d}:{:02d}'.format(
                        (totaltime % 3600 // 60), totaltime % 60))
                    playsound('Source/wow.mp3')
                    break
                else:
                    print("Answer: ", x-y)
                    print("=========================")
    elif level == '3':
        print("Medium Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 98, 2)
            y = random.randrange(1, 98, 2)
            if x > y:
                Problem += 1
                print(x, "-", y)
                z = (input())
                print("-------------------------")
                if z == str(x-y):
                    Correct += 1
                    e = int(time.time() - start_time)
                    print("Correct !!!")
                    print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                    print("=========================")
                elif z == 'q':
                    totaltime = int(time.time() - start_totaltime)
                    print("Total Problem: ", Problem)
                    print("Your Score:", Correct, "!!!")
                    print('Total Time: {:02d}:{:02d}'.format(
                        (totaltime % 3600 // 60), totaltime % 60))
                    playsound('Source/wow.mp3')
                    break
                else:
                    print("Answer: ", x-y)
                    print("=========================")
    elif level == '4':
        print("Medium Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 98+1, 2)
            y = random.randrange(1, 98+1, 2)
            if x > y:
                Problem += 1
                print(x, "-", y)
                z = (input())
                print("-------------------------")
                if z == str(x-y):
                    Correct += 1
                    e = int(time.time() - start_time)
                    print("Correct !!!")
                    print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                    print("=========================")
                elif z == 'q':
                    totaltime = int(time.time() - start_totaltime)
                    print("Total Problem: ", Problem)
                    print("Your Score:", Correct, "!!!")
                    print('Total Time: {:02d}:{:02d}'.format(
                        (totaltime % 3600 // 60), totaltime % 60))
                    playsound('Source/wow.mp3')
                    break
                else:
                    print("Answer: ", x-y)
                    print("=========================")
    elif level == '5':
        print("Hard Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 998, 2)
            y = random.randrange(1, 998, 2)
            if x > y:
                Problem += 1
                print(x, "-", y)
                z = (input())
                print("-------------------------")
                if z == str(x-y):
                    Correct += 1
                    e = int(time.time() - start_time)
                    print("Correct !!!")
                    print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                    print("=========================")
                elif z == 'q':
                    totaltime = int(time.time() - start_totaltime)
                    print("Total Problem: ", Problem)
                    print("Your Score:", Correct, "!!!")
                    print('Total Time: {:02d}:{:02d}'.format(
                        (totaltime % 3600 // 60), totaltime % 60))
                    playsound('Source/wow.mp3')
                    break
                else:
                    print("Answer: ", x-y)
                    print("=========================")
    elif level == '6':
        print("Hard Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 998+1, 2)
            y = random.randrange(1, 998+1, 2)
            if x > y:
                Problem += 1
                print(x, "-", y)
                z = (input())
                print("-------------------------")
                if z == str(x-y):
                    Correct += 1
                    e = int(time.time() - start_time)
                    print("Correct !!!")
                    print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                    print("=========================")
                elif z == 'q':
                    totaltime = int(time.time() - start_totaltime)
                    print("Total Problem: ", Problem)
                    print("Your Score:", Correct, "!!!")
                    print('Total Time: {:02d}:{:02d}'.format(
                        (totaltime % 3600 // 60), totaltime % 60))
                    playsound('Source/wow.mp3')
                    break
                else:
                    print("Answer: ", x-y)
                    print("=========================")

    else:
        print("Error!!!")

elif menu == '3':
    print("====== Select Multiplication Level ======")
    print("1: Easy Even")
    print("2: Easy Odd")
    print("3: Medium Even")
    print("4: Medium Odd")
    print("5: Hard Even")
    print("6: Hard Odd")
    print("====== =========== ======")
    level = input()
    print("=========================")

    if level == '1':
        print("Easy Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 8, 2)
            y = random.randrange(1, 8, 2)
            Problem += 1
            print(x, "*", y)
            z = (input())
            print("-------------------------")
            if z == str(x*y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x*y)
                print("=========================")
    elif level == '2':
        print("Easy Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 8+1, 2)
            y = random.randrange(1, 8+1, 2)
            Problem += 1
            print(x, "*", y)
            z = (input())
            print("-------------------------")
            if z == str(x*y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x*y)
                print("=========================")
    elif level == '3':
        print("Medium Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 98, 2)
            y = random.randrange(1, 98, 2)
            Problem += 1
            print(x, "*", y)
            z = (input())
            print("-------------------------")
            if z == str(x*y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x*y)
                print("=========================")
    elif level == '4':
        print("Medium Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 98+1, 2)
            y = random.randrange(1, 98+1, 2)
            Problem += 1
            print(x, "*", y)
            z = (input())
            print("-------------------------")
            if z == str(x*y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x*y)
                print("=========================")
    elif level == '5':
        print("Hard Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 998, 2)
            y = random.randrange(1, 998, 2)
            Problem += 1
            print(x, "*", y)
            z = (input())
            print("-------------------------")
            if z == str(x*y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x*y)
                print("=========================")
    elif level == '6':
        print("Hard Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 998+1, 2)
            y = random.randrange(1, 998+1, 2)
            Problem += 1
            print(x, "*", y)
            z = (input())
            print("-------------------------")
            if z == str(x*y):
                Correct += 1
                e = int(time.time() - start_time)
                print("Correct !!!")
                print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                print("=========================")
            elif z == 'q':
                totaltime = int(time.time() - start_totaltime)
                print("Total Problem: ", Problem)
                print("Your Score:", Correct, "!!!")
                print('Total Time: {:02d}:{:02d}'.format(
                    (totaltime % 3600 // 60), totaltime % 60))
                playsound('Source/wow.mp3')
                break
            else:
                print("Answer: ", x*y)
                print("=========================")

    else:
        print("Error!!!")

elif menu == '4':
    print("====== Select Division Level ======")
    print("1: Easy Even")
    print("2: Easy Odd")
    print("3: Medium Even")
    print("4: Medium Odd")
    print("5: Hard Even")
    print("6: Hard Odd")
    print("====== =========== ======")
    level = input()
    print("=========================")

    if level == '1':
        print("Easy Even")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 98, 2)
            y = random.randrange(1, 98, 2)
            if x > y and x % y == 0:
                Problem += 1
                print(x, "/", y)
                z = str(input())
                sum = str(round(x/y))
                print("-------------------------")
                if z == sum:
                    Correct += 1
                    e = int(time.time() - start_time)
                    print("Correct !!!")
                    print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                    print("=========================")
                elif z == 'q':
                    totaltime = int(time.time() - start_totaltime)
                    print("Total Problem: ", Problem)
                    print("Your Score:", Correct, "!!!")
                    print('Total Time: {:02d}:{:02d}'.format(
                        (totaltime % 3600 // 60), totaltime % 60))
                    playsound('Source/wow.mp3')
                    break
                else:
                    print("Answer: ", sum)
                    print("=========================")

    else:
        print("Error!!!")

    if level == '2':
        print("Easy Odd")
        print("=========================")
        start_totaltime = time.time()
        while True:
            start_time = time.time()
            x = random.randrange(1, 98, 2)
            y = random.randrange(1, 98, 2)
            if x > y and x % y == 0:
                Problem += 1
                print(x, "/", y)
                z = str(input())
                sum = str(round(x/y))
                print("-------------------------")
                if z == sum:
                    Correct += 1
                    e = int(time.time() - start_time)
                    print("Correct !!!")
                    print('{:02d}:{:02d}'.format((e % 3600 // 60), e % 60))
                    print("=========================")
                elif z == 'q':
                    totaltime = int(time.time() - start_totaltime)
                    print("Total Problem: ", Problem)
                    print("Your Score:", Correct, "!!!")
                    print('Total Time: {:02d}:{:02d}'.format(
                        (totaltime % 3600 // 60), totaltime % 60))
                    playsound('Source/wow.mp3')
                    break
                else:
                    print("Answer: ", sum)
                    print("=========================")

    else:
        print("Error!!!")
else:
    print("ERROR!!!")
time.sleep(5)
