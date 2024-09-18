from sqlalchemy import create_engine
import pandas as pd
from scipy import stats
import time

def str_time_prop(start, end, time_format, prop):
  stime = time.mktime(time.strptime(start, time_format))
  etime = time.mktime(time.strptime(end, time_format))

  ptime = stime + prop * (etime - stime)

  return time.strftime(time_format, time.localtime(ptime))

def random_date(start, end, prop):
  return str_time_prop(start, end, '%Y-%m-%d %H:%M:%S', prop)

def fabricate_data(n):
  df = pd.DataFrame()
  df.index.rename('id')
  df['total'] = stats.norm.rvs(50000, 20000, n).round().astype(int)
  df['customer_id'] = stats.uniform.rvs(1, 250000, n).round().astype(int)
  df['created_at'] = [
    random_date('2010-01-01 00:00:00', '2018-12-31 23:59:59', x)
    for x in stats.uniform.rvs(0, 1, n)
  ]
  return df

mio2_5 = 2500000
# df = fabricate_data(mio2_5)
# engine = create_engine('postgresql://postgres:mypass@localhost:5432/exampledb')
# df.to_sql('orders', engine, if_exists='append')