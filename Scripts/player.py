import pygame

class Player:
    def __init__(self, pos_x, pos_y):
        self.rect = pygame.Rect(pos_x, pos_y, 64, 64)
        self.speedx = 5
        self.speedy = -5
        self.force = -5
        self.velocity = 10
        self.jump_timer = 0
        self.jump_lehgt = 10

    def _jump(self):
        self.velocity = -10

    def _check_for_top_rect_collision_on_all_blocks(self, solid_object_list, player_rect) -> bool:
        for block in solid_object_list:
            if block.check_for_top_rect_collision(player_rect):
                return True
        return False

    def _check_for_rect_collision_on_all_blocks(self, solid_object_list, player_rect) -> bool:
        for block in solid_object_list:
            if block.check_for_rect_collision(player_rect):
                return True
        return False

    def update(self, internal_surface, solid_object_list, is_on_top):
        pygame.draw.rect(internal_surface, (255, 255, 255), self.rect)
        
        self.solid_object_list = solid_object_list
        self.is_on_top = is_on_top
        self.velocity += 0.75
        self.speedy += self.force
        self.jump_timer += 1
        
        if self.velocity > 10:
            self.velocity = 10

    def move(self, keys, space_just_pressed):
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speedx
            if self._check_for_rect_collision_on_all_blocks(self.solid_object_list, self.rect):
                self.rect.x -= self.speedx
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speedx
            if self._check_for_rect_collision_on_all_blocks(self.solid_object_list, self.rect):
                self.rect.x += self.speedx
        
        self.rect.y += self.velocity

        if self._check_for_top_rect_collision_on_all_blocks(self.solid_object_list, self.rect):
            self.rect.y -= self.velocity
            self.is_on_top = True

        if self.is_on_top:
            self.jump_timer = 0

        if space_just_pressed and self.is_on_top:
            self._jump()

        if not self.is_on_top and keys[pygame.K_SPACE] and self.jump_timer < self.jump_lehgt:
            if not self._check_for_rect_collision_on_all_blocks(self.solid_object_list, self.rect):
                self._jump()

