#文件路径信息
# 适应docker 环境下面的Linux环境配置
# FilePath={
#    'filePath':{
#       'report_path':'/var/jenkins_home/workspace/guoyin_auto_app/allure-report/',
#       'report_save_path':'/var/jenkins_home/workspace/guoyin_auto_app/allure-report/',
#       # 'log_save_path':'C:\devlopePath\yj_autoTest_UI\\log\\',
#       # 'SccreShort_save_path':'C:\\devlopePath\\yj_autoTest_UI\\SccreShrot\\',
#       'all_test_position':"/var/jenkins_home/workspace/guoyin_auto_app/"
#    }
# }
# 适应环境window环境的开发路径
FilePath={
   'filePath':{
      'report_path':'D:\\devlopePath\\gy_iot_autoTest\\reports',
      'report_save_path':'D:\\devlopePath\\gy_iot_autoTest\\reports',
      # 'log_save_path':'C:\devlopePath\yj_autoTest_UI\\log\\',
      'SccreShort_save_path':'D:\\devlopePath\\gy_iot_autoTest\\img',
      'all_test_position':"D:\\devlopePath\\gy_iot_autoTest\\test_case"
   }
}
REPORT_PATH=FilePath['filePath']['report_path']
REPORT_SAVE_PATH=FilePath['filePath']['report_save_path']
# LOG_SAVE_PATH=FilePath['filePath']['log_save_path']
SccreShort_SAVE_PATH=FilePath['filePath']['SccreShort_save_path']
"""所有测试用例的位置"""
test_all_path=FilePath['filePath']['all_test_position']



