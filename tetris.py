"""
xTODO: set screen and split it into following areas:
      - information panel on left side (score, next piece, top score info)
      - playground where pieces will be flowing, size would be 10 x 20 play points, every play point will be 20x20
TODO: create play ground
TODO: release square shape and animate it to the ground
TODO: move shape within playground - left, right, rotate, drop piece
TODO: generalize square shape and add following pieces (all consist from four parts):
      - I piece
      - L piece (both right and left oriented)
      - T piece
"""
import sys
import pygame

pygame.init()

class PlayGround(object):
    def __init__(self, surface, x, y, width, height, tile_size):
        self._rect = pygame.Rect(x, y, width, height)
        self._tile_size = tile_size
        self._surface = surface
        self._back_color = pygame.Color('black')
        w, h = tile_size
        self._area = self._create_area((width / w, height / h))

    def _create_area(self, size):
        w, h = size
        result = []
        for j in xrange(h):
            row = []
            for i in xrange(w):
                row.append(0)
            result.append(row)
        return result

    def detect_collision(self, shape):
        pass


    def draw_tile(self, x, y, color):
        tw, th = self._tile_size
        rect = pygame.Rect(x * tw, y * th, tw, th)
        rect = rect.move(self._rect.left, self._rect.top)
        pygame.draw.rect(self._surface, color, rect)

    def update(self):
        pygame.draw.rect(self._surface, self._back_color, self._rect)
        self._dbg_draw_tiles()

    def _dbg_draw_tiles(self):
        tw, th = self._tile_size
        tile_no = 0
        color = pygame.Color(20, 20, 20)
        for j in xrange(th):
            for i in xrange(tw):
                if tile_no % 2 == 0:
                    self.draw_tile(i, j, color)
                tile_no += 1
            tile_no += 1


class InfoPanel(object):
    def __init__(self, surface, x, y, width, height):
        self._rect = pygame.Rect(x, y, width, height)
        self._surface = surface
        self._back_color = pygame.Color('blue')

    def update(self):
        pygame.draw.rect(self._surface, self._back_color, self._rect)


def set_screen(width, height):
    surface = pygame.display.set_mode((width, height), 0)
    return surface
    
def refresh(screen, state):
    state['clock'].tick(25)
    pygame.display.flip()

def draw_background(screen, state):
    state['infopanel'].update()
    state['playground'].update()
    

def event_processing(state):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_UP: pass
            elif event.key == pygame.K_DOWN: pass
            elif event.key == pygame.K_LEFT: pass
            elif event.key == pygame.K_RIGHT: pass
            else:
                sys.exit()
        elif event.type == pygame.QUIT:
            sys.exit()

def main():
    screen = set_screen(300, 400)
    state = {
        'clock': pygame.time.Clock(),
        'infopanel': InfoPanel(screen, 0, 0, 100, 400),
        'playground': PlayGround(screen, 100, 0, 200, 400, (20, 20)),
    }
    
    while 1:
        event_processing(state)
        draw_background(screen, state)
        refresh(screen, state)


if __name__ == "__main__":
    main()
