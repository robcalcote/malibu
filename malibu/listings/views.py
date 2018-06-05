from django.shortcuts import render
from django.http import HttpResponse
from ebaysdk.trading import Connection as Trading
import json

def index(request):
    api = Trading(domain='api.sandbox.ebay.com',
                  config_file=None,
                  appid='RobertCa-MalibuMa-SBX-d2ccbdeee-b5a7d2e4	',
                  devid='9f307475-dd04-4d71-99ed-4446e6b13406',
                  certid='SBX-2ccbdeee858b-623c-4890-8cf2-9f26	',
                  token="AgAAAA**AQAAAA**aAAAAA**QtcVWw**nY+sHZ2PrBmdj6wVnY+sEZ2PrA2dj6wFk4agD5KCog+dj6x9nY+seQ**75gEAA**AAMAAA**jJQhDx7jrTyhbUOjKlbY7DJpovf0nt8XRiv/Wshr2E7MSSrvudLzJQOwG68DgPLVfklLvA7D3LI2auyzkBakCDmKjqOETPp5Jt46OuaDHr1G9ADwd6V6qqeZIhbZXazxgJxufl2Cq3AwiTWjrc5sY+NRbVr9fhwD7259G1dizz79kYyMhrIyrX2tXgvpiv1oegjO4BjIRH/3Yy9WXEO9LrRPu2srh8cZ0W5+BwQ/lfAxD9WUbhKhlk4b82sdCms0Eocir1nMLfnxRLLqn52+ZqFFdhJSJ0oMGbdjOkRFaNaEqoZ/QagujmVUg8DVHlLRnVQMbfxP0OP0Jbl6XsmXGrBWraemSBfO8TVx7ZOI9p7wz27c4vWXpKEs6g3eFf8iDQ0iBoir1Nht384Wtvy+ldRHLlgFt45JYOyMDhMcT/oz6FBd2zAz8yx62BqnNFIa5RnlUC1nrkIgxpVTIz0GVncChcOgbKvZIJWWFwtGtKvJ3uIjojMXKyX7Uz+HBji2/zpSd1+t3rughQR4ce8qHSStCdHYzrSkIX6dJoquhbby/+izQ3D0BW0n/+IezUyOKjsADT1eo5H8vcJF3LT2QklLM9fPVBbdB1uhQWzcSsonuK8jPz8ZX0qNbf8Huv8BTmeGUpurxm/X1vG1pdTzcMemePHdjJSCTRn9Fx5mERqM77+gEjvNCi3136Pio8sumOndt3BSEUJGdjOeWoQ0Sg24xQJcwDAZte1YLFZ7zm9KV6cxirqDhOaSE3k8uAqU")
    callData = {
        'DetailLevel': 'ReturnAll',
        'CategorySiteID': 0,
        'LevelLimit': 1
    }

    response = api.execute('GetCategories', callData)

    cats = response.dict()['CategoryArray']
    cat_array = cats['Category']
    s = "<br/>".join([e['CategoryName'] + "\t\t" + e['CategoryID'] for e in cat_array])

    return HttpResponse(s)

