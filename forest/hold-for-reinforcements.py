# 食人魔正在爬悬崖
# 为集结民兵组织保护足够长时间的农民。
loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    if flag:
        # 捡旗子
        self.moveXY(flag.pos.x, flag.pos.y)
    
    elif enemy:
        # 否则，攻击！
        # 使用旗子移动到指定位置，如果收割技能冷却，就使用收割技能。
        if self.isReady("cleave"):
            self.cleave(enemy)
        else:
            self.attack(enemy)
        
