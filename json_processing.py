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


def find_high_rated_books(books):
    print("\nBooks With Rating Greater Than 4")
    print("-" * 40)

    found = False

    for book in books:
        if book["rating"] > 4:
            print(book["title"])
            found = True

    if not found:
        print("No books found.")


def find_group_users(users):
    print("\nUsers Belonging to Companies Containing 'Group'")
    print("-" * 50)

    found = False

    for user in users:
        if "group" in user["company"].lower():
            print(user["name"], "-", user["company"])
            found = True

    if not found:
        print("No users found.")


def calculate_average_price(books):
    if not books:
        return 0

    prices = []

    for book in books:
        price = float(book["price"].replace("£", ""))
        prices.append(price)

    return sum(prices) / len(prices)


def create_report(users, books):

    average_price = calculate_average_price(books)

    report = {
        "total_users": len(users),
        "total_books": len(books),
        "average_price": round(average_price, 2)
    }

    with open("report.json", "w", encoding="utf-8") as file:
        json.dump(report, file, indent=4)

    return report


def main():

    # Load JSON files
    users = load_json("users.json")
    books = load_json("books.json")

    # C1
    print("Total Users:", len(users))
    print("Total Books:", len(books))

    # C2
    find_high_rated_books(books)

    # C3
    find_group_users(users)

    # C4
    report = create_report(users, books)

    print("\nCombined Report")
    print("-" * 40)
    print("Total Users:", report["total_users"])
    print("Total Books:", report["total_books"])
    print("Average Price:", report["average_price"])

    print("\nreport.json created successfully.")


if __name__ == "__main__":
    main()