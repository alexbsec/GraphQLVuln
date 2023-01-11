
import json
import requests
from requests import *
from bs4 import BeautifulSoup
import time


LETTERS = 'abcdefghijklmnopqrs'


class NormalQuery:
    def __init__(self, url, endpoint, method, induce_error=False, req_per_sec=10, timout=20, **kwargs):
        self.URL = url


class IntrospectionQuery:
    def __init__(self, url, endpoint, method, induce_error=False, req_per_sec=10, timeout=20, **kwargs):
        self.URL = url
        self.endpoint = endpoint
        self.induce_error = induce_error
        self.requests_per_second = req_per_sec
        self.timout = timeout

        self.query_db = [
            "{__schema}",
            "{__schema}",
            "{__schema{types}}",
            "{__schema{types{names}}}",
            "{__schema{queryType{name}}}"
        ]

        self.invalid_query_db = [
            "{__asdohk}",
            "{__schema{thisisnotavalidquery}}"
        ]

        self.error_responses = [
            "Cannot query field",
            "GraphQL introspection is not allowed"
        ]

        soups_responses = self.request_query(method)
        self.soup_analyzer(soups_responses)

        



    def request_query(self, method, **kwargs):
        soups = {}

        if not self.induce_error:
            for query in self.query_db:
                print(f'[-] Applying {self.method} request on {self.URL} with query {query}...')
                r = requests.method(self.URL, data={"query":query}, timout=self.timout)
                soup = BeautifulSoup(r.content, 'html.parser')
                soups[query] = soup
                time.sleep(self.requests_per_second)

            return soups

        for query in self.invalid_query_db:
            print(f'[-] Applying {self.method} request on {self.URL} with invalid query {query}...')
            r = requests.method(self.URL, data={"query":query})
            soup = BeautifulSoup(r.content, 'html.parser')
            soups[query] = soup
            time.sleep(self.requests_per_second)

        return soups
        
            
    def soup_analyzer(self, responses):
        keys = list(responses)
        self.errors = {}
        self.accepted = {}
        for query in keys:
            for error in self.error_responses:
                if error in responses[query]:
                    print(f"[+] Endpoint GraphQL returned an error {responses[query]}.")
                    self.errors[query] = responses[query]
                    print("[-] Analyzing possible vulnerabilities...")
                    self.error_breaches(responses[query])
                else:
                    print(f"[+] Query {responses[query]} received a response that could lead to information disclosure, sqli and CRSF.")
                    self.accepted[query] = responses[query]


        

    def error_breaches(self, error):
        if self.error_responses[1] in error:
            print("[!] Introspection is disabled.")
            print("[-] Try to enumerate fields with normal queries.")
            






        


