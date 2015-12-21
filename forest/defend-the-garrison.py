# 杀掉所有进攻的食人魔
# 使用旗子远离那些危险的食人魔

loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag("green")
    if flag:
        self.pickUpFlag(flag)
    if enemy and self.health > 100:
        if self.canElectrocute(enemy):
            self.electrocute(enemy)
        if self.isReady("cleave"):
            self.cleave(enemy)
        if self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)
