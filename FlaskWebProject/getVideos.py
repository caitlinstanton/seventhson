# Azure Videos script
# Andrea Jackson

from py_ms_cognitive import PyMsCognitiveVideoSearch

def getVideos(query):
  '''
  Input: string query for a Video
  Output: a dictionary of tuples of the video name and video display host_page_display_url
  The output contains relevant videos for the given query'''

  API_KEY = "82af3a845a3640318879cf8d6db7320a"
  search_term = query
  search_service = PyMsCognitiveVideoSearch(API_KEY, search_term)
  first_five_results = search_service.search(limit=5, format='json') #1-5

  return {(vid.name, vid.host_page_display_url) for vid in first_five_results}

# print getVideos("adele")

# def getName(videoDict):

