import turtle

# MINIMUM_BRANCH_LENGTH = 5

"""

def buildTree(t, branchLength, shortenBy, angle):
    if branchLength > MINIMUM_BRANCH_LENGTH:
        t.forward(branchLength)
        newLength = branchLength - shortenBy

        t.left(angle)
        buildTree(t, newLength, shortenBy, angle)

        t.right(angle * 2)
        buildTree(t, newLength, shortenBy, angle)

        t.left(angle)
        t.backward(branchLength)


"""
def kochFlake(t, iteration, length, shortenFactor, angle):
    if (iteration == 0):
        t.forward(length)
    else:
        iteration = iteration - 1
        length = length / shortenFactor

        kochFlake(t, iteration, length, shortenFactor, angle)
        t.left(angle)
        kochFlake(t, iteration, length, shortenFactor, angle)
        t.right(angle * 2)
        kochFlake(t, iteration, length, shortenFactor, angle)
        t.left(angle)
        kochFlake(t, iteration, length, shortenFactor, angle)
    

t = turtle.Turtle()
t.hideturtle()
t.color('blue')
for i in  range(3):
    kochFlake(t, 1, 600, 3, 60)
    t.right(120)

#buildTree(t, 50, 5, 30)
turtle.mainloop()


