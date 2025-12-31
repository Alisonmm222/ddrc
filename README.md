# Data Driven Reality Check (DDRC): Voting Intention 

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


**Course**: Datenvisualisierung 2025

**Topic**: Data Driven Reality Check 

**Authors:** Semanur Asalioglu, Alison Moldovan-Mauer

**Date:** 2025-01-29

## target group analysis
The primary target group for the project is eligible voters in Lower Bavaria (Niederbayern). 
This includes people of different age groups, educational levels, and political views who are looking for guidance before an election or who regularly use regional media. 
The target group is heterogeneous: it includes both people who are interested in politics and people who only engage with politics occasionally.


## Project Organization

```
├── LICENSE            <- Open-source license if one is chosen
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── notebooks         
├── reports            <- Generated analysis as HTML, PDF, LaTeX, etc.
│   └── figures        <- Generated graphics and figures to be used in reporting
│
├── requirements.txt   <- The requirements file for reproducing the analysis environment, e.g.
│                         generated with `pip freeze > requirements.txt`
│
├── setup.cfg          <- Configuration file for flake8
├── plots.py                <- Code to create visualizations
```

--------

## Installation

1. Clone the repository:
```bash git clone https://github.com/Alisonmm222/ddrc
cd ddrc
```

2. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
3. Install the package and dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```
4. (Optional) Copy and configure environment variables:
```bash
cp .env.example .env
```
