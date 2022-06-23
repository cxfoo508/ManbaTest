"""
Create by 吹着风的包子 on 2019-05-07
"""
import os
import random

__author__ = "吹着风的包子"
x_file = os.path.abspath("./data/w2v_sgns_win1_d80.kv")
new_list = []
with open(x_file) as f:
    for i in range(100):
        lines = f.readline()
        # a = random.choice(lines)
        before_a = lines.strip().split(" ")
        temp_list = (before_a[0], before_a[1:])
        new_list.append(temp_list)
print(new_list)
# with open(x_file, 'r') as f:
#     for line in f:
#         curLine = line.strip().split(" ")
#         print(curLine)
# new_list = []
# new_list2 = []
# with open(x_file, encoding="utf-8") as f:
#     for line in f.readlines():
#         curLine = line.strip().split(" ")
#         new_list.append(curLine)
# new_list.pop(0)
# # new = {"key":new_list}
# for k in new_list:
#     if k:
#         temp_list = (k[0],k[1:])
#         print(temp_list)
#         new_list2.append(temp_list)
#         # temp_list.clear()
#
#     #     print(k[0])
#     #     print(k[1])
# #         new_list_2 = [k[0], k[1:]]
# #         new_list.append(new_list_2)
# #         new_list_2.clear()
# new = {"key": new_list2}
# # # # new_dict = {k[0]: k[1:] for k in new_list}
# with open("result.json", "w", encoding="utf-8") as fp:
#     json.dump(new, fp, ensure_ascii=False)
