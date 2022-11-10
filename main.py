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
    term = searchTerm % i
    response = GoogleSearch().search(term)
    graphY.append(response.total)
    graphX.append(i)
    print(term, response.total)


plt.ylabel('')

# linear
plt.plot(graphX,graphY)
plt.yscale('linear')
plt.title(searchTerm.replace("%d", "x"))
plt.grid(True)

plt.show()
