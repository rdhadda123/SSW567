from datetime import datetime

#Personal brand for assignment
def my_brand(assignment):
    print("=*=*=*= Rishabh Dhadda =*=*=*=")
    print("=*=*=*= Course 2024F-SSW567-WS =*=*=*= ")
    print("=*=*=*=", assignment, "=*=*=*= ")
    print("=*=*=*=", datetime.now() ,"=*=*=*= ")

def classify_triangle(a, b, c):
    res = "" #Result container for answer

    if (a == b and b == c and a == c): #Conditions to check if equilateral
        res += "Equilateral"
    elif (a != b and b != c and a != c): #Conditions to check if scalene
        res += "Scalene"
    elif ((a == b and b != c and a != c) or (a == c and a != b and c != b) or (c == b and c != a and b != a)): #Conditions to check if isosceles
        res += "Isosceles"
    else:
        return "Not a triangle"
    
    if ((a * a + b * b == c * c) or (a * a + c * c == b * b) or (c * c + b * b == a * a)): #Conditions to check if right triangle
        res += " and Right"

    return res #Returns final answer

my_brand("HW 01 - Tools Setup")