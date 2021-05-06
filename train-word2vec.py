# imports needed and logging
import gzip
import gensim 
import logging
import bz2
import pprint
pp = pprint.PrettyPrinter(indent=4)

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

input_file = "news.crawl.bz2"
# # now to unzip the file 
# with bz2.open (input_file, 'rb') as f:
#         for i,line in enumerate (f):
#             print(line)
#             break


def read_input(input_file):
    """This method reads the input file which is in gzip format"""
    
    logging.info("reading file {0}...this may take a while".format(input_file))
    
    with bz2.open (input_file, 'rb') as f:
        for i, line in enumerate (f): 

            if (i%10000==0):
                logging.info ("read {0} reviews".format (i))
            # do some pre-processing and return a list of words for each review text
            yield gensim.utils.simple_preprocess (line)

# read the tokenized reviews into a list
# each review item becomes a series of words
# so this becomes a list of lists
documents = list (read_input (input_file))
logging.info ("Done reading data file")

# training word2vec model 
# model = gensim.models.Word2Vec (documents, vector_size=150, window=5, min_count=2, workers=10)

# build vocabulary and train model
model = gensim.models.Word2Vec(
    documents,
    vector_size=150,
    window=5,
    min_count=2,
    workers=10,
    epochs=10)

model.train(documents,total_examples=len(documents),epochs=10)

# Now to look at some output 
# All together 

#-----------------------------------
# No. 1
#-----------------------------------
# similarity between two different words
print("Similarity between 'dirty' and 'clean'")
print(model.wv.similarity(w1="dirty",w2="clean"))

print("Similarity between 'big' and 'dirty'")
print(model.wv.similarity(w1="big",w2="dirty"))

print("Similarity between 'big' and 'large'")
print(model.wv.similarity(w1="big",w2="large"))

print("Similarity between 'big' and 'small'")
print(model.wv.similarity(w1="big",w2="small"))

#----------------------------------
# No. 2 
#----------------------------------
# look up top 6 words similar to 'polite'
w1 = ["polite"]
print("Top most similar words for polite")
pp.pprint(model.wv.most_similar (positive=w1,topn=5))

# look up top 6 words similar to 'orange'
print("Top most similar words for orange")
w1 = ["orange"]
pp.pprint(model.wv.most_similar (positive=w1,topn=5))