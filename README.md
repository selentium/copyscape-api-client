# copyscape-api-client
Python Client for [Copyscape API](https://www.copyscape.com/api-guide.php)

## Usage example
```
import copyscape

client = copyscape.Client("your_username", "your_api_key")
result = client.search(url="http://example.org/")
```    
