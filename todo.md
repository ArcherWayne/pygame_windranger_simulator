# 重要: 全部使用topleft作为实际坐标, 然后用sprite的大小补偿到中心

# 待完成
1. 更新template, 包括dt和fps
2. 碰撞debug系统

#  笔记
1. centered_camera: 
   
	camera类的工作方式：首先根据给与的中心目标target计算出offset，这个offset实际上是camera的左上坐标

	对于玩家来说, player_pos = offset + 1/2 windows_size
		所以offset的计算公式是
		offset = player.rect.pos - 1/2 windows_size
	
	这样只要玩家移动自己的pos, 程序就会自动计算出对应的offset

	对于地面surface来说, 左上角永远是(0, 0), 但是绘制的时候相机的左上角是offset对应的坐标. 看起来就好像是相机的移动

	对于creep来说, 首先要求出相对于player的位置, 要有个Vector2来处理
	
	creep_pos = offset + player.rect.pos + Vector2 # Vector2就是creep相对于玩家的位置。



# 程序构思

