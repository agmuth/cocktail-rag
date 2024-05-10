import string
from concurrent.futures import ThreadPoolExecutor
import re
from lxml import etree

import requests
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
from tenacity import retry, wait_exponential

from src.settings import BASE_SETTINGS


class CocktailFriendScraper:
    base_url = "https://cocktailfriend.com/"
    data_dir = BASE_SETTINGS.DATA_DIR

    @classmethod
    def _get_cocktails_to_scrap(cls):
        url_extension = "drinklists/alldrinks/{page}"
        pages = ["numberdrinks.php"] + [
            f"{x}.php" if x != "a" else "" for x in string.ascii_lowercase
        ]
        ua = UserAgent()
        cocktail_urls = list()
        for page in pages:
            header = {"User-Agent": str(ua.random)}
            url = cls.base_url + url_extension.format(page=page)
            htmlContent = requests.get(url, headers=header)
            soup = BeautifulSoup(htmlContent.content, "html.parser")
            cocktail_urls += [
                cls.base_url + elem.a["href"]
                for elem in soup.find_all("td", class_="fs-6")
            ]
        return cocktail_urls

    @classmethod
    def scrape_cocktails(cls):
        cocktail_urls = cls._get_cocktails_to_scrap()

        with ThreadPoolExecutor() as executor:
            executor.map(cls.scrape_single_cocktail, cocktail_urls)

        # for cocktail_url in cocktail_urls:
        #     cls.scrape_single_cocktail(cocktail_url)

    @classmethod
    @retry(wait=wait_exponential(multiplier=1, min=1 / 64, max=8))
    def scrape_single_cocktail(cls, cocktail_url):
        cocktail_name = cocktail_url.split("&drink=")[-1]
        xpath_mappings = {
            "recipe": "/html/body/main/div[4]/div[3]/div/div[2]",
            "instructions": "/html/body/main/div[4]/div[4]/div[2]",
            "summary": "/html/body/main/div[4]/div[5]/div[1]/div[1]/div[2]",
            "shopping_list": "/html/body/main/div[4]/div[5]/div[2]/div[1]/div[2]",
        }
        
        ua = UserAgent()
        header = {"User-Agent": str(ua.random)}
        htmlContent = requests.get(cocktail_url, headers=header)
        soup = BeautifulSoup(htmlContent.content, "html.parser")
        dom = etree.HTML(str(soup))
        
        cocktail_text = [cocktail_name]
        
        for k, v in xpath_mappings.items():
            text = ''.join(dom.xpath(v)[0].itertext())
            text = text.splitlines()
            text = '\n'.join(x.strip() for x in text if x != '')
            cocktail_text.append(k)
            cocktail_text.append(text)
        
        with open(cls.data_dir.joinpath(f"{cocktail_name}.txt"), "w") as f:
            cocktail_text = "\n\n".join(cocktail_text)
            f.writelines(cocktail_text)
        


if __name__ == "__main__":
    CocktailFriendScraper.scrape_cocktails()
    
