import os

project_path = os.path.split(os.path.split(os.path.realpath(__file__))[0])[0]

# 截图存放目录
screenshot_path = os.path.join(project_path, 'TestResult', 'screenshot')
log_path = os.path.join(project_path, 'TestResult', 'log')
