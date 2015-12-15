# Inside a loop, use findNearestEnemy and attack!
loop:
    enemy = self.findNearestEnemy()
    self.attack(enemy)