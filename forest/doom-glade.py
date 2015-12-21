# 一波食人魔靠近，使用旗子赢得战役！

loop:
    enemy =self.findNearestEnemy()
    flag = self.findFlag("green")
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        elif self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
            
