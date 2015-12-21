# Help your friends beat the minions that Thoktar sends against you.
# 你需要更好的装备和策略去赢得战斗。
# 标记可能有用，不过它由你决定——要有创造性哦！



loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
                self.attack(enemy)


    
