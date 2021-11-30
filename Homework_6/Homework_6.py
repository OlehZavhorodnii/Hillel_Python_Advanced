def parse_parameters(link: str) -> dict:
    list_of_params = link.split('?')[1].split('&')
    params = {}
    if list_of_params == ['']:
        params = {}
    else:
        for i in list_of_params:
            s = i.split('=')
            params.update({s[0]: s[1]})
    return params


def parse_cookies(cookies: str) -> dict:
    list_of_user_params = cookies.split(';')
    list_cookies = []
    for i in list_of_user_params:
        if i != '':
            list_cookies.append(i)
    user_params = {}
    if list_cookies == ['']:
        user_params = {}
    else:
        for i in list_cookies:
            s = i.split('=')
            user_params.update({s[0]: s[1]})
    return user_params


if __name__ == '__main__':
    # Tests for function "parse_parameters"
    assert parse_parameters('http://example.com/?') == {}
    assert parse_parameters('https://example.com/path/to/page?name=ferret&color=purple') == \
           {'name': 'ferret', 'color': 'purple'}
    assert parse_parameters('https://www.google.com/search?q=dict+python&oq=dict&aqs='
                            'chrome.3.69i57j0i512l5j69i60j69i61.4601j0j7&sourceid=chrome&ie=UTF-8') == \
           {'q': 'dict+python', 'oq': 'dict', 'aqs': 'chrome.3.69i57j0i512l5j69i60j69i61.4601j0j7',
            'sourceid': 'chrome', 'ie': 'UTF-8'}
    assert parse_parameters('https://www.google.com/webhp?hl=uk&sa=X&ved=0ahUKEwif4O6-zJv0AhXh57sIHVBLAusQPAgI') == \
           {'hl': 'uk', 'sa': 'X', 'ved': '0ahUKEwif4O6-zJv0AhXh57sIHVBLAusQPAgI'}
    assert parse_parameters('https://www.youtube.com/watch?v=UbpoC2Y9DIA&ab_channel=GeoHistory') == \
           {'v': 'UbpoC2Y9DIA', 'ab_channel': 'GeoHistory'}

    # Tests for function "parse_cookies"
    assert parse_cookies('') == {}
    assert parse_cookies('name=Dima;') == {'name': 'Dima'}
    assert parse_cookies('id=1115.220;ip=187.162.102.158;age=18') == \
           {'id': '1115.220', 'ip': '187.162.102.158', 'age': '18'}
    assert parse_cookies('size=1360x768;browser=Chrome;OS=Ubuntu;') == \
           {'size': '1360x768', 'browser': 'Chrome', 'OS': 'Ubuntu'}
    assert parse_cookies(';') == {}
