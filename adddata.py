import csv
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'datacenter.settings')
django.setup()

from mysite.models import Post

with open("recycle.csv", newline="\n", encoding="utf-8") as csvfile:
	rows = csv.reader(csvfile, delimiter=",")
	for row in rows:
		print(row[1],row[2])
		newdata = Post(title =str(row[1]),body =str(row[2]))
		newdata.save()