names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

#make a dictionary using list comprehensions
students = {key:value for key,value in zip(names,heights)}
#print(students)

drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

zipped_drinks= zip(drinks,caffeine)

#printing values from a zip object
# for value in zipped_drinks:
#     print(value)

#anothery way of printing the zipped data
#print("zipped drinks: ", list(zipped_drinks))
    
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

plays = {songs:playcounts for songs, playcounts in zip(songs,playcounts)}

# print(plays)

plays.update({"Respect":{"album 1": "123 time played","album 2":"1231 time played", "album 3":"12311 time played"}})

#print(plays)

#print the value associated with the key in dictionary
# print(plays["Respect"])

#try to access key which does not exist, should not throw error

# zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

# zodiac_elements.update({"energy":"Not a Zodiac element"})

# key_to_check = "Landmark 81"

# if key_to_check in zodiac_elements:
#   print(zodiac_elements["Landmark 81"])

zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}

key_to_check = "energy"

#check if a key is present or not, will not throw error if not present
# if key_to_check in zodiac_elements:
#     print(zodiac_elements["energy"])

#Handle the non-exist key in the dictionary using the except block
# try:
#     print(zodiac_elements["energy"])
# except KeyError as K:
#     print("Key " +str(K)+ " does not exist in the dictionary")

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}

#get the value of key without any error, NONE will be received in case of no value found
tc_id = user_ids.get("teraCoder",100000)
#print(tc_id)

available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20

# You are designing the video game Big Rock Adventure. We have provided a dictionary of items that are in the player’s inventory which add points to their health meter. In one line, add the corresponding value of the key "stamina grains" to the health_points variable and remove the item "stamina grains" from the dictionary. If the key does not exist, add 0 to health_points.

health_points += available_items.get("stamina grains",0)
available_items.pop("stamina grains",0)

# print(health_points)

# In one line, add the value of "power stew" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.get("power stew",0)
available_items.pop("power stew",0)

# In one line, add the value of "mystic bread" to health_points and remove the item from the dictionary. If the key does not exist, add 0 to health_points.
health_points += available_items.get('mystic bread',0)
available_items.pop("mystic bread",0)

# Print available_items and health_points.
# print(available_items)
# print(health_points)

user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

# Create a variable called users and assign it to be all of the keys of the user_ids list.
users = sorted(user_ids.keys())

# Create a variable called lessons and assign it to be all of the keys of the num_exercises list.
lessons = num_exercises.keys()

#print(users)
# output: dict_keys(['teraCoder', 'pythonGuy', 'samTheJavaMaam', 'lyleLoop', 'keysmithKeith'])
#print(lessons)
# output: dict_keys(['functions', 'syntax', 'control flow', 'loops', 'lists', 'classes', 'dictionaries'])

#get all the keys of a dictionary but not as a list
# for test_user in user_ids.keys():
#     print(test_user)

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0

# get the valuues of the dictionaries and add its sum to the total_exercises
# for val in num_exercises.values():
#     total_exercises += val
    
# print(total_exercises)

pct_women_in_occupation = {"CEO": 28, "Engineering Managers": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}

#get and print both the keys and values using .items() method
# Women make up [value] percent of [key]s.
# for occupation, value in pct_women_in_occupation.items():
#     print("Women make up "+str(value)+" percent of "+occupation)

    
# create an empty dictionary 
# spread = {}

tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)

spread["present"] = tarot.pop(22)

spread["future"] = tarot.pop(10)

# for position, value in spread.items():
#   print("Your "+position+" is the "+value+" card.")

#prints only all keys in dictionary
# for element in tarot:
#     print(element)

combo_meals = {1: ["hamburger", "fries"], 2: ["hamburger", "fries", "soda"], 4: ["veggie burger", "salad", "soda"], 6: ["hot dog", "apple slices", "orange juice"]}
# print(combo_meals[3])

# this will check for the existence of key in dictionary
# print(2 in combo_meals)

inventory = {"iron spear": 12, "invisible knife": 30, "needle of ambition": 10, "stone glove": 20, "the peacemaker": 65, "demonslayer": 50}

# print(12 in inventory)

