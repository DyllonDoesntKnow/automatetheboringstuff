# page 61-77
def spam():
    global eggs
    eggs = 'spam' # this is the global

def bacon():
    eggs = 'bacon' # this is locals

def ham():
    print(eggs) # this is global

eggs = 42 # this is the global
spam()
print(eggs)

#prints spam
