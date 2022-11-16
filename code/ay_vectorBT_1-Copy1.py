#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# ay_vectorBT_1 for Hang Seng Index using moving average


# In[180]:


pip install vectorbt


# In[181]:


import vectorbt as vbt

#vbt.settings.data['alpaca']['key_id'] = 'Your API Key'
#vbt.settings.data['alpaca']['secret_key'] = 'Your Secret Key'


# In[182]:


#alpacadata = vbt.AlpacaData.Download(symbol='AAPL', start='4 days ago UTC`, end=`1 day ago UTC`)

#alpaca.get_data()


# In[183]:


# Hong Kong Hang Seng Index using moving average 


# In[184]:


data=vbt.YFData.download("HSI", interval="1d", start='2020-01-01', end='2022-11-01')


# In[185]:


data_close=data.get("Close")


# In[186]:


data_close.head()


# In[187]:


data_close.tail()


# In[188]:


# Parameters


# In[189]:


ma_fast=vbt.MA.run(data_close,8)


# In[190]:


ma_slow=vbt.MA.run(data_close,10)


# In[191]:


entries=ma_fast.ma_crossed_above(ma_slow)


# In[192]:


exits=ma_fast.ma_crossed_below(ma_slow)


# In[193]:


# Run the program


# In[194]:


pf=vbt.Portfolio.from_signals(data_close, entries=entries, exits=exits, freq="d")


# In[195]:


# HSI % Return


# In[196]:


pf.total_return()*100


# In[197]:


# Print the Win Rate in %


# In[198]:


metric="positions.win_rate"


# In[199]:


pf_perf=pf.deep_getattr(metric)


# In[200]:


print(pf_perf*100)


# In[201]:


# Statistics


# In[202]:


pf.stats()


# In[203]:


# Print Trade details


# In[204]:


print(pf.orders.records_readable)


# In[205]:


# Chart


# In[206]:


fig=pf.plot(subplots= ['cum_returns', 'orders','trade_pnl'])


# In[207]:


fig.show()


# In[208]:


###########################################################################################


# In[ ]:


# DJI using moving average


# In[212]:


data=vbt.YFData.download("DJI", interval="1d", start='2020-01-01', end='2022-11-01')


# In[213]:


data_close=data.get("Close")


# In[214]:


data_close.head()


# In[215]:


# Parameters


# In[216]:


ma_fast=vbt.MA.run(data_close,8)


# In[217]:


ma_slow=vbt.MA.run(data_close,10)


# In[218]:


entries=ma_fast.ma_crossed_above(ma_slow)


# In[219]:


exits=ma_fast.ma_crossed_below(ma_slow)


# In[220]:


# Run


# In[221]:


pf=vbt.Portfolio.from_signals(data_close, entries=entries, exits=exits, freq="d")


# In[222]:


# DJI Return in % 


# In[223]:


pf.total_return()*100


# In[224]:


# DJI % Win Rate


# In[225]:


metric="positions.win_rate"


# In[226]:


pf_perf=pf.deep_getattr(metric)


# In[227]:


print(pf_perf*100)


# In[228]:


# DJI Statistics


# In[229]:


pf.stats()


# In[230]:


# DJI Trade Details


# In[231]:


print(pf.orders.records_readable)


# In[232]:


# Charts


# In[233]:


fig=pf.plot(subplots= ['cum_returns', 'orders','trade_pnl'])


# In[234]:


fig.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




