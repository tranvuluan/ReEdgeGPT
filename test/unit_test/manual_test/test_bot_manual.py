import asyncio
import json
from pathlib import Path

from re_edge_gpt import Chatbot
from re_edge_gpt import ConversationStyle


# If you are using jupyter pls install this package
# from nest_asyncio import apply


async def test_ask() -> None:
    bot = None
    try:
        cookies: list[dict] = json.loads(open(
            str(Path(str(Path.cwd()) + "/bing_cookies.json")), encoding="utf-8").read())
        bot = await Chatbot.create(cookies=cookies)
        response = await bot.ask(
            prompt=r"""HELLO""",
            conversation_style=ConversationStyle.balanced,
            simplify_response=True
        )
        # If you are using non ascii char you need set ensure_ascii=False
        print(json.dumps(response, indent=2, ensure_ascii=False))
        # Raw response
        # print(response)
        assert response
    except Exception as error:
        raise
    finally:
        if bot is not None:
            await bot.close()


if __name__ == "__main__":
    # If you are using jupyter pls use nest_asyncio apply()
    # apply()
    try:
        loop = asyncio.get_running_loop()
    except RuntimeError:
        loop = asyncio.get_event_loop()
    loop.run_until_complete(test_ask())
