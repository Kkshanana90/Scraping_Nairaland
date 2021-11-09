# Scraping_Nairaland <br/>
This project scraped comments from the political section of popular Nigerian blog www.nairaland.com using the Python BeautifulSoup library, and saved the extracted comments and links in a CSV file.

# Create a new environment and install requirements <br/>
Create a new Anaconda environment with Python 3.8( Other Python versions could also be used), and pip install the required librairies using: <br/> 
'pip install -r Requirements.txt'.

# Run the Nairaland_pol_section.py file <br/>
This could be done using 'python Nairaland_pol_section.py' on Mac's terminal.

# Saved CSV File <br/>
The generated CSV file would be saved as 'Nairaland_df.csv'

# Cleaning <br/>
To read the generated 'Nairaland_df.csv' file in Jupyter Notebook, Google Colab, etc; you may want to replace 'Nairaland_df.csv' with own path in, for example,
'full_data= pd.read_csv('Nairaland_df.csv',lineterminator='\n')'. Codes for cleaning are available in the 'Cleaning_Nairaland_Scraping.py' file.

# Number of Comments <br/>
The script only extracts all comments in the first 10 pages as shown in "for i in range(0,10):" from the 'Nairaland_pol_section.py' file.

# Possible Use <br/>
A sentiment analysis could be performed on the extracted comments.

