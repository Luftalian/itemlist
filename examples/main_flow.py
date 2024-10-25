from jobflow import job, Flow

@job
def add_1(x):
    return x + 1

@job
def add_2(x):
    return x + 2

@job
def add_3(x):
    return x + 3

a = add_1(1)
b = add_2(a.output)
c = add_3(b.output)

flow = Flow([a, b, c])

a2 = add_1(2)
b2 = add_2(a2.output)
c2 = add_3(b2.output)

flow2 = Flow([a2, b2, c2])

a3 = add_1(3)
b3 = add_2(a3.output)
c3 = add_3(b3.output)

flow3 = Flow([a3, b3, c3])