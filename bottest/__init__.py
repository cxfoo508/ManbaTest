# coding = utf-8

import pytest

from bottest.modules.get_control import process_num, project_name, test_case, report_path
from bottest.modules.licence_control import init_licence
from bottest.modules.msg_control import SendMsg

init_licence()
case_info = test_case().split("||")
process = process_num()
project = project_name()
report_path = report_path()
run_info = [
    '--cache-clear',
    '-s',
    '--capture=fd',
    f'--html=report/{project}.html',
    '--self-contained-html'
]


def pytest_run():
    """
    run case info
    """
    if process == "1":
        run_info.extend(case_info)
    else:
        run_info.extend(case_info)
        run_info.append(f"-n={process}")
    return run_info


def main():
    pytest.main(pytest_run())
    SendMsg.send_json(report_path)
    SendMsg.send_msg_v1(report_path)

