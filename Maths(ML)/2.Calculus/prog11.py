def loss(w):
    return w**2 - 4*w+5
for w in [1,2,3]:
    print(f"Weight {w}: Loss {loss(w)}")