# PyDataLadies Dashboards

Materiály pro lekci o interaktivních vizualizacích a tvorbě dashboard aplikací.

## Příprava

1. Pokud nemáš, vytvořte si účet na GitHubu: https://github.com/signup
2. Použij svůj GitHub účet pro registraci na Streamlit Cloud: https://share.streamlit.io/signup
3. Nainstaluj si Git:
   * Nejjednodušší volba je [GitHub CLI](https://cli.github.com), podrobné instrukce k instalaci [zde](https://github.com/cli/cli?tab=readme-ov-file#installation), případně [Github Desktop](https://desktop.github.com/) pro grafické rozhraní.
   * Alternativní možnosti najdeš na https://www.atlassian.com/git/tutorials/install-git.
4. Udělej alespoň základní konfiguraci Gitu.
   * Pro GitHub CLI postupuj dle [instrukcí](https://cli.github.com/manual/).
     * Mělo by stačit spustit `gh auth login`.
   * Pokud používáte klienta v příkazovém řádku:
   ```
   git config --global user.name "Moje Jméno"
   git config --global user.email "muj@email.com"
   ```
   Instalaci ověříme v příkazové řádce pomocí:
   ```
   git config --list
   ```
   Mělo by se objevit něco na způsob
   ```
   user.name=Moje Jméno
   user.email=muj@email.com
   ```

Kdyby něco nefungovalo nebylo jasné, tak se hned ptejte v kanále [#poradna](https://pydata-kurz-praha.slack.com/archives/CSPRXPJGN).

## Materiály

1. [První část](notebooks/dashboardy-1.ipynb), pro zobrazení včetně interaktivních grafů: [nbviewer](https://nbviewer.jupyter.org/github/PyDataCZ/pydataladies-dashboard/blob/main/notebooks/dashboardy-1.ipynb).
2. [Druhá část](notebooks/dashboardy-2.ipynb)
