# 尽可能经常使用你的新技能“cleave”

self.moveXY(23, 23)
loop:
    enemy = self.findNearestEnemy()
    if self.isReady("cleave"):
        # “Cleave”掉敌人！
        self.cleave(enemy)
    else:
        # 否则（如果“cleave”还没准备好），就用你的普通攻击
        self.attack(enemy)