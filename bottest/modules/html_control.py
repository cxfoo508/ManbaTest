from bs4 import BeautifulSoup


class html_control:
    @classmethod
    def get_report_data(cls, path):
        with open(f'{path}/test.html', 'r', errors='ignore') as file:
            html = file.read()
        soup = BeautifulSoup(html, 'lxml')
        tables = soup.find_all('table')
        tbodys = tables[1].find_all('tbody')
        pass_num, faild_num, sum_num = 0, 0, 0
        range_len = len(tbodys)
        for i in range(range_len):
            trs = tbodys[i].find_all('tr')
            tds = trs[0].find_all('td')
            if tds[0].text == 'Failed':
                faild_num += 1
            elif tds[0].text == 'Passed':
                pass_num += 1
            sum_num += 1
        return pass_num, faild_num, sum_num
