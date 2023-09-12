import sys
from random import randrange

def generate_random_points(n):
    L = []
    for i in range(n):
        L.append((randrange(-10**6,10**6+1),randrange(-10**6,10**6+1)))
    return L

def estimate_pi(n):
    P = generate_random_points(n)
    c = 0
    for i in range(n):
        if P[i][0]**2+P[i][1]**2 <= 10**12:
            c += 1
    return 4 * c / n

def approx75(n):
    cnt = 0
    for i in range(1000):
        if 0 < (estimate_pi(n)-3.14159)*10**5 < 1:
            cnt += 1;
    return cnt >= 750

def binary_search_n(m,n):
    if m == n:
        return m
    if approx75((m+n)//2):
        return binary_search_n(m,(m+n)//2)
    else:
        return binary_search_n((m+n)//2,n)

def average_number_of_points_needed():
    return binary_search_n(90000,100000)

#average_number_of_points_needed()
print(estimate_pi(int(sys.argv[1])))
print('Does {} random points approximate 3.14159 >= 75 times out of 100? {}'\
      .format(sys.argv[1],approx75(int(sys.argv[1]))))
