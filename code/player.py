from settings import *

class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups, collision_sprites):
        super().__init__(groups)
        self.image = pygame.image.load(join("images", "player", "down", "0.png")).convert_alpha()
        self.rect = self.image.get_frect(center=pos)

        # movement
        self.speed = 300
        self.direction = pygame.Vector2()
        self.collision_sprites = collision_sprites

    def input(self):
        keys = pygame.key.get_pressed()
        # int() is not necessary, but for comprehension, i will put it
        self.direction.x = int(keys[pygame.K_d]) - int(keys[pygame.K_q])
        self.direction.y = int(keys[pygame.K_s]) - int(keys[pygame.K_z])
        # normalize
        self.direction = self.direction.normalize() if self.direction != pygame.Vector2() else self.direction

    def move(self, delta_time):
        self.rect.x += self.direction.x * self.speed * delta_time
        self.collision("horizontal")
        self.rect.y += self.direction.y * self.speed * delta_time
        self.collision("vertical")

    def collision(self, direction):
        for sprite in self.collision_sprites:
            if sprite.rect.colliderect(self.rect):
                if direction == 'horizontal':
                    if self.direction.x > 0: self.rect.right = sprite.rect.left
                    if self.direction.x < 0: self.rect.left = sprite.rect.right
                else:
                    if self.direction.y < 0: self.rect.top = sprite.rect.bottom
                    if self.direction.y > 0: self.rect.bottom = sprite.rect.top

    def update(self, delta_time):
        self.input()
        self.move(delta_time)
