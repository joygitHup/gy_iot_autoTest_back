import os
import sys
current_directory = os.path.dirname(os.path.abspath(__file__))
# root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
# sys.path.append(root_path)
report_save_path=os.path.abspath(os.path.join(os.getcwd(), ".."))
report_path=report_save_path+r'\gy_iot_autotest\reports'
alluredir_path=report_save_path+r'\gy_iot_autotest\result'
test_case=report_save_path+r'\gy_iot_autotest\test_case'
SccreShort=report_save_path+r'\gy_iot_autotest\img'

print(test_case)




