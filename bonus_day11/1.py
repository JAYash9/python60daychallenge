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
def format_filename():
    filename="report.txt"
    filenames=filename[:6].capitalize()
    return filenames
print(format_filename())

    