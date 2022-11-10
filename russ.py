from googlesearch.googlesearch import GoogleSearch
from sys import argv
import matplotlib.pyplot as plt
file, searchTerm, start, stop, step = argv
start = int(start)
stop = int(stop)
step = int(step)

graphY = []
graphX = []

for i in range(start, stop+1, step):
    graphY.append(GoogleSearch().search(searchTerm % i).total)
    graphX.append(i)
plt.plot(graphX,graphY)
plt.show()

plt.ylabel('')

# linear
# plt.yscale('linear')
# plt.title(searchTerm)
# plt.grid(True)

