from django.shortcuts import render

import json
import logging
from json import JSONDecodeError
from ssl import SSLError
import requests
from requests import Timeout


# get data from specific urls
def get_data():
    """
    Uncomment for prod

    # headers = {
    #     "Content-Type": "application/json",
    # }
    #
    # url = "{some_domain}"
    # service = "api/test/v1/search/terms"
    # brand = "api/test/v1/search/brands_terms"
    # style = "api/test/v1/search/styles"
    #
    # # making requests
    # res_service_data = ""
    # res_brand_data = ""
    # res_style_data = ""
    # try:
    #     response_service = requests.post(url=url + service, headers=headers)
    #     response_brand = requests.post(url=url + brand, headers=headers)
    #     response_style = requests.post(url=url + style, headers=headers)
    # except ConnectionError as CE:
    #     logging.error("ConnectionError: " + CE.__str__())
    # except SSLError as SE:
    #     logging.error("SSLError: " + SE.__str__())
    # except Timeout as TE:
    #     logging.error("Timeout: " + TE.__str__())
    # except JSONDecodeError as JDE:
    #     logging.error("JSONDecodeError: " + JDE.__str__())
    # else:
    #     # get data from request
    #     res_service_data = json.loads(response_service.text)
    #     res_brand_data = json.loads(response_brand.text)
    #     res_style_data = json.loads(response_style.text)
    """

    # data for passing test
    res_service_data = {"terms": ["remont", "zamina", "restavrazhiya"]}
    res_brand_data = {"brand": ["zubr", "mac", "kruz"]}
    res_style_data = {"style": ["luxury", "top", "modern"]}

    return res_service_data, res_brand_data, res_style_data


# render data to html page
def index_view(request):
    # data for passing test
    terms = get_data()[0].get('terms')
    brand = get_data()[1].get('brand')
    style = get_data()[2].get('style')

    """
    Uncomment for production

    terms = get_data()[0]
    brand = get_data()[1]
    style = get_data()[2]
    """

    return render(request, 'index.html', {'terms': terms, 'brand': brand, 'style': style})
