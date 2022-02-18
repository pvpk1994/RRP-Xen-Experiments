# MulZ - FFD, OPT, and ILO algorithms for single CPU
# Name: Pavan Kumar Paluri
# Plots
import matplotlib.pyplot as plt
import numpy as np

# X Axis
utilization_ratio = [0.8, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96, 0.98]

# Y Axes
MulZ_FFD = [0.903, 0.87, 0.823, 0.779, 0.658, 0.565, 0.45, 0.36, 0.223, 0.14]

MulZ_OPT = [0.943, 0.933, 0.899, 0.863, 0.80, 0.718, 0.648, 0.623, 0.473, 0.307]

MulZ_ILO = [0.943, 0.933, 0.899, 0.863, 0.80, 0.718, 0.648, 0.623, 0.473, 0.307]

# plot lines
plt.plot(utilization_ratio, MulZ_FFD, label="MulZ-FFD", marker='o')
plt.plot(utilization_ratio, MulZ_OPT, label="MulZ-OPT", marker="v")
plt.plot(utilization_ratio, MulZ_ILO, label="MulZ-ILO", marker=">")
plt.xlabel("Utilization Ratio")
plt.ylabel("Ratio of schedulable partition sets")
plt.legend()
plt.show()
