"""Versão web do catálogo de jogos.

Execute com: streamlit run app.py
"""

import json
from pathlib import Path

import streamlit as st


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "games.json"


@st.cache_data
def load_games():
    with DATA_FILE.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data if isinstance(data, list) else [data]


def cover_file(game):
    """Return the cover path only when it exists in the project."""
    cover = game.get("cover")
    if not cover:
        return None

    path = BASE_DIR / cover
    return path if path.is_file() else None


st.set_page_config(page_title="Game Catalog", page_icon="🎮", layout="wide")

st.title("🎮 My Game Catalog")
st.caption("Your game collection in just one website.")

games = load_games()

with st.sidebar:
    st.header("Filters")
    systems = sorted({game.get("system", "Not available") for game in games})
    genres = sorted({game.get("genre", "Not available") for game in games})
    statuses = sorted({game.get("status", "Not available") for game in games})

    chosen_systems = st.multiselect("System", systems)
    chosen_genres = st.multiselect("Genre", genres)
    chosen_statuses = st.multiselect("Status", statuses)
    search = st.text_input("Search by name.")


filtered_games = []
for game in games:
    if chosen_systems and game.get("system", "Not available") not in chosen_systems:
        continue
    if chosen_genres and game.get("genre", "Not available") not in chosen_genres:
        continue
    if chosen_statuses and game.get("status", "Not available") not in chosen_statuses:
        continue
    if search and search.casefold() not in game.get("name", "").casefold():
        continue
    filtered_games.append(game)

st.subheader(f"{len(filtered_games)} game(s) found.")

if not filtered_games:
    st.info("There is no game to the corresponding filter..")
else:
    for start in range(0, len(filtered_games), 4):
        columns = st.columns(4)
        for column, game in zip(columns, filtered_games[start : start + 4]):
            with column:
                cover = cover_file(game)
                if cover:
                    st.image(str(cover), use_container_width=True)
                else:
                    st.info("Capa ainda não adicionada")

                st.markdown(f"#### {game.get('name', 'Unnamed')}")
                st.write(f"**System:** {game.get('system', 'Not available')}")
                st.write(f"**Genre:** {game.get('genre', 'Not available')}")
                st.write(f"**Status:** {game.get('status', 'Not available')}")
                st.write(f"**Grade:** {game.get('grade', 'Not available')}")
