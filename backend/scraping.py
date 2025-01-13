import requests
from bs4 import BeautifulSoup
import re
import datetime
from playwright.sync_api import sync_playwright
from playwright_stealth import stealth_sync

def scrape_all_products(products):
    results = []
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36") 
        page = context.new_page()

        for product in products:
            name = product.get("Name")
            company = product.get("Company")
            url = product.get("URL")
            
            match company:
                case "Harvey Norman":
                    # price = get_harvey_norman_au_price(page, url)
                    price = "N/A Harvey Norman Got Bot Detection"
                case "David Jones":
                    price = get_david_jones_price(page, url)
                case "Myer":
                    price = get_myer_price(page, url)
                case "JB HI FI":
                    price = get_jb_price(page, url)
                case "The Good Guys":
                    price = get_good_guys_price(page, url)
                case "Kitchen Warehouse":
                    price = get_kitchen_warehouse_price(page, url)
                case "Harvey Norman NZ":
                    price = get_harvey_norman_nz_price(page, url)
                case "Stevens NZ":
                    price = get_stevens_price(page, url)
                case _:
                    price = "Company Not Avaliable - Please contact admin"

            results.append({
                "Name": name,
                "Company": company,
                "URL": url,
                "Price": price,
                "Date": datetime.datetime.now()
            })
        
        browser.close()
    return results

def get_single_price(url, company):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36") 
        page = context.new_page()
        match company:
            case "Harvey Norman":
                price = get_harvey_norman_au_price(page, url)
            case "David Jones":
                price = get_david_jones_price(page, url)
            case "Myer":
                price = get_myer_price(page, url)
            case "JB HI FI":
                price = get_jb_price(page, url)
            case "The Good Guys":
                price = get_good_guys_price(page, url)
            case "Kitchen Warehouse":
                price = get_kitchen_warehouse_price(page, url)
            case "Harvey Norman NZ":
                price = get_harvey_norman_nz_price(page, url)
            case "Stevens NZ":
                price = get_stevens_price(page, url)
            case _:
                price = "Company Not Avaliable - Please contact admin"
        browser.close()
    return price
    

def get_harvey_norman_au_price(playwright_page, url): #Bot Detection
    try:
            # headers = {
            #     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36",
            #     "Accept-Language": "en-US,en;q=0.9",
            #     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
            #     "Referer": "https://www.google.com/"
            # }
            # playwright_page.context.set_extra_http_headers(headers)
            stealth_sync(playwright_page)

            playwright_page.goto(url, wait_until="domcontentloaded", timeout=20000)
            playwright_page.wait_for_selector("span.PriceCard_sf-price-card__price__xQHV2", timeout=20000) 

            price_element = playwright_page.locator("span.PriceCard_sf-price-card__price__xQHV2")
            price = price_element.text_content().strip()

            return price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "N/A"


def get_david_jones_price(playwright_page, url):
    try:
        playwright_page.goto(url, wait_until="networkidle", timeout=10000)
        playwright_page.wait_for_selector("div.pricing", timeout=10000)

        price_element = playwright_page.locator("p.price.now span.price-display")
        price = price_element.text_content().strip()

        return price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "N/A"


def get_myer_price(playwright_page, url):
    try:
        playwright_page.goto(url, wait_until="networkidle", timeout=10000)
        playwright_page.wait_for_selector("div.css-1y4cb6d", timeout=10000)

        price_element = playwright_page.locator("p.css-1mxfaop").first
        price = price_element.text_content().strip()

        return price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "N/A"

def get_jb_price(playwright_page, url):
    try:
        playwright_page.goto(url, wait_until="domcontentloaded", timeout=10000)
        playwright_page.wait_for_selector("span.PriceFont_fontStyle__w0cm2q1.PriceTag_actual__1eb7mu9q", timeout=10000)

        price = playwright_page.locator("span.PriceFont_fontStyle__w0cm2q1.PriceTag_actual__1eb7mu9q").text_content().strip()

        return price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "N/A"

def get_good_guys_price(playwright_page, url):
    try:
        playwright_page.goto(url, wait_until="domcontentloaded", timeout=10000)
        price = playwright_page.locator("#offerPrice_3074457345621785168").text_content().strip()

        return price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "N/A"

def get_kitchen_warehouse_price(playwright_page, url):
    try:
        playwright_page.goto(url, wait_until="networkidle", timeout=20000)
        playwright_page.wait_for_selector("span.Typography_display_XS__SVpDH.text-base-black", timeout=20000)

        price = playwright_page.locator("span.Typography_display_XS__SVpDH.text-base-black").text_content().strip()

        return price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "N/A"

def get_harvey_norman_nz_price(playwright_page, url):
    try:
        playwright_page.goto(url, wait_until="domcontentloaded", timeout=10000)
        price = playwright_page.locator("#sec_discounted_price_77844").text_content().strip()
        return price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "N/A"

def get_stevens_price(playwright_page, url):
    try:
        playwright_page.goto(url, wait_until="domcontentloaded", timeout=10000)
        playwright_page.wait_for_selector("div.price__sale-container", timeout=10000)
        price = playwright_page.locator("span.price__now").text_content().strip()
        return price
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return "N/A"