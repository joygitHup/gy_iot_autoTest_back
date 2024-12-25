import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
# root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
# sys.path.append(root_path)
report_save_path=os.path.abspath(os.path.join(os.getcwd(), ".."))
report_path=report_save_path+r'/gy_iot_autoTest_back/result'
alluredir_path=report_save_path+r'/gy_iot_autoTest_back/report'
test_case=report_save_path+r'/gy_iot_autoTest_back/test_case'
SccreShort=report_save_path+r'/gy_iot_autoTest_back/img'

print(report_save_path)




