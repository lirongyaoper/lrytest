import sys
import pygame
from settiongs_lry import Settings
from ship_lry import Ship
class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self) :
        """初始化游戏病 创建游戏资源"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((self.settings.screen_width,self.settings.screen_height))
        pygame.display.set_caption("外星人入侵大战")
        self.ship   = Ship(self)



    def run_game(self):
        """开始游戏的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self._update_screen()

    def _check_events(self):
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                elif event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                elif event.key ==  pygame.K_LEFT:
                    self.ship.moving_left = False

    def _update_screen(self):
        #每次循环都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    ##创建游戏实例并运行游戏
    ai_lry = AlienInvasion()
    ai_lry.run_game()