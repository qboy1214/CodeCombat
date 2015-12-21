# 在村口巡逻。
# 如果发现敌人，击杀他们。

loop:
    self.moveXY(35, 34)
    leftEnemy = self.findNearestEnemy()
    if leftEnemy:
        self.attack(leftEnemy)
        self.attack(leftEnemy)
    # 现在移动到右侧。
    # 使用if指令判断是否有敌人，有的话，击杀他们。
    self.moveXY(60, 31)
    rightEnemy = self.findNearestEnemy()
    if rightEnemy:
        self.attack(rightEnemy)
        self.attack(rightEnemy)
