#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
# Python 2.7
import re
import curses, sys, os, signal,argparse,time
from multiprocessing import Process
from scapy.all import *
from subprocess import call, PIPE
from datetime import date, time, datetime



import os, sys
 
from PyQt4 import QtCore, QtGui

# ICI LA CLASSE CAPTURE

class Capture:
    def DebutCaptureTraffic(self,fichier,interface,duree):
        
        s=("timeout ---- tcpdump -i **** -s 0 -w ++++.pcap")
        s=s.replace("****", interface)
        s=s.replace("++++", fichier)
        s=s.replace("----", duree)
        call(s,shell=True)
           
            

# ICI LA CLASSE EXAMEN


class Archive:

    def CreationDossier(self,NomDossier):
        path = "/home/Archivage/+++++"
        path=path.replace("+++++","%s"%NomDossier)
        os.mkdir( path, 0777 );
        print "Le dossier a été crée avec succès"


class Examen: 

# Les informations concernant le fichier de capture
    def Capinfos(self,f):
             command=("capinfos ++++ > capinfos.txt")
             chaine=command.replace("++++","%s"%f)
             call(chaine, shell= True)
                  
             r=open('capinfos.txt','r')
             ligne=r.readlines()
             EncapsulationFichier=ligne[2].split("File encapsulation:")
             EncapsulationFichier=EncapsulationFichier[1].strip()
             TypeFichier=ligne[1].split("File type:")
             TypeFichier=TypeFichier[1].strip()
             NombrePaquets=ligne[4].split("Number of packets:")
             NombrePaquets=NombrePaquets[1].strip()
             TailleFichier=ligne[5].split("File size:")
             TailleFichier=TailleFichier[1].strip()
             DebutCapture=ligne[8].split("Start time:")
             DebutCapture=DebutCapture[1].strip()
             FinCapture=ligne[9].split("End time:")
             FinCapture=FinCapture[1].strip()
             DureeCapture=ligne[7].split("Capture duration:")
             DureeCapture=DureeCapture[1].strip()
             SHA1=ligne[14].split("SHA1:")
             SHA1=SHA1[1].strip()
             RIPEMD160=ligne[15].split("RIPEMD160:")
             RIPEMD160=RIPEMD160[1].strip()
             MD5=ligne[16].split("MD5:")
             MD5=MD5[1].strip()
             r.close()
             os.remove('capinfos.txt')
             return EncapsulationFichier,TypeFichier,NombrePaquets,TailleFichier,DebutCapture,FinCapture,DureeCapture,SHA1,RIPEMD160,MD5
           
            
           

#Le BSSID et le SSID de chaque point d'accès
             
    def BssidSsid(self,f):
          command="tcpdump -nne -r ++++ wlan[0]=0x80 | awk '{print $0}'> filebssid.txt"
          chaine=command.replace("++++","%s"%f)
          subprocess.call(chaine, shell=True)
          command="cat filebssid.txt|sort -u > tmp.txt"
          resultats=command
          subprocess.call(command,shell=True)
          os.remove('filebssid.txt')
        
    def search(self):
          f=open('tmp.txt','r')
          ligne=f.readlines()
          chaine1=[]
          chaine2=[]
          chaine3=[]
          for chaine in ligne:
            res2=re.search(r'CH: ([0-9]*)', chaine, re.I).group()
            res=re.search(r'BSSID:([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', chaine, re.I).group()
            res1= re.search(r'([(].*[)])', chaine, re.I).group()
            chaine1.append(res)
            chaine2.append(res2)
            chaine3.append(res1)
            chaine4=[]
          for chaine in chaine1:
            chaine=chaine.strip("BSSID:")
            chaine4.append(chaine)
          os.remove("tmp.txt")
          return chaine3,chaine4,chaine2
         
       
          #os.remove('tmp.txt')
      
           
          
      

#ICI LA CLASS ANALYSE
          
