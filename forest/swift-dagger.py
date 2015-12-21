# 长距离用你的弓，短距离用匕首

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        distance = self.distanceTo(enemy)
        if distance < self.throwRange:
            # 向敌人扔你的匕首
            self.throw(enemy)
        else:
            # 用你的弓攻击敌人
            self.attack(enemy)
            
