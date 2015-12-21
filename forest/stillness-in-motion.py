# 你可以将一个if语句放到另一个if语句当中。
# 但是，这样语句会变得很复杂，因此你必须注意这些if语句是如何互相影响的。
# 请确保代码缩进正确！
# 用注释来描述你的代码逻辑
# 在一个if/else语句中，对其里面的if/else进行注释将会很有帮助，如下所示：

loop:
    enemy = self.findNearestEnemy()
    
    # 如果这是一名敌人，就...
    if enemy:
        # 声明一个名为distanceTo的变量来代表距离
        distance =self.distanceTo(enemy)
        # 如果这名敌人小于5米的距离，那么attack()
        if distance < 5:
            self.attack(enemy)
        # 否则（这名敌人还离很远），就shield()
        else:
            self.shield()
            
        pass

    # 否则（没有敌人...）
    else:
        # ...回到位置X
        self.moveXY(40, 34)
