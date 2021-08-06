
#Testing how to call key/values in nested dictionaries

food = {
    'chicken': {'serve': '4oz', 'cal': 140, 'fat': 3, 'pro': 24, 'carb': 0,},
    'egg': {'serve': '1 egg', 'cal': 74, 'fat': 1, 'pro': 17, 'carb': 0,},
    'bacon': {'serve': '2 slices', 'cal': 180, 'fat': 8, 'pro': 20, 'carb': 0,},
}
print(food['chicken']['fat'])

cal_stat = []
fat_stat = []
pro_stat = []
carb_stat = []

meal_complete = False

#create a function that adds the nutrient values of an ingrediennt to the blanks lists for each nutrient value type

def food_stats(ingredient):
    if eat == 'chicken':
        cal_stat.append(food['chicken']['cal']*serving)
        fat_stat.append(food['chicken']['fat']*serving)
        pro_stat.append(food['chicken']['pro']*serving)
        carb_stat.append(food['chicken']['carb']*serving)
    elif eat == 'egg':
        cal_stat.append(food['egg']['cal']*serving)
        fat_stat.append(food['egg']['fat']*serving)
        pro_stat.append(food['egg']['pro']*serving)
        carb_stat.append(food['egg']['carb']*serving)

# run a while loop that calls the food_stats function, adding the vlaues from the nested list to later group then add the same nutrient values from diffrent foods
print("Type 'q' at any prompt to quit program.")

while not meal_complete:
    eat = input("Food: ")
    print(f"Serving size: {food[eat]['serve']}")
    serving = int(input("Serving: "))
    another = input("Another ingredient (y/n)? ")
    food_stats(eat)
    if another == 'y':
        continue
    elif another == 'n':
        meal_complete = True
    elif eat == 'q' or serving == 'q' or another == 'q':
        break


print(f"The total calories are {sum(cal_stat)}.")
print(f"The total grams of fat is {sum(fat_stat)}g.")
print(f"The total grams of protein are {sum(pro_stat)}g.")
print(f"The total grams of carbs are {sum(carb_stat)}g.")

#8/5/21 - the above code is debugged

