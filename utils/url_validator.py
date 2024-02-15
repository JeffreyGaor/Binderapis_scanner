from urllib.parse import urlparse

def is_valid_url(url):
  parsed_url = urlparse(url)
  return parsed_url.scheme in ['http', 'https'] and parsed_url.netloc != ''