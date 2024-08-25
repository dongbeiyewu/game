from ursina import Entity, color

def create_map():
    # 创建更大的地面
    ground = Entity(
        model='plane',
        scale=(40, 1, 40),  # 扩大地面
        texture='white_cube',
        texture_scale=(40, 40),
        color=color.dark_gray,
        collider='box'
    )
    
    # 创建地牢墙壁
    wall_thickness = 1
    wall_height = 5

    # 外围墙壁
    walls = [
        Entity(model='cube', scale=(40, wall_height, wall_thickness), position=(0, wall_height / 2, -20), color=color.gray, collider='box'),  # 上墙
        Entity(model='cube', scale=(40, wall_height, wall_thickness), position=(0, wall_height / 2, 20), color=color.gray, collider='box'),   # 下墙
        Entity(model='cube', scale=(wall_thickness, wall_height, 40), position=(-20, wall_height / 2, 0), color=color.gray, collider='box'), # 左墙
        Entity(model='cube', scale=(wall_thickness, wall_height, 40), position=(20, wall_height / 2, 0), color=color.gray, collider='box')   # 右墙
    ]
    
    # 内部墙壁
    inner_walls = [
        Entity(model='cube', scale=(wall_thickness, wall_height, 20), position=(10, wall_height / 2, 10), color=color.gray, collider='box'), # 垂直内部墙1
        Entity(model='cube', scale=(wall_thickness, wall_height, 15), position=(-10, wall_height / 2, -5), color=color.gray, collider='box'), # 垂直内部墙2
        Entity(model='cube', scale=(15, wall_height, wall_thickness), position=(0, wall_height / 2, -10), color=color.gray, collider='box'), # 水平内部墙1
        Entity(model='cube', scale=(10, wall_height, wall_thickness), position=(5, wall_height / 2, 5), color=color.gray, collider='box')  # 水平内部墙2
    ]

    # 你可以继续添加更多的墙壁或其他地牢元素来扩展地图
