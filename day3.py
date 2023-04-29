#Enclosed scope

def get_total(a, b):
    #enclosed variable declared inside a function
    total = a + b
    def double_it():
        #local variable
        double = total * 2
        print(double)
    double_it()

    #double variable will not be accessible
    print(double)
    return total
