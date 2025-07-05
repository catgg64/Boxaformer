import pygame

class Block:
    def __init__(self, pos_x, pos_y, size_x, size_y, solid_object_list):
        self.rect = pygame.Rect(pos_x, pos_y, size_x, size_y)
        self.top_rect = pygame.Rect(pos_x, pos_y, size_x, 5)
        solid_object_list.append(self)
        
    def update(self, internal_surface):
        pygame.draw.rect(internal_surface, 'gray', self.rect)
        pygame.draw.rect(internal_surface, 'antiquewhite4', self.top_rect)

    def check_for_top_rect_collision(self, player_rect):
        if self.top_rect.colliderect(player_rect):
            return True
        return False
    
    def check_for_rect_collision(self, player_rect):
        if self.rect.colliderect(player_rect):
            return True
        return False

class Wall:
    def __init__(self, pos_x, pos_y, size_x, size_y, solid_object_list):
        self.rect = pygame.Rect(pos_x, pos_y, size_x, size_y)
        solid_object_list.append(self)
        
    def update(self, internal_surface):
        pygame.draw.rect(internal_surface, 'gray', self.rect)
        
    def check_for_top_rect_collision(self, player_rect):
        return False
    
    def check_for_rect_collision(self, player_rect):
        if self.rect.colliderect(player_rect):
            return True
        return False