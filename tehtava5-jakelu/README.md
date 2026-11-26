HUOM! jakelu kohta b) muokkailtu näyttämään countries_cleaned.json tehtäväosiosta muuntaminen.

1. Sisäänluku (API -> JSON)
   JSONPlaceholder API
     ──> tpl-dkp-sisaanluku/client/api_client.py (haku)
     ──> tpl-dkp-sisaanluku/utils/validators.py (validointi)
     ──> tpl-dkp-sisaanluku/main.py
     ──> tpl-dkp-sisaanluku/data/posts.json

2. Muuntaminen (Raaka JSON -> Puhdistettu JSON)
   tpl-dkp-muuntaminen/data/countries_noisy.json (262 riviä)
     ──> tpl-dkp-muuntaminen/data_transform/transform.py (siivous, NA-poisto, duplikaatit, tyypit & järjestys)
     ──> tpl-dkp-muuntaminen/main.py
     ──> tpl-dkp-muuntaminen/data/countries_cleaned.json (241 riviä)

3. Varastointi (Sanakirja -> SQLite -> Kysely)
   Kirjadata (main.py)
     ──> tpl-dkp-varastointi/db/database.py (create_db, add_data, query_data)
     ──> tpl-dkp-varastointi/sqlite_books.db (books-taulu)
     ──> tpl-dkp-varastointi/main.py (Top 5 kirjaa DataFramena konsoliin)

4. Jakelu (API & selainkäyttöliittymä)
   a) FastAPI:
      tehtava5-jakelu/fastapi/main.py ──> http://127.0.0.1:8000/ (ja /items/{item_id}, /docs)
   b) Streamlit:
      tpl-dkp-muuntaminen/data/countries_cleaned.json
        ──> tehtava5-jakelu/streamlit/app.py (Path-polku + pandas)
        ──> http://localhost:8501/ (slider, taulukko, pylväskaavio)