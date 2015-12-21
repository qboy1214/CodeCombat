# 如果有敌人，则攻击之
# 如果没有敌人，则攻击财宝箱

loop:
    # 使用if/else语句
    enemy = self.findNearestEnemy()
    if enemy:
        self.attack(enemy)
    else:
        self.attack("Chest")
    
    
