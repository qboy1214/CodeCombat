# 呆在中间防守

loop:
    enemy = self.findNearestEnemy()
    if enemy:
        # 主动出击
       self.attack(enemy) 
        
    else:
        # 回到你的阵地防守
        self.moveXY(40, 37)