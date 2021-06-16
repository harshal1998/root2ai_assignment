from django.shortcuts import render
from .models import *
import pandas as pd
import csv
import psycopg2
import numpy as np

with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    c = len(next(reader))

    for i in reader:
        temp = demo.objects.values_list('a', flat=True)
        if i[0] in temp:
            continue
        else:
            d = demo(a=i[c - 19], b=i[c - 18], c=i[c - 17], d=i[c - 16], e=i[c - 15], f=i[c - 14], g=i[c - 13],
                     h=i[c - 12], i=i[c - 11], j=i[c - 10], k=i[c - 9], l=i[c - 8], m=i[c - 7], n=i[c - 6], o=i[c - 5],
                     p=i[c - 4], q=i[c - 3], r=i[c - 2], s=i[c - 1])
            d.save()


def display(request):
    # a = pd.read_sql_query('select * from app_demo', con=engine)
    data = demo.objects.all()
    return render(request, 'a.html', {"data": data})
