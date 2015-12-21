# 从2~3个树丛里 收集100个金币
# 如果你赢了，会变得更难（并且有更多奖励）
# 如果你输了，需要等待一天再次挑战
# 记住，每次提交都会得到新的随机种子。
loop:
    item = self.findNearestItem()
    enemy = self.findNearestEnemy()
    flag = self.findFlag("green")
    if flag:
        self.pickUpFlag(flag)
    if item:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy:
        if self.isReady("bash"):
            self.bash(enemy)
        elif self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
