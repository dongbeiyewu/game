from ursina import Entity, Vec3, held_keys, time, camera, color, boxcast

class Player(Entity):
    def __init__(self):
        super().__init__(
            model='cube',  # 替换为你的小人模型
            scale=(0.5, 1, 0.5),
            color=color.orange,
            position=(0, 1, 0),
            collider='box'  # 添加碰撞检测
        )

    def update(self):
        speed = 5 * time.dt
        direction = Vec3(
            held_keys['d'] - held_keys['a'],  # 左右方向
            0,
            held_keys['w'] - held_keys['s']   # 前后方向
        ).normalized()
        
        # 计算移动后的新位置
        new_position = self.position + direction * speed
        
        # 检查是否会发生碰撞
        hit_info = boxcast(self.position, direction, distance=speed, ignore=[self], thickness=(0.5, 1, 0.5))
        
        if not hit_info.hit:
            self.position = new_position  # 如果没有碰撞，更新位置
        
        # 更新摄像机位置
        camera.position = self.position + Vec3(0, 20, -20)
        camera.look_at(self.position)
