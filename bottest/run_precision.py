from engine_case.test_precision import PrecisionCase

if __name__ == '__main__':

    # file_name = "{51Talk（未缩减）}知识点_2021-03-31 07_08_25"
    # file_name = '{Dior知识库（未缩减）}知识点_2021-03-31 07_03_51'
    # file_names = ["51talktop100", 'Niketop100', '新东方top100', '育学园top100', '迪奥top100']
    file_names = ["育学园top100"]
    for f in file_names:
        file_path = f"/Users/chengxinfei/PycharmProjects/MyCode/data/"
        pre = PrecisionCase(file_path, f)
        pre.process_run(10)
