# 使用旗子加入战斗或者撤退。
# If you fail, press Submit again for new random enemies and try again!
# You'll want at least 300 health, if not more.

loop:
    enemy = self.findNearestEnemy()
    flag = self.findFlag()
    if flag:
        # 捡起旗子。
        pass
        self.pickUpFlag(flag)
    elif enemy:
        # 打！
        pass
        self.attack(enemy)
