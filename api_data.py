import requests
import json


API_URL = "https://jsonplaceholder.typicode.com/users"


def fetch_users():
    try:
        response = requests.get(API_URL, timeout=10)
        response.raise_for_status()

        users = response.json()
        return users

    except requests.exceptions.RequestException as e:
        print("Error while fetching API data:", e)
        return []


def process_users(users):
    processed_users = []

    for user in users:
        user_data = {
            "name": user["name"],
            "email": user["email"],
            "company": user["company"]["name"]
        }

        processed_users.append(user_data)

    return processed_users


def save_users(users):
    with open("users.json", "w", encoding="utf-8") as file:
        json.dump(users, file, indent=4)


def main():

    users = fetch_users()

    if not users:
        print("No user data found.")
        return

    print("Total Users:", len(users))

    print("\nUser Details:")
    for user in users:
        print("Name:", user["name"])
        print("Username:", user["username"])
        print("Email:", user["email"])
        print("Company:", user["company"]["name"])
        print("-" * 40)

    company_names = []

    for user in users:
        company_names.append(user["company"]["name"])

    print("\nCompany Names:")
    for company in company_names:
        print(company)

    processed_users = process_users(users)

    save_users(processed_users)

    print("\nProcessed user data saved to users.json")


if __name__ == "__main__":
    main()