# How to run:
# python3 matrix.py
import numpy, sys, time
import csv
#if (len(sys.argv) != 2):
    #print("usage: python %s N" % sys.argv[0])
    #quit()
n_time = []

f = open('n_time.csv', 'w')
writer = csv.writer(f)
for n in range(2, 300):
    n = int(n)
    a = numpy.zeros((n, n)) # Matrix A
    b = numpy.zeros((n, n)) # Matrix B
    c = numpy.zeros((n, n)) # Matrix C

    n_time = [] # n and time required are going to be saved

    # Initialize the matrices to some values.
    for i in range(n):
        for j in range(n):
            a[i, j] = i * n + j
            b[i, j] = j * n + i
            c[i, j] = 0

    begin = time.time()

    # ---- my code ---- # 

    for i in range(n):
        for j in range(n):
            sum_column = 0
            for k in range(n):
                sum_column += a[i, k] * b[k, j]
            c[i, j] = sum_column

    # ------------------ #

    end = time.time()
    writer.writerow([n, end - begin])
    print("time: %.6f sec" % (end - begin))

f.close()



# Print C for debugging. Comment out the print before measuring the execution time.
"""
total = 0
for i in range(n):
    for j in range(n):
        # print c[i, j]
        total += c[i, j]"""
# Print out the sum of all values in C.
# This should be 450 for N=3, 3680 for N=4, and 18250 for N=5.
#print("sum: %.6f" % total)

#with open("n_time.csv", 'w', newline='') as f:
    #writer = csv.writer(f, quoting=csv.QUOTE_ALL, delimiter=',')
    #writer.writerows(n_time)