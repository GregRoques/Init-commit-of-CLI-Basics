# A For loop expects a starting point and an ending point.
# The ending point is non-inclusive, meaning it will stop when/BEFORE it gets there.

for i in range(1,10):
    print i

# Lists
# lists = arrays in any other language; technically, a group of variables that are indexed beginning with 0 (ALWAYS)
student1 = "Brian"
student2 = "Brandon"
student3 = "Zac"
student4 = "J.R."
#or...
students = ["Brian", "Brandon", "Zac", "J.R."]
print students[0]

numOfStudents = len(students)
print numOfStudents

#A tuple is a list who's elements CANNOT be changed: () vs []

atlantaTeams = []
atlantaTeams.append("Falcons")
atlantaTeams.append("Braves")
atlantaTeams.append("Hawks")
atlantaTeams.append("Thrashers")

atlantaTeams.pop(3)
print atlantaTeams
atlantaTeams.append("United")

#Sort

print sorted(atlantaTeams)
print atlantaTeams
atlantaTeams.reverse()
print atlantaTeams

#if you want to sort but not change the original list, used sorted(listname)

#split (same as JS)
reindeer = "Dasher, Dancer, Prancer, Vixon"
reindeerList = reindeer.split(', ')
print reindeerList

#slice

#if you want part of a list, use [x:y]. This will create a copy of the array. It will not change the original. It will start copying at the xth index and it will stop at the yth.

dancerPrancer = reindeerList[1:3]
print dancerPrancer

