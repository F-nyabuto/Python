weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in m: "))
bmi = float(weight / (height ** 2))


def bmicalc():
    bmi = float(weight / (height ** 2))
    print(f"Your BMI is {bmi}")


def evaluat():
    if (bmi > 18.5) and (bmi < 24.9):
        print("you are healthy")
    elif bmi > 25:
        print("You are fat")
    else:
        print("You are underweight")

def concatenative(bmicalc, evaluator):
    bmicalc(weight, height)
    evaluator(bmi)

concatenative()
