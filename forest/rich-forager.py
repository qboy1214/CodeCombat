# 使用 if 和 else if 来处理任何情况
# 放置它来防御敌人，收集金币
# 确保你从物品商店买到伟大的盔甲，建议400点以上的健康。

loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    item = self.findNearestItem()

    if flag:
        # 当我发现旗子的时候发生了什么？
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    elif enemy:
        # 当我找到敌人的时候发生了什么？
        self.attack(enemy)
    elif item:
        # 当我找到一个物品的时候，发生了什么？
        self.moveXY(item.pos.x, item.pos.y)
        
