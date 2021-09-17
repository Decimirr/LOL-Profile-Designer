import io

from PIL import Image, ImageFont, ImageDraw
from LOLcard import colors, riot

font_tier = ImageFont.truetype('LOLcard/fonts/NanumSquareEB.ttf', 45)
font_lp = ImageFont.truetype('LOLcard/fonts/NanumSquareR.ttf', 15)
font_name = ImageFont.truetype('LOLcard/fonts/NanumSquareB.ttf', 20)
font_background = ImageFont.truetype('LOLcard/fonts/NanumSquareEB.ttf', 100)

font_error = ImageFont.truetype('LOLcard/fonts/NanumSquareB.ttf', 30)


queue_type_text = {
    "RANKED_SOLO_5x5": "SOLO",
    "RANKED_FLEX_SR": "FLEX",
}


def draw(data):
    color_background = colors.color_background[data["tier"]]
    card = draw_gradient(360, 150, color_background[0], color_background[1])
    edge_rounder(card, 18)

    canvas = Image.new("RGBA", (370, 160), "black")
    edge_rounder(canvas, 20)
    canvas.paste(card, (5, 5), card)

    canvas = draw_text_center(canvas, queue_type_text[data["queueType"]], font_background, (0, -10), alpha=70)

    canvas = draw_text_center(canvas, riot.tier_text(data), font_tier, (0, -30))
    lp_text = str(data["leaguePoints"]) + "LP"
    win_lose_text = str(data["wins"]) + "W - " + str(data["losses"]) + "L"
    canvas = draw_text_center(canvas, lp_text + " / " + win_lose_text, font_lp, (0, 5))
    canvas = draw_text_center(canvas, data["summonerName"], font_name, (0, 30))

    arr = io.BytesIO()
    canvas.save(arr, format="PNG")
    arr.seek(0)
    return arr


def draw_gradient(width, height, start_color, end_color):
    image = Image.new("RGBA", (width, height), 0xffffff00)

    for y in range(height):
        for x in range(width):
            p = (width * x + height * y) / (width**2 + height**2)
            image.putpixel((x, y), lerp(start_color, end_color, p))
    return image


def edge_rounder(image, r):
    for y in range(r):
        for x in range(r):
            if ((x-r)**2 + (y-r)**2) > (r+1)**2:
                image.putpixel((x, y), (0, 0, 0, 0))
                image.putpixel((image.size[0]-1 - x, y), (0, 0, 0, 0))
                image.putpixel((x, image.size[1]-1 - y), (0, 0, 0, 0))
                image.putpixel((image.size[0]-1 - x, image.size[1]-1 - y), (0, 0, 0, 0))
    return image


def draw_text_center(image, msg, font, pos, alpha=255):
    text = Image.new("RGBA", image.size, (255, 255, 255, 0))
    draw = ImageDraw.Draw(text)
    text_width, text_height = draw.textsize(msg, font)
    position = (image.size[0] - text_width)/2 + pos[0], (image.size[1] - text_height)/2 + pos[1]
    draw.text(position, msg, fill=(255, 255, 255, alpha), font=font)
    combine = Image.alpha_composite(image, text)
    return combine


def draw_error(errormsg):
    card = Image.new("RGBA", (360, 150), "gray")
    edge_rounder(card, 18)

    canvas = Image.new("RGBA", (370, 160), "black")
    edge_rounder(canvas, 20)
    canvas.paste(card, (5, 5), card)

    canvas = draw_text_center(canvas, "ERROR", font_background, (0, -10), alpha=70)
    canvas = draw_text_center(canvas, errormsg, font_error, (0, 0))

    arr = io.BytesIO()
    canvas.save(arr, format="PNG")
    arr.seek(0)
    return arr


def lerp(start, end, p):
    return tuple(map(int, ((1-p) * start[0] + p * end[0], (1-p) * start[1] + p * end[1], (1-p) * start[2] + p * end[2], (1-p) * start[3] + p * end[3])))
