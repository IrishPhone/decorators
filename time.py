import time

NUM_RUNS = 10

def time_this(func):
    def wrapp():
        results = []
        for i in range(NUM_RUNS):
            t0 = time.time()
            func()
            t1 = time.time()
            results.append(t1 - t0)
        print("Average time for {0} passes is {1} s.".format(NUM_RUNS, sum(results) / len(results)))
        return
    return wrapp

@time_this
def f1():
    for j in range(1000000):
        a = j * 5

@time_this
def f2():
    for j in range(1000000):
        a = j / 5

f1()
f2()