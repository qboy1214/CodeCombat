loop:
    enemy = self.findNearestEnemy()
    distance = self.distanceTo(enemy)
    if distance < 12:
        # 如果他们与农民太近，就攻击他们
        if self.isReady("cleave"):
           self.cleave(enemy)
        else:
           self.attack(enemy) 
        
    # 否则的话，呆在农民旁边！
    else:
        self.moveXY(39, 36)
    
