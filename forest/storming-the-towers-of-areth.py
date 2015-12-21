self.moveXY(55, 14)
self.moveXY(92, 9)

# 在红色的 X 位置建造一个火焰陷阱
# 撤退到木的 X 位置，来避免伤害。
# 等雇佣兵发现闪亮的火焰陷阱
# 进入营地，放置火焰陷阱在红色的 X 位置
# 冲你的部队喊撤退（提示：使用 say 命令, "Retreat!"）
# 逃回到左边的木的 X 位置

self.buildXY("fire-trap", 94, 20)
self.moveXY(79, 6)
self.moveXY(92, 9)
self.moveXY(60, 63)
self.buildXY("fire-trap", 60, 63)
self.moveXY(90, 53)
self.buildXY("fire-trap", 90, 53)
self.moveXY(94, 20)
self.moveXY(5, 14)
self.say("Retreat")
self.moveXY(-16, 39)
