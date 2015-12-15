# 生存时间比敌人的英雄长！

loop:
    # 制定自己的战略。有创意!
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)