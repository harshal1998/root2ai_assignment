from django.shortcuts import render
from .models import *
import pandas as pd

# Create your views here.
# from sqlalchemy import create_engine
#
# #
# engine = create_engine('postgresql://postgres:root@localhost:5432/root2ai')
# df = pd.read_csv('data.csv')
# df.to_sql('app_demo', con=engine, if_exists='append', index=False)

import csv
import psycopg2

conn = psycopg2.connect("host=localhost dbname=root2ai user=postgres password=root")
cur = conn.cursor()
with open('data.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
 # Skip the header row.
    for row in reader:
        cur.execute(
            "INSERT INTO app_demo (a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",row
        )
conn.commit()


def display(request):
    # a = pd.read_sql_query('select * from app_demo', con=engine)
    data = demo.objects.all()
    # print(a)
    return render(request, 'a.html', {"data": data})
