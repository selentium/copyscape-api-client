import decimal
import codecs

import requests
import xmltodict

class CopyscapeApiError(Exception):
    pass

class Client:

    api_url = "https://www.copyscape.com/api/"

    def __init__(self, username, api_key):
        self.username = username
        self.api_key = api_key

    def search(self, url=None, text=None, operation="csearch", encoding="UTF-8", full_comparisons=0, ignore_sites=(), spend_limit=None, is_test=False):
        if url is None and text is None:
            raise ValueError("You should provide either URL or text.")
        valid_operations = ("csearch", "psearch", "cpsearch") 
        if operation not in valid_operations:
            raise ValueError("Invalid operation") 
        full_comparisons = int(full_comparisons)
        if full_comparisons < 0 or full_comparisons > 10:
            raise ValueError("Full comparisons should be between 0 and 10.")
        if spend_limit is not None:
            spend_limit = decimal.Decimal(spend_limit)
        if text:  
            try:
                codecs.lookup(encoding)
            except LookupError:
                raise ValueError("Invalid encoding.")
        params = {
            "c": full_comparisons
        }        
        if ignore_sites:
            ignore_sites = ",".join(ignore_sites)
            params['ignore_sites'] = ignore_sites
        if spend_limit:
            params['spend_limit'] = round(spend_limit, 2)
        if is_test:
            params['x'] = '1'         
        if url:
            params['q'] = url 
            r = self._api_call(operation, params)
        else:
            params['t'] = text
            params['e'] = encoding
            r = self._api_call(operation, params, "POST")
        return r['response']


    def add_to_private_index(self, url=None, text=None, article_id=None, encoding="UTF-8", article_title=None):
        if url is None and text is None:
            raise ValueError("You should provide either URL or text.")
        if text:  
            try:
                codecs.lookup(encoding)
            except LookupError:
                raise ValueError("Invalid encoding.")
        if url:
            params = {
                "q": url
            }    
            if article_id:
                params['i'] = article_id
            r = self._api_call("pindexadd", params)   
        else:
            params = {
                "e": encoding,
                "t": text
            }            
            if article_title:
                params['a'] = article_title
            if article_id:
                params['i'] = article_id
            r = self._api_call("pindexadd", params, "POST")      
        return r['response']               

    def delete_from_private_index(self, handle):
        params = {"handle": handle}
        r = self._api_call("pindexdel", params)
        return r['response']
        

    def check_balance(self):
        r = self._api_call("balance")
        return r['remaining']

    def _api_call(self, operation, params={}, method="GET"):
        params.update({
            "u": self.username,
            "k": self.api_key,
            "o": operation
        })    
        if method == "GET":
            r = requests.get(self.api_url, params=params)
        else:
            r = requests.post(self.api_url, data=params)
        result = xmltodict.parse(r.text)    
        if "response" in result and "error" in result['response']:
            raise CopyscapeApiError(result['response']['error'])
        return result    


                           
