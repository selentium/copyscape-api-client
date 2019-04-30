# Copyscape API Client
Python Client for [Copyscape API](https://www.copyscape.com/api-guide.php)

## Installation
`pip install copyscape-api`

## Usage example
```
import copyscape_api

client = copyscape_api.Client("your_username", "your_api_key")
result = client.search(url="http://example.org/")
```    
