# 在短距离中释放你的『吸取生命』技能。
# 使用你的法丈在远距离攻击。

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        distance = self.distanceTo(enemy)
        if distance < 15:
            # 在敌人里释放『吸取生命』技能。
            self.cast("drain-life", enemy)
        else:
            # 使用你的盟友攻击敌人。
            self.attack(enemy)
            
