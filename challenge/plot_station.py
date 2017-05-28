#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
from highest_mean import datadict


station = sys.argv[1]

plt.plot(range(len(datadict[station])), datadict[station])
plt.title('Station {} ridership'.format(station))
plt.xlabel('Days after Jan 01, 2001')
plt.ylabel('Riders')

plt.show()


