# 炮火的天启在接近我们！
# 在60秒内躲避炮弹。
# 提示：旗子可能派上用场，比如Coinucopia这关。
# 因为攻击是每次提交时随机的，所以你不能使用moveXY这个指令。
loop:
    flag = self.findFlag("green")
    if flag:
        self.pickUpFlag(flag)
    self.shield()
        
