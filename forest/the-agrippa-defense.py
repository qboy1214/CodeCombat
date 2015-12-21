loop:
    enemy = self.findNearestEnemy()
    if enemy:
        pass  # 用你自己的代码替换这行
        # 用 distanceTo 获取与敌人的距离。
        distance = self.distanceTo(enemy)
        # 如果距离小于5米...
        if distance < 5:
            # ...如果 “cleave”技能准备好了，就“cleave”掉他们！
            if self.isReady("cleave"):
                self.cleave(enemy)
            # ...否则，仅仅进行普通攻击。
            else:
                self.attack(enemy)
