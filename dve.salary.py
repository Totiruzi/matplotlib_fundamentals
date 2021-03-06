from matplotlib import pyplot as plt

plt.style.use('seaborn-talk')

ages_x = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54]
plt.title("Salary of Developers by age")
plt.xlabel("Developer age range")
plt.ylabel("Salary (USD)")

py_dev_y = [45372, 48876, 53850, 57287, 63016, 65998, 70003, 70000, 71496, 75370, 83640, 84666, 84392, 78254, 85000, 87038, 91991, 100000, 94796, 97962, 93302, 99240, 102736, 112285, 100771, 104708, 108423, 101407, 112542, 122870]
plt.plot(ages_x, py_dev_y, linestyle='--', marker='x', color='b', label='Python')

js_dev_y = [37810, 43515, 46823, 49293, 53437, 56373, 62375, 66674, 68745, 68746, 74583, 79000, 78957, 79996, 80403, 83820, 88833, 91660, 87892, 96243, 90000, 99313, 91660, 102264, 100000, 100000, 91660, 99240, 108000, 105000]
plt.plot(ages_x, js_dev_y,label='JavaScript')

dev_y = [38496, 42000, 46752, 49320, 53200, 56000, 62316, 64928, 67317, 68748, 73752, 77232, 78000, 78508, 79536, 82488, 88935, 90000, 90056, 95000, 90000, 91633, 91660, 98150, 98964, 100000, 98988, 100000, 108923, 105000]
plt.plot(ages_x, dev_y,label='All Devs')

plt.legend()
# plt.grid(True)
plt.savefig('dve.salary.pdf')

plt.show()