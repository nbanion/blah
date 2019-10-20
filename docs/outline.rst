===============
Project Outline
===============


Process
=======

1. Scrape web pages and save in data folder.
2. Process raw data into clean dataframes.
3. Insert clean dataframes into a database.


Packages
========

This python project uses:

- ``scrapy`` for web scraping.
- ``pandas`` for data processing.
- ``peewee`` for working with the database.


Project structure
=================

Inspired by `drivendata/cookiecutter-data-science
<https://github.com/drivendata/cookiecutter-data-science>`_. ::

  st-marys/
    README.md     # Project description.
    Makefile      # Coordinate different scripts in project.
    setup.py      # For package setup.
    docs/         # Project documentation.
    st-marys/
      __init__.py
      spiders/    # For crawling web pages.
      data/       # Scripts to generate raw data.
      features/   # Scripts to create processed data.
      analysis/   # Scripts to analyze data.
    data/
      raw/        # Unaltered data from web scraping.
      processed/  # Clean datasets for analysis.
    docs/         # Sphinx project.
    notebooks/    # Exploratory analyses.
    references/   # Data documentation.
