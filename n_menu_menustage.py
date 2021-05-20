from n_mygameworld import *
from n_menu_gamestage import *
#from n_menu_main import scr

class Menustage(MyStage):
    # 0-menu; 1-game
    scr: int = 0
    game: GameStage

    def exit(self, pos, btn):
        exit()

    def game(self, pos, btn):
        self.game = GameStage(self)
        self.scr = 1

    def __init__(self):
        super().__init__()
        menuitem1: MyActor = MyActor("star.png", pos=(100, 100), anchor=(0, 0))
        self.add_actor(menuitem1)
        menuitem1.set_on_mouse_down_listener(self.game)

        menuitem2: MyActor = MyActor("star.png", pos=(100, 250), anchor=(0, 0))
        self.add_actor(menuitem2)
        menuitem2.set_on_mouse_down_listener(self.exit)

    def draw(self):
        if self.scr == 0:
            super().draw()
        if self.scr == 1:
            self.game.draw()

    def update(self, deltaTime: float = 0.0166666666666666666666):
        if self.scr == 0:
            super().update(deltaTime)
        if self.scr == 1:
            self.game.update(deltaTime)

    def on_mouse_down(self, pos, button):
        if self.scr == 0:
            super().on_mouse_down(pos, button)
        if self.scr == 1:
            self.game.on_mouse_down(pos, button)



