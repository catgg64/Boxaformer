import pygame
import player
import solid_objects

pygame.init()

class Boxaformer:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 400
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        pygame.display.set_caption('Boxaformer')
        self.clock = pygame.time.Clock()
        self.internal_surface = pygame.Surface((self.screen_width * 4, self.screen_height * 4))
        self.running = True

        self.solid_object_list = []
        self.tilesize = 64
        self.world = [
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0 ,0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 2, 2, 0, 0, 0, 0, 0 ,0, 0, 0],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ,1, 1, 1],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ,0, 0, 0]
        ]

        self.viewportx = 0
        self.viewporty = 0

        #self.player = player.Player(self.screen_width / 2, self.screen_height / 2)
        self.player = player.Player(100, 100)

        self.box_1 = solid_objects.Block(100, 200, 64, 64, self.solid_object_list)

        self.space_just_down = False
        
        for row_idx, row in enumerate(self.world):
            for tile_idx, tile in enumerate(row):
                x = tile_idx * 64
                y = row_idx * 64
                if tile == 1:
                    solid_objects.Block(x, y, 64, 64, self.solid_object_list)
                if tile == 2:
                    solid_objects.Wall(x, y, 64, 64, self.solid_object_list)


    def _event_handling(self, running):
        running = running
        space_down = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    space_down = True
        
        return running, space_down

    def _check_for_top_rect_collision_on_all_blocks(self, solid_object_list, player_rect) -> bool:
        for block in solid_object_list:
            if block.check_for_top_rect_collision(player_rect):
                return True
        return False

    def update(self):
        self.running, self.space_just_down = self._event_handling(self.running)

        self.internal_surface.fill("cadetblue1")

        self.keys = pygame.key.get_pressed()

        if self.player.rect.x > self.screen_width / 2:
            self.viewportx = -1 * self.player.rect.x + self.screen_width / 2
        if self.player.rect.y > self.screen_height / 2:
            self.viewporty = -1 * self.player.rect.y + self.screen_height / 2

        self.player.update(self.internal_surface, self.solid_object_list, self._check_for_top_rect_collision_on_all_blocks(self.solid_object_list, self.player.rect))
        self.player.move(self.keys, self.space_just_down)

        for solid_object in self.solid_object_list:
            solid_object.update(self.internal_surface)

        self.space_just_down = False

        self.screen.blit(self.internal_surface, (self.viewportx, self.viewporty))
        self.clock.tick(60)
        pygame.display.update()

boxaformer = Boxaformer()

while boxaformer.running:
    boxaformer.update()
