# This is a sample application

def test_lowercase(data):
    if data.islower():
        print("Lower Case: Check", data, "Has Passed the test case")
    else:
        print("Lower Case: Check", data, "Has failed the test case")

def test_uppercase(data):
    if data.isupper():
        print("Upper Case: Check", data, "Has Passed the test case")
    else:
        print("Upper Case: Check", data, "Has Failed the test case")


with open("test_data.txt" , "r") as file:
    datas = file.readlines()
    for i in datas:
        test_lowercase(i)
        test_uppercase(i)
