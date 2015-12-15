# 使用移动命令到达迷宫的终点。
# 计算你收集到的宝石数量，然后在到达火球陷阱时通过说出当前的宝石数量来使陷阱失效。
# 在起点的地方会有一只乌鸦告诉你一个密码。在门的附近说出该密码来开门。
# 当你靠近食人魔时杀死它。
# 你可以在需要的时候使用loop来重复所有的指令。
# 如果你通过了这个关卡，你就可以直接跳到边远地区的森林！
x = 0
loop:
    self.moveUp()
    self.moveRight(3)
    self.moveUp()
    x += 1
    self.moveDown()
    self.moveRight()
    self.say("Friend")
    self.moveRight(2)
    self.moveUp()
    self.say(x)
    self.moveUp(2)
    enemy = self.findNearestEnemy()
    self.attack(enemy)
    self.attack(enemy)
    self.moveLeft(4)
    self.moveUp(2)