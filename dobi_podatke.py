import re
import orodja

pattern = re.compile(
    r'<tr id="gamelog\.(?P<st_tekme>\d+)" >.*?'
    r'data-stat="age" >(?P<starost>\d{2}-\d{3})<.*?'
    r'data-stat="opp_id" ><a href="/teams/(?P<nasprotnik>\D{3})/\d{4}.html">.*?'
    r'data-stat="goals" >(?P<zadetki>\d)<.*?'
    r'data-stat="assists" >(?P<asistence>\d)<.*?'
    r'data-stat="points" >(?P<tocke>\d)<.*?'
    r'data-stat="plus_minus" >(?P<plus_minus>-?\d)<.*?'
    r'data-stat="pen_min" >(?P<kazni>\d)<.*?'
    r'data-stat="shots" >(?P<streli>\d)<.*?'
    ,
    flags=re.DOTALL)
    

sez = []
sezone = list(range(1991,2005)) + list(range(2006,2009)) + list(range(2012,2018))
for i in sezone:
    ime_datoteke = "Jagr{}-{}.html".format("%02d" %((i-1)%100), "%02d" % (i%100))
    print(ime_datoteke)
    with open(ime_datoteke) as f:
        iterator = re.finditer(pattern, f.read())
        for tekma in iterator:
            sez.append(tekma.groupdict())
            

orodja.zapisi_tabelo(sez,['st_tekme','starost','nasprotnik','zadetki','asistence','tocke','plus_minus','kazni','streli'],'jagr.csv')
                                
print("Končano!")                        
                                       
   
    
    
