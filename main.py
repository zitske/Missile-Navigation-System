# MNS - Missile Navigation System 
# by Zitske Technology


import matplotlib.path as mpath
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import math
Path = mpath.Path

path = 0.7

l = (0,10)
t = (20,0)

c = (t[0],l[1])

lpd = math.hypot(c[0] - l[0], c[1] - l[1]) * path
tpd = math.hypot(c[0] - t[0], c[1] - t[1]) * path

lp = (lpd,l[1])
print(lp)
tp = (t[0],tpd)
print(tp)


#Curve P1 and P2
x1 = lp[0]
y1 = lp[1]

x2 = tp[0]
y2 = tp[1]





fig, ax = plt.subplots()
pp1 = mpatches.PathPatch(
    Path([l,(x1, y1), (c[0], c[1]), (x2, y2), (lp[0], y2)],
         [Path.MOVETO,Path.LINETO, Path.CURVE3, Path.CURVE3,Path.STOP]),
    fc="none", transform=ax.transData)
pp2 = mpatches.PathPatch(
    Path([(x2, y2),t],[Path.MOVETO,Path.LINETO]))
ax.add_patch(pp1)
ax.add_patch(pp2)
ax.plot(l[0], l[1], "ro")
ax.plot(t[0], t[1], "ro")
ax.plot(lp[0], lp[1], "ro")
ax.plot(tp[0], tp[1], "ro")
ax.plot(c[0], c[1], "ro")
ax.plot(lp[0], y2, "ro")
ax.set_title('MNS - MISSILE NAVIGATION SYSTEM')

plt.show()
