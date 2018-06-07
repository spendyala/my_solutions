import requests

list_registrars = []
processed = set()
response = requests.get('https://www.icann.org/registrar-reports/accredited-list.html')
with open('registrant_1.log', 'w') as registrant_log:
    registrant_log.write('Example\n')
    for each_line in response.text.split('\n'):
        if 'td><a href' in each_line:
            _, url, name, *_ = each_line.split('"')
            name = name.replace('>', '').split('</a')[0]
            try:
                if url in processed:
                    continue
                acc_reg_res = requests.get(url, timeout=5)
                if acc_reg_res.status_code == 200:
                    processed.add(url)
                    registrant_log.write('%s|||%s\n' % (url, name))
                    print(url, name)
            except Exception:
                try:
                    acc_reg_res = requests.get(url.replace('https://', 'http://'), timeout=5)
                    if acc_reg_res.status_code == 200:
                        processed.add(url)
                        registrant_log.write('%s|||%s\n' % (url, name))
                        print(url, name)
                except Exception:
                    print('ERROR', url, name)
                    registrant_log.write('%s|||%s|||%s\n' % ('ERROR', url, name))
                    pass
