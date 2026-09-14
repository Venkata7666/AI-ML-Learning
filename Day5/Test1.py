#Conduct a short coding test on variables, data types, input/output, if-else, loops, and functions. 
#Candidates should solve the problems independently within a time limit
def test_variables():
    var1 = 11
    return var1 
def test_data_types():
    var2 = 2
    return type(var2)
def test_input_output():
    user_input = input("Enter a number: ")
    print("Entered number:", user_input)
def test_if_else():
    n= int(input("Enter a number: "))
    if n%2==0:
        print("Even number")
    else:
        print("Odd number")
def test_loops():
    for i in range(10):
        print("Loop iteration:", i)    
def test_functions():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    def add(a, b):
        return a + b
    result = add(a, b)
    print("Sum:", result)

if __name__ == "__main__":
    print("Variable test:", test_variables())
    print("Data type test:", test_data_types())
    test_input_output()
    test_if_else()
    test_loops()
    test_functions()   

