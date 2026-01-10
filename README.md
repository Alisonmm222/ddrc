# Data Driven Reality Check (DDRC)

<a target="_blank" href="https://cookiecutter-data-science.drivendata.org/">
    <img src="https://img.shields.io/badge/CCDS-Project%20template-328F97?logo=cookiecutter" />
</a>


**Course**: Datenvisualisierung 2025/2026

**Topic**: Data Driven Reality Check 

**Authors:** Alison Moldovan-Mauer, Semanur Asalioglu

**Date:** January 2026

## Target Group 
The primary Target Group for the Project is eligible voters in Lower Bavaria (Niederbayern). 
This includes people of different age groups, educational levels, and political views who are looking for guidance before an election or who regularly use regional media. 
The target group is heterogeneous: it includes both people who are interested in politics and people who only engage with politics occasionally.


## Project Organization

```           
├── README.md         
├── data    
│   ├── processed   # cleaned data 
│   └── raw         # original input data          
├── plots           
│   └── figures     # plotting scripts and generated plots (.png)
├── src             # cleaning script
├── requirements.txt   

```

--------

## Installation
1. Clone this repository
```bash 
git clone https://github.com/Alisonmm222/ddrc
cd ddrc
````
2. Install dependencies:
```bash
pip install -r requirements.txt
