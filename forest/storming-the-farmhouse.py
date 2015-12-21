# 士兵会慢慢到达，但是食人魔会淹没他们。
# 基本的攻击循环是不能够让你活下来的

loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    if enemy:
        distance = self.distanceTo(enemy)
        if self.isReady("cleave"):
            self.cleave(enemy)
        elif self.isReady("bash"):
            self.bash(enemy)
        else:
            self.attack(enemy)
            
