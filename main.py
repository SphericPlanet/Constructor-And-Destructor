class Employee:        
    #constructer
    def __init__ (self):
        print("Employee Created !!")
    
    #destructor
    def __del__(self):
        print("Employee Deleted !!")

    #main
    #object
employee1 = Employee()
del employee1