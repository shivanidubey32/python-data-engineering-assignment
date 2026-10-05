import requests
from bs4 import BeautifulSoup
import json


BASE_URL = "https://books.toscrape.com/catalogue/page-{}.html"

RATING_MAP = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}


def scrape_books():

    books = []
    page = 1

    try:
        while len(books) < 20:

            url = BASE_URL.format(page)

            response = requests.get(url, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            book_items = soup.select("article.product_pod")

            if not book_items:
                break

            for book in book_items:

                title = book.select_one("h3 a")["title"]

                price = book.select_one(".price_color").text.strip()
                price = price.replace("Â", "")

                rating_word = book.select_one(
                    ".star-rating"
                )["class"][1]

                rating = RATING_MAP[rating_word]

                book_data = {
                    "title": title,
                    "price": price,
                    "rating": rating
                }

                books.append(book_data)

                if len(books) == 20:
                    break

            page += 1

        return books

    except requests.exceptions.RequestException as error:
        print("Error while accessing website:", error)
        return []


def analyze_books(books):

    prices = []

    for book in books:
        price = float(book["price"].replace("£", "").replace("A",""))
        prices.append(price)

    most_expensive = max(
        books,
        key=lambda book: float(book["price"].replace("£", ""))
    )

    least_expensive = min(
        books,
        key=lambda book: float(book["price"].replace("£", ""))
    )

    average_price = sum(prices) / len(prices)

    print("\nBook Analysis")
    print("-" * 40)

    print("Most Expensive Book:")
    print(most_expensive["title"])
    print(most_expensive["price"])

    print("\nLeast Expensive Book:")
    print(least_expensive["title"])
    print(least_expensive["price"])

    print("\nAverage Book Price:")
    print(f"£{average_price:.2f}")


def save_books(books):

    with open("books.json", "w", encoding="utf-8") as file:
        json.dump(books, file, indent=4)


def main():

    books = scrape_books()

    if not books:
        print("No books were collected.")
        return

    print("Total Books Scraped:", len(books))

    print("\nBook Details")
    print("-" * 40)

    for book in books:
        print("Title:", book["title"])
        print("Price:", book["price"])
        print("Rating:", book["rating"])
        print("-" * 40)

    analyze_books(books)

    save_books(books)

    print("\nData saved successfully to books.json")


if __name__ == "__main__":
    main()