import re

string = "Well, I will have to change the scoring on my"
print(string.replace(re.compile('[^a-zA-Z]'), " "))