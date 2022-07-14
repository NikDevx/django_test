from django.shortcuts import render

import json
import logging
from json import JSONDecodeError
from ssl import SSLError
import requests
from requests import Timeout


# get data from specific urls
def get_data():
    headers = {
        "Content-Type": "application/json",
    }

    url = "https://onboarding.art-code.team"
    service = "/api/test/v1/search/terms"
    brand = "/api/test/v1/search/brands_terms"
    style = "/api/test/v1/search/styles"

    # making requests
    res_service_data = ""
    res_brand_data = ""
    res_style_data = ""
    try:
        response_service = requests.get(url=url + service, headers=headers)
        response_brand = requests.get(url=url + brand, headers=headers)
        response_style = requests.get(url=url + style, headers=headers)
    except ConnectionError as CE:
        logging.error("ConnectionError: " + CE.__str__())
    except SSLError as SE:
        logging.error("SSLError: " + SE.__str__())
    except Timeout as TE:
        logging.error("Timeout: " + TE.__str__())
    except JSONDecodeError as JDE:
        logging.error("JSONDecodeError: " + JDE.__str__())
    else:
        # get data from request
        res_service_data = json.loads(response_service.text)['data']
        res_brand_data = json.loads(response_brand.text)['data']
        res_style_data = json.loads(response_style.text)['data']

    return res_service_data, res_brand_data, res_style_data


# render data to html page
def index_view(request):
    # getting terms
    terms = get_data()[0]
    # getting brand
    brand = get_data()[1]
    # getting style
    style = get_data()[2]

    terms_label = [d['label'] for d in terms if 'label' in d]
    terms_slug = [d['slug'] for d in terms if 'slug' in d]
    brand_label = [d['label'] for d in brand if 'label' in d]
    brand_slug = [d['slug'] for d in brand if 'slug' in d]
    style_label = [d['label'] for d in style if 'label' in d]
    style_slug = [d['slug'] for d in style if 'slug' in d]

    return render(request, 'index.html', {'terms': zip(terms_label, terms_slug),
                                          'brand': zip(brand_label, brand_slug),
                                          'style': zip(style_label, style_slug)})
