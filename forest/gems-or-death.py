# 在 if 条件下的命令只有在条件为真的时候运行。
# 修复所有的 if 条件判定来赢得本关

# ==的意思是等于
if 1 + 1  == 3:  # ? Make this false.
    self.moveXY(5, 15)  # 移动到第一个地雷位置

if 2 + 2 < 5:  # ? Make this true.
	self.moveXY(15, 40)  # 移动到第一个宝石的位置。

# !=的意思是不等于
if 2 + 2 != 40:  # ? Make this true.
	self.moveXY(25, 15)  # 移动到第二个宝石的位置
	
# <的意思是比什么小
if 2 + 2 > 3:  # ? Make this true.
    enemy = self.findNearestEnemy()
    self.attack(enemy)

if 2 < 2:  # ? Make this false.
	self.moveXY(40, 55)

if False:  # ? Make this false.
	self.moveXY(50, 10)

if True:  # ? Make this true.
	self.moveXY(55, 25)