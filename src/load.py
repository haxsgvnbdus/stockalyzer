from BeautifulSoup import BeautifulSoup
from datetime import datetime
import os

import click
import pandas as pd
 
import time
import urllib2



SP500_INDEX = './SP500INDEX/constituents-financials.csv' 
DATA_DIR = './data/'
 


def load_symbol(): 
	df = pd.read_csv(SP500_INDEX)
	df.sort_values('Market Cap', ascending=False, inplace=True)
	symbols = df['Symbol'].unique().tolist()	
	print '%d symbols' %len(symbols) 
	
	return symbols

def load_data(symbol, out_name): 

	today = datetime.now().strftime("%b+%d,+%Y")
	BASE_URL = "https://finance.google.com/finance/historical?output=csv&q={0}&startdate=Jan+1%2C+1980&enddate={1}"
    	symbol_url = BASE_URL.format(urllib2.quote(symbol), urllib2.quote(today, '+'))
    	
	print 'Fetching %s' % symbol
	print symbol_url
	
	
	try:
		f = urllib2.urlopen(symbol_url)
		fin = open(out_name, 'w')
		fin.write(f.read())
		fin.close()

	except urllib2.HTTPError:
        	print "{} failed".format(symbol)
		return False
	
	 
@click.command(help="Fetch stock prices/Quantity 505")
@click.option('--continued', is_flag=True)
def main(continued):
	if not os.path.exists(DATA_DIR):
		os.mkdir(DATA_DIR, 0777)  
	
 
	
	symbols = load_symbol()
	for sym in symbols:			
		output = os.path.join(DATA_DIR, sym + ".csv")
		load_data(sym, output)
		


if __name__ == "__main__":
	main()
