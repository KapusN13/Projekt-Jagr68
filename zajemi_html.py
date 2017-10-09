import orodja
import re

def zajemi_html():
    sezone = list(range(1991,2005))+list(range(2006,2009))+list(range(2012,2018)) #seznam sezon v katerij je nastopal
    osnova = "https://www.hockey-reference.com/players/j/jagrja01/gamelog/" #osnovni spletni naslov
    for sezona in sezone:
        naslov = "{}{}".format(osnova, sezona)
        ime_datoteke = "Jagr{}-{}.html".format("%02d" %((sezona-1)%100), "%02d" % (sezona%100))
        orodja.shrani(naslov, ime_datoteke)
        
zajemi_html()
