import random

d_a = input("| 1/5 | Set an element: ")
d_b = input("| 2/5 | Set an element: ")
d_c = input("| 3/5 | Set an element: ")
d_d = input("| 4/5 | Set an element: ")
d_e = input("| 5/5 | Set an element: ")

dlist = [d_a, d_b, d_c, d_d, d_e]

print("\nYour list of elements: ", dlist, "\n")

print("Random element: ", dlist.pop(random.randint(0,4)) )