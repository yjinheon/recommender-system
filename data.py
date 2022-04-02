# get zip
url = 'https://files.grouplens.org/datasets/movielens/ml-latest-small.zip' # movie 


from urllib.request import urlopen
from io import BytesIO
from zipfile import ZipFile


def download_and_unzip(url, extract_to='.'):
    http_response = urlopen(url)
    zipfile = ZipFile(BytesIO(http_response.read()))
    zipfile.extractall(path="data/"+extract_to)
    
    
download_and_unzip(url)