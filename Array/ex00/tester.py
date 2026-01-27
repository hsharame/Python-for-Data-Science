from give_bmi import give_bmi, apply_limit

height = [2.71, 1.15]
weight = [165.3, 38.4]
bmi = give_bmi(height, weight)
print(bmi, type(bmi))
print(apply_limit(bmi, 26))

print("*" * 50)
try: 
    height = [2.71, height]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except Exception as error:
    print(error)

print("*" * 50)
try:
    height = [2.71, 1.15]
    weight = [165.3, 38.4, 158]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except Exception as error:
    print(error)

print("*" * 50)
try:
    height = [2.71, 1.15]
    weight = [165.3, -38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(bmi, 26))
except Exception as error:
    print(error)

print("*" * 50)
try:
    height = [2.71, 1.15]
    weight = [165.3, 38.4]
    bmi = give_bmi(height, weight)
    print(bmi, type(bmi))
    print(apply_limit(26, bmi))
except Exception as error:
    print(error)