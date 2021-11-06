from logging import Logger
from services import BinanceScraper, queue
from load_config import *

def main(configs):
    scraper = BinanceScraper()
    last_article_id = 72913
    new_coins = scraper.get_latest_coins(last_article_id)
    Logger.debug(f"New coins: {', '.join(new_coins)}")
    with queue(configs["queue"]) as q:
        for coin in new_coins:
            Logger.info(f"Pushing {coin} to queue")
            q.push(coin)


if __name__ == '__main__':
    Logger.info("Scanning announcements...")
    configs = load_config("config.yml")
    main(configs)