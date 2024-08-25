from ursina import Entity, Vec3, held_keys, time, camera, color

class Player(Entity):
    def __init__(self):
        super().__init__(
            model='cube',
            scale=(1, 2, 1),
            color=color.orange,
            position=(0, 1, 0),
            collider='box'
        )

    def update(self):
        speed = 5 * time.dt
        direction = Vec3(
            held_keys['d'] - held_keys['a'],  # 左右方向
            0,
            held_keys['w'] - held_keys['s']   # 前后方向
        ).normalized()
        self.position += direction * speed
        
        # 设置摄像机位置为角色上方和后方，创建2.5D视角
        camera.position = self.position + Vec3(0, 20, -20)
        camera.rotation_x = 30  # 俯视角度
        camera.look_at(self.position)  # 摄像机看向角色
