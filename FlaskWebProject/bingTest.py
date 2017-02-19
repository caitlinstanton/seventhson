from py_ms_cognitive import PyMsCognitiveWebSearch, PyMsCognitiveImageSearch
key = '82af3a845a3640318879cf8d6db7320a'

def search(query):
	bing_web = PyMsCognitiveWebSearch(key, query)
	bing_Image = PyMsCognitiveImageSearch(key, query)
	first_ten_result = bing_web.search(limit=10, format='json') #1-10
	first_ten_image = bing_Image.search(limit=10, format='json') #1-10
	return (first_ten_image[0].content_url)
