from ursina import camera

def setup_camera():
    camera.position = (0, 20, -20)  # 设置摄像机在角色上方和后方
    camera.rotation_x = 30          # 俯视角度
