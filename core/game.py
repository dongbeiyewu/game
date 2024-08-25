from panda3d.core import loadPrcFileData
from ursina import Ursina
from core.camera import setup_camera
from core.player import Player
from core.game_map import create_map

# 手动指定显示管道 (可根据需要调整)
loadPrcFileData("", "load-display pandagl")

def start_game():
    app = Ursina()

    setup_camera()
    create_map()
    player = Player()

    app.run()
