#Dictionaries
# Dictionaries are just like lists, except instead of numbered indiceses it has English indiceses
#Key value pair

# Greg = {
#     "Gender":"Male",
#     "Height":"Tall",
#     "Job":"Developer",
# }

zombie={}
# zombies=[]



zombie["weapon"] = "fist"
zombie["speed"] = 10
zombie["health"] = 100


# for key,value in zombie.items():
#     print "zombie has a key of %s with a value of %s" % (key, value)

#remove weapon key
# del zombie["weapon"]
# print zombie

# if(isNightTime):
#     zombie["health"] +=50

    # put lists and dictionaries together
zombies = []
zombies.append({
    "name": "Hank",
    "weapon": "Baseball Bat",
    "speed": 10,
})
zombies.append({
    "name": "Willie",
    "weapon": "axe",
    "speed": 5,
    "victims":[
        "squirell",
        "racoon",
        "dragon"
    ]
})
print zombies[0]["weapon"]
print zombies[1]["victims"]