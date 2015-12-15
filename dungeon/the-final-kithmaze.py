# 使用loop循环移动并攻击目标

loop:
    self.moveRight()
    self.moveUp()
    enemy = self.findNearestEnemy()
    self.attack(enemy)
    self.attack(enemy)
    self.moveRight()
    self.moveDown(2)
    self.moveUp()