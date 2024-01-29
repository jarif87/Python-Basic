def check_number(data):
    if len(data)==len(set(data)):
        return True
    else:
        return False
    
data=[1,2,3,4,5]
data_x=[1,2,3,4,5,5,6]
print(check_number(data))
print("+++++++++++++++++++++++++++++++")
print(check_number(data_x))
     