class Analyse:          
              
    
#Nombre de trames de données envoyées et reçues par le point d'accès    
    def NbrTramDataSendWAP(self,f,bssid):
        command="tshark -r fichier -R '((wlan.fc.type_subtype==0x20)&&(wlan.bssid==++++))'|wc -l > NbrTramDataSendWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        subprocess.call(x,shell=True)

        f=open('NbrTramDataSendWAP.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('NbrTramDataSendWAP.txt')
        return ligne
    def ssidAP(self,ssid,bssid1,bssid):
       
        for ch in bssid1:
                    if ch==bssid:
                        ssid=ssid[bssid1.index(ch)]
                        return ssid
#Le nombre de trames de données chiffrées
    def NbrTramDataCrypt(self,f,bssid):
        command="tshark -r fichier -R '((wlan.fc.type_subtype==0x20)&&(wlan.fc.protected==1))&&(wlan.bssid==++++)'|wc -l > NbrTramDataCrypt.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        subprocess.call(x,shell=True)
        f=open('NbrTramDataCrypt.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('NbrTramDataCrypt.txt')
        return ligne
    
#Type du chiffrement  
    def TypeDuChiffrement(self,f,bssid):
        a=Analyse()
        a.x=a.NbrTramDataSendWAP(f,bssid)
        a.y=a.NbrTramDataCrypt(f,bssid)
        if a.x==a.y:
            ligne="WEP"
        else:
            ligne="WPA"
        return ligne
           
               
        

              
#Les station associées au point d'accès                
    def StationAssocie(self,f,bssid):
             command="tcpdump -nne -r fichier 'wlan[0]=0x10 and wlan[26:2]=0x0000 and wlan src ++++' |awk '{print $0}'|sort|uniq -c|sort -nr > StationAssocie.txt"
             x=command.replace("++++","%s"%bssid)
             x=x.replace("fichier","%s"%f)
             subprocess.call(x,shell=True)
             r=open('StationAssocie.txt','r')
             ligne=r.readlines()
             chaine=[]
             for ch in ligne:
                exp=re.search(r'DA:([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})', ch, re.I).group()
                chaine.append(exp)
       
             i=0   
             while i in range(0, len(ligne)):
                 z=ligne[i].strip()
                 z=z.split(' ')
                 if z[i]!=chaine[i]:
                    i=i+1
                 else:
                    pos=i             
                    return str(pos)
                  
            #print chaine
    def StationAssocieResultat(self,f,bssid,position):
             command="tcpdump -nne -r fichier 'wlan[0]=0x10 and wlan[26:2]=0x0000 and wlan src ++++' |awk '{print $position}'|sort|uniq -c|sort -nr > StationAssocie.txt"
             y=command.replace("++++","%s"%bssid)
             y=y.replace("fichier","%s"%f)
             y=y.replace("position","%s"%position)
             subprocess.call(y,shell=True)
             r=open('StationAssocie.txt','r')
             ligne=r.readlines()
             x1=[]
             x2=[]
             for i in range(0, len(ligne)):
                 x=ligne[i].split(':',1)
                 x[1]=x[1].replace("\n"," ")
                 x[1]=x[1].strip()
                 x[0]=x[0].strip("DA")
                 x[0]=x[0].strip()
                 x1.append(x[1])
                 x2.append(x[0])
             r.close()  
             return x1, x2   
     
                
             #os.remove('StationAssocie.txt')  

#Nombre de trames de données envoyées par chaque station
    def NbrDataFramSendFromStation(self,f,bssid):
              command="tshark -r fichier -R '((wlan.fc.type_subtype==0x20)&&(wlan.fc.protected==1))&&(wlan.bssid==++++)' -T fields -e wlan.sa|sort|uniq -c |sort -nr > NbrDataFramSendFromStation.txt"
              x=command.replace("++++","%s"%bssid)
              x=x.replace("fichier","%s"%f)
              subprocess.call(x,shell=True)
 
              f=open('NbrDataFramSendFromStation.txt','r') 
              ligne=f.readlines()
              chaine1 = []
              chaine2 = []
            
              for i in range(0, len(ligne)):
                  x=ligne[i].strip()
                  x=x.replace(" ",",")
                  x=x.split(",")
                  bssid=x[1]
                  nbr=x[0]
                
                 
                  chaine1.append(nbr)
                  chaine2.append(bssid)
                      
              max=0
              for i in chaine1:
                if int(i) > max:
                    max=i
                    suspect=chaine2[chaine1.index(max)]
                    return suspect,max
             
              #os.remove('DestDataFrameSendByStation.txt')

    def NbrDataFramSendFromStation2(self,f,bssid):
              command="tshark -r fichier -R '((wlan.fc.type_subtype==0x20)&&(wlan.fc.protected==1))&&(wlan.bssid==++++)' -T fields -e wlan.sa|sort|uniq -c |sort -nr > NbrDataFramSendFromStation.txt"
              x=command.replace("++++","%s"%bssid)
              x=x.replace("fichier","%s"%f)
              subprocess.call(x,shell=True)
 
              f=open('NbrDataFramSendFromStation.txt','r') 
              ligne=f.readlines()
              chaine1 = []
              chaine2 = []
            
              for i in range(0, len(ligne)):
                  x=ligne[i].strip()
                  x=x.replace(" ",",")
                  x=x.split(",")
                  bssid=x[1]
                  nbr=x[0]
                
                 
                  chaine1.append(nbr)
                  chaine2.append(bssid)
              return chaine1, chaine2
                  
#Le nombre de trames de données reçues par chaque station
    def DestDataFrameSendByStation(self,f,bssid):
              command="tshark -r fichier '((wlan.fc.type_subtype==0x20)&&(wlan.fc.protected==1))&&(wlan.bssid==++++)' -T fields -e wlan.da|sort|uniq -c |sort -nr > DestDataFrameSendByStation.txt"
              x=command.replace("++++","%s"%bssid)
              x=x.replace("fichier","%s"%f)
              subprocess.call(x,shell=True)

              f=open('DestDataFrameSendByStation.txt','r') 
              ligne=f.readlines()
              for i in range(0, len(ligne)):
                  x=ligne[i].strip()
                  x=x.replace(" ",";")
                  x=x.split(";")
                  f.close()
              #os.remove('DestDataFrameSendByStation.txt')

                
#Le nombre de trames de données envoyées par chaque station
    def SrcDestDataFramSendStation(self,f,bssid):
              command="tshark -r fichier '((wlan.fc.type_subtype==0x20)&&(wlan.fc.protected==1))&&(wlan.bssid==++++)' -T fields -e wlan.sa -e wlan.da|sort|uniq -c |sort -nr > SrcDestDataFramSendStation.txt"
              x=command.replace("++++","%s"%bssid)
              x=x.replace("fichier","%s"%f)
              subprocess.call(x,shell=True)
              f=open('SrcDestDataFramSendStation.txt','r')
              ligne=f.readlines()
              ch1=[]
              ch2=[]
              ch3=[]
              for i in range(0, len(ligne)):
                  x=ligne[i].strip()
                  x=x.replace(" ",";")
                  x=x.split(";")
                  z=x[1].split("\t")
                  f.close()
                  ch1.append(z[0])
                  ch2.append(x[0])
                  ch3.append(z[1])
              return ch1, ch2, ch3 
              #os.remove('SrcDestDataFramSendStation.txt')
                  

#La date de début d'envoi des trames de données par la station suspecte
    def DebSendDataStation(self,f,bssid,station):
        command="tshark -r fichier '(wlan.bssid==++++)&&(wlan.sa==****)&&(wlan.fc.type_subtype==0x20)' -T fields -e frame.time|head -1 > DebSendDataStation.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)
          
        f=open('DebSendDataStation.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('DebSendDataStation.txt')
        return ligne
              
#La date de fin d'envoi des trames de données par la station suspecte
    def FinSendDataStation(self,f,bssid,station):
        command="tshark -r fichier '(wlan.bssid==++++)&&(wlan.sa==****)&&(wlan.fc.type_subtype==0x20)' -T fields -e frame.time|tail -1 > FinSendDataStation.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

        f=open('FinSendDataStation.txt','r')
        ligne=f.read()
        f.close()
                  
        #os.remove('FinSendDataStation.txt')
        return ligne

              
#Le nombre des trames de dés-authentification par le point d'accès à la station suspecte
    def NbrDesauthWAP(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0c)&&(wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.da==****)' -T fields -e frame.time|wc -l > NbrDesauthWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)


        f=open('NbrDesauthWAP.txt','r')
        ligne=f.read()
       
        f.close()
        #os.remove('NbrDesauthWAP.txt')
        return ligne      
#La date de début d'envoi des trames de dés-authentification par le point d'accès à la station suspecte
    def authWAP(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0c)&&(wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.da==****)' -T fields -e frame.time|awk '{print $0}'|head -1 > authWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)
        f=open('authWAP.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('authWAP.txt')
        return ligne
              
#La date de fin d'envoi des trames de dés-authentification par le point d'accès à la station suspecte
    def DateFinDesauthWAP(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0c)&&(wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.da==****)' -T fields -e frame.time|awk '{print $0}'|tail -1 > DateFinDesauthWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

   
        f=open('DateFinDesauthWAP.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('DateFinDesauthWAP.txt')
        return ligne
              
#Compter le nombre de trame d'authentification enovoyées par la station inconnue au WAP
    def NbrAuthStationToWAP(self,f,bssid,station):
        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.sa==****)&&(wlan.fc.type_subtype==0x0b))'|wc -l > NbrAuthStationToWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

        f=open('NbrAuthStationToWAP.txt','r')
        ligne=f.read()

        f.close()
        #os.remove('NbrAuthStationToWAP.txt')
              
#Afficher la date de début d'envoi de trame d'authentification par la station inconnu au WAP
    def DateDebAuthStationToWAP(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.bssid==++++)&&(wlan.sa==****)&&(wlan.fc.type_subtype==0x0b)' -T fields -e frame.time|head -1 > DateDebAuthStationToWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

        f=open('DateDebAuthStationToWAP.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('DateDebAuthStationToWAP.txt')
        return ligne


#Afficher la date de la fin d'envoi des trames d'authentification par la station inconnu au AP
    def DateFinAuthStationToWAP(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.bssid==++++)&&(wlan.sa==****)&&(wlan.fc.type_subtype==0x0b)' -T fields -e frame.time|tail -1 > DateFinAuthStationToWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

        f=open('DateFinAuthStationToWAP.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('DateFinAuthStationToWAP.txt')
        return ligne
              
#Comptrer le nombre des trames d'association envoyé par la station inconnu vers le AP
    def NbrAssoStationToWAP(self,f,bssid,station):
        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.sa==****)&&(wlan.fc.type_subtype==0x00))'|wc -l > NbrAssoStationToWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

    
        f=open('NbrAssoStationToWAP.txt','r')
        ligne=f.read()
     
        f.close()
        #os.remove('NbrAssoStationToWAP.txt')


#Affiche le début d'envoi des trames d'association de la station inconnu vers le WAP
    def DateDebAssoStationToWAP(self,f,bssid,station):
        command18="tshark -r fichier -R '(wlan.bssid==++++)&&(wlan.sa==****)&&(wlan.fc.type_subtype==0x00)' -T fields -e frame.time|head -1 > DateDebAssoStationToWAP.txt"
        x=command18.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

        f=open('DateDebAssoStationToWAP.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('DateDebAssoStationToWAP.txt')
        return ligne

#Affiche le fin d'envoi des trames d'association de la station inconnu vers le WAP
    def DateFinAssoStationToWAP(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.bssid==++++)&&(wlan.sa==****)&&(wlan.fc.type_subtype==0x00)' -T fields -e frame.time|tail -1>DateFinAssoStationToWAP.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)
           
        f=open('DateFinAssoStationToWAP.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('DateFinAssoStationToWAP.txt')
        return ligne

#Compter le nombre de trame de des-association envoyé par le WAP vers la station inconnue:
    def NbrDesassoWAPToStation(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0a)&&(wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.da==****)' -T fields -e frame.time|wc -l > NbrDesassoWAPToStation.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

   
        f=open('NbrAssoStationToWAP.txt','r')
        ligne=f.read()
    
        f.close()
        #os.remove('NbrDesassoWAPToStation.txt')

#Afficher la date de début d'envoi des trames de des-association par le poitnt d'accès à la station inconnu:

    def assoWAPToStation(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0a)&&(wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.da==****)' -T fields -e frame.time|awk '{print $0}'|head -1 > assoWAPToStation.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

        f=open('assoWAPToStation.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('assoWAPToStation.txt')
        return ligne

#Afficher la date de fin d'envoi de trame de désassociation par le point d'accès vers la station inconnue
    def DateFinDesassoWAPToStation(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0a)&&(wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.da==****)' -T fields -e frame.time|awk '{print $0}'|tail -1 > DateFinDesassoWAPToStation.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)
        
        f=open('DateFinDesassoWAPToStation.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('DateFinDesassoWAPToStation.txt')
        return ligne

#Méthode qui permet le crack des clés WEP
    def crackWEP(self,f,bssid):
        command="aircrack-ng -b ++++ fichier"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        subprocess.call(x,shell=True)

#Méthode qui permet de décrypter le trafic WEP
    def Decrypt(self,f,bssid,PW):
        command="airdecap-ng -l -b ++++ -w **** fichier"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("fichier","%s"%f)
        x=x.replace("****","%s"%PW)
        subprocess.call(x,shell=True)

#Calculer le nombre de vecteurs d'initialisation avant l'attaque
    def NbrVIsAvant(self,f,station,bssid,DatAvant):
        command="tshark -r fichier '(wlan.bssid==++++)&&(wlan.sa!=****)&&(frame.time < \"----\")' -T fields -e wlan.wep.iv|sort -u|wc -l > NbrVIsAvant.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("****","%s"%station)
        x=x.replace("fichier","%s"%f)
        x=x.replace("----","%s"%DatAvant)
        subprocess.call(x,shell=True)

        f=open('NbrVIsAvant.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('NbrVIsAvant.txt')
        return ligne
              
        
#Calculer le nombre de vecteurs d'initialisation durant l'attaque
    def NbrVIsDurant(self,f,station,bssid,DatApres,DatAvant):
        command="tshark -r fichier -R '(wlan.bssid==++++)&&(wlan.sa!=****)&&(frame.time<= \"----\")&&(frame.time>= \"....\")' -T fields -e wlan.wep.iv|sort -u|wc -l > NbrVIsDurant.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("****","%s"%station)
        x=x.replace("fichier","%s"%f)
        x=x.replace("----","%s"%DatApres)
        x=x.replace("....","%s"%DatAvant)
        subprocess.call(x,shell=True)

        f=open('NbrVIsDurant.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('NbrVIsDurant.txt')
        return ligne
    
#Calculer le nombre de vecteurs d'initialisation après l'attaque
    def NbrVIsApres(self,f,station,bssid,DatApres):
        command="tshark -r fichier -R '(wlan.bssid==++++)&&(wlan.sa!=****)&&(frame.time> \"----\")' -T fields -e wlan.wep.iv|sort -u|wc -l > NbrVIsApres.txt"
        x=command.replace("++++","%s"%bssid)
        x=x.replace("****","%s"%station)
        x=x.replace("fichier","%s"%f)
        x=x.replace("----","%s"%DatApres)
        subprocess.call(x,shell=True)
        
        f=open('NbrVIsApres.txt','r')
        ligne=f.read()
        f.close()
        #os.remove('NbrVIsApres.txt')
        return ligne
        
#Chronologie des activité de l'attaquant
    def ChronoAttaqueWEP(self,f,bssid,station):
        e=Examen()
        a=Analyse()
        a.DateDebAuthStationToWAP=a.DateDebAuthStationToWAP(f,bssid,station)
        a.authWAP=a.authWAP(f,bssid,station)
        a.DebSendDataStation=a.DebSendDataStation(f,bssid,station)
        a.assoWAPToStation=a.assoWAPToStation(f,bssid,station)
        a.FinSendDataStation=a.FinSendDataStation(f,bssid,station)
        a.DateFinDesauthWAP=a.DateFinDesauthWAP(f,bssid,station)
        a.DateFinAuthStationToWAP=a.DateFinAuthStationToWAP(f,bssid,station)
     
        return a.DateDebAuthStationToWAP,a.authWAP,a.DebSendDataStation,a.assoWAPToStation,a.FinSendDataStation,a.DateFinDesauthWAP,a.DateFinAuthStationToWAP

#Connaitre le type d'attaque qui a été réalisé sur le point d'accès
    def TypeAttaque(self,NbrVIsAvant,NbrVIsDurant,NbrVIsApres):
        if (NbrVIsDurant > NbrVIsAvant and NbrVIsApres < NbrVIsDurant and NbrVIsDurant>1):
            TypeAttaque="WEP attack"
        else:
            TypeAttaque="No WEP attack"
        return TypeAttaque

    
#Durée de l'attaque WEP
    def DureeAttaque(self,DatAvant,DatApres):
        try:
            DatAvant=DatAvant.split(",")
            DatAvant=DatAvant[1].replace(" ",",")
            DatAvant=DatAvant.split(",")
            DatAvant=DatAvant[2]
            DatAvant=DatAvant.replace(":",",")
            DatAvant=DatAvant.replace(".",",")
            DatAvant=DatAvant.split(",")
            HD=DatAvant[0]
            MD=DatAvant[1]
            SD=DatAvant[2]
           
            DatApres=DatApres.split(",")
            DatApres=DatApres[1].replace(" ",",")
            DatApres=DatApres.split(",")
            DatApres=DatApres[2]

            DatApres=DatApres.replace(":",",")
            DatApres=DatApres.replace(".",",")
            DatApres=DatApres.split(",")
            HF=DatApres[0]
            MF=DatApres[1]
            SF=DatApres[2]
            Duree=datetime(year=2014,month=1,day=1,hour=int(HF),minute=int(MF),second=int(SF))-datetime(year=2014,month=1,day=1,hour=int(HD),minute=int(MD),second=int(SD))
            return Duree.seconds
        except:
            return '0'



#---------------------------------------Evil Twin:--------------------------
#----------------------------------------------------------------------------
    

#Date de debut de des-authentification envoyé du WAP à Broadcast.
    def DatDebDesauthWAPToBroad(self,f,bssid):
        command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0c)&&(wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.da==ff:ff:ff:ff:ff:ff)' -T fields -e frame.time|head -1>DatDebDesauth.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        subprocess.call(x,shell=True)
        f=open('DatDebDesauth.txt','r')
        ligne=f.read()
        f.close()
        ligne=ligne.replace("\n"," ")
        ligne=ligne.strip()
        #os.remove('NbrVIsDurant.txt')
     
        if ligne!='':
            return ligne
        else:
            return 'Not available'

    #Nombre de désauthentification envoyé par le AP à @ de diffusion.
    def NbrDesauthEnvoyParAPToBroad(self,f,bssid):
            try:
                command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0c)&&(wlan.bssid==++++)&&(wlan.da==ff:ff:ff:ff:ff:ff)' |sort -u|wc -l >nbrDesauthAPtoBroad.txt"
                x=command.replace("fichier","%s"%f)
                x=x.replace("++++","%s"%bssid)
                subprocess.call(x,shell=True)
                f=open('nbrDesauthAPtoBroad.txt','r')
                ligne=f.read()
                f.close()
                ligne=ligne.replace("\n"," ")
                ligne=ligne.strip()
                #os.remove('NbrVIsDurant.txt')
                return ligne
            except:
                return 'Not available'

    
#Date de fin de des-authentification envoyé du WAP à Broadcast.
    def DatFinDesauthWAPToBroad(self,f,bssid):
        command="tshark -r fichier -R '(wlan.fc.type_subtype==0x0c)&&(wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.da==ff:ff:ff:ff:ff:ff)' -T fields -e frame.time|tail -1>DatFinDesauth.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        subprocess.call(x,shell=True)

        f=open('DatFinDesauth.txt','r')
        ligne=f.read()
        f.close()
        ligne=ligne.replace("\n"," ")
        ligne=ligne.strip()
        #os.remove('DatFinDesauth.txt')
        if ligne!='':
            return ligne
        else:
            return 'Not available'
   
    
#Numero de sequence pendant la des-authentification.
    #def NSeqDurantDesauth(self,f,DatDebDesauth,DatFinDesauth):
     #   command="tshark -nn -r fichier -R '((wlan.fc.type_subtype==0x08||wlan.fc.type_subtype==0x05)&&(wlan_mgt.fixed.capabilities.ibss==0)&&(frame.time>\"++++\")&&(frame.time<\"****\"))' -T fields -e frame.time -e wlan.seq -e wlan.fc.subtype|sort -u>NSeqDuranDesauth.txt"
      #  x=command.replace("fichier","%s"%f)
       # x=x.replace("++++","%s"%DatDebDesauth)
        #x=x.replace("****","%s"%DatFinDesauth)
        #subprocess.call(x,shell=True)
        #f=open('NSeqDuranDesauth.txt','r')
        #ligne=f.readlines()
        #for chaine in ligne:
        #    chaine=chaine.replace("\t","?")
         #   chaine=chaine.replace(" ","?")
          #  chaine=chaine.split("?")
           # print("Heure :%s ==> Numéro de séquence: %s ==> Sous-type de la trame de gestion envoyé par le point d'accès :%s")%(chaine[4],chaine[5],chaine[6])
        #os.remove('NSeqDuranDesauth.txt')
            #return chaine[4],chaine[5],chaine[6]


#Numéro de séquence aprés désauthentification.
    def NSeqApreDesauth(self,f,bssid,DatFinDesauth):
        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.fc.type_subtype==0x08)&&(wlan_mgt.fixed.capabilities.ess==1)&&(wlan_mgt.fixed.capabilities.ibss==0)&&(frame.time>=\"----\"))' -T fields -e frame.time -e wlan.sa -e wlan.seq -e wlan.fc.subtype|sort -u|head -20>nseqapredesaut.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%DatFinDesauth)
        subprocess.call(x,shell=True)
        f=open('nseqapredesaut.txt','r')
        ligne=f.readlines()
        chaine1=[]
        chaine2=[]
        chaine3=[]
        chaine4=[]
        for chaine in ligne:
            chaine=chaine.replace("\t","?")
            chaine=chaine.replace(" ","?")
            chaine=chaine.split("?")
            chaine1.append(chaine[4])
            chaine2.append(chaine[5])
            chaine3.append(chaine[6])
            chaine4.append(chaine[7])
        return chaine1,chaine2,chaine3,chaine4
#La creation de evil twin si SN=0 et SSID=broadcast.
    def CreationEvil(self,f,bssid,DatDebDesauth):
        try:
            command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.fc.type_subtype==0x08)||(wlan.fc.type_subtype==0x05)&&(wlan_mgt.fixed.capabilities.ess==1)&&(wlan_mgt.fixed.capabilities.ibss==0)&&(wlan.seq==0)&&(frame.time<\"----\"))'>creationevil.txt"
            x=command.replace("fichier","%s"%f)
            x=x.replace("++++","%s"%bssid)
            x=x.replace("----","%s"%DatDebDesauth)
            subprocess.call(x,shell=True)
            f=open('creationevil.txt','r')
            ligne=f.readlines()
            for chaine in ligne:
                chaine=chaine.replace("\t","?")
                chaine=chaine.replace(" ","?")
                chaine=chaine.split("?")
            return chaine[13],chaine[17]
        except:
            return 'Not available','Not available'       
        #os.remove('creationevil.txt')

        
#Le moment de creation de Evil Twin.
    def MomentCreationEvil(self,f,bssid,DatDebDesauth):
        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.fc.type_subtype==0x08)||(wlan.fc.type_subtype==0x05)&&(wlan_mgt.fixed.capabilities.ess==1)&&(wlan_mgt.fixed.capabilities.ibss==0)&&(wlan.seq==0)&&(frame.time<\"----\"))' -T fields -e frame.time -e wlan.seq -e wlan.sa -e wlan.da|head>momentcreationevil.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%DatDebDesauth)
        subprocess.call(x,shell=True)
        f=open('momentcreationevil.txt','r')
        ligne=f.readline()
        ligne=ligne.replace("\t0","?")
        ligne=ligne.split("?")
        DateCreationEvil=ligne[0]
        DateCreationEvil=DateCreationEvil.replace(" ","",1)
        DateCreationEvil=DateCreationEvil.replace("\n"," ")
        DateCreationEvil=DateCreationEvil.strip()
        #os.remove('momentcreationevil.txt')
        return DateCreationEvil

#canal de transmission utilisé par les stations avant la creation de evil (14:08:13)
    def CanalAvantCreationEvil(self,f,bssid,DatCreationEvil):

        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.fc.type_subtype==0x08)||(wlan.fc.type_subtype==0x05)&&(frame.time<\"****\"))' -T fields -e wlan_mgt.ds.current_channel -e wlan.sa -e wlan.da|sort -u>canalavantcreationevil.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("****","%s"%DatCreationEvil)
        subprocess.call(x,shell=True)
        
        f=open('canalavantcreationevil.txt','r')
        ligne=f.readlines()
        
        chaine1=[]
        chaine2=[]
        chaine3=[]
        for chaine in ligne:
             chaine=chaine.replace("\t","?")
             chaine=chaine.replace(" ","?")
             chaine=chaine.split("?")
             chaine[2]=chaine[2].replace("\n"," ")
             chaine[2]=chaine[2].strip()
             chaine[1]=chaine[1].replace("\n"," ")
             chaine[1]=chaine[1].strip()
             chaine[0]=chaine[0].replace("\n"," ")
             chaine[0]=chaine[0].strip()
             chaine1.append(chaine[0])
             chaine2.append(chaine[1])
             chaine3.append(chaine[2])
             
        return chaine1, chaine2, chaine3
        
        
        #canal de transmission des différents stations après la creation de evil twin

    def CanalApreCreationEvil(self,f,bssid,DatCreationEvil):
        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.fc.type_subtype==0x08)||(wlan.fc.type_subtype==0x05)&&(frame.time>\"----\"))' -T fields -e wlan_mgt.ds.current_channel -e wlan.sa -e wlan.fc.subtype|sort -u > canalAprescreationevil.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%DatCreationEvil)
        subprocess.call(x,shell=True)
        f=open('canalAprescreationevil.txt','r')
        ligne=f.readlines()
        chaine1=[]
        chaine2=[]
        chaine3=[]
        for chaine in ligne:
            chaine=chaine.replace("\t","?")
            chaine=chaine.replace(" ","?")
            chaine=chaine.split("?")
            chaine[2]=chaine[2].replace("\n"," ")
            chaine[2]=chaine[2].strip()
            chaine[1]=chaine[1].replace("\n"," ")
            chaine[1]=chaine[1].strip()
            chaine[0]=chaine[0].replace("\n"," ")
            chaine[0]=chaine[0].strip()
            chaine1.append(chaine[0])
            chaine2.append(chaine[1])
            chaine3.append(chaine[2])
            
        return chaine1,chaine2,chaine3
         

#Le canal sur lequel a été envoyé la 1ere trame de balise par le evil twin.

    def NumCanalPremiereBalise(self,f,bssid,DatCreationEvil):
        a=Analyse()
        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.fc.type_subtype==0x08)||(wlan.fc.type_subtype==0x05)&&(frame.time>\"----\"))' -T fields -e wlan.fc.type_subtype -e wlan_mgt.ds.current_channel -e wlan.sa -e wlan.da -e frame.time|head > numcanal1balise.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%DatCreationEvil)
        subprocess.call(x,shell=True)
        f=open('numcanal1balise.txt','r')
        ligne=f.readlines()
        chaine1=[]
        chaine2=[]
        chaine3=[]
        chaine4=[]
        for chaine in ligne:
            chaine=chaine.replace("\t","?")
            chaine=chaine.split("?")
            chaine[4]=chaine[4].replace("\n"," ")
            chaine[4]=chaine[4].strip()
            chaine[1]=chaine[1].replace("\n"," ")
            chaine[1]=chaine[1].strip()
            chaine[2]=chaine[2].replace("\n"," ")
            chaine[2]=chaine[2].strip()
            chaine[0]=chaine[0].replace("\n"," ")
            chaine[0]=chaine[0].strip()
            chaine1.append(chaine[1])
            chaine2.append(chaine[0])
            chaine3.append(chaine[2])
            chaine4.append(chaine[4])
         
        return chaine1,chaine2, chaine3, chaine4

#Le canal du evil twin    
    def CanalEvilTwin(self,chaine,liste):
            i=0
            while i < len(liste):
                if liste[i]<>chaine.strip("CH: "):
                    return liste[i]
                i=i+1
            return 'Non disponnible'
        
     
            
#Début de evil twin

    def DebEvil(self,f,bssid,DatCreationEvil,n):
        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.fc.type_subtype==0x08)||(wlan.fc.type_subtype==0x05)&&(frame.time>\"----\")&&(wlan_mgt.ds.current_channel==****))' -T fields -e wlan.fc.type_subtype -e wlan_mgt.ds.current_channel -e wlan.sa -e wlan.da -e frame.time|head -1 > debEvil.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%DatCreationEvil)
        x=x.replace("****","%s"%n)
        subprocess.call(x,shell=True)
        f=open('debEvil.txt','r')
        ligne=f.readlines()
        for chaine in ligne:
            chaine=chaine.replace("\t","?")
            chaine=chaine.split("?")
            chaine[4].replace("\n"," ")
            chaine[4].strip()
            chaine[4]=chaine[4].replace(" ","",1)
            chaine=chaine[4]
            return chaine
            
        #os.remove('momentcreationevil.txt')
        

#fin de evil
    def FinEvil(self,f,bssid,DatCreationEvil,n):
        command="tshark -r fichier -R '((wlan.bssid==++++)&&(wlan.sa==++++)&&(wlan.fc.type_subtype==0x08)||(wlan.fc.type_subtype==0x05)&&(frame.time>\"----\")&&(wlan_mgt.ds.current_channel==****))' -T fields -e wlan.fc.type_subtype -e wlan_mgt.ds.current_channel -e wlan.sa -e wlan.da -e frame.time|tail -1>FinEvil.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%DatCreationEvil)
        x=x.replace("****","%s"%n)
        subprocess.call(x,shell=True)
        f=open('FinEvil.txt','r')
        ligne=f.readlines()
        for chaine in ligne:
            chaine=chaine.replace("\t","?")
            chaine=chaine.split("?")
            chaine[4].replace("\n"," ")
            chaine[4]=chaine[4].replace(" ","",1)
            chaine[4].strip()
            chaine=chaine[4]
            return chaine

#Nbr de trame de gestion envoyé par station legitime/wap/station suspect(à quoi elle sert)
    def NbrGestionEnvoyParStation(self,f,bssid,station):
        command="tshark -r fichier -R '(wlan.fc.type==0)&&(wlan.bssid==++++)&&(wlan.sa==****)' -T fields -e wlan.da|sort|uniq -c|sort -nr>NbrGestion.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("****","%s"%station)
        subprocess.call(x,shell=True)

    def TypeAttaqueEvil(self,legitime,evil):
        if legitime!=evil and evil!='Non disponnible':
             typeattaque="Attaque EVIL TWIN"
        else:
            typeattaque="Aucune Attaque Evil"
        return typeattaque
    
#-----------------------------------------------Attaque DOS------------------------------------------------------------------------------------
#Station qui a envoyé les trames de données NULL.
    def StationNULL(self,f,bssid):
        try:
            command="tshark -r fichier -R '((wlan.fc.type_subtype==0x24)&&(wlan.bssid==++++))' -T fields  -e wlan.sa -e wlan.da|sort|uniq -c|sort -nr>StationNULL.txt"
            x=command.replace("fichier","%s"%f)
            x=x.replace("++++","%s"%bssid)
            subprocess.call(x,shell=True)
            f=open('StationNULL.txt','r')
            ligne=f.readlines()
            ligne[0]=ligne[0].strip()
            ligne[0]=ligne[0].replace(" ","\t")
            ligne=ligne[0]
            ligne=ligne.split("\t")
            return ligne[0],ligne[1]
        except:
            return '0','Not available'
#Réussite de l'attaque   
    def TypeAttaqueDos(self,NbrDesauth):
        if int(NbrDesauth)>1000:
            typeattaque="DoS attack"
        else:
            typeattaque="No DoS attack"
        return typeattaque

#Nombre Trame NULL envoyé par toutes les station


    def NbrNULL(self,f,bssid):
        try:
            command="tshark -r fichier -R '((wlan.fc.type_subtype==0x24)&&(wlan.bssid==++++))'|wc -l > StationNULL.txt"
            x=command.replace("fichier","%s"%f)
            x=x.replace("++++","%s"%bssid)
            subprocess.call(x,shell=True)
            f=open('StationNULL.txt','r')
            ligne=f.readlines()
            ligne=ligne[0]
            return ligne
        except:
            return '0'
	
#Nombre Trame NULL envoyé avant désauthentification
    def NbrNullAvanAttak(self,f,bssid,debDesauth):
        command="tshark -r fichier -R '((wlan.fc.type_subtype==0x24)&&(wlan.bssid==++++)&&(frame.time<\"----\"))'|wc -l>nbrNULLavant.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%debDesauth)
        subprocess.call(x,shell=True)

        f=open('nbrNULLavant.txt','r')
        ligne=f.readlines()
        ligne=ligne[0]
        return ligne

#Nombre de trame NULL envoyé durant désauthentification.	
    def NbrNULLduranAttak(self,f,bssid,debDesauth,finDesauth):
        command="tshark -r fichier -R '((wlan.fc.type_subtype==0x24)&&(wlan.bssid==++++)&&(frame.time<=\"----\")&&(frame.time>=\"****\"))'|wc -l > NbrNULLduranAttak.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%finDesauth)
        x=x.replace("****","%s"%debDesauth)
        subprocess.call(x,shell=True)

        f=open('NbrNULLduranAttak.txt','r')
        ligne=f.readlines()
        ligne=ligne[0]
        return ligne


#Nombre de trame NULL envoyé aprés désauthentification.

    def NbrNullApresAttak(self,f,bssid,finDesauth):
        command="tshark -r fichier -R '((wlan.fc.type_subtype==0x24)&&(wlan.bssid==++++)&&(frame.time>\"----\"))'|wc -l >NbrNullApresAttak.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        x=x.replace("----","%s"%finDesauth)
        subprocess.call(x,shell=True)
        f=open('NbrNullApresAttak.txt','r')
        ligne=f.readlines()
        ligne=ligne[0]
        return ligne


#Début  d'envoi de trame NULL.

    def DebEnvoiNULL(self,f,bssid):
        command="tshark -r fichier -R '((wlan.fc.type_subtype==0x24)&&(wlan.bssid==++++))' -T fields -e frame.time|head -1 > DebEnvoiNULL.txt"
        x=command.replace("fichier","%s"%f)
        x=x.replace("++++","%s"%bssid)
        subprocess.call(x,shell=True)
        f=open('DebEnvoiNULL.txt','r')
        ligne=f.readlines()
        for chaine in ligne:
             chaine.replace("\n"," ")
             chaine=chaine.replace(" ","",1)
             chaine.strip()
             return chaine

#Fin d'envoi de trame NULL

    def FinEnvoiNULL(self,f,bssid):
         command="tshark -r fichier -R '((wlan.fc.type_subtype==0x24)&&(wlan.bssid==++++))' -T fields -e frame.time|tail -1 > FinEnvoiNULL.txt"
         x=command.replace("fichier","%s"%f)
         x=x.replace("++++","%s"%bssid)
         subprocess.call(x,shell=True)
         f=open('FinEnvoiNULL.txt','r')
         ligne=f.readlines()
         for chaine in ligne:
             chaine.replace("\n"," ")
             chaine=chaine.replace(" ","",1)
             chaine.strip()
             return chaine
     
   
