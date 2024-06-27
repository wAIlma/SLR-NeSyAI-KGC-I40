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

# Example usage
bibtex_file = BIBTEX_FILE
df = bibtex_to_dataframe(bibtex_file)

# Print the DataFrame
print(df.head())