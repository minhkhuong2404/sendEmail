from crontab import CronTab

cron = CronTab('minhkhuonglu')

job = cron.new(command='/usr/bin/python python sendEmail.py')
job.minute.every(1)
print(job.enable())
for job in cron:
    print(job)
cron.write()

cron.remove(job)
# remove all
# cron.remove_all()
# for job in cron:
#     print(job)