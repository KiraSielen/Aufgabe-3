import numpy as np
import matplotlib.pyplot as plt


#a)
print('a)')
a = 1
h = 0.5
x_0 = 0.5

def euler(a, h, x_0):
    result = x_0 + h*(-a)*x_0
    return result

t = 0
while t<7:
    y = euler(a, h, x_0)
    print(y)
    x_0 = y*1 #rechnung, die nichts macht, damit man y unabh. von x_0 ändern kann
    t = t + h #h anstatt 0.5, damit allgemeiner
    plt.plot(t, y, "o")

plt.xlabel('$t$')
plt.ylabel('$euler(a, h, x_0)$')
plt.show()


#b)
print('b)')
a = 1
h = 0.1
x_0 = 0.5

def euler(a, h, x_0):
    result = x_0 + h*(-a)*x_0
    return result

t = 0
while t<7:
    y = euler(a, h, x_0)
    print(y)
    x_0 = y*1
    t = t + 0.01
    plt.plot(t, y)

plt.xlabel('$t$')
plt.ylabel('$euler(a, h, x_0)$')
plt.show()


#c)
print('c)')
a = 1
h = 0.01
x_0 = 0.5

def euler(a, h, x_0):
    result = x_0 + h*(-a)*x_0
    return result

t = 0
while t<7:
    y = euler(a, h, x_0)
    print(y)
    x_0 = y*1
    t = t + 0.01
    plt.plot(t, y)

plt.xlabel('$t$')
plt.ylabel('$euler(a, h, x_0)$')
plt.show()


#d)
print('d)')
a = 3
h = 0.5
x_0 = 3

def euler(a, h, x_0):
    result = x_0 + h*(-a)*x_0
    return result

t = 0
while t<7:
    y = euler(a, h, x_0)
    print(y)
    x_0 = y*1
    t = t + 0.5
    plt.plot(t, y)

plt.xlabel('$t$')
plt.ylabel('$euler(a, h, x_0)$')
plt.show()