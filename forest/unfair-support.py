# 偷偷穿过森林，伏击萨满。
# 听从指挥官Craig 小心接近中的敌人。
# 放置旗子后，按提交。

loop:
    flag = self.findFlag()
    enemy = self.findNearestEnemy()
    if flag:
        self.moveXY(flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
        
    elif enemy:
        # 攻击视野内的敌人。
        if enemy:
            self.attack(enemy)
        
