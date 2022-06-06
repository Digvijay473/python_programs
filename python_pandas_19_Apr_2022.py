from matplotlib import pyplot as plt # importing matplotlib module

# x-axis values

##x = [5, 2, 9, 4, 7]
##
### Y-axis values
##
##y = [10, 5, 8, 4, 2]
##
##
#### Function to plot or bar
##
###plt.plot(x,y)
##plt.bar(x,y)
##
### function to show the plot or bar
##
##plt.show()

from matplotlib import pyplot as bar
x = [5, 2, 9, 4, 7]
y = [10, 5, 8, 4, 20]
##bar.scatter(x,y)
##bar.bar(x,y)
bar.bar(x,y,color='red')
#bar.axis([0, 10, 0, 20])
bar.xlabel('runs')
bar.ylabel('overs')
bar.show()
