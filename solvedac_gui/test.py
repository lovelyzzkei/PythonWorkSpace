import re

p = re.compile('^[a-zA-Z0-9]+')
uid = "march381@naver.com"
print(p.match(uid).group())

