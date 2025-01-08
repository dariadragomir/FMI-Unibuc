import schedule
import time
import django
import os
import sys
from aplicatie import tasks
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'proiect1.settings')
django.setup()

def run_scheduler():
    schedule.every(120).seconds.do(tasks.delete_unconfirmed_users)
    schedule.every().monday.at("12:00").do(tasks.send_newsletter) 
    schedule.every().day.at("00:00").do(tasks.custom_task_1)
    schedule.every().day.at("12:00").do(run_monthly_task, tasks.custom_task_2, day=15)
    while True:
        schedule.run_pending()
        time.sleep(1)
        
def run_monthly_task(task_func, day):
    from datetime import datetime
    if datetime.now().day == day:
        task_func()
if __name__ == "__main__":
    try:
        run_scheduler()
    except KeyboardInterrupt:
        print("Scheduler oprit manual.")
        sys.exit()
   

#python /Users/dariadragomir/Facultate/AN2/SEM1/Django/proiect_django/ruleaza_taskuri.py