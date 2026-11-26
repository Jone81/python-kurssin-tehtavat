import pandas as pd

def clean_strings(df: pd.DataFrame) -> pd.DataFrame:
    """Siivoa tekstisarakkeet poistamalla välilyönnit ja muuttamalla title-caseen."""
    df = df.copy()
    for col in ["name", "capital"]:
        if col in df.columns:
            df[col] = df[col].str.strip().str.title()
    return df


def handle_missing(df: pd.DataFrame) -> pd.DataFrame:
    """Korvaa puuttuvia arvoja kuvaavat merkkijonot pd.NA:lla, tulostaa määrät ja poistaa puuttuvat rivit."""
    df = df.copy()
    missing_values = ["N/A", "n/a", "NA", "na", "", "None", "null"]
    df = df.replace(missing_values, pd.NA)
    print("Missing values per column:")
    print(df.isna().sum())
    df = df.dropna()
    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    """Poista päällekkäiset rivit 'name'-sarakkeen perusteella."""
    df = df.copy()
    df = df.drop_duplicates(subset=["name"])
    return df


def fix_types_and_sort(df: pd.DataFrame) -> pd.DataFrame:
    """Muunna numeromuotoiset sarakkeet numeerisiksi ja järjestä nimen mukaan."""
    df = df.copy()
    if "population" in df.columns:
        df["population"] = pd.to_numeric(df["population"], errors="coerce")
    if "name" in df.columns:
        df = df.sort_values(by="name").reset_index(drop=True)
    return df


"""
Alla oleva lista määrittelee moduulin julkiset funktiot, eli mitkä funktionimet tuodaan mukaan, 
kun käytetään from module import * -syntaksia.
"""
__all__ = [
    "clean_strings",
    "handle_missing",
    "remove_duplicates",
    "fix_types_and_sort"
]
