from django.shortcuts import render
from .models import *
import pandas as pd
import csv
import psycopg2


with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    # Skip the header row.
    for i in reader:
        temp = demo.objects.values_list('a', flat=True)
        if i[0] in temp:
            continue
        else:
            d = demo(a=i[0], b=i[1], c=i[2], d=i[3], e=i[4], f=i[5], g=i[6], h=i[7], i=i[8], j=i[9], k=i[10], l=i[11],
                     m=i[12], n=i[13], o=i[14], p=i[15], q=i[16], r=i[17], s=i[18])
            d.save()


def display(request):
    # a = pd.read_sql_query('select * from app_demo', con=engine)
    data = demo.objects.all()
    # print(a)
    return render(request, 'a.html', {"data": data})
