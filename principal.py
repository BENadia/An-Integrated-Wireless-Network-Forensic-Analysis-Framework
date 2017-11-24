# -*- coding: utf-8 -*-
import re
import curses, sys, os, signal,argparse
from multiprocessing import Process
from scapy.all import *
from subprocess import call, PIPE
from methode import *
from datetime import date, time, datetime


def main():
   
      print("===========================================================================================================================")
      print("=                                                          WN2F                                                           =")
      print("=                                          WIRELESS NETWORK FORENSICS FRAMEWORK                                           =")
      print("=    *****************************************************************************************************************    =")
      print("=                                                          MENU                                                           =")
      print("=    *****************************************************************************************************************    =")
      print("= Pour examiner le fichier de trace : tapez e                                                                             =")
      print("= Pour analyser le fichier de trace : tapez a                                                                             =")
      print("===========================================================================================================================")
      print("Entrez votre choix ?")
      n=raw_input("Choix :")
      
      choix=['e','a']
      while n not in choix:
            print("Entrez le bon choix SVP")
            n=raw_input("Choix :")
            
      #LA PHASE EXAMEN:
      #DANS CETTE PHASE LE PROGRAMME EXAMINE LE FICHIER DE TRACE
      if n=="e":
            e=Examen()
            print("Vous avez choisi l'examen du fichier de trace!!")
            f=raw_input("Entrer le nom du fichier: \n")
            print("===========================================================================================================================")
            print("================================================Résultats d'examen=========================================================")
            print("=    *****************************************************************************************************************    =")
            print("\nInformations sur le fichier de trace :")
            e.Capinfos(f)
            print("===========================================================================================================================")
            print("\nSSID et BSSID de chaque point d'accès :")
            e.BssidSsid(f)
            e.TraitFile()
            e.SSID,e.BSSID=e.search()
            for ssid in e.SSID:
                  print "SSID :%s==>%s"%(ssid,e.BSSID[e.SSID.index(ssid)])
            print("===========================================================================================================================")
            os.remove('tmp.txt')
      elif n=="a":
            e=Examen()
            print("\nVous avez choisi l'analyse du fichier de trace!!\n")
      #LA PHASE ANALYSE:
      #DANS CETTE PHASE LE PROGRAMME ANALYSE LE FICHIER DE TRACE
            print("===========================================================================================================================")
            print("=                                                   MENU  D'ANALYSE                                                       =")
            print("=    *****************************************************************************************************************    =")
            print("=                                               Choisir le type d'attaque                                                 =")
            print("=    *****************************************************************************************************************    =")
            print("= Pour enqueter sur l'attaque WEP : tapez w                                                                               =")
            print("= Pour enqueter sur l'attaque DoS: tapez d                                                                                =")
            print("= Pour enqueter sur l'attaque Evil Twin : tapez t                                                                         =")
            print("===========================================================================================================================")
            print("Entrez votre choix ?")
            n=raw_input("Choix :")
      
            choix=['w','t','d']
            while n not in choix:
                  print("Entrez le bon choix SVP")
                  n=raw_input("Choix :")
            if n=="w":
                  print("Vous avez choisi l'investigation sur une attaque WEP")
                  print("===========================================================================================================================")
                  a=Analyse()
                  f=raw_input("Donnez le fichier de trace \n")
                  print("===========================================================================================================================")
                  bssid=raw_input("Donnez le BSSID du point d'accès à analyser\n")
                  print("===========================================================================================================================")
                  print("==================================Nombre de trames de données envoyées par chaque station==================================")
                  a.suspect=a.NbrDataFramSendFromStation(f,bssid)
                  print("===============================================Stations associées avec succès==============================================")
                  a.StationAssocie(f,bssid)
                  print("====================Nombre des trames des trames dés-authentification envoyées à la station inconnue=======================")
                  a.NbrDesauthWAP(f,bssid,a.suspect)
                  print("====================Nombre des trames des trames d'authentification envoyées par la station inconnue=======================")
                  a.NbrAuthStationToWAP(f,bssid,a.suspect)
                  a.DatAvant=a.DebSendDataStation(f,bssid,a.suspect)
                  a.DatApres=a.FinSendDataStation(f,bssid,a.suspect)
                  
                  a.Duree=a.DureeAttaque(a.DatAvant,a.DatApres)
                  a.TypeChif=a.TypeDuChiffrement(f,bssid)
                  a.NbrVIsAvant=a.NbrVIsAvant(f,a.suspect,bssid,a.DatAvant)
                  a.NbrVIsDurant=a.NbrVIsDurant(f,a.suspect,bssid,a.DatApres,a.DatAvant)
                  a.NbrVIsApres=a.NbrVIsApres(f,a.suspect,bssid,a.DatApres)
                  a.TypeAttaque=a.TypeAttaque(a.NbrVIsAvant,a.NbrVIsDurant,a.NbrVIsApres)
                  a.bssid_ssid(f)
                  a.ssid_wep=a.ssid_wep(bssid)
                
              
                  print("==========================================================================================================================")
                  print("=====================================================Résultats D'analyse==================================================")
                  print("=    ******************************************************************************************************************  =")
                  print("==========================================================================================================================")
                  print("= SSID du point d'accès                                                             : %s")%a.ssid_wep
                  print("= BSSID du point d'accès                                                            : %s")%bssid
                  print("= Type du chiffrement                                                               : %s")%a.TypeChif
                  print("= Addresse MAC du suspect                                                           : %s")%a.suspect
                  print("= Type de l'attaque réalisée                                                        : %s")%a.TypeAttaque
                  print("= Durée de l'attaque                                                                : %s secondes")%a.Duree
                  print("= Nombre des trames de données envoyées par le suspect                              : %s")%a.max
                  print("= Nombre des vecteurs d'initialisation durant la diffusion des trames de données    : %s")%a.NbrVIsDurant
                  print("= Nombre des vecteurs d'initialisation avant la diffusion des trames de données     : %s")%a.NbrVIsAvant
                  print("= Nombre des vecteurs d'initialisation après la diffusion des trames de données     : %s")%a.NbrVIsApres
                  print("==============================================Chronologie des activités du suspect=========================================")
                  print("=    ******************************************************************************************************************   =")
                  a.ChronoAttaqueWEP(f,bssid,a.suspect)
                  print("===========================================================================================================================")
                  
                  os.remove('FinSendDataStation.txt')
                  os.remove('DebSendDataStation.txt')
                  os.remove('NbrTramDataCrypt.txt')
                  os.remove('NbrAuthStationToWAP.txt')
                  os.remove('NbrDataFramSendFromStation.txt')
                  os.remove('NbrTramDataSendWAP.txt')
                  os.remove('NbrVIsApres.txt')
                  os.remove('NbrVIsAvant.txt')
                  os.remove('NbrDesauthWAP.txt')
                  os.remove('NbrVIsDurant.txt')
                  os.remove('StationAssocie.txt')
                  os.remove('tmp.txt')
                  os.remove('DateDebAuthStationToWAP.txt')
                  os.remove('DateDebDesassoWAPToStation.txt')
                  os.remove('DateDebDesauthWAP.txt')
                  os.remove('DateFinAuthStationToWAP.txt')
                  os.remove('DateFinDesauthWAP.txt')
                  

                  
            elif n=="d":
                  a=Analyse()
                  print("Vous avez choisi attaque dos")
                  
                  print("Vous aves choisi attaque Evil Twin")
                  print("===========================================================================================================================")
                  a=Analyse()
                  f=raw_input("Donnez le fichier de trace \n")
                  print("===========================================================================================================================")
                  bssid=raw_input("Donnez le BSSID du point d'accès à analyser\n")
                  print("===========================================================================================================================")
                  a.NbrNullStat,a.suspect=a.StationNULL(f,bssid)
                  a.DatDebDes=a.DatDebDesauthWAPToBroad(f,bssid)
                  a.DatFinDes=a.DatFinDesauthWAPToBroad(f,bssid)
                  a.NbrDesauth=a.NbrDesauthEnvoyParAPToBroad(f,bssid)
                  a.DureeAttaqueDos=a.DureeAttaque(a.DatDebDes,a.DatFinDes)
                  a.TypeAttaqueDos=a.TypeAttaqueDos(a.NbrDesauth)
                  a.NbrNull=a.NbrNULL(f,bssid)
                  a.NbrNullAvanAttak=a.NbrNullAvanAttak(f,bssid,a.DatDebDes)
                  a.NbrNULLduranAttak=a.NbrNULLduranAttak(f,bssid,a.DatDebDes,a.DatFinDes)
                  a.NbrNullApresAttak=a.NbrNullApresAttak(f,bssid,a.DatFinDes)
                  a.DebEnvoiNULL=a.DebEnvoiNULL(f,bssid)
                  a.FinEnvoiNULL=a.FinEnvoiNULL(f,bssid)
                  a.DureeNull=a.DureeAttaque(a.DebEnvoiNULL,a.FinEnvoiNULL)
                  os.remove('NbrNULLduranAttak.txt')
                  os.remove('nbrNULLavant.txt')
                  os.remove('NbrNullApresAttak.txt')
                  os.remove('DebEnvoiNULL.txt')
                  os.remove('StationNULL.txt')
                  os.remove('FinEnvoiNULL.txt')
                  #os.remove('StationNULL.txt')
                  os.remove('nbrDesauthAPtoBroad.txt')
                  os.remove('DatFinDesauth.txt')
                  os.remove('DatDebDesauth.txt')
                  a.bssid_ssid(f)
                  a.ssid_wep=a.ssid_wep(bssid)
                  print("==========================================================================================================================")
                  print("=====================================================Résultats D'analyse==================================================")
                  print("=    ******************************************************************************************************************  =")
                  print("==========================================================================================================================")
                  print("= SSID du point d'accès                                                             : %s")%a.ssid_wep
                  print("= BSSID du point d'accès                                                            : %s")%bssid
                  print("= Addresse MAC du suspect                                                           : %s")%a.suspect
                  print("= Type de l'attaque réalisée                                                        : %s")%a.TypeAttaqueDos
                  print("= Nombre des trames de dés-authentification diffusées par le AP                     : %s")%a.NbrDesauth
                  print("= Date de début diffusion désauthentification par le AP                             : %s")%a.DatDebDes
                  print("= Date de fin diffusion désauthentification                                         : %s")%a.DatFinDes
                  print("= Nombre des trames de données du type NULL envoyées par toutes les stations        : %s")%a.NbrNull
                  print("= Nombre des trames de données du Type NULL avant la dés-authentification           : %s")%a.NbrNullAvanAttak
                  print("= Nombre des trames de données du Type NULL durant la dés-authentification          : %s")%a.NbrNULLduranAttak
                  print("= Nombre des trames de données du Type NULL après la dés-authentification           : %s")%a.NbrNullApresAttak
                  print("= Nombre des trames de données du type NULL envoyées par le suspect                 : %s")%a.NbrNullStat
                  print("= Date de début d'envoi des trames de données du type NULL                          : %s")%a.DebEnvoiNULL
                  print("= Date de fin d'envoi des trames de données du type NULL                            : %s")%a.FinEnvoiNULL
                  print("= Durée de l'innondation du AP avec des trames NULL                                 : %s secondes")%a.DureeNull
                  print("= Durée de l'attaque                                                                : %s secondes")%a.DureeAttaqueDos
                  print("==========================================================================================================================")
                  
                  
                  
            elif n=="t":
                  print("Vous avez choisi attaque Evil Twin")
                  print("===========================================================================================================================")
                  a=Analyse()
                  f=raw_input("Donnez le fichier de trace \n")
                  print("===========================================================================================================================")
                  bssid=raw_input("Donnez le BSSID du point d'accès à analyser\n")
                  #print("===========================================================================================================================")
                  #print("======================Date de début et fin de diffusion des trames de dés-authentification=================================")
                  a.DatDebDes=a.DatDebDesauthWAPToBroad(f,bssid)
                  a.DatFinDes=a.DatFinDesauthWAPToBroad(f,bssid)
                  print("===========================================================================================================================")
                  print("=================Numéros de séquance  après le début de diffusion des trames de dés-authentification=======================")
                  print("=    ******************************************************************************************************************  =")
                  a.NSeqApreDesauth=a.NSeqApreDesauth(f,bssid,a.DatDebDes)
                  #print("===========================================================================================================================")
                  print("===========================================Date de creation du Evil TWIN===================================================")
                  print("==============================================Signatures d'usurpation======================================================")
                  print("=    ******************************************************************************************************************  =")
                  a.SN,a.ssidEvil= a.CreationEvil(f,bssid,a.DatDebDes)
                  a.MomentCreationEvil=a.MomentCreationEvil(f,bssid,a.DatDebDes)
                 
                  #print("===========================================================================================================================")
                  print("=====================================Canaux de transmission avant la création du Evil twin=================================")
                  print("=    *******************************************************************************************************************  =")
                  a.CanalAvantCreationEvil=a.CanalAvantCreationEvil(f,bssid,a.MomentCreationEvil)
                  print("=====================================Canaux de transmission après la création du Evil twin=================================")
                  print("=    *******************************************************************************************************************  =")
                  a.NumCanalPremiereBalise=a.NumCanalPremiereBalise(f,bssid,a.MomentCreationEvil)
                  print("======================================================Signatures EVIL TWIN=================================================")
                  print("=    *******************************************************************************************************************  =")
                  a.CanalEvilTwin=a.CanalEvilTwin(a.CanalAvantCreationEvil,a.NumCanalPremiereBalise)
                  a.CanalApreCreationEvil(f,bssid,a.MomentCreationEvil)
                  #print("=================================================Durée du Evil twin========================================================")
                  a.DebEvil=a.DebEvil(f,bssid,a.MomentCreationEvil,a.CanalEvilTwin)
                  a.FinEvil=a.FinEvil(f,bssid,a.MomentCreationEvil,a.CanalEvilTwin)
                  a.DureeEvil=a.DureeAttaque(a.DebEvil,a.FinEvil)
                  a.TypeAttaqueEvil=a.TypeAttaqueEvil(a.CanalAvantCreationEvil, a.CanalEvilTwin)
                  
                  a.NbrDesauth=a.NbrDesauthEnvoyParAPToBroad(f,bssid)
                  a.bssid_ssid(f)
                  a.ssid=a.ssid_evil(bssid)
                  
                  os.remove('canalAprescreationevil.txt')
                  os.remove('canalavantcreationevil.txt')
                  os.remove('creationevil.txt')
                  os.remove('DatDebDesauth.txt')
                  os.remove('DatFinDesauth.txt')
                  os.remove('debEvil.txt')
                  os.remove('FinEvil.txt')
                  os.remove('momentcreationevil.txt')
                  os.remove('nbrDesauthAPtoBroad.txt')
                  os.remove('numcanal1balise.txt')
                  os.remove('tmp.txt')
                  os.remove('nseqapredesaut.txt')
                  #os.remove('NSeqDuranDesauth.txt')
            
                 
                  print("==========================================================================================================================")
                  print("=====================================================Résultats D'analyse==================================================")
                  print("=    ******************************************************************************************************************  =")
                  print("==========================================================================================================================")
                  print("= SSID du point d'accès                                                             : %s")%a.ssid
                  print("= BSSID du point d'accès                                                            : %s")%bssid
                  print("= Addresse MAC du EVIL TWIN                                                         : %s")%bssid
                  print("= Type de l'attaque réalisée                                                        : %s")%a.TypeAttaqueEvil
                  print("= Nombre des trames de dés-authentification diffusées par le AP                     : %s")%a.NbrDesauth
                  print("= Date début diffusion désauthentification par le AP                                : %s")%a.DatDebDes
                  print("= Date fin diffusion désauthentification                                            : %s")%a.DatFinDes
                  print("= Signatures du moment de la création du Evil Twin                                  : %s avec %s")%(a.SN,a.ssidEvil)
                  print("= Date de création du Evil Twin                                                     : %s")%a.DebEvil
                  print("= Date de la fin du Evil Twin                                                       : %s")%a.FinEvil
                  print("= Durée de l'attaque                                                                : %s secondes")%a.DureeEvil
                  print("= Canal de transmission du AP légitme                                               : %s")%a.CanalAvantCreationEvil
                  print("= Canal de transmission du AP EVIL TWIN                                             : %s")%a.CanalEvilTwin
                  print("==========================================================================================================================")
                                     
      else:
            print("Choix non disponnible")
                 

        
#Archivage
        #NomDossier=raw_input("Entrer le nom du dossier \n")
        #b=Archive()
        #b.CreationDossier(NomDossier)
  
      

        
if __name__ == u'__main__':
    main()
