# import json
#
# from case.
#
# skills = skills_data_new_calss()
# attr = dir(skills)
# attrs = []
# with open('new_case_data.py', 'w+') as file:
#     for i in attr:
#         if 'case' in i:
#             case = getattr(skills, i)
#             case_data = case[0]
#             asserts = case[1]
#             environbel = case[2]
#             param_001 = {
#                 "lable": "",
#                 "data": case_data,
#                 "functionClass": "",
#                 "function": 'app_action',
#                 "assert": asserts,
#                 "environ": environbel,
#                 "method": {}
#             }
#             # case_json = json.dumps(param_001)
#             file.write(f'{i}={param_001}\n')
