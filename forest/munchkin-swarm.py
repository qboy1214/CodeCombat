loop:
    enemy = self.findNearestEnemy()
    distance = self.distanceTo(enemy)
    if distance < 10:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
    else:
        self.attack("Chest")
