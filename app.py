import pandas as pd
import plotly.express as px
import streamlit as st


DATA_FILES = {
    "Ryby 🐟🐠🐡": "data/fish_data.csv",
    "Tučňáci 🦆🦅🦉": "data/penguins_size_nona.csv",
}


def app():
    st.title("PyDataLadies Dashboard")

    # vstup 1: výběr datové sady
    dataset = st.selectbox("Dataset", DATA_FILES.keys())
    data_file_path = DATA_FILES[dataset]

    # vlastní načtení dat
    data = pd.read_csv(data_file_path)

    # vstup 2: výběr parametrů scatter matrix
    dimensions = st.multiselect("Osy pro scatter matrix", list(data.columns), default=list(data.columns))
    color = st.selectbox("Barva", data.columns)
    opacity = st.slider("Průhlednost", 0.0, 1.0, 0.5)

    # scatter matrix plot
    st.write(px.scatter_matrix(data, dimensions=dimensions, color=color, opacity=opacity))

    # pomocí sloupců poskládáme vstupní widgety vedle sebe
    col1, col2, col3 = st.columns(3, vertical_alignment="bottom")
    with col1:
        # výběr sloupce pro zobrazení rozdělení dat
        column_for_analysis = st.selectbox("Sloupec pro analýzu rozdělení", data.columns)
    with col2:
        # výběr funkce pro zobrazení rozdělovací funkce
        dist_plot_type = st.selectbox("Typ grafu", ["box", "histogram", "violin"])
    with col3:
        # volba, jestli se má použít barva
        use_color = st.checkbox(f"Použít barvu ({color})")

    if dist_plot_type == "box":
        st.write(px.box(data, x=column_for_analysis, color=color if use_color else None))
    elif dist_plot_type == "histogram":
        st.write(px.histogram(data, x=column_for_analysis, color=color if use_color else None))
    elif dist_plot_type == "violin":
        st.write(px.violin(data, x=column_for_analysis, color=color if use_color else None))
    else:
        st.error("Neplatný typ grafu")


if __name__ == "__main__":
    app()
