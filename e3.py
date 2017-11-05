#!/usr/bin/env python

import pandas as pd

result_list = []
columns = ['Democratic', 'Republican', 'Total Votes Cast', 'Year']
rows = ['Accomack County', 'Albemarle County', 'Alexandria City', 'Alleghany County']

for line in open('ELECTION_ID'):
  year = line.split()[0]
  file_name = 'president_general_' + year + '.csv'
  header = pd.read_csv(file_name, nrows=1).dropna(axis=1)
  d = header.iloc[0].to_dict()

  df = pd.read_csv(file_name, index_col=0, thousands=',', skiprows=[1])

  df.rename(inplace=True, columns=d)  # rename to democrat/republican
  df.dropna(inplace=True, axis=1)    # drop empty columns
  df['Year'] = year

  filtered_rows = df.loc[df.index.map(lambda x: x in rows)]
  filtered = filtered_rows[columns]

  result_list.append(filtered)

final = pd.concat(result_list)
final['Republican Share'] = (final['Republican'] / final['Total Votes Cast']) * 100

for place in rows:
  file_name = place.replace(' ', '_').lower()
  title = 'Republican Vote Share Over Time\nin ' + place
  plt = final[final.index == place].sort('Year').plot(x='Year', y='Republican Share', legend=False, title=title)
  plt.set_ylabel('Republican Vote Share (%)')
  plt.figure.savefig(file_name + '.pdf')
