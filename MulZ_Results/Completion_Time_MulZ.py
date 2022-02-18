# Completion Time in Log scale
# Name: Pavan Kumar Paluri
# MulZ - FFD, OPT, and ILO algorithms for 64 CPUs
# Name: Pavan Kumar Paluri
# Plots for Dissertation
import matplotlib.pyplot as plt
import numpy as np
import pylatex as pltx

# X Axis
# num_cpus = [0, 1, 2, 3, 4, 5, 6]
num_cpus = np.array([0, 1, 2, 3, 4, 5, 6])

# Y Axes
MulZ_FFD = np.array([-6.587, -3.879, -2.987, -1.972, -0.502, 0.979, 2.808])

MulZ_OPT = np.array([-2.380, 2.040, 9.456, 17.901, np.nan, np.nan, np.nan])

MulZ_ILO = np.array([0.827, 2.702, 4.145, 6.534, 8.887, 11.522, 13.436])

# plot lines
plt.plot(num_cpus, MulZ_FFD, label="MulZ-FFD", marker='o', color="blue")
plt.plot(num_cpus, MulZ_OPT, label="MulZ-OPT", marker="v", color="orange")
plt.plot(num_cpus, MulZ_ILO, label="MulZ-ILO", marker=">", color="green")
plt.xlabel("log\u2082(m)")
plt.ylabel("log\u2082(CT) (ms)")
plt.legend()
plt.show()