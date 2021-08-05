import numpy as np
import matplotlib.pyplot as plt 


def displacement(s0, a, t):
    s = s0 + np.multiply(v0,t) + 1/2*np.multiply(a,pow(t,2))
    return s

def velocity(v0, a, t):
    # editing this function so that it works with a array/list as input (for t) as well
    v = v0 + np.multiply(t, a)
    return v

def plot_velocity(v0, a, t):
    # assumes t is a list/array of time values, plots velocity as a function of time.
    v = velocity(v0, a, t)
    plt.figure()
    plt.scatter(t, v)
    plt.title('Velocity vs Time plot')
    plt.xlabel("Time")
    plt.ylabel("Velocity")
    plt.grid()
    plt.show()
    return

def plot_displacement(s0, a, t):
    s = displacement(s0, a, t)
    plt.plot(t, s)
    plt.title('Displacement vs Time plot')
    plt.ylabel("displacement")
    plt.xlabel("time")
    plt.show()
    return 

if __name__ == '__main__':
    t = np.linspace(0, 2 , num=20)
    #s = np.linspace(0, 0 , num=200)
    s0 = 0
    v0 = 0
    a = -10
