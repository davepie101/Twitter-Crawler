#!/usr/bin/env python  

import os
import sys
import math
import lucene
from java.io import File
from java.nio.file import Paths
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser, QueryParserBase, MultiFieldQueryParser
from org.apache.lucene.store import RAMDirectory, FSDirectory
from org.apache.lucene.analysis.standard import StandardAnalyzer
from org.apache.pylucene.search.similarities import PythonClassicSimilarity

class SimpleSimiliarity(PythonClassicSimilarity):

    def lengthNorm(self, numTerms):
        return 1

class Rank:

    def search(query):
        lucene.initVM()
        luceneDirectory = "/index/"

        path = str(os.path.abspath(os.getcwd()) + luceneDirectory)
        directory = FSDirectory.open(Paths.get(path))
        reader = DirectoryReader.open(directory)
        searcher = IndexSearcher(reader)
        analyzer = StandardAnalyzer()

        #args = len(sys.argv) - 1

        #if args < 1:
         #   print ("\n No query was submitted! \n")
        #else:
            #query_string = ""
            #position = 1
            #while(args >= position):
                #query_string = query_string + str(sys.argv[position]) + " "
                #position = position + 1

        print ("Searching for '" + query + "'")
    
        fields_to_search = ["text", "page title", "date"]
        filter_date = 'date:"May 25"'    
      
        filtered_query = filter_date + "AND " + query

        parser = MultiFieldQueryParser(fields_to_search, analyzer)
        updated_query = MultiFieldQueryParser.parse(parser, filtered_query)
        scored_documents = searcher.search(updated_query, 10).scoreDocs # array of docs
        
        print ("Found " + str((len(scored_documents))) + " matches in the collection.")
        
        results = []
        for doc in scored_documents:
            scoredTweet = dict()
            scoredTweet['score'] = doc.score
            result = searcher.doc(doc.doc)
            scoredTweet['username'] = result.get("username")
            scoredTweet['tweet_body'] = result.get("text")
            scoredTweet['date'] = result.get("date")
            results.append(scoredTweet)
            print(scoredTweet)

        return results

    if __name__ == '__main__':
        lucene.initVM()
        search("trump")

