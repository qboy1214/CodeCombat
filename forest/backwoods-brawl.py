# 生存一分钟。
# 如果你赢了，这关卡将会变得更难（以及更好的奖励）。
# 如果你输了，你必须等待24小时后才能再次挑战。
# 记得，每一次提交都会获得不同的地图。
loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()

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
