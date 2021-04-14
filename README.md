# apscheduler

## tested version specs
- python 3.8.3
- django 3.1.7


## packages & django setup commands (just to share)
- pip install django==3.1.7
- pip install apscheduler
- pip install django-apscheduler
- pip instal mysqlclient

- django-admin startproject [project-name]
- (moved to [project-directory])
- django-admin startapp scheduler 

## updated or created files
- settings.py
- conf/database/mariadb/my.cnf (synchronize with your database)
- scheduler/scheduler.py
- scheduler/apps.py
- scheduler/models.py

## simple steps to use apscheduler
1. update settings.py file
2. update my.cnf file with proper database info
3. python manage.py makemigrations (make migrations for apscheduler related tables & comment Info model in models.py if you don't want to create Info table)
4. python manage.py migrate
5. python manage.py runserver --noreload( --noreload is needed to prevent duplicate schedulers)
6. check if scheduler works and data is inserted
7. add proper scheduler jobs and time period
8. cron trigger type  parameter tuning(https://apscheduler.readthedocs.io/en/stable/modules/triggers/cron.html)
9. interval trigger paramter tuning(https://apscheduler.readthedocs.io/en/stable/modules/triggers/interval.html#module-apscheduler.triggers.interval)

## apscheduler vs. celery 
- https://www.programmersought.com/article/6923889412/


## bugs to be fixed
- apscheduler <-> database timezone synchronization 
- table django_apscheduler_djangojob [job_state] column encoding problem
  
