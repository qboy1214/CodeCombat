# 成功击败所有食人魔

self.moveUp()
self.moveRight(3)
self.moveDown(2)
self.moveLeft()
enemy1 = self.findNearestEnemy()
self.attack(enemy1)
enemy2 = self.findNearestEnemy()
self.attack(enemy2)
self.moveDown()