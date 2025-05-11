import pyqtgraph as pg
import numpy as np

heights = np.random.randint(12, 45, 10)
labels = 'a d c e w t g u p m'.split()
x = range(len(labels))

win = pg.plot()
bar = pg.BarGraphItem(x=x, height=heights, width=0.6, brush='lightblue')
win.addItem(bar)

ax = win.getAxis('bottom')
ax.setTicks([list(zip(x, labels))])

# import pyqtgraph as pg
# import numpy as np
# x = np.arange(1000)
# y = np.random.normal(size=(3, 1000))
# plotWidget = pg.plot(title="Three plot curves")
# for i in range(3):
#     plotWidget.plot(x, y[i], pen=(i,3)) 

pg.QtGui.QGuiApplication.exec()