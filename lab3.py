# Create a list of student scores
scores = [88, 92, 79, 93, 85]
print("Scores:", scores)

# Find average score
average = sum(scores) / len(scores)
print("Average Score:", average)

scores.append(10)
print(scores)
scores.remove(92)
print(scores)
 
 #task2  Create a tuple of subject names
subjects =("English,urdu,math,science")
print(subjects)
#tuple are immutable thats why we can,t add anything in it

#section2
import pandas as pd

data = {
    "Student": ["Ali", "Sara", "John", "Ayesha"],
    "Math": [88, 92, 79, 93],
    "Science": [90, 85, 88, 95]
}

df = pd.DataFrame(data)
print(df)

table=[
    ["Name", "Age", "city"],
    ["Ali", 22,"Lahore"],
     ["Ahmad", 24,"Isl"],
     ["Abdul Hadi",23,"Karachi"],
     ["Hania",25,"UK"],
     ["Rubab", 31,"Asia"]
]
#print(table)
headers=table[0]
print(f"{headers[0]:<10} {headers[1]:<5} {headers[2]:<15}")
print("-"*30)
for row in table[1:]:
    print(f"{row[0]:<10} {row[1]:<5} {row[2]:<15}")
    print("second row:" , table[2])
print("Age column:")
for row in table[1:]:
    print(row[1])

    numbers=[1,2,3,4,5,6,7]
    numbers_tuple= tuple(numbers)
    print(numbers_tuple)

    points=[(1,2),(3,4),(5,6)]
    for point in points:
        print(point)

        lang=["python","java","c++"]
        lang.append("javascript")
        lang.insert(0 ,"#c")
        lang.remove("java")
        print(lang)
        numb=(10,250,30)
        x,y,z=numb
        print("x=",x)
        print("y=",y)
        print("z=",z)
        
