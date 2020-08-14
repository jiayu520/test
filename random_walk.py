from random import choice

class RandomWalk():
    '''一个随机漫步数据的类'''

    def __init__(self,num_points=5000):
        '''初始化随机漫步的属性'''
        self.num_points = num_points

        #所有随机漫步都始于（0,0）
        self.x_values = [0]
        self.y_values = [0]


    def fill_walk(self):
        '''计算随机漫步包含的所有点'''

        #不断漫步，知道列表达到指定的长度
        while len(self.x_values) < self.num_points:
            #决定前进方向以及延这个方向前进的距离
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_setup = x_direction * x_distance

            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_setup = y_direction * y_distance

            #拒绝原地踏步
            if x_setup == 0 and y_setup == 0:
                continue

            #计算下一个点的x和y值
            next_x = self.x_values[-1] + x_setup
            next_y = self.y_values[-1] + y_setup

            self.x_values.append(next_x)
            self.y_values.append(next_y)