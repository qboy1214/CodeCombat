# 铲除所有遗留的小食人魔
# 确保你有足够的护甲。

loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        self.cleave(enemy)
    else:
        self.shield()
        
