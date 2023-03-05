import pygame
class Ship:
    """管理飞船的类"""
    def __init__(self,ai_name):
        """初始化飞船病设置其初始位置。"""
        self.screen = ai_name.screen
        self.settings = ai_name.settings
        self.screen_rect = ai_name.screen.get_rect()
        #加载飞船图像并获取其外接矩形
        self.image = pygame.image.load('E:/lrytest/python/lry_python_projects/LryAlienInvasion/images/ship.bmp')
        self.rect = self.image.get_rect()
        #对于每艘新飞船，都将其放在屏幕地步的中央
        self.rect.midbottom = self.screen_rect.midbottom

        #在飞船的属性x中存储小数值  
        self.x = float(self.rect.x)
        #移动标志
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right:
            self.x  +=  self.settings.ship_speed
        if self.moving_left:
            self.x  -=  self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self):
        """在指定位置绘制飞船"""
        self.screen.blit(self.image,self.rect)