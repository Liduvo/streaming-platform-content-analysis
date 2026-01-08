import pandas as pd
import numpy as np

netflix = pd.read_csv("netflix_titles.csv")
disney = pd.read_csv("disney_plus_titles.csv")
amazon = pd.read_csv("amazon_prime_titles.csv")

netflix['platform'] = 'Netflix'
disney['platform'] = 'Disney+'
amazon['platform'] = 'Prime Video'

combined = pd.concat([netflix, disney, amazon])

# Yearly released content
yearly_releases = (combined.groupby(['platform', 'release_year']).size().reset_index(name='content_count'))

yearly_table = yearly_releases.pivot(index='release_year',columns='platform',values='content_count')

print(yearly_table.tail())

# Content type analysis
type_focus = (combined.groupby(['platform', 'type']).size().reset_index(name='count'))

type_ratio = (
    type_focus.assign(ratio=lambda x: x['count'] /x.groupby('platform')['count'].transform('sum'))
)

print(type_ratio)