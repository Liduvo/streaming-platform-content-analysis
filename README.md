# streaming-platform-content-analysis
Analyzing content volume and release trends across major streaming platforms.
# 🎬 Streaming Platform Content Analysis

A comparative data analysis of Netflix, Disney+, and Amazon Prime Video

# 📌 Project Overview

This project analyzes and compares the content libraries of Netflix, Disney+, and Amazon Prime Video using real-world datasets.
The goal is to understand how each platform’s content strategy has evolved over time and whether they focus more on movies or TV shows.

# 📊 Datasets

The project uses three publicly available datasets:

netflix_titles.csv

disney_plus_titles.csv

amazon_prime_titles.csv

Each dataset contains the following main fields:

title

type (Movie / TV Show)

release_year

country

director

cast

# 🛠 Technologies Used

Python

Pandas

NumPy

# 🔍 Analysis Performed

The following analyses were conducted:

1️⃣ Platform Content Size

The total number of movies and TV shows available on each platform was calculated.

2️⃣ Yearly Content Growth

For titles released from 2015 onwards, the number of new titles added each year was analyzed for:

Netflix

Disney+

Amazon Prime Video

3️⃣ Movies vs TV Shows

The ratio of movies to TV shows was calculated for each platform to identify their content focus.

4️⃣ United States Market Focus

Only titles available in the United States were filtered to analyze how each platform targets the U.S. market.

# 🧠 Methods Used

The following data processing techniques were used:

Merging multiple datasets using concat

Handling missing values

Grouping data by platform and release year

Calculating content ratios

Creating pivot tables for comparison
