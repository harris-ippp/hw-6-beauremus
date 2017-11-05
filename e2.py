#!/usr/bin/env python

import requests

def get_election(election_id):
  return requests.get(
      'http://historical.elections.virginia.gov/elections/download/{}/precincts_include:0/'.format(election_id))

def write_csv(file_name, text):
  with open(file_name + '.csv', 'w') as output:
    output.write(text)

for line in open('ELECTION_ID'):
  line_list = line.split()
  resp = get_election(line_list[1])
  write_csv('president_general_' + line_list[0], resp.text)
