# PyDataLadies Dashboards

Materiály pro lekci o interaktivních vizualizacích a tvorbě dashboard aplikací.

## Příprava

1. Nainstalovat Git:
   * Windows: https://gitforwindows.org/
   * Mac OS: https://sourceforge.net/projects/git-osx-installer/files/ (případně další možnosti popsané na https://www.atlassian.com/git/tutorials/install-git).
   * Linux: Nejspíš tam už bude nebo určitě víš jak na to :)
2. Alespoň základní konfigurace Gitu. V příkazovém řádku (vyplňte své jméno a email):
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
3. Založit bezplatný Heroku účet na https://signup.heroku.com/signup/dc.
4. Nainstalovat si Heroku klienta:
   * Postupujte podle https://devcenter.heroku.com/articles/heroku-cli
Instalaci vyzkoušíme pomocí
```
heroku --version
```
Výstupem by mělo být zhruba
```
heroku/7.47.12 darwin-x64 node-v12.16.2
```
Kdyby něco nefungovalo nebylo jasné, tak se hned ptejte v kanále [#poradna](https://pydata-kurz-praha.slack.com/archives/CSPRXPJGN).

## Materiály

1. [První část](notebooks/dashboardy-1.ipynb)
1. [Druhá část](notebooks/dashboardy-2.ipynb)
