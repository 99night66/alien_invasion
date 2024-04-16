import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    """管理⻜船所发射⼦弹的类"""
    def __init__(self, ai_game):
        """在飞船所处的位置创建⼀个子弹对象"""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # 在（0，0）处创建⼀个⼦弹，再设置正确的位置
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, 
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # 存储⽤⼩数表⽰的⼦弹位置。
        self.y = float(self.rect.y)

    def update(self):
        """向上移动子弹"""
        # 更新表⽰⼦弹位置的⼩数值。
        self.y -= self.settings.bullet_speed
        # 更新表⽰⼦弹的rect的位置。
        self.rect.y = self.y

    def draw_bullet(self):
        """在屏幕上绘制子弹"""
        pygame.draw.rect(self.screen, self.color, self.rect)
