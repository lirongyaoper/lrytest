import sys
import pygame
from settiongs_lry import Settings
from ship_lry import Ship
from bullet_lry import Bullet

class AlienInvasion:
    """管理游戏资源和行为的类"""
    def __init__(self) :
        """初始化游戏病 创建游戏资源"""
        pygame.init()

        self.settings = Settings()
        self.screen = pygame.display.set_mode((0,0),pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height      
        pygame.display.set_caption("外星人入侵大战")
        self.ship   = Ship(self)
        self.bullets = pygame.sprite.Group()



    def run_game(self):
        """开始游戏,，的主循环"""
        while True:
            self._check_events()
            self.ship.update()
            self.bullets.update()
            self._update_screen()

    def _check_events(self):
        #监视键盘和鼠标事件
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True  
        elif event.key == pygame.K_q:
            sys.exit()    
        elif event.key == pygame.K_SPACE:
            self._fire_bullet()
    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key ==  pygame.K_LEFT:
            self.ship.moving_left = False    
    def _fire_bullet(self):
        #"""创建一颗子弹，并将其加入编组bullets中"""  
        new_bullet= Bullet(self)
        self.bullets.add(new_bullet)       

    def _update_screen(self):
        #每次循环都重新绘制屏幕
        self.screen.fill(self.settings.bg_color)
        self.ship.blitme()
        for bullet in self.bullets.sprites():
            bullet.draw_bullet()
        #让最近绘制的屏幕可见
        pygame.display.flip()

if __name__ == '__main__':
    ##创建游戏实例并运行游戏
    ai_lry = AlienInvasion()
    ai_lry.run_game()