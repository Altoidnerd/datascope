#!/usr/bin/env python3

import matplotlib.pyplot as plt
import sys
from highest_weekday_stddev import datadict


station = sys.argv[1]

plt.plot(range(len(datadict[station])), datadict[station])
plt.title('Station {} ridership (weekdays only)'.format(station))
plt.xlabel('Days after Jan 01, 2001')
plt.ylabel('Riders')

plt.show()


