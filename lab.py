import matplotlib.pyplot as plt
import numpy as np

y_fourier = []
limit = 15
pi = np.pi

def fourier(x):
    global y_fourier
    result = 0
    for n in range(1, limit+1):
        #result += 1/pi/n*np.sin(2*pi*n*x)
        result += ((2*(3*pi*n-9*np.sin(pi*n/3)))/3/pi/pi/n/n + \
            + 2*(3*np.sin(pi*n/3)-3*np.sin(2*pi*n/3)+pi*n*np.cos(pi*n/3))/pi/pi/n/n + \
                + 2*(3*np.sin(2*pi*n/3)+pi*n*np.cos(2*pi*n/3))/pi/pi/n/n)*np.sin(pi*n*x/3)
        #result += ((12*np.sin(pi*n/6)*np.sin(pi*n/6))/pi/pi/n/n + \
        #    + 4*np.sin(pi*n/6)*(3*np.sin(pi*n/2)-pi*n*np.cos(pi*n/6))/pi/pi/n/n + \
        #        + -2*(pi*n*np.sin(2*pi*n/3)-3*np.cos(2*pi*n/3)+3*np.cos(pi*n))/pi/pi/n/n)*np.cos(pi*n*x/3)
    return result

x_ax_m3 = np.arange(-3, -2, 0.0001)
x_ax_m2 = np.arange(-2, -1, 0.0001)
x_ax_m1 = np.arange(-1, 0, 0.0001)
x_ax = np.arange(0, 1, 0.0001)
x_ax_2 = np.arange(1, 2, 0.0001)
x_ax_3 = np.arange(2, 3, 0.0001)

def plot_total():
    global x_ax

    plt.plot(x_ax_m1, [fourier(x) for x in x_ax_m1], 'm')
    plt.plot(x_ax_m2, [fourier(x) for x in x_ax_m2], 'm')
    plt.plot(x_ax_m3, [fourier(x) for x in x_ax_m3], 'm')
    plt.plot(x_ax, [fourier(x) for x in x_ax], 'm', label='Ряд Фурье')
    plt.plot(x_ax_2, [fourier(x) for x in x_ax_2], 'm')
    plt.plot(x_ax_3, [fourier(x) for x in x_ax_3], 'm')

    plt.plot(x_ax_m1, [-1-x for x in x_ax_m1], 'b')
    plt.plot(x_ax_m2, [-2-x for x in x_ax_m2], 'b')
    plt.plot(x_ax_m3, [-3-x for x in x_ax_m3], 'b')
    plt.plot(x_ax, [1-x for x in x_ax], 'b', label='f(x) = 1 - {x}')
    plt.plot(x_ax_2, [2-x for x in x_ax_2], 'b')
    plt.plot(x_ax_3, [3-x for x in x_ax_3], 'b')
    
    plt.legend(shadow=True)
    plt.grid(True)
    plt.savefig('graph.png')
    #plt.show()

plot_total()