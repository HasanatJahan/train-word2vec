# imports needed and logging
import gzip
import gensim 
import logging
import bz2

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

input_file = "news.crawl.bz2"
# now to unzip the file 
with bz2.open (input_file, 'rb') as f:
        for i,line in enumerate (f):
            print(line)
            # break