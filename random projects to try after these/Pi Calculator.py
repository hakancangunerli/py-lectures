import math
import numpy as np
import matplotlib.pyplot as plt
import random

def estimate_pi(n):
    np_circle = 0
    np_total = 0
    for _ in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0, 1)
        dist = math.sqrt(x**2 + y**2)
        if dist <= 1:
            plt.plot(x, y, "o", color="green")
            np_circle += 1
            np_total += 1
        elif dist > 1:
            plt.plot(x, y, "o", color="red")
            np_total += 1

    plt.title((4*np_circle)/(np_total))
    plt.suptitle("Estimated Value of PI")
    plt.xlabel("X")
    plt.ylabel("Y")

    plt.show()

estimate_pi(10000)




