from logger import logger
from services import BinanceScraper, CoinService, queue
from load_config import *

def main(configs):
    scraper = BinanceScraper(CoinService())
    last_article_id = 0
    new_coins = scraper.get_latest_coins(last_article_id)
    logger.debug(f"New coins: {', '.join(new_coins)}")
    #retry loop
    with queue(configs["queue"]) as q:
        for coin in new_coins:
            logger.info(f"Pushing {coin} to queue")
            q.push(coin)


if __name__ == '__main__':
    logger.info("Scanning announcements...")
    configs = load_config("config.yml")
    main(configs)