import approx
import itertools as it
import numpy as np


def build_initial_conditions(number):
    conditions = []
    while len(conditions) < 100:
        angle = np.random.uniform(low=-math.pi, high=math.pi)
        velocity = np.random.uniform(low=-2.1, high=2.1)

        kinetic_energy = 0.5 * velocity ** 2
        potential_energy = np.cos(angle)

        if np.abs(kinetic_energy - potential_energy) < 0.99:
            conditions.append((position, velocity))

    return conditions


# def generate_gaussian(angle):
#     x_cm = np.cos(angle - math.pi/2)
#     y_cm = np.sin(angle - math.pi/2)

#     for x, y in it.product(np.linspace(-1.5, 1.5, num=51),
#                            np.linspace(-1.5, 1.5, num=51)):
#         x_pos = x - x_cm
#         y_pos = y - y_cm
#         yield np.exp(-20*(x_pos**2+y_pos**2))


def calculate_gaussian_ball(x_cm, y_cm):
    x = np.linspace(-1.5, 1.5, 51)
    y = np.linspace(-1.5, 1.5, 51)
    xx, yy = np.meshgrid(x, y, sparse=True)
    gaussian = np.exp(-20*(xx**2 + yy**2))

    a = np.zeros((500, 500))
    a[x_cm-25:x_cm+26, y_cm-25:y_cm+26] = gaussian
    return a


if __name__ == "__main__":
    u0 = math.pi / 12
    du0 = v0 = 0
    tmax = 10.0
    n = 2000

    u, thetas = approx.runge_kutta(u0, v0, tmax, n)

    for theta in thetas[::100]:
        print(theta)
        length = 150
        x = 250 + length * np.sin(theta)
        y = 250 - (length * (1 - np.cos(theta)))
        plt.imshow(calculate_gaussian_ball(int(y), int(x)))
        plt.show()
