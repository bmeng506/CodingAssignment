def something(r):
    s = 0
    for i in r:
        s += i
    return s / len(r)

def how_is_it(x):
    if x > 8.5:
        print("Excellent")
    elif x > 7:
        print("Good")
    elif x > 5:
        print("Average")
    else:
        print("Poor")

def fit(x, scale=100):
    out = []
    for i in x:
        out.append(i/scale*10)
    return out

print("Running tests") # test

r = [87, 93, 76, 100, 65]
z = fit(r)
avg = something(z)
fit(avg)
