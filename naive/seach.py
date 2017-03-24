from google.appengine.api import search

# a query string like this comes from the client
querystring = 'stories'
try:
  index = search.Index(INDEX_NAME)
  search_query = search.Query(
      query_string=querystring,
      options=search.QueryOptions(
          limit=doc_limit))
  search_results = index.search(search_query)
except search.Error:
  print("error")
