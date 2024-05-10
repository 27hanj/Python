#comments are like this

# python is powerful and is important for jobs
# this because it has a lot of libraries
# libraries are tools made by ppl to do stuff
# there's a library that lets you make graphs for example\

hi = 4
yay = "cs club"
second = yay[hi]
print(second)
asdf = "arjunsikka"
cool = [] # list
uncool = ("a", "b", "c") # tuple (can do "tuple()" for more clarity)
coolio = set() # set
cooly = {"score1":0,"score2":0} # dictionary

for i in range(len(asdf)):
  #print(str(i)+": "+asdf[i])
  if asdf[i] == "a":
    print(i)
  cool.append(asdf[i]+str(i))

cool[9] = "egg"
print(cool)

print(cooly["score1"])


# Lists: ordered, mutable, allows duplicates
# Tuples: ordered, immutable, allows duplicates
# Sets: unordered, mutable, no duplicates, good for detecting if a specified value is in a set
# Dictionaries: unordered, mutable, no duplicate keys

def sum(a,b): # function
  return a+b

print(sum(1,3))

