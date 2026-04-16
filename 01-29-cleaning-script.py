
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Read data set
df = pd.read_csv('movies.csv')

# Fix year column and split it into two
df.YEAR = df.YEAR.str[1:-1]
df.YEAR = df.YEAR.str.replace(r'\D', ' ', regex=True)
df.YEAR = df.YEAR.str.strip()
df[['Year Released','Year Concluded']] = df.YEAR.str.split(' ', expand=True)

# Remove extra blanks from genre column
df.GENRE = df.GENRE.str.strip()

# Remove extra blanks from one-line description column and add missing values
df['ONE-LINE'] = df['ONE-LINE'].str.strip()
df['ONE-LINE'] = df['ONE-LINE'].replace('Add a Plot', None)

# Remove extra blanks from stars column, then split it into director and stars
df.STARS = df.STARS.str.strip()
df.STARS = df.STARS.str.replace(r'\s+',' ',regex=True)
halves = df.STARS.str.split(r' \| ',expand=True)
df['DIRECTOR'] = np.where(halves.iloc[:,1].isna(), None, halves.iloc[:,0])
df.DIRECTOR = df.DIRECTOR.str[9:].str.strip()
df.STARS = np.where(halves.iloc[:,1].isna(), halves.iloc[:,0], halves.iloc[:,1])
df.STARS = df.STARS.str[6:].str.strip()

# Convert votes column into a number
df.VOTES = df.VOTES.str.replace(',', '')
df.VOTES = df.VOTES.astype(float)

# Convert revenue column into a number
# (Note: We verified first that every non-null entry starts with $ and ends with M.)
df.Gross = df.Gross.str[1:-1]
df.Gross = df.Gross.astype(float) * 1_000_000

# Give all columns better names and reorder them more sensibly
df.columns = ['Title','Year','Genres','Rating','Description','Stars','Votes','Runtime','Revenue','Year Released','Year Concluded','Director']
df = df[['Title','Year Released','Year Concluded','Runtime','Genres','Description','Director','Stars','Rating','Votes','Revenue']]

# Create histogram of revenue
plt.hist(df.Revenue / 1_000_000, bins=20, rwidth=0.8, color='#607c8e', edgecolor='black')
plt.title('Distribution of Revenue')
plt.xlabel('Revenue (in millions of USD)')
plt.ylabel('Number of titles')
plt.ticklabel_format(style='plain', useOffset=False, axis='both')
plt.savefig('movies-revenue-hist.png')

# Create histogram of ratings
plt.hist(df.Rating, bins=20, rwidth=0.8, color='#607c8e', edgecolor='black')
plt.title('Distribution of Ratings')
plt.xlabel('Rating')
plt.ylabel('Number of titles')
plt.savefig('movies-ratings-hist.png')
