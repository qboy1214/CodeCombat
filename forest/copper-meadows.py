# 收集每片草地的所有金币。
# 使用旗子在草地间移动。
# 当你准备好放置旗子时点击“提交”

loop:
    flag = self.findFlag()
    if flag:
        pass  # “pass”是一个占位符，它没有任何作用
        # Pick up the flag.
        self.pickUpFlag(flag)
    else:
        # Automatically move to the nearest item you see.
        item = self.findNearestItem()
        if item:
            position = item.pos
            x = position.x
            y = position.y
            self.moveXY(x, y)
