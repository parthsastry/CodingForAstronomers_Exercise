import numpy as np
import matplotlib.pyplot as plt 

CONST_G = -10 # m/s**2

def velocity(v0, a, t):
    # editing this function so that it works with a array/list as input (for t) as well
    v = v0 + np.multiply(t, a)
    return v

def plot_velocity(v0, a, t):
    # assumes t is a list/array of time values, plots velocity as a function of time.
    v = velocity(v0, a, t)
    plt.figure()
    plt.plot(t, v, 'r')
    plt.title('Velocity vs Time plot')
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    plt.grid()
    plt.show()
    return

if __name__ == '__main__':
    t = np.linspace(0, 20)
    a = -2
    v0 = 0
    plot_velocity(v0, a, t)