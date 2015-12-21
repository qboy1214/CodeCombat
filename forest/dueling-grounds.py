# 在决斗中击败敌人的英雄！

loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        self.cleave(enemy)
    else:
        self.attack(enemy)
