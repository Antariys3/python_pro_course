from urllib.parse import urlparse, parse_qs


def parse(query: str) -> dict:
    parsed_url = urlparse(query)
    query_params = parse_qs(parsed_url.query)
    dict_query = {key: value[0] for key, value in query_params.items()}
    return dict_query


if __name__ == '__main__':
    assert parse('https://example.com/path/to/page?name=ferret&color=purple') == {'name': 'ferret', 'color': 'purple'}
    assert parse('https://example.com/path/to/page?name=ferret&color=purple&') == {'name': 'ferret', 'color': 'purple'}
    assert parse('http://example.com/') == {}
    assert parse('http://example.com/?name=Dima') == {'name': 'Dima'}
    assert parse('https://example.com/path/to/page?age=25&city=Kharkiv') == {'age': '25', 'city': 'Kharkiv'}
    assert parse('https://example.com/path/to/page?animal=dog') == {'animal': 'dog'}
    assert parse('https://example.com/path/to/page?fruit=apple&color=red') == {'fruit': 'apple', 'color': 'red'}
    assert parse('https://example.com/path/to/page?name=Roman&occupation=programmer') == {'name': 'Roman',
                                                                                          'occupation': 'programmer'}
    assert parse('https://example.com/path/to/page?country=Ukraine&language=Ukrainian') == {'country': 'Ukraine',
                                                                                            'language': 'Ukrainian'}
    assert parse('https://example.com/path/to/page?score=95&subject=Math') == {'score': '95', 'subject': 'Math'}
