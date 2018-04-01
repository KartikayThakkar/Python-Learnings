# Dynamic Arguments

def emp(name,age,*address):
    print("Name : {} and age : {}".format(name,age))
##    print("Address : {}".format(address))
    for a in address:
        print("Address",a)

emp("Ram","16","xyz","abc","address_1","address_2")
