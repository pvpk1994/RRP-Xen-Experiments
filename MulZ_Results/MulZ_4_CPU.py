# MulZ - FFD, OPT, and ILO algorithms for 4 CPUs
# Name: Pavan Kumar Paluri
# Plots for Dissertation
import matplotlib.pyplot as plt
import numpy as np

# plt.rcParams["figure.figsize"] = [7.50, 3.50]
plt.rcParams["figure.autolayout"] = True
# X Axis
utilization_ratio = [0.8, 0.82, 0.84, 0.86, 0.88, 0.90, 0.92, 0.94, 0.96, 0.98]

# Y Axes
MulZ_FFD = [0.936, 0.917, 0.860, 0.722, 0.594, 0.363, 0.179, 0.045, 0.008, 0.001]

MulZ_OPT = [0.943, 0.931, 0.903, 0.830, 0.750, 0.562, 0.315, 0.120, 0.018, 0.001]

MulZ_ILO = [0.943, 0.930, 0.903, 0.825, 0.742, 0.555, 0.312, 0.120, 0.018, 0.001]

# plot lines
plt.plot(utilization_ratio, MulZ_FFD, label="MulZ-FFD", marker='o', lw=2)
plt.plot(utilization_ratio, MulZ_OPT, label="MulZ-OPT", marker="v", lw=2)
plt.plot(utilization_ratio, MulZ_ILO, label="MulZ-ILO", marker=">", lw=2)
plt.xlabel("Utilization Ratio")
plt.ylabel("Ratio of schedulable partition sets")
plt.legend(loc="lower left")

# axes = plt.axes([.30, .6, .20, .15])
axes = plt.axes([.65, .6, .20, .20])
utilization_ratio_zoom = [0.86, 0.88, 0.90]

# Y Axes
# MulZ_FFD_zoom = [0.722, 0.594, 0.363]

MulZ_OPT_zoom = [0.83, 0.75, 0.562]

MulZ_ILO_zoom = [0.79, 0.71, 0.51]

# axes.plot(utilization_ratio_zoom, MulZ_FFD_zoom, label="MulZ-FFD", marker='o', lw=1)
axes.plot(utilization_ratio_zoom, MulZ_OPT_zoom, label="MulZ-OPT", marker="v", lw=1, color="orange")
axes.plot(utilization_ratio_zoom, MulZ_ILO_zoom, label="MulZ-ILO", marker=">", lw=1, color="green")

plt.show()