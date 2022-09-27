# 待完成
1. 更新template, 包括dt和fps
2. 将jugg simulator里面的可以复用的代码拿过来, 一边写一边思考, 考虑下那些是符合这个游戏的, 如何修改比较合适. 多花一点时间, 这个不着急
3. 小兵添加三个系统:
	1. 随机生成系统(完成)
	2. 向英雄移动系统(完成)
	3. 碰撞系统
      	1. 设置一个碰撞父类, 然后不同的游戏实体生产不同的碰撞子类, 然后碰撞类和sprite类相互同步位置
      	2. 主体master时时矫正collision_box的位置, 但是当碰撞发生时, collision_box才能矫正master的位置, 进而矫正自己的位置. 
	以上三个系统都参考jugg simulator
4. 添加树: (完成)

#  笔记
1. centered_camera: 
	
	对于玩家来说, player_pos = offset + 1/2 windows_size
		所以offset的计算公式是
		offset = player.rect.pos - 1/2 windows_size
	
	这样只要玩家移动自己的pos, 程序就会自动计算出对应的offset

	对于地面surface来说, 左上角永远是(0, 0), 但是绘制的时候相机的左上角是offset对应的坐标. 看起来就好像是相机的移动

	对于creep来说, 首先要求出相对于player的位置, 要有个Vector2来处理
	
	creep_pos = offset + player.rect.pos + Vector2

# 程序构思

