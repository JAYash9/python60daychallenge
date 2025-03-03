import csv
with open("writer.csv")as file:
    data=list(csv.reader(file))
print(data)
# Webbrowser module
import webbrowser
user_term=input("Enter a search term:")
url=f"https://www.google.com/search?q={user_term}"
webbrowser.open(url)