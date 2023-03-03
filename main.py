from googlesearch.googlesearch import GoogleSearch
from sys import argv
import matplotlib.pyplot as plt
file, searchTerm, start, stop, step = argv
start = int(start)
stop = int(stop)
step = int(step)

progBarWidth = 70
rollsPerBar = int(stop-start/progBarWidth)
barsToDraw = 0

graphY = []
graphX = []

for i in range(start, stop+1, step):
    term = searchTerm % i
    response = GoogleSearch().search(term)
    graphY.append(response.total)
    graphX.append(i)

    barsToDraw = int(((i-start) / (1+stop-start))*progBarWidth)
    print("\rProgress: |%s%s| %s" % ("#"*barsToDraw, "-"*(progBarWidth-barsToDraw-1), term), end="")
print()

with plt.xkcd():
    plt.ylabel("frequency")

    # linear
    plt.plot(graphX,graphY)
    plt.yscale('linear')
    plt.title(searchTerm.replace("%d", "x"))
    plt.grid(True)


    plt.show()
