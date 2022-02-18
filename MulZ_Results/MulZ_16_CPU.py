# MulZ - FFD, OPT, and ILO algorithms for 64 CPUs
# Name: Pavan Kumar Paluri
# Plots for Dissertation
import matplotlib.pyplot as plt
import numpy as np

# X Axis
utilization_ratio = [0.8, 0.82, 0.84, 0.86, 0.88, 0.9, 0.92, 0.94, 0.96, 0.98]

# Y Axes
MulZ_FFD = [1.0, 1.0, 0.99, 0.97, 0.98, 0.72, 0.25, 0, 0, 0]

# MulZ_OPT = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

MulZ_ILO = [1.0, 1.0, 0.99, 0.96, 0.97, 0.77, 0.47, 0.12, 0, 0]

# plot lines
plt.plot(utilization_ratio, MulZ_FFD, label="MulZ-FFD", marker='o', color="blue")
# plt.plot(utilization_ratio, MulZ_OPT, label="MulZ-OPT", marker="v")
plt.plot(utilization_ratio, MulZ_ILO, label="MulZ-ILO", marker=">", color="green")
plt.xlabel("Utilization Ratio")
plt.ylabel("Ratio of schedulable partition sets")
plt.legend()
plt.show()
