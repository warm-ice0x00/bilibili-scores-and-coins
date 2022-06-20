import csv

import requests


def get_bangumi_info(session: requests.Session, media_id: int) -> dict:
    return session.get(
        "https://api.bilibili.com/pgc/view/web/season",
        params={"season_id": str(media_id)},
        headers={
            "User-Agent": "Mozilla/5.0 (compatible; bingbot/2.0; +http://www.bing.com/bingbot.htm)",
        },
    ).json()


START, END = 1, 41790
with open(
    f"scores-ss{START}-ss{END}.csv", "w", encoding="utf8", newline=""
) as file_out:
    writer = csv.writer(file_out)
    writer.writerow(
        (
            "season_id",
            "media_id",
            "title",
            "is_finish",
            "score",
            "coins",
            "danmakus",
            "favorite",
            "favorites",
            "likes",
            "reply",
            "share",
            "views",
        )
    )
    session = requests.Session()
    for media_id in range(START, END + 1):
        print(media_id)
        response = get_bangumi_info(session, media_id)
        if (
            "result" in response
            and "rating" in response["result"]
            and "score" in response["result"]["rating"]
        ):
            writer.writerow(
                (
                    response["result"]["season_id"],
                    response["result"]["media_id"],
                    response["result"]["title"],
                    response["result"]["publish"]["is_finish"],
                    response["result"]["rating"]["score"],
                    response["result"]["stat"]["coins"],
                    response["result"]["stat"]["danmakus"],
                    response["result"]["stat"]["favorite"],
                    response["result"]["stat"]["favorites"],
                    response["result"]["stat"]["likes"],
                    response["result"]["stat"]["reply"],
                    response["result"]["stat"]["share"],
                    response["result"]["stat"]["views"],
                )
            )
