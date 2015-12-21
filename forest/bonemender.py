# 拯救盟友的士兵来突围
loop:
    if self.canCast("regen"):
        bernardDistance = self.distanceTo("Bernard")
        if bernardDistance < 10:
            # Bernard需要治疗！
            self.cast("regen", "Bernard")
        
        # 使用『if』和『distanceTo』来治疗 Chandra
        # 如果她小于10米的距离。
        chandraDistance =self.distanceTo("Chandra")
        if chandraDistance < 10:
            # Chandra需要治疗！
            self.cast("regen", "Chandra")
    else:
        # 如果你没有执行 regen，使用 if 和 distanceTo 
        # 来攻击那些小于一定距离的敌人 self.attackRange.
        enemy = self.findNearestEnemy()
        if enemy:
            edistance = self.distanceTo(enemy)
            if edistance < 20:
                self.attack(enemy)
