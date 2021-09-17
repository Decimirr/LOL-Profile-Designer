import json

from LOLcard import riot, console, graphics


def create_card(nickname, queue_type=""):
    try:
        playerData = riot.get_player_id(nickname)
        stat = riot.get_player_stat(playerData['id'])
    except:
        return graphics.draw_error("그런 유저는 없읍니다")

    print(json.dumps(stat, indent=4))

    stat_solo = [x for x in stat if x['queueType'] == 'RANKED_SOLO_5x5']
    stat_flex = [x for x in stat if x['queueType'] == 'RANKED_FLEX_SR']

    exist_solo = True if stat_solo else False
    exist_flex = True if stat_flex else False

    if not queue_type:
        if exist_solo:
            return graphics.draw(stat_solo[0])
        elif exist_flex:
            return graphics.draw(stat_flex[0])
        else:
            return graphics.draw_error("랭크 기록이 없읍니다")
    elif queue_type == "솔랭":
        if exist_solo:
            return graphics.draw(stat_solo[0])
        else:
            return graphics.draw_error("솔로 랭크 기록이 없읍니다")
    elif queue_type == "자랭" or queue_type == "팀랭":
        if exist_flex:
            return graphics.draw(stat_flex[0])
        else:
            return graphics.draw_error("자유 랭크 기록이 없읍니다")
    else:
        return


if __name__ == '__main__':
    print(console.MAIN)
    nickname = input()
    create_card(nickname)