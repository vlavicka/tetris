from tools import area

play_pieces = {
        'square': ((0, 0), (0, 1), (1, 0), (1, 1)),
    }

class PlayGroundModel(object):
    EMPTY_TILE = 0
    def __init__(self, sx, sy):
        self._area = area.Area(sx, sy, PlayGroundModel.EMPTY_TILE)
        self._current_piece = None

    @property
    def width(self):
        return self._area.width

    @property
    def height(self):
        return self._area.height

    def set_piece(self, name):
        self._current_piece = play_pieces.get(name, None)

    def set_color(self, x, y, value):
        self._area[x, y] = value
    
    def get_color(self, x, y):
        return self._area[x, y]

    def get_filled(self):
        result = []
        for y in range(self._area.height):
            is_filled = True
            for x in range(self._area.width):
                if self._area[x, y] == PlayGroundModel.EMPTY_TILE:
                    is_filled = False
                    break
            if is_filled:
                result.append(y)
        return result

    def dump_str(self):
        result = []
        result.append('+' + '-' * self._area.width + '+')
        for y in range(self._area.height):
            line = ''
            for x in range(self._area.width):
                line += ' ' if self._area[x, y] == PlayGroundModel.EMPTY_TILE else 'x'
            result.append('|' + line + '|')
        result.append('+' + '-' * self._area.width + '+')
        return '\n'.join(result)

    def dump_console(self):
        """ Dump playground into console - output is colored """
        raise NotImplementedError
