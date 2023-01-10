
import json


class GraphqlQuery:
    def __init__(self, induce_error=False,*args, **kwargs):
        # Analyzing what kind of arguments are passed to 
        # be parsed into a valid query.
        self.induce_error = induce_error
        key_types = ["Type of query input",
        "Induce error query"
        ]
        self.inputs = {}
        self.args = args
        self.kwargs = kwargs

        interpreter = Interpreter(args, kwargs)



    def json_query(self, json_file):
        self.


class Interpreter:
    def __init__(self, *args, **kwargs):
        self.args = args
        self.kwargs = kwargs
        for kwarg in kwargs:
            query_type = self.identifier(kwarg)



    def identifier(self, query):
        if type(query) == dict:
            return "JSON"
        elif type(query) == str:
            self.match_reader(query)



    def match_reader(self, string):
        first_patterns = ['query'
        ]

        string = string.replace(' ', '')

        if '\n' in string:
            string = string.replace('\n', '')


        if string[0] != '{':
            for i in range(len(first_patterns[0])):
                pattern = first_patterns[0]
                if pattern[i] != string[i]:
                    raise MismatchError('string', pattern, string, i)


        for char in string:
            print('o')





class MismatchError:

    def __init__(self, what_type, expected, given, location):
        self.location = location
        self.expected = expected
        self.given = given

        if what_type == 'string':
            self.what_type = what_type
            self.string_mismatch()


    def string_mismatch(self):
        print(f'MismatchError: Expected query does not match the one provided. Expected {self.expected[self.location]}, got {self.given[self.locatio]} in char [{self.location}.\n Type of query: {self.what_type}')