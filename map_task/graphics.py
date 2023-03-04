from matplotlib import pyplot as plt

cpp = {"n": [], "time": [], "size": []}
with open("out-cpp.txt", "r") as file:
    for line in file:
        line = list(map(int, line.split()))
        cpp["n"] += [line[0]]
        cpp["time"] += [line[1]]
        cpp["size"] += [line[2]]

py = {"n": [], "time": [], "size": []}
with open("out-py.txt", "r") as file:
    for line in file:
        line = list(map(int, line.split()))
        py["n"] += [line[0]]
        py["time"] += [line[1]]
        py["size"] += [line[2]]

ax = plt.subplot(1, 2, 1)
plt.title("Зависимость скорости выполнения\nот кол-ва элементов")
plt.xlabel("Кол-во элементов")
plt.ylabel("Время выполнения(наносекунды)")
plt.plot(cpp["n"], cpp["time"], label="C++")
plt.plot(py["n"], py["time"], label="Python")
ax.set_xscale("log")
ax.set_yscale("log")
plt.grid()
plt.legend()

ax = plt.subplot(1, 2, 2)
plt.title("Зависимость объёма памяти\nот кол-ва элементов")
plt.xlabel("Кол-во элементов")
plt.ylabel("Размер(байт)")
plt.plot(cpp["n"], cpp["size"], label="C++")
plt.plot(py["n"], py["size"], label="Python")
ax.set_xscale("log")
ax.set_yscale("log")
plt.grid()
plt.legend()

plt.show()