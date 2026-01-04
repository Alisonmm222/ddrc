# Data Driven Reality Check (DDRC): Voting Intention 

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


**Course**: Datenvisualisierung 2025/2026

**Topic**: Data Driven Reality Check 

**Authors:** Semanur Asalioglu, Alison Moldovan-Mauer

**Date:** January 2026

## target group analysis
The primary target group for the project is eligible voters in Lower Bavaria (Niederbayern). 
This includes people of different age groups, educational levels, and political views who are looking for guidance before an election or who regularly use regional media. 
The target group is heterogeneous: it includes both people who are interested in politics and people who only engage with politics occasionally.


## Project Organization

```
├── LICENSE           
├── README.md         
├── data    
│   ├── processed     
│   └── raw            
├── plots            
│   └── figures     
├── src   
├── requirements.txt   

```

--------

## Installation
1. Create a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```
2. Install the package and dependencies:
```bash
pip install -r requirements.txt
pip install -e .
```
3. Cofigure .env
```bash
RAW_DIR = Path(".../data/raw")
PROCESSED_DIR = Path(".../data/processed")
```