import numpy as np
import matplotlib.pyplot as plt
# Single core Single VCPU experiments redis server and cli experiment readings
Num_groups = 6
# Counter values of Various VMs with timeslice of 1ms
counter_vals_1ms = (1180, 2436, 3752, 4973, 6376, 7641)
# Counter values of Various VMs with timeslice of 30ms
counter_vals_30ms = (1212, 2520, 3835, 5130, 6517, 7816)

ind = np.arange(Num_groups)
# set width param
width = 0.25

plt.bar(ind, counter_vals_1ms, width, label='1ms')
plt.bar(ind+width, counter_vals_30ms, width, label='30ms')

plt.ylabel('Redis-cli Counter')
# Not required for now
#plt.title()

plt.xticks(ind + width / 2, ('1/7VM', '2/7VM','3/7VM', '4/7VM', '5/7VM', '6/7VM'))
plt.legend(loc='best')
#plt.show()
plt.savefig('redis-counter_exp.pdf')
