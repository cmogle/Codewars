# given a string, replace each letter with its position in the alphabet
# If anything in the string is not a letter, ignore it and don't return it.
# return as a string
# "a" = 1, "b" = 2, etc.
def alphabet_position(text):
  return " ".join(str(ord(c)-ord("a")+1) for c in text.lower() if c.isalpha())