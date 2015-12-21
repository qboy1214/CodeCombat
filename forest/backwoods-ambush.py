# 移动到各个节点，并消灭每一个食人魔。
self.moveXY(24, 42)
enemy1 = self.findNearestEnemy()
# 在攻击之前，使用if语句来确保当前有敌人存在。
if enemy1:
	self.attack(enemy1)
	self.attack(enemy1)

self.moveXY(27, 60)
enemy2 = self.findNearestEnemy()
if enemy2:
	self.attack(enemy2)
	self.attack(enemy2)

self.moveXY(42, 50)
# 再使用一个if语句并攻击！
enemy3 = self.findNearestEnemy()
if enemy3:
	self.attack(enemy3)
	self.attack(enemy3)

# 移动到下一个节点并消灭剩余的食人魔。
self.moveXY(39, 24)
enemy4 = self.findNearestEnemy()
if enemy4:
	self.attack(enemy4)
	self.attack(enemy4)
self.moveXY(55, 29)
enemy5 = self.findNearestEnemy()
if enemy5:
	self.attack(enemy5)
	self.attack(enemy5)
