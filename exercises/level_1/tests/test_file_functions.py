import os
import json

# test this function
def get_json_file(path):
    with open(path) as f:
        return json.load(f)





# @@@@@@@@@@@ solutions @@@@@@@@@@@


def test_missing_file():
    get_json_file('t.json')


def test_empty_file():
    filename = 'test_json_empty.json'
    open(filename, 'w').close()
    try:
        get_json_file(filename)
    finally:
        os.remove(filename)


def test_valid_json_file():
    filename = 'test_json_valid.json'
    valid_data = [
        {
            'string': 'string',
            'integer': 1,
            'float': 1.4,
            'null': None,
            'boolean true': True,
            'boolean fale': False,
            'array': [],
            'hash': {},
        },
        [0, 1, 2, 3, 4, 5, 6, 7, 8]
    ]

    def assert_js(data1, data2):
        if isinstance(data1, list):
            assert type(data1) == type(data2)
            assert len(data1) == len(data2)
            for d1, d2 in zip(sorted(data1), sorted(data2)):
                assert_js(d1, d2)

        elif isinstance(data1, dict):
            assert type(data1) == type(data2)
            assert len(data1) == len(data2)
            for k1, k2 in zip(sorted(data1.keys()), sorted(data2.keys())):
                assert k1 == k2
                assert_js(data1[k1], data2[k2])
        else:
            assert data1 == data2
    try:
        for data in valid_data:
            with open(filename, 'w') as f:
                json.dump(data, f)

            js = get_json_file(filename)
            assert_js(js, data)
    finally:
        os.remove(filename)
