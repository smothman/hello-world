#Sam Othman
#1991756
word=input()
password = ''
for i in range(len(word)):
  if 'i' in word[i]:
    password += '!'
  elif 'a' in word[i]:
    password += '@'
  elif 'm' in word[i]:
    password += 'M'
  elif 'B' in word[i]:
    password += '8'
  elif 'o' in word[i]:
    password += '.'
  else:
    password += word[i]
password += 'q*s'
print(password)