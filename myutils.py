import requests
from pathlib import Path
import json
import re


def moodle_log_in(id, password):
    s = requests.Session()
    payload = {
        'username': id,
        'password': password
    }
    # res = s.post('https://lemida.biu.ac.il/blocks/login_ldap/login.php', json=payload)
    # s.headers.update({'authorization': json.loads(res.content)['token']})
    # print(res.content)
    # return s
    with requests.Session() as s:
        p = s.post('https://lemida.biu.ac.il/blocks/login_ldap/login.php', data=payload)
        p1 = s.post('https://lemida.biu.ac.il/course/view.php?id=67199', data=payload)

        # print the html returned or something more intelligent to see if it's a successful login page.
        # print (p.text)

        f = open('moodle.html', 'w', encoding='utf-8')
        f.write(p1.text)
        f.close()

        indices_of_files = [i for i in range(len(p1.text)) if
                            p1.text.startswith('https://lemida.biu.ac.il/mod/resource/view.php?id=', i)]
        print(indices_of_files)
        urls_of_files = set()
        for index in indices_of_files:
            file_url = p1.text[index:index + len('https://lemida.biu.ac.il/mod/resource/view.php?id=') + 7]
            urls_of_files.add(file_url)
            print(file_url)

        # i = 1
        # for url in urls_of_files:
        #     p2 = s.post(url, data=payload)
        #     # start_index = p2.text.find('https://lemida.biu.ac.il/pluginfile.php')
        #     # end_index = find_index_of_substring(p2.text, 'pdf', start_index) + 3
        #     # real_url = p2.text[start_index:end_index]
        #     # print(real_url)
        #     name = 'num' + str(i) + '.pdf'
        #     with open(name, 'wb') as fd:
        #         fd.write(p2.text.encode())
        #     i +=1

        # i = 1
        # for url in urls_of_files:
        #
        #     name = 'num' + str(i) + '.pdf'
        #     r = requests.get(url, stream=True)
        #     with open(name, 'wb') as fd:
        #         for chunk in r.iter_content(1024):
        #             fd.write(chunk)
        #     i += 1

def find_index_of_substring(text, pattern, start_from):
    sliced_text = text[start_from:]
    index = sliced_text.find(pattern)
    index = start_from + index
    return index

#if __name__ == "__main__":
    session = moodle_log_in('207424490', 'Learning10')
