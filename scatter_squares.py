import matplotlib.pyplot as plt


x_value = list(range(1,1001))
y_value = [x**2 for x in x_value]

plt.scatter(x_value,y_value,s=40)
#设置图标标题并给坐标轴加上标签
plt.title("Square Number",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Vlaue",fontsize=14)
#设置刻度标记的大小
plt.axis([0,1100,0,1100000])
#plt.tick_params(axis='both',which='major',labelsize=14)
plt.show()