# -*-coding:utf-8 -*-

"""
# File       : apschedulerClass.py
# Time       :2021/11/23 21:15
# Author     :zhengyong
# Description:
"""
from datetime import datetime
from apscheduler.schedulers.blocking import BlockingScheduler


def intervalJob():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def dateJob():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


def cronJob():
    print(datetime.now().strftime("%Y-%m-%d %H:%M:%S"))


if __name__ == '__main__':
    # 该示例代码生成了一个BlockingScheduler调度器，使用了默认的任务存储MemoryJobStore，以及默认的执行器ThreadPoolExecutor，并且最大线程数为10。
    # 每隔5秒钟执行一次
    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    scheduler = BlockingScheduler()
    # 采用阻塞的方式
    # 采用固定时间间隔（interval）的方式，每隔5秒钟执行一次
    scheduler.add_job(intervalJob, 'interval', seconds=5)
    '''
    weeks (int) – 间隔几周
    days (int) – 间隔几天
    hours (int) – 间隔几小时
    minutes (int) – 间隔几分钟
    seconds (int) – 间隔多少秒
    start_date (datetime|str) – 开始日期
    end_date (datetime|str) – 结束日期
    timezone (datetime.tzinfo|str) – 时区
    '''
    scheduler.start()

    # BlockingScheduler：在进程中运行单个任务，调度器是唯一运行的东西
    # 在特定的时间执行一次
    scheduler = BlockingScheduler()
    # 采用阻塞的方式
    # 采用date的方式，在特定时间只执行一次
    scheduler.add_job(dateJob, 'date', run_date='2018-09-21 15:30:00')
    scheduler.start()

    # 每天间隔10分钟执行一个任务
    scheduler = BlockingScheduler()
    scheduler.add_job(cronJob, 'cron', day_of_week='*', hour='*', minute='10')
    # 每隔一天 执行一次程序
    # scheduler.add_job(everyday_job, 'interval', days=1)
    # 每天早上十点半和十八点半各执行一次程序
    scheduler.add_job(cronJob, 'cron', hour='10, 18', minute='30')
    scheduler.start()

    #  可被2整除的通配符。
    scheduler.add_job(cronJob, 'cron', minute='*/2')

    # 6-8,11-12月第三个周五 00:00, 01:00, 02:00, 03:00运行
    scheduler.add_job(cronJob, 'cron', month='6-8,11-12', day='3rd fri', hour='0-3')
    # 每周一到周五运行 直到2024-05-30 00:00:00
    scheduler.add_job(cronJob, 'cron', day_of_week='mon-fri', hour=5, minute=30, end_date='2024-05-30')


__doc__ = """
    https://www.cnblogs.com/tian777/p/15584371.html
    
    func：Job执行的函数

    trigger：apscheduler定义的触发器，用于确定Job的执行时间，根据设置的trigger规则，计算得到下次执行此job的时间， 满足时将会执行
    
    args=None, kwargs=None
    
    id：指定作业的唯一ID
    
    name：指定作业的名字
    
    misfire_grace_time：Job的延迟执行时间，例如Job的计划执行时间是21:00:00，但因服务重启或其他原因导致21:00:31才执行，如果设置此key为40,则该job会继续执行，否则将会丢弃此job
    
    max_instances：执行此job的最大实例数，executor执行job时，根据job的id来计算执行次数，根据设置的最大实例数来确定是否可执行
    
    next_run_time：Job下次的执行时间，创建Job时可以指定一个时间[datetime],不指定的话则默认根据trigger获取触发时间
    
    coalesce：Job是否合并执行，是一个bool值。例如scheduler停止20s后重启启动，而job的触发器设置为5s执行一次，因此此job错过了4个执行时间，如果设置为是，则会合并到一次执行，否则会逐个执行
    
    executor：apscheduler定义的执行器，job创建时设置执行器的名字，根据字符串你名字到scheduler获取到执行此job的 执行器，执行job指定的函数
    """

