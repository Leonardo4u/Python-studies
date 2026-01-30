import pandas as pd

book_catalog_df = pd.read_csv('Basic/book_catalog_10.csv')

book_catalog = book_catalog_df.to_dict(orient='records')

print(book_catalog)

def getTitle(book):
    return book['title']

def sort_catalog_by_title(catalog): 
    catalog.sort(key=getTitle)

sort_catalog_by_title(book_catalog)

for book in book_catalog:
    print(
        f"Title: {book['title']}, "
        f"Author: {book['author']}, "
        f"Publication Year: {book['publication_year']}"
    )
