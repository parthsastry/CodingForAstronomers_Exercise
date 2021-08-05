import numpy as np
import matplotlib.pyplot as plt 

CONST_G = -10 # m/s^2

def displacement(s0, a, t):
    s = s0 + np.multiply(v0,t) + 0.5*np.multiply(a,np.square(t))
    return s

def velocity(v0, a, t):
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
    return

def plot_displacement(s0, a, t):
    s = displacement(s0, a, t)
    plt.scatter(t, s, c='r')
    plt.title('Displacement vs Time plot')
    plt.ylabel("Displacement")
    plt.xlabel("Time")
    plt.show()
    return 

if __name__ == '__main__':
    t = np.linspace(0, 2 , num=21)
    #s = np.linspace(0, 0 , num=200)
    s0 = 0
    v0 = 10
    a = CONST_G
    plot_velocity(v0, a, t)
    plot_displacement(s0, a, t)
    plt.ylabel('Displacement/Velocity')
    plt.title('Displacement/Velocity vs Time plot')
