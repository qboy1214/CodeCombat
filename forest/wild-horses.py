loop:
    # 你怎么寻找最近的友好单位？
    # 马=？
    friends = self.findFriends()
    horse = self.findNearest(friends)
    if horse:
        x1 = horse.pos.x - 7
        x2 = horse.pos.x + 7
        
        if x1 >= 1:
            self.moveXY(x1, horse.pos.y)
            
        elif x2 <= 79:
            self.moveXY(x2, horse.pos.y)
            
        distance = self.distanceTo(horse)
        if distance <= 10:
            self.say("Whoa")
            # 移到到红色的x来使马返回农场。
            self.moveXY(28, 54)
            # 移回牧场开始寻找下一匹马。
            
            
