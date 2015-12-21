# 在你想要建造陷阱的位置插旗
# 当你没有在建造陷阱的时候，收集金币！

loop:
    flag = self.findFlag()
    if flag:
        # 我们该如何通过旗子的位置得到 fx 和 fy 呢？
        # （向下看如何得到物品的 x 和 y）
        
        
        self.buildXY("fire-trap", flag.pos.x, flag.pos.y)
        self.pickUpFlag(flag)
    else:
        item = self.findNearestItem()
        if item:
            itemPos = item.pos
            itemX = itemPos.x
            itemY = itemPos.y
            self.moveXY(itemX, itemY)
