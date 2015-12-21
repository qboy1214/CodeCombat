# 只攻击幼小食人魔和投掷者食人魔。
# 别攻击树榴，遇到食人魔快跑。

loop:
    enemy = self.findNearestEnemy()
    
    # 记住：别攻击树榴『burl』
    if enemy.type is "burl":
        self.say("我不攻击树榴『burl』")

    # type 属性告诉你它是什么种类的生物
    if enemy.type is "munchkin":
        self.attack(enemy)
    
    # 使用『if』来攻击投掷者『thrower』
    if enemy.type is "thrower":
        self.attack(enemy)
    
    # 如果它是一个食人魔『ogre』，跑到村口去！
    if enemy.type is "ogre":
        self.moveXY(40, 47)
    
