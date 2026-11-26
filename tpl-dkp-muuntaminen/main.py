import pandas as pd
from data_transform.transform import (
    clean_strings,
    handle_missing,
    remove_duplicates,
    fix_types_and_sort,
)


def main():
    file_path = "data/countries_noisy.json"
    save_path = "data/countries_cleaned.json"

    data = pd.read_json(file_path)

    print("Original data sample:")
    print(data.head(10))
    print(f"Row count before cleaning: {len(data)}")

    # Suorittaa kaikki siivousvaiheet peräkkäin
    data = clean_strings(data)
    data = handle_missing(data)
    data = remove_duplicates(data)
    data = fix_types_and_sort(data)

    data.to_json(save_path, orient="records", indent=4, force_ascii=False)

    print("Cleaned data sample:")
    print(data.head(10))
    print(f"Row count after cleaning: {len(data)}")


if __name__ == "__main__":
    main()
