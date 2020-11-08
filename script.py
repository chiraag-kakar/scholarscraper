import requests
from bs4 import BeautifulSoup as bs

queries = ['Role for migratory wild birds in the global spread of avian influenza H5N8',
         'Uncoupling conformational states from activity in an allosteric enzyme',
         'Technological Analysis of the World’s Earliest Shamanic Costume: A Multi-Scalar, Experimental Study of a Red Deer Headdress from the Early Holocene Site of Star Carr, North Yorkshire, UK',
         'Oxidative potential of PM 2.5  during Atlanta rush hour: Measurements of in-vehicle dithiothreitol (DTT) activity',
         'Primary Prevention of CVD','Growth and Deposition of Au Nanoclusters on Polymer-wrapped Graphene and Their Oxygen Reduction Activity',
         'Relations of Preschoolers Visual-Motor and Object Manipulation Skills With Executive Function and Social Behavior',
         'We Know Who Likes Us, but Not Who Competes Against Us']

with requests.Session() as s:
    for query in queries:
        url = 'https://scholar.google.com/scholar?q=' + query + '&ie=UTF-8&oe=UTF-8&hl=en&btnG=Search'
        r = s.get(url)
        soup = bs(r.content, 'lxml') # or 'html.parser'
        title = soup.select_one('h3.gs_rt a').text if soup.select_one('h3.gs_rt a') is not None else 'No title'
        link = soup.select_one('h3.gs_rt a')['href'] if title != 'No title' else 'No link'
        citations = soup.select_one('a:contains("Cited by")').text if soup.select_one('a:contains("Cited by")') is not None else 'No citation count'
        print(title, link, citations) 