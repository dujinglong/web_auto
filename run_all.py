import unittest
from common import HTMLTestRunner_cn
# 用例路径
casePath = "D:\\python3.7\\web_auto\\case"
rule = "test*.py"
# discover = unittest.defaultTestLoader.discover(start_dir=casePath,pattern=rule)
discover = unittest.defaultTestLoader.discover(casePath)
print(discover)
reportPath = "D:\\python3.7\\web_auto\\report\\" + "result.html"
fp = open(reportPath, "wb")
runner = HTMLTestRunner_cn.HTMLTestRunner(stream=fp, title="报告名称", description="描述：商家后台测试报告", retry=1)
runner.run(discover)
fp.close()