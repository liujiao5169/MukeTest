# coding=utf-8
from keywordselenium.actionMethod import ActionMethod
from util.excel_init import ExcelInit


# 执行Excel测试用例，写入测试结果
class KeywordCase(object):
    def run_main(self):
        self.action_method = ActionMethod()
        excel_handle = ExcelInit("C:/Users/TSDLJ/PycharmProjects/UITest_muke/config/keyword.xls")
        # 获取总行行数
        lines = excel_handle.get_lines()
        # 循环行数执行case
        for i in range(1, lines):
            is_run = excel_handle.get_col_value(i, 3)
            if is_run == 'yes':
                method = excel_handle.get_col_value(i, 4)
                send_value = excel_handle.get_col_value(i, 5)
                handle_value = excel_handle.get_col_value(i, 6)
                except_method = excel_handle.get_col_value(i, 7)
                except_result = excel_handle.get_col_value(i, 8)
                self.run_method(method, handle_value, send_value)
                if except_result:
                    except_value = self.except_value(except_result)
                    if except_value[0] == "text":
                        result = self.run_method(except_method)
                        if except_value[1] in result:
                            excel_handle.write_value(i, "pass")
                        else:
                            excel_handle.write_value(i, "fail")
                    elif except_value[0] == "element":
                        result = self.run_method(except_method, except_value[1])
                        print(result)
                        if result:
                            excel_handle.write_value(i, "pass")
                        else:
                            excel_handle.write_value(i, "fail")
                else:
                    print("没有预期结果")

    def except_value(self, data):
        return data.split("=")

    def run_method(self, method, handle_value='', send_value=''):
        method_value = getattr(self.action_method, method)
        # if有输入数据
        if send_value != '' and handle_value != '':
            # 执行方法（key，value）
            result = method_value(handle_value, send_value)
        # 没有输入数据
        elif send_value == '' and handle_value != '':
            # 执行方法（key）
            result = method_value(handle_value)
        elif send_value == '' and handle_value == '':
            result = method_value()
        else:
            result = method_value(send_value)
        return result


if __name__ == '__main__':
    test = KeywordCase()
    test.run_main()
