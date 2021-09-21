import json

from LOLcard import riot, console, graphics, exceptions

allowed_queueType = ['솔랭', '자랭', '팀랭', '롤체']


def create_card(nickname, queue_type):
    if queue_type not in allowed_queueType:
        return

    try:
        lol_id = riot.get_player_id(nickname)
        tft_id = riot.get_tft_id(nickname)
        stat = riot.get_player_stat(lol_id, tft_id)
    except exceptions.UserNotFoundException:
        return graphics.draw_error("그런 유저는 없읍니다")
    except exceptions.UnauthorizedException:
        return graphics.draw_error("서버와 통신할 수 없읍니다")

    print(json.dumps(stat, indent=1))

    stat_solo = stat['RANKED_SOLO_5x5'] if 'RANKED_SOLO_5x5' in stat else None
    stat_flex = stat['RANKED_FLEX_SR'] if 'RANKED_FLEX_SR' in stat else None
    stat_tft = stat['RANKED_TFT'] if 'RANKED_TFT' in stat else None
    stat_turbo = stat['RANKED_TFT_TURBO'] if 'RANKED_TFT_TURBO' in stat else None

    exist_solo = True if stat_solo else False
    exist_flex = True if stat_flex else False
    exist_tft = True if stat_tft else False
    exist_turbo = True if stat_turbo else False

    if not queue_type:
        if exist_solo:
            return graphics.draw(stat_solo)
        elif exist_flex:
            return graphics.draw(stat_flex)
        else:
            return graphics.draw_error("랭크 기록이 없읍니다")
    elif queue_type == "솔랭":
        if exist_solo:
            return graphics.draw(stat_solo)
        else:
            return graphics.draw_error("솔로 랭크 기록이 없읍니다")
    elif queue_type == "자랭" or queue_type == "팀랭":
        if exist_flex:
            return graphics.draw(stat_flex)
        else:
            return graphics.draw_error("자유 랭크 기록이 없읍니다")
    elif queue_type == "롤체":
        if exist_tft:
            return graphics.draw(stat_tft)
        else:
            return graphics.draw_error("롤체 랭크 기록이 없읍니다")
    else:
        return


if __name__ == '__main__':
    print(console.MAIN)
    nickname = input()
    create_card(nickname)