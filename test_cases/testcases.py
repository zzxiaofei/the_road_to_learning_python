import unittest
from common.httprequest import HttpRequest
from ddt import ddt, data, unpack, file_data
from common.read_excel_handle import ReadExcel

read_excel = ReadExcel(filepath=r'../data/testcase.xls')
case_data = read_excel.read_excel()


@ddt
class TestCases(unittest.TestCase):
    """测试用例类：xx接口项目"""

    @classmethod
    def setUpClass(self) -> None:
        self.session = HttpRequest()

    @data(*case_data)
    def test_case01(self, case_datas):
        """
        :method: Post,json传参（参数为字典类型）
        :method: Get, params传参（参数为字典类型）
        :method: form, form表单类型 data传参
        :return:
        """

        print(case_datas)
        apiName = case_datas[0]
        args = case_datas[2]
        method = case_datas[1]
        request_type = case_datas[5]
        tiqu = case_datas[6]
        url = 'http://127.0.0.1:7001/api/qingfeng/{}'.format(apiName)
        res = self.session.send_request(url=url, method=method, args=args, request_type=request_type, tiqu=tiqu)
        print(res)


if __name__ == '__main__':
    unittest.main()
