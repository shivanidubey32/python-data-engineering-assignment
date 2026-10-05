import json


def load_json(filename):

    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)

    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

    except json.JSONDecodeError:
        print(f"Error: {filename} contains invalid JSON.")
        return []


def user_analysis(users):

    total_users = len(users)

    companies = set()

    for user in users:
        companies.add(user["company"])

    unique_companies = len(companies)

    sorted_companies = sorted(companies)
    top_5_companies = sorted_companies[:5]

    print("\nUSER ANALYSIS")
    print("-" * 40)

    print("Total Users:", total_users)

    print("Unique Companies:", unique_companies)

    print("\nTop 5 Companies Alphabetically:")

    for company in top_5_companies:
        print(company)


def book_analysis(books):

    prices = []

    for book in books:
        price = float(book["price"].replace("£", ""))
        prices.append(price)

    average_price = sum(prices) / len(prices)

    highest_rating = max(book["rating"] for book in books)

    highest_rated_books = []

    for book in books:
        if book["rating"] == highest_rating:
            highest_rated_books.append(book["title"])

    rating_counts = {
        1: 0,
        2: 0,
        3: 0,
        4: 0,
        5: 0
    }

    for book in books:
        rating_counts[book["rating"]] += 1

    print("\nBOOK ANALYSIS")
    print("-" * 40)

    print("Average Price: £{:.2f}".format(average_price))

    print("\nHighest Rating:", highest_rating)

    print("Highest Rated Books:")

    for title in highest_rated_books:
        print(title)

    print("\nNumber of Books in Each Rating Category:")

    for rating in rating_counts:
        print(
            "Rating",
            rating,
            ":",
            rating_counts[rating],
            "books"
        )


def main():

    users = load_json("users.json")
    books = load_json("books.json")

    if not users:
        print("No user data available.")
        return

    if not books:
        print("No book data available.")
        return

    user_analysis(users)

    book_analysis(books)


if __name__ == "__main__":
    main()
    