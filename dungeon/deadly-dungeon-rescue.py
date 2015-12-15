# 在你救出受酷刑的农民后，逃出地牢。
# 你可以藏在滴水兽后面。
# 杀了警卫会得到不希望的结果。
# 如果你掠夺了所有的宝藏，会得到附件的奖励。

loop:
    flag =self.findFlag("green")
    enemies = self.findEnemies()
    enemy = self.findNearest(enemies)
    item = self.findNearest(self.findItems())
    
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if item:
        self.moveXY(item.pos.x, item.pos.y)
    if enemy :
        distance = self.distanceTo(enemy)
        if distance < 8:
            self.attack(enemy)
    


