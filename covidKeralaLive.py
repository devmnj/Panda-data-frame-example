import json
import pandas as pd
import datetime
import matplotlib.pyplot as plt
import urllib2
import seaborn as sns

def getDistrictData(data,dist):
    ddata=data["Kerala"]["districtData"][dist]
    return ddata
        

def main():    
    urldata = 'https://api.covid19india.org/state_district_wise.json'
    weburl = urllib2.urlopen(urldata)
    print("result code :" + str(weburl.getcode()))
    if (weburl.getcode() == 200):        
        data = weburl.read()
        jdata=json.loads(data)
        mpm=getDistrictData(jdata,"Malappuram")
        pkd=getDistrictData(jdata,"Palakkad")
        thrs=getDistrictData(jdata,"Thrissur")
        khz=getDistrictData(jdata,"Kozhikode")
        alp=getDistrictData(jdata,"Alappuzha")
        erk=getDistrictData(jdata,"Ernakulam")
        idk=getDistrictData(jdata,"Idukki")
        kan=getDistrictData(jdata,"Kannur")
        kaz=getDistrictData(jdata,"Kasaragod")
        kol=getDistrictData(jdata,"Kollam")
        ktm=getDistrictData(jdata,"Kottayam")
        pat=getDistrictData(jdata,"Pathanamthitta")
        wyd=getDistrictData(jdata,"Wayanad")
        tvm=getDistrictData(jdata,"Thiruvananthapuram")
        
     
        con_kz= khz["confirmed"]
        con_thr= thrs["confirmed"]
        con_mpm= mpm["confirmed"]
        con_pkd= pkd["confirmed"]
        con_alp=alp["confirmed"]
        con_erk= erk["confirmed"]
        con_idk= idk["confirmed"]
        con_kan= kan["confirmed"]
        con_kaz= kaz["confirmed"]
        con_kol= kol["confirmed"]
        con_ktm= ktm["confirmed"]
        con_pat= pat["confirmed"]
        con_wyd= wyd["confirmed"]
        con_tvm= tvm["confirmed"]
  
        
        data={'confirmed':[con_kz,con_mpm,con_pkd,con_thr,con_alp,con_erk,con_idk,con_kan,con_kaz,con_kol,con_ktm,con_pat,con_wyd,con_tvm]}        
        df2= pd.DataFrame(data,columns=['confirmed'],index=['Kozhikode','Malappuram','Palakkad','Thrissur','Alappuza',
                          'Ernakulam','Idukki','Kannur','Kasaragod','Kollam','Kottayam','Pathanamthitta','Wayanad',"Thiruvananthapuram"])
        df2.plot.pie(y='confirmed',figsize=(13,13),autopct='%1.1f%%',startangle=90)
        dt = datetime.date.today()
        plt.title('Convid-19 Update-Confirmed-[Kerala] - Powered by Python and Pandas - [developerm.dev]-%s ' %dt)
        plt.text(-1,-1,'Data obtained from https://api.covid19india.org/')
        plt.legend(loc='lower center',ncol=7)
        plt.savefig('covidkereala_confirmed_cases%s' %dt)      
        
        print(df2)
        
        
        dec_kz= khz["deceased"]
        dec_thr= thrs["deceased"]
        dec_mpm= mpm["deceased"]
        dec_pkd= pkd["deceased"]
        dec_alp=alp["deceased"]
        dec_erk= erk["deceased"]
        dec_idk= idk["deceased"]
        dec_kan= kan["deceased"]
        dec_kaz= kaz["deceased"]
        dec_kol= kol["deceased"]
        dec_ktm= ktm["deceased"]
        dec_pat= pat["deceased"]
        dec_wyd= wyd["deceased"]
        dec_tvm= tvm["deceased"]
        
        data={'deceased':[dec_kz,dec_mpm,dec_pkd,dec_thr,dec_alp,dec_erk,dec_idk,dec_kan,dec_kaz,dec_kol,dec_ktm,dec_pat,dec_wyd,dec_tvm]}        
        df2= pd.DataFrame(data,columns=['deceased'],index=['Kozhikode','Malappuram','Palakkad','Thrissur','Alappuza',
                          'Ernakulam','Idukki','Kannur','Kasaragod','Kollam','Kottayam','Pathanamthitta','Wayanad',"Thiruvananthapuram"])
        df2.plot.pie(y='deceased',figsize=(13,13),autopct='%1.1f%%',startangle=90)
        dt = datetime.date.today()
        plt.title('Convid-19 Update-Deceased- [Kerala] - Powered by Python and Pandas - [developerm.dev]-%s ' %dt)
        plt.text(-1,-1,'Data obtained from https://api.covid19india.org/')
        plt.legend(loc='lower center',ncol=7)
        plt.savefig('covidkereala_deceased_cases%s' %dt)       
        
        
        rec_kz= khz["recovered"]
        rec_thr= thrs["recovered"]
        rec_mpm= mpm["recovered"]
        rec_pkd= pkd["recovered"]
        rec_alp=alp["recovered"]
        rec_erk= erk["recovered"]
        rec_idk= idk["recovered"]
        rec_kan= kan["recovered"]
        rec_kaz= kaz["recovered"]
        rec_kol= kol["recovered"]
        rec_ktm= ktm["recovered"]
        rec_pat= pat["recovered"]
        rec_wyd= wyd["recovered"]
        rec_tvm= tvm["recovered"]
        
        data={'recovered':[rec_kz,rec_mpm,rec_pkd,rec_thr,rec_alp,rec_erk,rec_idk,rec_kan,rec_kaz,rec_kol,rec_ktm,rec_pat,rec_wyd,rec_tvm]}        
        df2= pd.DataFrame(data,columns=['recovered'],index=['Kozhikode','Malappuram','Palakkad','Thrissur','Alappuza',
                          'Ernakulam','Idukki','Kannur','Kasaragod','Kollam','Kottayam','Pathanamthitta','Wayanad',"Thiruvananthapuram"])
        df2.plot.pie(y='recovered',figsize=(13,13),autopct='%1.1f%%',startangle=90)
        dt = datetime.date.today()
        plt.title('Convid-19 Update -recovered-[Kerala] - Powered by Python and Pandas - [developerm.dev]-%s ' %dt)
        plt.text(-1,-1,'Data obtained from https://api.covid19india.org/')
        plt.legend(loc='lower center',ncol=7)
        plt.savefig('covidkereala_recovered_cases%s' %dt)       
        print(df2)
        
        act_kz= khz["active"]
        act_thr= thrs["active"]
        act_mpm= mpm["active"]
        act_pkd= pkd["active"]
        act_alp=alp["active"]
        act_erk= erk["active"]
        act_idk= idk["active"]
        act_kan= kan["active"]
        act_kaz= kaz["active"]
        act_kol= kol["active"]
        act_ktm= ktm["active"]
        act_pat= pat["active"]
        act_wyd= wyd["active"]
        act_tvm= tvm["active"]
        
        data={'active':[act_kz,act_mpm,act_pkd,act_thr,act_alp,act_erk,act_idk,act_kan,act_kaz,act_kol,act_ktm,act_pat,act_wyd,act_tvm]}        
        df2= pd.DataFrame(data,columns=['active'],index=['Kozhikode','Malappuram','Palakkad','Thrissur','Alappuza',
                          'Ernakulam','Idukki','Kannur','Kasaragod','Kollam','Kottayam','Pathanamthitta','Wayanad',"Thiruvananthapuram"])
        df2.plot.pie(y='active',figsize=(13,13),autopct='%1.1f%%',startangle=90)
        dt = datetime.date.today()
        plt.title('Convid-19 Update -active- [Kerala] - Powered by Python and Pandas - [developerm.dev]-%s ' %dt)
        plt.text(-1,-1,'Data obtained from https://api.covid19india.org/')
        plt.legend(loc='lower center',ncol=7)
        plt.savefig('covidkereala_active_cases%s' %dt)     
        
        
        
        ax = plt.gca()
        df3= pd.DataFrame({'districts':['Kozhikode','Malappuram','Palakkad','Thrissur','Alappuza',
                          'Ernakulam','Idukki','Kannur','Kasaragod','Kollam','Kottayam','Pathanamthitta','Wayanad',"Thiruvananthapuram"],
    'active':[act_kz,act_mpm,act_pkd,act_thr,act_alp,act_erk,act_idk,act_kan,act_kaz,act_kol,act_ktm,act_pat,act_wyd,act_tvm],
    'confirmed':[con_kz,con_mpm,con_pkd,con_thr,con_alp,con_erk,con_idk,con_kan,con_kaz,con_kol,con_ktm,con_pat,con_wyd,con_tvm]}
    )
 
  
    else:
        print "Some server related error occurs"


if __name__ == "__main__":
    main()
# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

