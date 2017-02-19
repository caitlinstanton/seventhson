from py_ms_cognitive import PyMsCognitiveWebSearch, PyMsCognitiveImageSearch
key = '82af3a845a3640318879cf8d6db7320a'
query = "New York City"
bing_web = PyMsCognitiveWebSearch(key, query)
bing_Image = PyMsCognitiveImageSearch(key, query)
first_ten_result = bing_web.search(limit=10, format='json') #1-10
first_ten_image = bing_Image.search(limit=10, format='json') #1-10

print (first_ten_image[0].name)
