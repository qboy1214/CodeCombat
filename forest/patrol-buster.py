# 记得敌人可能还不存在。

loop:
    enemy = self.findNearestEnemy()
    # 如果是敌人，攻击它！
    if enemy:
        self.attack(enemy)