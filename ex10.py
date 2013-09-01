tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

#
Request_Format = """I want to bring:\n
\t*%s
\t*The number %d
\t*%r
\nThis trip will be a blast!"""

Inventory = ('apples',10,"a large balloon")
print Request_Format % Inventory

print "A \v B \v C" # tests verticle tabbing, cascading characters from top left to bottom right.

# Quick Ref:
# "I am 6'\2" tall." # escape double-quote inside string
# 'I am 6\'2" tall." # escape single-quote inside string

# Escape sequences to add
# \v verticle tab, creates new line with an indention
# \t tabs (8 spaces)
# \n creates new line


