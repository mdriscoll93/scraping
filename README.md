# HTML Table Scraper

## Steps

1. Within `table_scraper.py`, edit value of `state_urls` with the URL to scrape tables from. 
   - *Chrome keyboard shortcuts URL hard-coded as example*
2. If not already installed, `pip install scrapy`
3. Run `scrapy runspider` however you want the data to output:

### Examples:
 - output to **stdout**: `scrapy runspider table_scraper.py`
 - output to **JSON**: `scrapy runspider --nolog -o output-table.json table_scraper.py`

---

### TODO

- [ ] enable scraping all tables from sites with multiple tables more effectively.
- example selectors: 
```python
# extract using element ids
response.xpath('//*[@id="table"]//tbody//tr')
response.xpath('//*[@id="nice-table"]//tbody//tr')
```

- [ ] implement threading & dataframes for processing & storing large datasets in JSON or SQL
```python
# extract all text from entire table using primary table
response.xpath('//table//text()').extract()

# create table
output = [data[i:i + num_cols] for i in range(0, len(data), num_cols)]

# create dictionary using pandas
dictionary = pandas.DataFrame(output[1:], columns=output[0]).set_index('Date').to_dict()
```
