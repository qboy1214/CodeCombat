# 拿下那些兽人 

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        distance = self.distanceTo(enemy)
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
