# 使用炸药干掉食人魔
# 然后用你的弓干掉他们

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        if self.isReady("throw"):
            distance = self.distanceTo(enemy)
            # 如果食人魔距离多于15米的时候，扔炸药炸他
            # 使用 if 来比较距离和15
            if distance > 15:
                self.throw(enemy)
            # 使用 else 来攻击它如果你不能够炸它
            else self.attack(enemy)
        else:
            self.attack(enemy)
