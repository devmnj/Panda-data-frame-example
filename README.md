# CovideKeralaUpdates
This `Python` script fetch latest Covid19 updates for the State of Kerala [India]. I also used panda to generate dataframes and plot the data. The `plots were automatically` saved as `PNG` file to `hard disk`

# API

`API` I used was provided by api.covid19india.org
  https://api.covid19india.org/state_district_wise.json 


# Screen Shot
`IDE` I used is Spyder which comes with Anaconda distribution
![IDE ScreenShot](https://github.com/manojap/CovideKeralaUpdates/blob/master/covidgithub.png)

# Panda DataFrames
``` 
 data={'confirmed':[con_kz,con_mpm,con_pkd,con_thr,con_alp,con_erk,con_idk,con_kan,con_kaz,con_kol,con_ktm,con_pat,con_wyd,con_tvm]}        
        df2= pd.DataFrame(data,columns=['confirmed'],index=['Kozhikode','Malappuram','Palakkad','Thrissur','Alappuza',
                          'Ernakulam','Idukki','Kannur','Kasaragod','Kollam','Kottayam','Pathanamthitta','Wayanad',"Thiruvananthapuram"])
 ```
 
 # Plots
 
 ````
 df2.plot.pie(y='confirmed',figsize=(13,13),autopct='%1.1f%%',startangle=90)
 ````
