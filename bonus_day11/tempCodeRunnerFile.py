# def get_average() :
#     with open("data.txt","r")as file:
#      data =file.readlines()
#     #  modify single item in list 
#     values=data[1:]
#     # convert all list iteam to float
#     values=[float(i) for i in values]
#     # get an average values
#     averages=sum(values)/len(values)
#     return averages
# average=get_average()   
# print(average)
def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum=min(grades)
    value=f"Max: {maximum}, Min: {minimum}"
    return value
    
print(get_max())
