# 在一波波的食人魔攻击中活下来。
# 如果你赢了，本关会变得更难，但给更多的奖励。
# 如果你输了，你必须等一天之后才能重新提交。
# 每次提交都会获得新的随机种子。

loop:
    enemy = self.findNearest(self.findEnemies())
    flag = self.findFlag("green")
    item = self.findNearest(self.findItems())
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if item:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)