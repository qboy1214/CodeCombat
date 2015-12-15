self.moveDown()

# 妈妈总对我说，随便吃点你在地牢里找到的蘑菇。

self.moveRight()
self.moveDown()
self.moveUp()
self.moveLeft()
self.moveDown(2)
self.moveRight(4)
self.moveUp()
self.moveLeft()
self.moveUp()
self.moveRight()
self.moveUp()
self.moveLeft()
self.moveDown()

# 找到你去地牢守卫者的路。

loop:
    enemy = self.findNearest(self.findEnemies())
    if enemy:
        self.attack(enemy)