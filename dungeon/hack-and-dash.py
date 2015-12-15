# 你可以在循环前写代码
# 使用循环逃离迷宫

self.moveRight()
self.moveUp()
self.attack("Chest")
self.attack("Chest")
self.moveDown()

loop:
    # 移动3次
    self.moveRight(3)
    self.moveDown(3)