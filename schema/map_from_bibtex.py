
#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" 
Convert Bibtex file into a Knowledge Graph 

This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
"""

__author__ = "Diego Rincon-Yanez"
__copyright__ = "MIT"
__date__ = "2024/06/20"
__deprecated__ = False
__status__ = "stable"
__version__ = "0.0.1"

import pandas as pd
from bibtexparser.bparser import BibTexParser

def bibtex_to_dataframe(bibtex_file):
  """
  Reads a BibTeX file and converts it into a Pandas DataFrame.

  Args:
    bibtex_file: The path to the BibTeX file.

  Returns:
    A Pandas DataFrame containing the bibliographic data.
  """

  with open(bibtex_file, 'r') as bibtex_file:
    bib_database = BibTexParser().parse_file(bibtex_file)

  entries = []
  for bib_id in bib_database.entries:
    entry = {}
    for key in bib_id.keys():
      entry[key] = bib_id[key]
    entries.append(entry)

  df = pd.DataFrame(entries)
  return df

if __name__ == "__main__":

  #Read the Bibtex file
  bibtex_file = '../data/selected_papers.bib'
  
  df = bibtex_to_dataframe(bibtex_file)
  df.to_csv('selected_papers.csv', index=False)
