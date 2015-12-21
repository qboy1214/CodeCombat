# 在村口巡逻。
# 当你见到食人魔，建立一个火焰陷阱。
# 不要让任何农民受到伤害。

loop:
    self.moveXY(43, 50)
    topEnemy = self.findNearestEnemy()
    if topEnemy:
        self.buildXY("fire-trap", 43, 50)
        
    self.moveXY(25, 34)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.buildXY("fire-trap", 25, 34)
    
    self.moveXY(43, 20)
    bottomEnemy = self.findNearestEnemy()
    if bottomEnemy:
        self.buildXY("fire-trap", 43, 20)
    
