# %% 

from vectors import Point

ITERATIONS = 2500
DT = 0.01

def lorenz(sigma = 10, rho = 28, beta = 8/3, start = Point(0,0,0)):
    history = []

    x = start.x
    y = start.y
    z = start.z

    a = sigma # σ
    b = rho # ρ
    c = beta # β

    for _ in range(ITERATIONS):
        dx = a * (y-x) * DT
        dy = (x * (b-z) - y) * DT
        dz = (x*y - c*z) * DT

        x += dx
        y += dy
        z += dz

        history.append((x, y, z))

    x, y, z = zip(*history)
    return x, y, z

import matplotlib.pyplot as plt

x, y, z = lorenz(start=Point(0, 0.5, 0))
plt.plot(x, z)

x, y, z = lorenz(start=Point(0, 1, 0))
plt.plot(x, z)

plt.show()

# %%
