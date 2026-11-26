import pandas as pd
from client.api_client import fetch_data
from utils.validators import validate_items


def main():

    api_url = "https://jsonplaceholder.typicode.com/posts"

    print("Fetching paginated data…")
    items = fetch_data(api_url)
    if not items:
        print("Failed to fetch data.")
        return

    print("Validating items…")
    try:
        validate_items(items)
    except ValueError as e:
        print(f"Validation failed: {e}")
        return

    json_file_path = "data/posts.json"
    df = pd.DataFrame(items)
    df.to_json(json_file_path)
    print(f"Data saved to {json_file_path}")


if __name__ == "__main__":
    main()