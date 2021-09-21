def to_colortuple(value):
    return (value >> 16) % 0xFF, (value >> 8) % 0xFF, value % 0xFF, 0xFF


def to_colortupleA(value):
    return (value >> 24) % 0xFF, (value >> 16) % 0xFF, (value >> 8) % 0xFF, value % 0xFF


color_outline = to_colortuple(0x000000FF)

color_background = {
    'IRON': ((189, 195, 199, 255), (44, 62, 80, 255)),
    'BRONZE': ((183, 152, 145, 255), (148, 113, 107, 255)),
    'SILVER': ((96, 108, 136, 255), (63, 76, 107, 255)),
    'GOLD': ((237, 141, 30, 255), (245, 200, 0, 255)),
    'PLATINUM': ((0, 176, 155, 255), (150, 201, 61, 255)),
    'DIAMOND': ((0, 180, 219, 255), (0, 131, 176, 255)),
    'MASTER': ((170, 7, 107, 255), (97, 4, 95, 255)),
    'GRANDMASTER': ((211, 16, 39, 255), (234, 56, 77, 255)),
    'CHALLENGER': (to_colortuple(0xD4D66D), to_colortuple(0xEEEFA2)),

#롤체 초고속 전용
    'GREY': ((), ()),
    'GREEN': ((), ()),
    'BLUE': ((), ()),
    'PURPLE': ((), ()),
    'HYPER': ((), ()),
}

