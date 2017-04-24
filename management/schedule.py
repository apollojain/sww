import datetime 
from apscheduler.scheduler.blocking import BlockingScheduler

def run_function(f, run_date, args): 
	sched = BlockingScheduler 
	sched.add_job(f, 'date', run_date=run_date, args=args)
	sched.start()