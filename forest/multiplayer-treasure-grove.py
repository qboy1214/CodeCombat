# 当第一个收集100个金币的人！
# 如果你死了，重生的时候只有原来金币的67%

loop:
    # 找到金币并攻击敌人
    # 使用旗子和特殊的移动策略来赢得比赛！
    
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        distance1 = self.distanceTo(enemy)
        if distance1 < 1:
            self.attack(enemy)
    if item:
        distance2 = self.distanceTo(item)
        if distance2 < 5:
            self.moveXY(item.pos.x, item.pos.y)
    
