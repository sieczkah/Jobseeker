import requests
from bs4 import BeautifulSoup


class StatusCodeException(Exception):
    def __init__(self, status_code) -> None:
        self.status_code = status_code
        super().__init__(f"Request failed. Status: {status_code}")


class WebScrapper:
    valid_domains = {
        "linkedin": (
            "div",
            ".show-more-less-html__markup show-more-less-html__markup--clamp-after-5",
        ),
    }

    def __init__(self, webpage_url, domain):
        self.webpage_url = webpage_url
        self.domain = domain
        self.scraped_element = None

    def get_domain_selectors(self, domain) -> list | None:
        if domain.lower() in self.valid_domains.keys():
            return self.valid_domains[domain.lower()]
        else:
            _domains = " ".join(key for key in self.valid_domains.keys())
            raise ValueError(
                f"Domain is invalid. Available domains for scrapping are {_domains}"
            )

    @staticmethod
    def get_response(url: str):
        response = requests.get(url)
        if response.status_code == 200:
            return response
        else:
            raise StatusCodeException(response.status_code)

    def scrape_webpage(self):
        element, element_selector = self.get_domain_selectors(self.domain)
        response = self.get_response(self.webpage_url)
        soup = BeautifulSoup(response.content, "html.parser")
        if element_selector.startswith("."):
            return soup.find(element, class_=element_selector.rstrip("."))
        elif element_selector.startswith("#"):
            return soup.find(element, class_=element_selector.rstrip("#"))
        else:
            raise ValueError("Wrong selector")

    def get_string(self):
        for br in self.scraped_element.find_all("br"):
            br.replace_with("\n")
        for li in self.scraped_element.find_all("li"):
            li.insert_before("-")
            li.insert_after("\n")
        return self.scraped_element.get_text()


scraper = WebScrapper("https://www.linkedin.com/jobs/view/3601965896", "linkediN")
scraper.scrape_webpage()
print(scraper.get_string())
