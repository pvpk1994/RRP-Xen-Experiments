# MulZ - FFD, OPT, and ILO algorithms for 4 CPUs
# Name: Pavan Kumar Paluri
# Plots for Dissertation
import matplotlib.pyplot as plt
import numpy as np

num_groups = 3
# X Axis
utilization_ratio = [0.86, 0.88, 0.90]

# Y Axes
# MulZ_FFD = [0.722, 0.594, 0.363]

MulZ_OPT = [0.83, 0.75, 0.562]

MulZ_ILO = [0.825, 0.742, 0.555]

width = 0.25
# plot lines
# plt.plot(utilization_ratio, MulZ_FFD, label="MulZ-FFD", marker='o', color="")
plt.plot(utilization_ratio, MulZ_OPT, label="MulZ-OPT", marker="v", color="orange")
plt.plot(utilization_ratio, MulZ_ILO, label="MulZ-ILO", marker=">", color="green")
# plt.bar(utilization_ratio, MulZ_FFD, width, label="MulZ-FFD", color="blue")
# plt.bar(utilization_ratio, MulZ_OPT, width, label="MulZ-OPT", color="orange")
# plt.bar(utilization_ratio, MulZ_ILO, width, label="MulZ-ILO", color="green")
plt.xlabel("Utilization Ratio")
plt.ylabel("Ratio of schedulable partition sets")
plt.legend()

plt.show()