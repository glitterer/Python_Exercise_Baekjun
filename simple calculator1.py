import time

time.sleep(1)
print ("This is calculator experiment 1")
print ("Experiment take 1")
print ("-------------------------------------------------------------")

time.sleep(2)
print("Choose from the following: ")
print ("1.Plus")
print ("2.Minus")
print ("3.Multiply")
print ("4.Divide")
character_choose = int(input())


def calc(a,b):
    
    if (character_choose == 1):
        
        return (a + b)

    if (character_choose == 2):
        return (a - b)

    if (character_choose == 3):
        return (a * b)

    if (character_choose == 4):
        return (a / b)
    
    
def main():
    a = int(input('Type in the first number: '))
    b = int(input('Type in the second number: '))
    
    print("The answer is...")
    print(calc(a,b))


if __name__ == '__main__':
    main()
