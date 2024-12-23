import os
import  sys
current_directory = os.path.dirname(os.path.abspath(__file__))
root_path = os.path.abspath(os.path.dirname(current_directory) + os.path.sep + ".")
sys.path.append(root_path)
from config import path_config
class create_File_path():
    '''将报告和日志输送到指定文件'''
    def create_File_path_report(self):
        report_save_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        report_path = report_save_path + '\\report'
        return report_path
    def creat_file_path_log(self):
        log_save_path = os.path.abspath(os.path.join(os.getcwd(), ".."))
        log_path = log_save_path + '\\log'
        return log_path
if __name__=="__main__":
    op=create_File_path()
    print(op.create_File_path_report())
    print(op.creat_file_path_log())