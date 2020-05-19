# Write a Python program to check whether an alphabet is a vowel or consonant
# Expected Output:
#
# Input a letter of the alphabet: k
# k is a consonant.

char = 'X'
char = char.lower()
print(char)
if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'):
  print(char," is a vovel")
else:
  print(char," is a consonant")