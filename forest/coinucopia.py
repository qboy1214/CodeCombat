# 当你放好旗帜后点提交.
# 点击提交后，旗帜按钮出现在左下角. 
loop:
    flag = self.findFlag()
    if flag:
        self.pickUpFlag(flag)
    else:
        self.say("为英雄放置一面旗帜来移动.")
    
