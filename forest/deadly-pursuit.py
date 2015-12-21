# 收集金币使用旗子来建造陷阱
# 你在这处理这些食人魔

loop:
    flag = self.findFlag()
    
    if flag:
        self.buildXY("fire-trap", flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if item:
            
            self.moveXY(item.pos.x, item.pos.y)
        
