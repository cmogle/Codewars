# Create hashtag generator.
# Result must start with hashtag (#).
# All words must have first letter capitalized.
# If the final result is longer than 140 chars it must return false.
# If the input or the result is an empty string it must return false.

def generate_hashtag(s):
    if len(s) == 0:
        return False
    else:
        s = s.title()
        s = s.replace(" ", "")
        s = "#" + s
        if len(s) > 140:
            return False
        else:
            return s

#best practice code
# def generate_hashtag(s):
#     output = "#"
#
#     for word in s.split():
#         output += word.capitalize()
#
#     return False if (len(s) == 0 or len(output) > 140) else output
