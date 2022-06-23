import os
from tools.build_module import OperationExcel
dir_path = "/Users/chengxinfei/Downloads"
files = os.listdir(dir_path)
for file in files:
    if "吾来" in file and "测试用例" in file and file.endswith('.xlsx') and "saas全量" not in file:
        excelPath = f"/Users/chengxinfei/Downloads/{file}"
        print("alter start:"+excelPath)
        excel = OperationExcel(excel_path=excelPath)
        # 修改创建人，重要程度,用例步骤，预期结果
        values = excel.get_values()
        for i in range(len(values)):
            person = "关璐"
            level = "P1"
            excel.update_excel(i, 2, person)
            excel.update_excel(i, 4, level)
            step = values[i][6]
            result = values[i][7]
            if step != "":
                step = '1.' + str(step).replace('\n', '').strip()
                result = '1.' + str(result).replace('\n', '').strip()
            excel.update_excel(i, 3, "功能测试")
            excel.update_excel(i, 6, step)
            excel.update_excel(i, 7, result)
        print("alter end:"+excelPath)
