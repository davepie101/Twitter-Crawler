#!/usr/bin/env python

import os
import sys
import lucene
from java.io import File
from java.nio.file import Paths
from org.apache.lucene.search import IndexSearcher
from org.apache.lucene.index import DirectoryReader
from org.apache.lucene.queryparser.classic import QueryParser, QueryParserBase, MultiFieldQueryParser
from org.apache.lucene.store import RAMDirectory, FSDirectory

lucene.initVM()
luceneDirectory = "/index/"

path = str(os.path.abspath(os.getcwd()) + luceneDirectory)
print path

directory = FSDirectory.open(Paths.get(path))
reader = DirectoryReader.open(directory)

#searcher = IndexSearcher(reader)
#analyzer = StandardAnalyzer()

#query = str(sys.argv)
#if query == '':
    #print "/n No query was submitted! \n"
#else:
 #       print "Searching for " + query + "... \n"
  ##     parsed_query.setDefaultOperator(QueryParserBase.AND_OPERATOR)

        # For looking at multiple fields later...
        #parser = MultiFieldQueryParser(fields, analyzer)
        #updated_query = MultiFieldQueryParser.parse(parser, query)

    #    scored_documents = searcher.search(parsed_query, 10).scoreDocs # array of docs
        
     #   print "Found " + str((len(scored_documents))) + " matches in the collection."
        
      #  for doc in scored_documents:
       #     result = searcher.doc(doc)
        #    tweet_body = result.get("tweet")
