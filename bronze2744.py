# 1 - X
"""
def translate():
  
  x = input("Write some text!\n>")
  
  new = ""
  
  for one in x:
    if one.islower():
      new += one.upper()
    elif one.isupper():
      new += one.lower()
  
  return new
      
print(translate())"""

# 2 - X
"""res = ""
for i in input("Write some text!\n>"):
  res += i.lower() if i.isupper() else i.upper()
print(res)"""

# 3 - X
"""for i in input("Write some text!\n>"):
  if i.isupper():
    print(i.lower(), end='')
  else:
    print(i.upper(), end='')"""

#  4 - o
print(input().swapcase())