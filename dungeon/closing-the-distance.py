self.moveRight()

# 通过上一个关卡，你应该能认识这个。
enemy1 = self.findNearestEnemy()
# 现在，攻击那个变量，

self.attack(enemy1)
self.attack(enemy1)
self.moveRight(2)
self.moveUp()
enemy2 = self.findNearestEnemy()
self.attack(enemy2)
self.moveDown()
self.moveRight()