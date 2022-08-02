import  matplotlib
from matplotlib import pyplot as plt
from celluloid import camera

fig = plt.figure()
camera = camera(fig)
for i in range(5):
    t = plt.plot(range(i,i+5))
    plt.legend(t, [f'line{i}'])
    camera.snap()
plt.show()
plt.savefig('/home/zhoubin/study/python/test.png')
#animation = camera.animate()