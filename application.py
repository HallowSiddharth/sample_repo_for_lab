# This is a sample application

with open("results.txt", "w") as report:

    def test_lowernew(data):
        print("Checking if data" , data, "is upper case")
        assert data.isupper()

    def test_lowercase(data):
        if data.islower():
            print("Lower Case: Check", data, "Has Passed the test case")
            report.write(f"LOWER CASE TEST:\t{data}\tPASSED\n")
        else:
            print("Lower Case: Check", data, "Has failed the test case")
            report.write(f"LOWER CASE TEST:\t{data}\tFAILED\n")

    def test_uppercase(data):
        if data.isupper():
            print("Upper Case: Check", data, "Has Passed the test case")
            report.write(f"UPPER CASE TEST:\t{data}\tPASSED\n")
        else:
            print("Upper Case: Check", data, "Has Failed the test case")
            report.write(f"UPPER CASE TEST:\t{data}\tFAILED\n")

    with open("test_data.txt" , "r") as file:
        datas = file.readlines()
        for i in datas:
            #test_lowernew(i)
            test_lowercase(i)
            test_uppercase(i)


