import json
import random
import time
import traceback
import urllib.error
import urllib.parse
import urllib.request


def fetchUrl(url):
        
        if not url:
            return None

        result = {
            'code': None,
            'status': None,
            'content': None,
            'headers': None,
            'realurl': url
        }

        url = url.strip()

        return result



def darksearch(query, page):
    params = {
        "query": '"' + query.encode('raw_unicode_escape').decode("ascii", errors='replace') + '"',
        "page": str(page)
    }

    res = fetchUrl("https://darksearch.io/api/search?" + urllib.parse.urlencode(params))
    time.sleep(2)

    if res['content'] is None:
            return None

    try:
        data = json.loads(res['content'])
    except Exception as e:
        print("Error processing JSON request: {e}")
        return None

    print(data)