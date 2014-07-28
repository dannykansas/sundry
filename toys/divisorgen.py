import math
import datetime
import os
import matplotlib
import matplotlib.mlab as mlab

from matplotlib.figure import Figure
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas


def divisorGenerator(n):
    large_divisors = []
    for i in xrange(1, int(math.sqrt(n) + 1)):
        if n % i is 0:
            yield i
            if i is not n / i:
                large_divisors.insert(0, n / i)
    for divisor in large_divisors:
        yield divisor

def iterator():
    i = 0 
    top = 10000 
    l = {}
    print "Beginning divisor generation..."
    while i <= top:
	l[i] = list(divisorGenerator(i))
	i+=1
    print "Finished divisor generation..."
    listbuilder(l)
    print "(Wrapping up...)"

def listbuilder(l):
    print "Building list of coordinates..."
    x_list = []
    y_list = []
    for x in l:
	for y in l[x]:
	    x_list.append(x)
	    y_list.append(y)
    print "Coordinate list built..."
    plotter(x_list,y_list)    
    
def plotter(x,y):
    # Create a figure of size 10 x 10 inches
    fig = Figure(figsize=(10,10))
    
    # Create a canvas to add fig to
    canvas = FigureCanvas(fig)
    
    ax = fig.add_subplot(111) 
    ax.grid(True,linestyle='-',color='0.15')

    print "Building scatter plot..."
    ax.scatter(x,y,s=1,color='tomato');
    filename = str(os.path.expanduser('~')) + '/plots/plot_' + str(datetime.datetime.now().time()) + '.png'
    try: 
        canvas.print_figure(filename,dpi=300)
        print "Built and saved scatterplot to {0}".format(filename)
    except:
        "Failed to build scatterplot."        
    
if __name__=='__main__':iterator() 
