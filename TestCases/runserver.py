
from concurrent.futures import ThreadPoolExecutor

from TestCases import entrance
from entity.opertation_file import properties
import os,settings,pytest,time

def ExecutorTestCase(server='',model=''):
    # 生成测试结果
    model_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__))) + os.path.sep + 'TestCases'
    run_model = model_path + os.path.sep + server + os.path.sep + model
    result_dir = settings.REPORT_RESULT
    run_cmd = ['-q', '-s', '--timeout-method=thread', '--timeout=120', run_model,
               '--alluredir={dir}'.format(dir=result_dir)]
    pytest.main(run_cmd)

    # 写入ENV环境参数
    properties()

    # 启动报告服务
    entrance.restart()

if __name__ == '__main__':
    thread_pool = ThreadPoolExecutor(20)
    server = 'Demo'
    model = 'DemoXiaoth'
    thread_pool.submit(ExecutorTestCase,server,model)