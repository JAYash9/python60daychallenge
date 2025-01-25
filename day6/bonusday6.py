# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
# filenames = ['a.txt', 'b.txt', 'c.txt', 'd.txt', 'e.txt', 'f.txt']
# for country, filename in zip(countries, filenames):
#     with open(filename, "w") as file:
#         file.write(country)
# countries = ["Albania", "Belgium", "Canada", "Denmark", "Ethiopia", "France"]
# for country in countries:
#     with open(country+".txt","w")as file:
#         file.write(country)
# member=input("add a new member")+"\n"
# file=open('members.txt','r')
# mems=file.readlines()
# file.close()
# mems.append(member)
# file=open('members.txt','w')
# mems=file.writelines(mems)
# file.close()
filenames = ['doc.txt', 'report.txt', 'presentation.txt']
for filename in filenames:
    with open(filename,"w") as file:
        file.write("Hello")