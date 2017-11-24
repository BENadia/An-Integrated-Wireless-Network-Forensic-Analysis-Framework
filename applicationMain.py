#!/usr/bin/python
# -*- coding: utf-8 -*-
#!/usr/bin/python
# -*- coding: utf-8 -*-
from __future__ import division
# Python 2.7
import curses, signal,argparse,time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from PyQt4.QtGui import QMessageBox
from application import *
from methode import *
import thread
from examen import *
from resultatAnalWep import *
from capture import *
from traitement import *
from multiprocessing import Process
from subprocess import call, PIPE
import os,sys,shutil,time
from resultatDoS import *
from resultatEvil import *
from about import *
from PIL import Image
import Queue
queue=Queue.Queue()
chaineWEP=[]
chaineEVIL=[]
chaineDOS=[]
class myAppBD (QMainWindow,Ui_MainWindow):
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.setupUi(parent)
        #cliquez sur le menu collecte traffic 802.11
        self.connect(self.pushButton, SIGNAL("clicked()"),self.collecte)
        #cliquez sur le menu Examen du fichier de trace.
        self.connect(self.pushButton_2, SIGNAL("clicked()"),self.examen)
        #cliquez sur le menu Analyse du fichier de trace.
        self.connect(self.pushButton_3, SIGNAL("clicked()"),self.anal)
        self.connect(self.pushButton_4, SIGNAL("clicked()"),self.aboutWN2F)
    def aboutWN2F(self):
        self.aboutWN2F=QtGui.QDialog()
        self.ui7=Ui_about()
        self.ui7.setupUi(self.aboutWN2F)
        self.aboutWN2F.show()
    def collecte(self):
        self.capture=QtGui.QWidget()
        self.capture.setWindowFlags(Qt.CustomizeWindowHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.ui2=Ui_Form()
        self.ui2.setupUi(self.capture)
        self.connect(self.ui2.pushButton, SIGNAL("clicked()"),self.collecteTraffic)
        self.connect(self.ui2.pushButton_3, SIGNAL("clicked()"),self.sauvgarderFichier)
        self.capture.show()
    def sauvgarderFichier(self):
        filename = QtGui.QFileDialog.getSaveFileName(self, 'Save File', os.getenv('HOME'))
        self.ui2.lineEdit.setText(filename)
        f = open(filename, 'w')
        #filedata = self.text.toPlainText()
        #f.write(filedata)
        f.close()

    def collecteTraffic(self):
     
        x=self.ui2.lineEdit.text()
        y=self.ui2.comboBox.currentText()
        z=self.ui2.lineEdit_6.text()
        exp=r'([0-9])'
        if x=="":
            QMessageBox.warning(self,"Allerte champ",self.trUtf8("Give the name of trace file! \n"))
          
        elif re.search(exp, z) is None:
            QMessageBox.warning(self,"Allerte Durée",self.trUtf8("Enter numerical value in duration field \n"))
        else:
            self.thread=GenericThread(self.DebutCaptureTraffic,x,y,z)
            self.disconnect( self, QtCore.SIGNAL("signalfincapture(PyQt_PyObject)"), self.signalfincapture ) # diconnecter le signal si il exist deja
            self.connect( self, QtCore.SIGNAL("signalfincapture(PyQt_PyObject)"), self.signalfincapture ) 
            self.thread.start() 
    def DebutCaptureTraffic(self,x,y,z):  
            c=Capture()
            c.DebutCaptureTraffic(x,y,z)
            self.emit( QtCore.SIGNAL('signalfincapture(PyQt_PyObject)'),x)        
    """def signalfincapture(self,x):
             QMessageBox.information(self,"Fin de capture",self.trUtf8("Le chemin d'accès du fichier de trace est:/home/")+x)"""
        
    def examen(self):
        self.exam=QtGui.QWidget()
        self.exam.setWindowFlags(Qt.CustomizeWindowHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.ui3=Ui_Form2()
        self.ui3.setupUi(self.exam)
        #cliquez sur le button 'charger' de la fenetre Examen du traffic 802.11
        self.connect(self.ui3.pushButton_8, SIGNAL("clicked()"), self.uploadFichier2)
        #cliquez sur le button 'Lancez examen' de la fenetre Examen du traffic 802.11
        self.connect(self.ui3.pushButton_3, SIGNAL("clicked()"), self.verifierExamen)
        self.connect(self.ui3.pushButton_2, SIGNAL("clicked()"),self.threadAnal)
        self.exam.show()

    def threadAnal(self):
        f= self.ui3.lineEdit_3.text()
        bssid= self.ui3.lineEdit.text()
        if f=="":
            QMessageBox.warning(self,"Allerte Fichier",self.trUtf8("Upload trace file \n"))
        elif bssid=="":
            QMessageBox.warning(self,"Allerte Analyse",self.trUtf8("You have to launch examination and select the BSSID to start analysis \n"))
        
        else:
            self.exam.hide()
            self.anal=QtGui.QWidget()
            self.ui4=Ui_Form3()
            self.ui4.setupUi(self.anal)
            self.ui4.lineEdit.setText(str(bssid))
            self.ui4.lineEdit_2.setText(str(f))
            self.connect(self.ui4.pushButton, SIGNAL("clicked()"),self.uploadFichierAnal)
            self.connect(self.ui4.pushButton_2, SIGNAL("clicked()"),self.allerte)
            self.anal.show()
       
    def LancerAnalExamen(self,bssid,f):
    
        try:
            self.methodeDOS(bssid,f)
            self.methodeEVIL(bssid,f)
            self.methodeWEP(bssid,f)
        except:
            QMessageBox.information(self,"Allerte",self.trUtf8("No attack has been realized  \n"))

           
            
    def uploadFichier2(self):
        fichier = QFileDialog.getOpenFileName(self,
                                                "Open file",
                                                "/home/puiseux/images",
                                               "File (*.pcap *.cap )")
        if fichier:
                  QMessageBox.information(self,
                                    "Fichier",
                                   self.trUtf8("You have selected :\n") + fichier)
        self.ui3.lineEdit_3.setText(fichier)
        
    def verifierExamen(self):
        f=self.ui3.lineEdit_3.text()
        if f=="":
            QMessageBox.warning(self,"Alert",self.trUtf8("Upload trace file \n"))
        else:
            self.waitingExamen()
            self.thread=GenericThread(self.LancerExamen,f)
            self.connect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
            self.disconnect( self, QtCore.SIGNAL("afficheExamen(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.afficheExamen ) # diconnecter le signal si il exist deja
            self.connect( self, QtCore.SIGNAL("afficheExamen(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.afficheExamen ) 
        
            self.thread.start()    

    def LancerExamen(self,x):
            self.emit( QtCore.SIGNAL('handleButton(PyQt_PyObject)'),x)
            em=Examen()
            em.encap,em.typ,em.nbrp,em.tail,em.debc,em.finc,em.durec,em.sha1,em.rip,em.md5=em.Capinfos(x)
            em.BssidSsid(x)
        
            em.SSID,em.BSSID,em.canal=em.search()
            self.emit( QtCore.SIGNAL('afficheExamen(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)'),em.encap,em.typ,em.nbrp,em.tail,em.debc,em.finc,em.durec,em.sha1,em.rip,em.md5,em.SSID,em.BSSID,em.canal)
            
            
    def afficheExamen(self,encap,typ,nbrp,tail,debc,finc,durec,sha1,rip,md5,SSID,BSSID,canal):    
        self.ui3.tableWidget.setColumnCount(1)
        self.ui3.tableWidget.resizeRowsToContents()
        self.ui3.tableWidget.resizeColumnsToContents()
        self.ui3.tableWidget.setColumnWidth(0,400)
        
        self.ui3.tableWidget.setRowCount(10)
        titre=QTableWidgetItem("Informations")
        self.ui3.tableWidget.setHorizontalHeaderItem(0,titre)

        a = QTableWidgetItem("Type of traffic")
        self.ui3.tableWidget.setVerticalHeaderItem (0, a)
        item0=QTableWidgetItem("%s"%(encap))
        self.ui3.tableWidget.setItem(0,0,item0)

        b = QTableWidgetItem("Type of file")
        self.ui3.tableWidget.setVerticalHeaderItem (1, b)
        item1=QTableWidgetItem("%s"%(typ))
        self.ui3.tableWidget.setItem(1,0,item1)
        
        c = QTableWidgetItem("Packet number")
        self.ui3.tableWidget.setVerticalHeaderItem (2, c)
        item2=QTableWidgetItem("%s"%(nbrp))
        self.ui3.tableWidget.setItem(2,0,item2)
        
        d= QTableWidgetItem("File size")
        self.ui3.tableWidget.setVerticalHeaderItem (3, d)
        item3=QTableWidgetItem("%s"%(tail))
        self.ui3.tableWidget.setItem(3,0,item3)
        
        e = QTableWidgetItem("Start date of packet capture")
        self.ui3.tableWidget.setVerticalHeaderItem (4, e)
        item4=QTableWidgetItem("%s"%(debc))
        self.ui3.tableWidget.setItem(4,0,item4)
        
        f = QTableWidgetItem("End date of packet capture")
        self.ui3.tableWidget.setVerticalHeaderItem (5, f)
        item5=QTableWidgetItem("%s"%(finc))
        self.ui3.tableWidget.setItem(5,0,item5)
        
        g = QTableWidgetItem("Capture duration")
        self.ui3.tableWidget.setVerticalHeaderItem (6, g)
        item6=QTableWidgetItem("%s"%(durec))
        self.ui3.tableWidget.setItem(6,0,item6)
        
        h = QTableWidgetItem("SHA1")
        self.ui3.tableWidget.setVerticalHeaderItem (7, h)
        item7=QTableWidgetItem("%s"%(sha1))
        self.ui3.tableWidget.setItem(7,0,item7)
        
        i = QTableWidgetItem("RIPEMD160")
        self.ui3.tableWidget.setVerticalHeaderItem (8, i)
        item8=QTableWidgetItem("%s"%(rip))
        self.ui3.tableWidget.setItem(8,0,item8)
        
        j = QTableWidgetItem("MD5")
        self.ui3.tableWidget.setVerticalHeaderItem (9, j)
        item9=QTableWidgetItem("%s"%(md5))
        self.ui3.tableWidget.setItem(9,0,item9)
        
        
        #Definition de nombre de colonnes et de leurs taille de 2eme tableau.
        self.ui3.tableWidget_2.setColumnCount(3)
        self.ui3.tableWidget_2.resizeRowsToContents()
        self.ui3.tableWidget_2.resizeColumnsToContents()
        self.ui3.tableWidget_2.setColumnWidth(0,200)
        self.ui3.tableWidget_2.setColumnWidth(1,200)
        self.ui3.tableWidget_2.setColumnWidth(2,200)
   

        i=0
        j=0
        l=0
        line=0
        ssid1=list(set(SSID))
        for ssid in ssid1:
                   self.ui3.tableWidget_2.setRowCount(line+1)
                   a = QTableWidgetItem("SSID")
                   self.ui3.tableWidget_2.setHorizontalHeaderItem (0, a)
                   ite0=QTableWidgetItem("%s"%(ssid))
                   self.ui3.tableWidget_2.setItem(i,0,ite0)
                   i=i+1
                   b = QTableWidgetItem("BSSID")
                   self.ui3.tableWidget_2.setHorizontalHeaderItem (1, b)
                   ite1=QTableWidgetItem("%s"%(BSSID[SSID.index(ssid)]))
                   self.ui3.tableWidget_2.setItem(j,1,ite1)
                   j=j+1
                   c = QTableWidgetItem("Channel")
                   self.ui3.tableWidget_2.setHorizontalHeaderItem (2, c)
                   ite2=QTableWidgetItem("%s"%(canal[SSID.index(ssid)]))
                   self.ui3.tableWidget_2.setItem(l,2,ite2)
                   l=l+1
                   line=line+1
        self.ui3.tableWidget_2.installEventFilter(self)
 
        # lancera la méthode saisieval à chaque changement de case
        QtCore.QObject.connect( self.ui3.tableWidget_2, QtCore.SIGNAL('currentCellChanged(int,int,int,int)'), self.saisieval)   
        self.emit(QtCore.SIGNAL("stopaction()"))    
    def saisieval(self, lig, col, lig0, col0):
        """Méthode lancée à chaque changement de case du tableau"""
        val = self.prendcase(self.ui3.tableWidget_2, lig, 1)
        self.ui3.lineEdit.setText(val)
    def prendcase(self,table, row, col):
        """Retourne la valeur de la case [row, col] de la table QTableWidget"""
        item = table.item(row, 1)
        if item == None:
            return u""
        else:
            return unicode(item.text())
    def eventFilter(self, obj, event):
        """Filtrages des évènements"""
        if obj == self.ui3.tableWidget_2:
            if event.type() == QtCore.QEvent.FocusOut:
                lig = self.ui3.tableWidget_2.currentRow()
                col = self.ui3.tableWidget_2.currentColumn()
                self.val = self.prendcase(self.ui3.tableWidget_2, lig, 1)
                self.ui3.lineEdit.setText(self.val)
                return True
            else:
                return False
        else:
            # transmission au parent de la fenêtre
            pass
    def anal(self):
        self.anal=QtGui.QWidget()
        self.anal.setWindowFlags(Qt.CustomizeWindowHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
        self.ui4=Ui_Form3()
        self.ui4.setupUi(self.anal)
        self.connect(self.ui4.pushButton, SIGNAL("clicked()"),self.uploadFichierAnal)
        self.connect(self.ui4.pushButton_2, SIGNAL("clicked()"),self.allerte)
        self.anal.show()
    
    def uploadFichierAnal(self):
        fichier = QFileDialog.getOpenFileName(self,
                                                "Open file",
                                                "/home/puiseux/images",
                                               "File (*.pcap *.cap)")
        if fichier:
                  QMessageBox.information(self,
                                    "Fichier",
                                   self.trUtf8("You have selected :\n") + fichier)
                  self.ui4.lineEdit_2.setText(fichier)
    
    def methodeWEP(self,bssid,f):
        an=Analyse()
        exam=Examen()
        del chaineWEP[:]
        try:
                an.suspect,an.max=an.NbrDataFramSendFromStation(f,bssid)
                an.DatAvant=an.DebSendDataStation(f,bssid,an.suspect)
                an.DatApres=an.FinSendDataStation(f,bssid,an.suspect)
                an.DatAvant=an.DatAvant.replace("\n"," ")
                an.DatAvant=an.DatAvant.strip()
                an.DatApres=an.DatApres.replace("\n"," ")
                an.DatApres=an.DatApres.strip()
                an.Duree=an.DureeAttaque(an.DatAvant,an.DatApres)
                an.NbrVIsAvant=an.NbrVIsAvant(f,an.suspect,bssid,an.DatAvant)
                an.NbrVIsDurant=an.NbrVIsDurant(f,an.suspect,bssid,an.DatApres,an.DatAvant)
                an.NbrVIsApres=an.NbrVIsApres(f,an.suspect,bssid,an.DatApres)
                an.NbrDesauthWAP=an.NbrDesauthWAP(f,bssid,an.suspect)
                an.TypeAttaque=an.TypeAttaque(an.NbrVIsAvant,an.NbrVIsDurant,an.NbrVIsApres)
                exam.BssidSsid(f)
                exam.ssidSearch,exam.bssidSearch,exam.canalSearch=exam.search()
                an.ssidAP=an.ssidAP(exam.ssidSearch,exam.bssidSearch,bssid)
                if  an.TypeAttaque=="No WEP attack":
                    an.suspect="Not available"
                    an.Duree="0"
                    an.DatAvant="Not available"
                    an.DatApres="Not available"
                    an.max="Not available"
                    an.NbrDesauthWAP="Not available"
                an.pos=an.StationAssocie(f,bssid)
                if an.pos==None:
                    an.pos='14'
                an.stat,an.nbAsso=an.StationAssocieResultat(f,bssid,str(an.pos))
                an.NBR, an.macStation=an.NbrDataFramSendFromStation2(f,bssid)
                an.src,an.NbrT,an.dest=an.SrcDestDataFramSendStation(f,bssid)
                an.debAuth,an.debDes,an.debSendData,an.deDesasso,an.finSendData,an.finDes,an.finAuth=an.ChronoAttaqueWEP(f,bssid,an.suspect)
                chaineWEP.append(bssid)
                chaineWEP.append(an.suspect)
                chaineWEP.append(an.max)
                chaineWEP.append(an.DatAvant)
                chaineWEP.append(an.DatApres)
                chaineWEP.append(an.Duree)
                chaineWEP.append(an.NbrVIsAvant)
                chaineWEP.append(an.NbrVIsDurant)
                chaineWEP.append(an.NbrVIsApres)
                chaineWEP.append(an.NbrDesauthWAP)
                chaineWEP.append(an.TypeAttaque)
                chaineWEP.append(an.ssidAP)
                chaineWEP.append(an.debAuth)
                chaineWEP.append(an.debDes)
                chaineWEP.append(an.debSendData)
                chaineWEP.append(an.deDesasso)
                chaineWEP.append(an.finSendData)
                chaineWEP.append(an.finDes)
                chaineWEP.append(an.finAuth)
                #Suppression des fichiers tmp
                os.remove('FinSendDataStation.txt')
                os.remove('DebSendDataStation.txt')
                os.remove('NbrDataFramSendFromStation.txt')
                os.remove('NbrVIsApres.txt')
                os.remove('NbrVIsAvant.txt')
                os.remove('NbrDesauthWAP.txt')
                os.remove('NbrVIsDurant.txt')
                os.remove('SrcDestDataFramSendStation.txt')
                os.remove('DateDebAuthStationToWAP.txt')
                os.remove('DateFinAuthStationToWAP.txt')
                os.remove('DateFinDesauthWAP.txt')
                if an.TypeAttaque=="WEP attack":
                    self.emit(QtCore.SIGNAL("stopaction()"))
                    self.emit(QtCore.SIGNAL('custom_show1(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)'),chaineWEP,an.Duree,an.TypeAttaque,an.suspect,an.max,an.debAuth,an.debDes,an.debSendData,an.DatAvant,an.DatApres,an.deDesasso,an.finSendData,an.finDes,an.finAuth,an.stat,an.nbAsso,an.NBR,an.macStation,an.src,an.NbrT,an.dest)
                else:
                    self.emit(QtCore.SIGNAL("stopaction()"))
                    self.emit(QtCore.SIGNAL('custom_show1(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)'),chaineWEP,"Non Disponnible",an.TypeAttaque,"Non Disponnible","Non Disponnible","Non Disponnible","Non Disponnible","Non Disponnible","Non Disponnible","Non Disponnible","Non Disponnible","Non Disponnible","Non Disponnible","Non Disponnible",an.stat,an.nbAsso,an.NBR,an.macStation,an.src,an.NbrT,an.dest)
        except:
             self.emit(QtCore.SIGNAL("warning()"))
             self.emit(QtCore.SIGNAL("stopaction()"))
    def methodeDOS(self,bssid,f):
            an=Analyse()
            exam=Examen()
            del chaineDOS[:]
            try:
                 an.NbrNullStat,an.suspect=an.StationNULL(f,bssid )
                 an.NbrDesauth=an.NbrDesauthEnvoyParAPToBroad(f,bssid)
                 an.DatDebDes=an.DatDebDesauthWAPToBroad(f,bssid)
                 an.DatFinDes=an.DatFinDesauthWAPToBroad(f,bssid)
                 an.DureeAttaqueDos=an.DureeAttaque(an.DatDebDes,an.DatFinDes)
                 an.TypeAttaqueDos=an.TypeAttaqueDos(an.NbrDesauth)
                 an.NbrNull=an.NbrNULL(f,bssid)
                 an.NbrNullAvanAttak=an.NbrNullAvanAttak(f,bssid,an.DatDebDes)
                 an.NbrNULLduranAttak=an.NbrNULLduranAttak(f,bssid,an.DatDebDes,an.DatFinDes)
                 an.NbrNullApresAttak=an.NbrNullApresAttak(f,bssid,an.DatFinDes)
                 an.DebEnvoiNULL=an.DebEnvoiNULL(f,bssid)
                 if an.DebEnvoiNULL==None:
                    an.DebEnvoiNULL='Not available'
                
                 an.FinEnvoiNULL=an.FinEnvoiNULL(f,bssid)
                 if an.FinEnvoiNULL==None:
                    an.FinEnvoiNULL='Not available'
                 if an.TypeAttaqueDos=='No DoS attack':
                    an.suspect='Not available'
                    an.NbrNullStat='Not available'
                 an.DureeNull=an.DureeAttaque(an.DebEnvoiNULL,an.FinEnvoiNULL)
                
                 exam.BssidSsid(f)
                 exam.ssidSearch,exam.bssidSearch,exam.canalSearch=exam.search()
                 an.ssidAP=an.ssidAP(exam.ssidSearch,exam.bssidSearch,bssid)
                 chaineDOS.append(bssid)
                 chaineDOS.append(an.NbrNullStat)
                 chaineDOS.append(an.suspect)
                 chaineDOS.append(an.DatDebDes)
                 chaineDOS.append(an.DatFinDes)
                 chaineDOS.append(an.NbrDesauth)
                 chaineDOS.append(an.DureeAttaqueDos)
                 chaineDOS.append(an.TypeAttaqueDos)
                 chaineDOS.append(an.NbrNull)
                 chaineDOS.append(an.NbrNullAvanAttak)
                 chaineDOS.append(an.NbrNULLduranAttak)
                 chaineDOS.append(an.NbrNullApresAttak)
                 chaineDOS.append(an.DebEnvoiNULL)
                 chaineDOS.append(an.FinEnvoiNULL)
                 chaineDOS.append(an.DureeNull)
                 chaineDOS.append(an.ssidAP)
                 os.remove('NbrNULLduranAttak.txt')
                 os.remove('nbrNULLavant.txt')
                 os.remove('NbrNullApresAttak.txt')
                 os.remove('DebEnvoiNULL.txt')
                 os.remove('StationNULL.txt')
                 os.remove('FinEnvoiNULL.txt')
                 os.remove('nbrDesauthAPtoBroad.txt')
                 os.remove('DatFinDesauth.txt')
                 os.remove('DatDebDesauth.txt')
                 self.emit(QtCore.SIGNAL("stopaction()"))
                 self.emit( QtCore.SIGNAL('custom_show(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)'),chaineDOS[0],chaineDOS[5],chaineDOS[2],chaineDOS[4],chaineDOS[3],chaineDOS[1],chaineDOS[6],chaineDOS[7],chaineDOS[8],chaineDOS[9],chaineDOS[10],chaineDOS[11],chaineDOS[12],chaineDOS[13],chaineDOS[14],chaineDOS[15]) # envoyer un signal au processus pere   
                       
            except:
                 self.emit(QtCore.SIGNAL("stopaction()"))
                 self.emit(QtCore.SIGNAL("warning()"))
        
    def methodeE(self,bssid,f):
            an=Analyse()
            exam=Examen()
            del chaineEVIL[:]
            try:
                #Les méthodes
                an.DatDebDes=an.DatDebDesauthWAPToBroad(f,bssid)
                chaineEVIL.append(bssid)
                chaineEVIL.append(an.DatDebDes)
                an.DatFinDes=an.DatFinDesauthWAPToBroad(f,bssid)
                chaineEVIL.append(an.DatFinDes)
                an.heureApresDiff,an.bssidApresDiff,an.snApresDiff,an.typeApresDiff=an.NSeqApreDesauth(f,bssid,an.DatDebDes)          
                an.MomentCreationEvil=an.MomentCreationEvil(f,bssid,an.DatDebDes)
                an.NumCanalPremiereBalise,an.typeApres,an.bssidApres,an.dateApres=an.NumCanalPremiereBalise(f,bssid,an.MomentCreationEvil)
                an.canalTrans,an.adresseBSSID,an.adresseStation=an.CanalAvantCreationEvil(f,bssid,an.MomentCreationEvil)
                an.canalAvant=an.canalTrans[0]
                chaineEVIL.append(an.canalAvant)
                an.CanalEvilTwin=an.CanalEvilTwin(an.canalTrans[0],an.NumCanalPremiereBalise)
                chaineEVIL.append(an.CanalEvilTwin)
                an.SN,an.ssidEvil= an.CreationEvil(f,bssid,an.DatDebDes)
                chaineEVIL.append(an.SN)
                chaineEVIL.append(an.ssidEvil)
                an.DebEvil=an.DebEvil(f,bssid,an.MomentCreationEvil,an.CanalEvilTwin)
                chaineEVIL.append(an.DebEvil)
                an.FinEvil=an.FinEvil(f,bssid,an.MomentCreationEvil,an.CanalEvilTwin)
                chaineEVIL.append(an.FinEvil)
                an.DureeEvil=an.DureeAttaque(an.DebEvil,an.FinEvil)
                chaineEVIL.append(an.DureeEvil)
                an.TypeAttaqueEvil=an.TypeAttaqueEvil(an.CanalAvantCreationEvil, an.CanalEvilTwin)
                chaineEVIL.append(an.TypeAttaqueEvil)
                an.NbrDesauth=an.NbrDesauthEnvoyParAPToBroad(f,bssid)
                chaineEVIL.append(an.NbrDesauth)
                exam.BssidSsid(f)
                exam.ssidSearch,exam.bssidSearch,exam.canalSearch=exam.search()
                an.ssidAP=an.ssidAP(exam.ssidSearch,exam.bssidSearch,bssid)
                chaineEVIL.append(an.ssidAP)
                an.CreationEvil(f,bssid,an.DatDebDes)
                an.canalApres,an.typeApres,an.bssidApres=an.CanalApreCreationEvil(f,bssid,an.MomentCreationEvil)
                chaineEVIL.append(an.typeApres)
                chaineEVIL.append(an.bssidApres)
                os.remove('canalAprescreationevil.txt')
                os.remove('creationevil.txt')
                os.remove('debEvil.txt')
                os.remove('FinEvil.txt')
                os.remove('momentcreationevil.txt')
                os.remove('nbrDesauthAPtoBroad.txt')
                os.remove('numcanal1balise.txt')
                os.remove('nseqapredesaut.txt')
                if an.TypeAttaqueEvil=="EVIL TWIN attack":
                    self.emit(QtCore.SIGNAL("stopaction()"))
                    self.emit( QtCore.SIGNAL('custom_show2(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)'),an.CanalEvilTwin,an.SN,an.canalTrans[0],an.NbrDesauth,an.ssidEvil,an.DatFinDes,an.DatDebDes,an.DureeEvil,an.FinEvil,an.DebEvil,an.TypeAttaqueEvil,bssid,an.ssidAP,an.adresseStation,an.adresseBSSID,an.canalTrans,an.bssidApres,an.canalApres,an.typeApres,an.dateApres,an.NumCanalPremiereBalise,an.snApresDiff,an.heureApresDiff,an.bssidApresDiff,an.typeApresDiff)
            except:
                self.emit(QtCore.SIGNAL("stopaction()"))
                self.emit(QtCore.SIGNAL("warningEVIL()"))
                
    def methodeD(self,bssid,f):
            an=Analyse()
            exam=Examen()
            del chaineDOS[:]
            try:
                 an.NbrNullStat,an.suspect=an.StationNULL(f,bssid )
                 an.NbrDesauth=an.NbrDesauthEnvoyParAPToBroad(f,bssid)
                 an.DatDebDes=an.DatDebDesauthWAPToBroad(f,bssid)
                 an.DatFinDes=an.DatFinDesauthWAPToBroad(f,bssid)
                 an.DureeAttaqueDos=an.DureeAttaque(an.DatDebDes,an.DatFinDes)
                 an.TypeAttaqueDos=an.TypeAttaqueDos(an.NbrDesauth)
                 an.NbrNull=an.NbrNULL(f,bssid)
                 an.NbrNullAvanAttak=an.NbrNullAvanAttak(f,bssid,an.DatDebDes)
                 an.NbrNULLduranAttak=an.NbrNULLduranAttak(f,bssid,an.DatDebDes,an.DatFinDes)
                 an.NbrNullApresAttak=an.NbrNullApresAttak(f,bssid,an.DatFinDes)
                 an.DebEnvoiNULL=an.DebEnvoiNULL(f,bssid)
                 an.FinEnvoiNULL=an.FinEnvoiNULL(f,bssid)
                 an.DureeNull=an.DureeAttaque(an.DebEnvoiNULL,an.FinEnvoiNULL)
                 exam.BssidSsid(f)
                 exam.ssidSearch,exam.bssidSearch,exam.canalSearch=exam.search()
                 an.ssidAP=an.ssidAP(exam.ssidSearch,exam.bssidSearch,bssid)
                 chaineDOS.append(bssid)
                 chaineDOS.append(an.NbrNullStat)
                 chaineDOS.append(an.suspect)
                 chaineDOS.append(an.DatDebDes)
                 chaineDOS.append(an.DatFinDes)
                 chaineDOS.append(an.NbrDesauth)
                 chaineDOS.append(an.DureeAttaqueDos)
                 chaineDOS.append(an.TypeAttaqueDos)
                 chaineDOS.append(an.NbrNull)
                 chaineDOS.append(an.NbrNullAvanAttak)
                 chaineDOS.append(an.NbrNULLduranAttak)
                 chaineDOS.append(an.NbrNullApresAttak)
                 chaineDOS.append(an.DebEnvoiNULL)
                 chaineDOS.append(an.FinEnvoiNULL)
                 chaineDOS.append(an.DureeNull)
                 chaineDOS.append(an.ssidAP)
                 os.remove('NbrNULLduranAttak.txt')
                 os.remove('nbrNULLavant.txt')
                 os.remove('NbrNullApresAttak.txt')
                 os.remove('DebEnvoiNULL.txt')
                 os.remove('StationNULL.txt')
                 os.remove('FinEnvoiNULL.txt')
                 os.remove('nbrDesauthAPtoBroad.txt')
                 os.remove('DatFinDesauth.txt')
                 os.remove('DatDebDesauth.txt')
                 if an.TypeAttaqueDos=="DoS attack":
                     self.emit(QtCore.SIGNAL("stopaction()"))
                     self.emit( QtCore.SIGNAL('custom_show(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)'),chaineDOS[0],chaineDOS[5],chaineDOS[2],chaineDOS[4],chaineDOS[3],chaineDOS[1],chaineDOS[6],chaineDOS[7],chaineDOS[8],chaineDOS[9],chaineDOS[10],chaineDOS[11],chaineDOS[12],chaineDOS[13],chaineDOS[14],chaineDOS[15]) # envoyer un signal au processus pere   
                 else:   
                    self.emit(QtCore.SIGNAL("stopaction()"))
                    self.emit(QtCore.SIGNAL("warningDOS()"))
            except:
                self.emit(QtCore.SIGNAL("stopaction()"))
                self.emit(QtCore.SIGNAL("warningDOS()"))
            
    def methodeW(self,bssid,f):
        an=Analyse()
        exam=Examen()
        del chaineWEP[:]
        try:
                an.suspect,an.max=an.NbrDataFramSendFromStation(f,bssid)
                an.DatAvant=an.DebSendDataStation(f,bssid,an.suspect)
                an.DatApres=an.FinSendDataStation(f,bssid,an.suspect)
                an.DatAvant=an.DatAvant.replace("\n"," ")
                an.DatAvant=an.DatAvant.strip()
                an.DatApres=an.DatApres.replace("\n"," ")
                an.DatApres=an.DatApres.strip()
                an.Duree=an.DureeAttaque(an.DatAvant,an.DatApres)
                an.NbrVIsAvant=an.NbrVIsAvant(f,an.suspect,bssid,an.DatAvant)
                an.NbrVIsDurant=an.NbrVIsDurant(f,an.suspect,bssid,an.DatApres,an.DatAvant)
                an.NbrVIsApres=an.NbrVIsApres(f,an.suspect,bssid,an.DatApres)
                an.NbrDesauthWAP=an.NbrDesauthWAP(f,bssid,an.suspect)
                an.TypeAttaque=an.TypeAttaque(an.NbrVIsAvant,an.NbrVIsDurant,an.NbrVIsApres)
                exam.BssidSsid(f)
                exam.ssidSearch,exam.bssidSearch,exam.canalSearch=exam.search()
                an.ssidAP=an.ssidAP(exam.ssidSearch,exam.bssidSearch,bssid)
                if  an.TypeAttaque=="No WEP attack":
                    an.suspect="Not available"
                    an.Duree="0"
                    an.DatAvant="Not available"
                    an.DatApres="Not available"
                    an.max="Not available"
                    an.NbrDesauthWAP="Not available"
                an.pos=an.StationAssocie(f,bssid)
                if an.pos==None:
                    an.pos='14'
                an.stat,an.nbAsso=an.StationAssocieResultat(f,bssid,str(an.pos))
                an.NBR, an.macStation=an.NbrDataFramSendFromStation2(f,bssid)
                an.src,an.NbrT,an.dest=an.SrcDestDataFramSendStation(f,bssid)
                an.debAuth,an.debDes,an.debSendData,an.deDesasso,an.finSendData,an.finDes,an.finAuth=an.ChronoAttaqueWEP(f,bssid,an.suspect)
                chaineWEP.append(bssid)
                chaineWEP.append(an.suspect)
                chaineWEP.append(an.max)
                chaineWEP.append(an.DatAvant)
                chaineWEP.append(an.DatApres)
                chaineWEP.append(an.Duree)
                chaineWEP.append(an.NbrVIsAvant)
                chaineWEP.append(an.NbrVIsDurant)
                chaineWEP.append(an.NbrVIsApres)
                chaineWEP.append(an.NbrDesauthWAP)
                chaineWEP.append(an.TypeAttaque)
                chaineWEP.append(an.ssidAP)
                chaineWEP.append(an.debAuth)
                chaineWEP.append(an.debDes)
                chaineWEP.append(an.debSendData)
                chaineWEP.append(an.deDesasso)
                chaineWEP.append(an.finSendData)
                chaineWEP.append(an.finDes)
                chaineWEP.append(an.finAuth)
                #Suppression des fichiers tmp
                os.remove('FinSendDataStation.txt')
                os.remove('DebSendDataStation.txt')
                os.remove('NbrDataFramSendFromStation.txt')
                os.remove('NbrVIsApres.txt')
                os.remove('NbrVIsAvant.txt')
                os.remove('NbrDesauthWAP.txt')
                os.remove('NbrVIsDurant.txt')
                os.remove('SrcDestDataFramSendStation.txt')
                os.remove('DateDebAuthStationToWAP.txt')
                os.remove('DateFinAuthStationToWAP.txt')
                os.remove('DateFinDesauthWAP.txt')
                if an.TypeAttaque=="WEP attack":
                    self.emit(QtCore.SIGNAL("stopaction()"))
                    self.emit(QtCore.SIGNAL('custom_show1(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)'),chaineWEP,an.Duree,an.TypeAttaque,an.suspect,an.max,an.debAuth,an.debDes,an.debSendData,an.DatAvant,an.DatApres,an.deDesasso,an.finSendData,an.finDes,an.finAuth,an.stat,an.nbAsso,an.NBR,an.macStation,an.src,an.NbrT,an.dest)
                else:
                    self.emit(QtCore.SIGNAL("stopaction()"))
                    self.emit(QtCore.SIGNAL("warningWEP()"))
                   
        except:
             self.emit(QtCore.SIGNAL("warningWEP()"))
             self.emit(QtCore.SIGNAL("stopaction()"))
            
             
                    
    def methodeEVIL(self,bssid,f):
            an=Analyse()
            exam=Examen()
            del chaineEVIL[:]
            try:
                #Les méthodes
                an.DatDebDes=an.DatDebDesauthWAPToBroad(f,bssid)
                exam.BssidSsid(f)
                exam.ssidSearch,exam.bssidSearch,exam.canalSearch=exam.search()
                for chaine in exam.bssidSearch:
                    if chaine==bssid:
                        an.canalAvant=exam.canalSearch[exam.bssidSearch.index(chaine)]
         
                chaineEVIL.append(bssid)
                chaineEVIL.append(an.DatDebDes)
                an.DatFinDes=an.DatFinDesauthWAPToBroad(f,bssid)
                chaineEVIL.append(an.DatFinDes)
                an.heureApresDiff,an.bssidApresDiff,an.snApresDiff,an.typeApresDiff=an.NSeqApreDesauth(f,bssid,an.DatDebDes)          
                an.MomentCreationEvil=an.MomentCreationEvil(f,bssid,an.DatDebDes)
                an.NumCanalPremiereBalise,an.typeApres,an.bssidApres,an.dateApres=an.NumCanalPremiereBalise(f,bssid,an.MomentCreationEvil)
                an.canalTrans,an.adresseBSSID,an.adresseStation=an.CanalAvantCreationEvil(f,bssid,an.MomentCreationEvil)

                chaineEVIL.append(an.canalAvant)
                an.CanalEvilTwin=an.CanalEvilTwin(an.canalAvant,an.NumCanalPremiereBalise)
                chaineEVIL.append(an.CanalEvilTwin)
                an.SN,an.ssidEvil= an.CreationEvil(f,bssid,an.DatDebDes)
                chaineEVIL.append(an.SN)
                chaineEVIL.append(an.ssidEvil)
                an.DebEvil=an.DebEvil(f,bssid,an.MomentCreationEvil,an.CanalEvilTwin)
                if an.DebEvil==None:
                    an.DebEvil='Not available'
                chaineEVIL.append(an.DebEvil)
                an.FinEvil=an.FinEvil(f,bssid,an.MomentCreationEvil,an.CanalEvilTwin)
                if an.FinEvil==None:
                    an.FinEvil='Not available'
                chaineEVIL.append(an.FinEvil)
                an.DureeEvil=an.DureeAttaque(an.DebEvil,an.FinEvil)
                chaineEVIL.append(an.DureeEvil)
                an.TypeAttaqueEvil=an.TypeAttaqueEvil(an.CanalAvantCreationEvil, an.CanalEvilTwin)
                chaineEVIL.append(an.TypeAttaqueEvil)
                an.NbrDesauth=an.NbrDesauthEnvoyParAPToBroad(f,bssid)
                chaineEVIL.append(an.NbrDesauth)
                an.ssidAP=an.ssidAP(exam.ssidSearch,exam.bssidSearch,bssid)
                chaineEVIL.append(an.ssidAP)
                an.CreationEvil(f,bssid,an.DatDebDes)
                an.canalApres,an.typeApres,an.bssidApres=an.CanalApreCreationEvil(f,bssid,an.MomentCreationEvil)
                chaineEVIL.append(an.typeApres)
                chaineEVIL.append(an.bssidApres)
              
                if an.TypeAttaqueEvil=="No EVIL TWIN attack":
                    an.bssidEvil='Not available'
                else:
                    an.bssidEvil=bssid
                chaineEVIL.append(an.bssidEvil)
                os.remove('canalAprescreationevil.txt')
                #os.remove('canalavantcreationevil.txt')
                os.remove('creationevil.txt')
                os.remove('debEvil.txt')
                os.remove('FinEvil.txt')
                os.remove('momentcreationevil.txt')
                os.remove('nbrDesauthAPtoBroad.txt')
                os.remove('numcanal1balise.txt')
                os.remove('nseqapredesaut.txt')
                self.emit(QtCore.SIGNAL("stopaction()"))
                self.emit( QtCore.SIGNAL('custom_show2(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)'),an.bssidEvil,an.CanalEvilTwin,an.SN,an.canalAvant,an.NbrDesauth,an.ssidEvil,an.DatFinDes,an.DatDebDes,an.DureeEvil,an.FinEvil,an.DebEvil,an.TypeAttaqueEvil,bssid,an.ssidAP,an.adresseStation,an.adresseBSSID,an.canalTrans,an.bssidApres,an.canalApres,an.typeApres,an.dateApres,an.NumCanalPremiereBalise,an.snApresDiff,an.heureApresDiff,an.bssidApresDiff,an.typeApresDiff)
            
            except:
                self.emit(QtCore.SIGNAL("stopaction()"))
                self.emit(QtCore.SIGNAL("warning()"))
                
                
    def warning(self):
       QMessageBox.information(self,"RESULT",self.trUtf8("No such attack has been realized \n"))
    def warningDOS(self):
       QMessageBox.information(self,"RESULT",self.trUtf8("No DoS attack has been realized \n")) 
    def warningWEP(self):
       QMessageBox.information(self,"RESULT",self.trUtf8("No WEP cracking attack has been realized \n"))     
    def warningEVIL(self):
       QMessageBox.information(self,"RESULTAT",self.trUtf8("No EVIL TWIN attack has been realized \n"))   
    def custom_show2(self,bssidEvil,CanalEvilTwin,SN,canalTrans1,NbrDesauth,ssidEvil,DatFinDes,DatDebDes,DureeEvil,FinEvil,DebEvil,TypeAttaqueEvil,bssid,ssid,adresseStation,adresseBSSID,canalTrans,bssidApres,canalApres,typeApres,dateApres,NumCanalPremiereBalise,snApresDiff,heureApresDiff,bssidApresDiff,typeApresDiff):
           
                self.resultatAnalyse=QtGui.QDialog()
                self.ui7=Ui_Dialog3()
                self.ui7.setupUi(self.resultatAnalyse)
                #Affichage dans le tableau 1:(canaux de transmssion avant creation de EVIL TWIN.
                
                self.ui7.tableWidget.setColumnCount(3)
                self.ui7.tableWidget.resizeRowsToContents()
                self.ui7.tableWidget.resizeColumnsToContents()
                self.ui7.tableWidget.setColumnWidth(0,150)
                self.ui7.tableWidget.setColumnWidth(1,150)
                self.ui7.tableWidget.setColumnWidth(2,140)
                a = QTableWidgetItem("BSSID")
                b = QTableWidgetItem("MAC address")
                c = QTableWidgetItem("Channel ")
                i=0
                j=0
                k=0
                count=0
                for stat in adresseStation:
                    self.ui7.tableWidget.setRowCount(count+1)
                    self.ui7.tableWidget.setHorizontalHeaderItem (0, a)
                    ite0=QTableWidgetItem("%s"%(adresseBSSID[adresseStation.index(stat)]))
                    self.ui7.tableWidget.setItem(i,0,ite0)
                    i=i+1
                    self.ui7.tableWidget.setHorizontalHeaderItem (1, b)
                    ite1=QTableWidgetItem("%s"%(stat))
                    self.ui7.tableWidget.setItem(j,1,ite1)
                    j=j+1
                    self.ui7.tableWidget.setHorizontalHeaderItem (2, c)
                    ite2=QTableWidgetItem("%s"%(canalTrans[adresseStation.index(stat)]))
                    self.ui7.tableWidget.setItem(k,2,ite2)
                    k=k+1
                    count=count+1   
                #Canaux de transmission après attaque
                self.ui7.tableWidget_2.setColumnCount(3)
                self.ui7.tableWidget_2.resizeRowsToContents()
                self.ui7.tableWidget_2.resizeColumnsToContents()
                self.ui7.tableWidget_2.setColumnWidth(0,120)
                self.ui7.tableWidget_2.setColumnWidth(1,140)
                self.ui7.tableWidget_2.setColumnWidth(2,150)
                a = QTableWidgetItem("Frame")
                b = QTableWidgetItem("Channel ")
                c = QTableWidgetItem("BSSID")           
                i=0
                j=0
                k=0
                cnt=0
                for canal in canalApres:
                    self.ui7.tableWidget_2.setRowCount(cnt+1)
                    self.ui7.tableWidget_2.setHorizontalHeaderItem (0, a)
                    ite0=QTableWidgetItem("%s"%(bssidApres[canalApres.index(canal)]))
                    self.ui7.tableWidget_2.setItem(i,0,ite0)
                    i=i+1
                  
                    self.ui7.tableWidget_2.setHorizontalHeaderItem (1, b)
                    ite1=QTableWidgetItem("%s"%(canal))
                    self.ui7.tableWidget_2.setItem(j,1,ite1)
                    j=j+1
                
                    self.ui7.tableWidget_2.setHorizontalHeaderItem (2, c)
                    ite2=QTableWidgetItem("%s"%(typeApres[canalApres.index(canal)]))
                    self.ui7.tableWidget_2.setItem(k,2,ite2)
                    k=k+1
                    cnt=cnt+1
                    
           #Affichage canaux après création de evil twiin
                self.ui7.tableWidget_3.setColumnCount(4)
                self.ui7.tableWidget_3.resizeRowsToContents()
                self.ui7.tableWidget_3.resizeColumnsToContents()
                self.ui7.tableWidget_3.setColumnWidth(0,55)
                self.ui7.tableWidget_3.setColumnWidth(1,130)
                self.ui7.tableWidget_3.setColumnWidth(2,55)
                self.ui7.tableWidget_3.setColumnWidth(3,195)
                a = QTableWidgetItem("Channel")
                b = QTableWidgetItem("BSSID")
                c = QTableWidgetItem("Frame")          
                d = QTableWidgetItem("Date")   
                i=0
                j=0
                k=0
                l=0
                cnt=0
                
                for date in dateApres:
                    self.ui7.tableWidget_3.setRowCount(cnt+1)
                    self.ui7.tableWidget_3.setHorizontalHeaderItem (0, a)
                    ite0=QTableWidgetItem("%s"%(NumCanalPremiereBalise[dateApres.index(date)]))
                    self.ui7.tableWidget_3.setItem(i,0,ite0)
                    i=i+1
                  
                    self.ui7.tableWidget_3.setHorizontalHeaderItem (1, b)
                    ite1=QTableWidgetItem("%s"%(typeApres[dateApres.index(date)]))
                    self.ui7.tableWidget_3.setItem(j,1,ite1)
                    j=j+1
             
                    self.ui7.tableWidget_3.setHorizontalHeaderItem (2, c)
                    ite2=QTableWidgetItem("%s"%(bssidApres[canalApres.index(canal)]))
                    self.ui7.tableWidget_3.setItem(k,2,ite2)
                    k=k+1
                    
                    self.ui7.tableWidget_3.setHorizontalHeaderItem (3, d)
                    ite3=QTableWidgetItem("%s"%(date))
                    self.ui7.tableWidget_3.setItem(l,3,ite3)
                    l=l+1
                    cnt=cnt+1
                    
                #Désséquencement des numéros de séquences
                 #Affichage canaux après création de evil twiin
                self.ui7.tableWidget_4.setColumnCount(4)
                self.ui7.tableWidget_4.resizeRowsToContents()
                self.ui7.tableWidget_4.resizeColumnsToContents()
                self.ui7.tableWidget_4.setColumnWidth(0,160)
                self.ui7.tableWidget_4.setColumnWidth(1,150)
                self.ui7.tableWidget_4.setColumnWidth(2,150)
                self.ui7.tableWidget_4.setColumnWidth(3,70)
                
                a = QTableWidgetItem("Time")
                b = QTableWidgetItem("BSSID")
                c = QTableWidgetItem("Sequence Number")          
                d = QTableWidgetItem("Frame")  
                i=0
                j=0
                k=0
                l=0
                cnt=0
                
                for sn in snApresDiff:
                    self.ui7.tableWidget_4.setRowCount(cnt+1)
                    self.ui7.tableWidget_4.setHorizontalHeaderItem (0, a)
                    ite0=QTableWidgetItem("%s"%(heureApresDiff[snApresDiff.index(sn)]))
                    self.ui7.tableWidget_4.setItem(i,0,ite0)
                    i=i+1
                 
                    self.ui7.tableWidget_4.setHorizontalHeaderItem (1, b)
                    ite1=QTableWidgetItem("%s"%(bssidApresDiff[snApresDiff.index(sn)]))
                    self.ui7.tableWidget_4.setItem(j,1,ite1)
                    j=j+1
            
                    self.ui7.tableWidget_4.setHorizontalHeaderItem (2, c)
                    ite2=QTableWidgetItem("%s"%(sn))
                    self.ui7.tableWidget_4.setItem(k,2,ite2)
                    k=k+1
                    
                    self.ui7.tableWidget_4.setHorizontalHeaderItem (3, d)
                    ite3=QTableWidgetItem("%s"%(typeApresDiff[snApresDiff.index(sn)]))
                    self.ui7.tableWidget_4.setItem(l,3,ite3)
                    l=l+1
                    cnt=cnt+1
                
                self.resultatAnalyse.show()
                #Affichage des résultats EVIL TWIN
                self.ui7.lineEdit.setText(str(ssid))
                self.ui7.lineEdit_2.setText(str(bssid))
                self.ui7.lineEdit_3.setText(str(bssidEvil))
                self.ui7.lineEdit_4.setText(str(TypeAttaqueEvil)) 
                self.ui7.lineEdit_5.setText(str(DebEvil))
                self.ui7.lineEdit_6.setText(str(FinEvil))
                self.ui7.lineEdit_7.setText(str(str(DureeEvil)))
                self.ui7.lineEdit_8.setText(str(DatDebDes)) 
                self.ui7.lineEdit_9.setText(str(DatFinDes))
                self.ui7.lineEdit_10.setText(str(ssidEvil))
                self.ui7.lineEdit_11.setText(str(NbrDesauth))
                self.ui7.lineEdit_12.setText(str(canalTrans1))
                self.ui7.lineEdit_13.setText(str("CH: "+CanalEvilTwin))
                self.ui7.lineEdit_14.setText(str(SN.strip(",")))
                self.connect(self.ui7.pushButton_2,SIGNAL("clicked()"),self.imprimerEVIL)
    def affiche(self,fichierpdf):
        # afficher le fichier pdf avec le visionneur pdf par défaut
        try:
            os.startfile(fichierpdf) # solution pour Windows
        except:
            os.system('xdg-open ' + fichierpdf)# solution pour Linux récent
    
    def imprimerWEP(self):
        # créer l'imprimante
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setOutputFileName(u"fichier.pdf") # => impression dans un pdf
        printer.setCreator(u"monapplication")
        printer.setDocName(u"mondocument")
        printer.setPageSize(QtGui.QPrinter.A4)
        printer.setOrientation(QtGui.QPrinter.Portrait)
        printer.setFullPage(True) # NB: incompatible avec les marges!
        resolution = printer.resolution() # en principe, c'est 1200dpi
        # utilitaire pour convertir mm => pixels
        mm2px = lambda mm: int(mm/25.4*resolution)
        # créer et démarrer l'outil de dessin
        painter = QtGui.QPainter()
        painter.begin(printer)
        # configurer la police de caractères
        font = QtGui.QFont()
        font.setFamily("DejaVue Sans")
        font.setPointSize(12)
        #font.setBold(True)
        font.setItalic(False)
        #font.setUnderline(True) 
        painter.setFont(font)

        # imprimer un texte au milieu de la page A4
        x = mm2px(30)
        y = mm2px(20/2)
        trg = mm2px(30)
        trd = mm2px(30/2)
        ssid= mm2px(10/2)
        ssid1= mm2px(50/2)
        a = mm2px(10/2)
        b = mm2px(70/2)
        c = mm2px(10/2)
        d = mm2px(90/2)
        e = mm2px(10/2)
        f = mm2px(110/2)
        g = mm2px(10/2)
        h = mm2px(130/2)
        i = mm2px(10/2)
        j = mm2px(150/2)
        k = mm2px(10/2)
        l = mm2px(170/2)
        m = mm2px(10/2)
        n = mm2px(190/2)
        o = mm2px(10/2)
        p = mm2px(210/2)
        q = mm2px(10/2)
        r = mm2px(230/2)
        s = mm2px(10/2)
        t = mm2px(250/2)
        v= mm2px(10/2)
        w = mm2px(270/2)
        sig= mm2px(180/2)
        cachet = mm2px(500/2)
        painter.drawText(x, y, u"Report on investigation results (WEP cracking attack)")
        painter.drawText(trg, trd, u"------------------------------------------------------------------------------")
        painter.drawText(ssid, ssid1, u"SSID :%s"%(str(chaineWEP[11])))
        painter.drawText(a, b, u"BSSID :%s"%(str(chaineWEP[0])))
        painter.drawText(c, d, u"Suspect :%s"%(str(chaineWEP[1])))
        painter.drawText(e, f, u"Type of attack :%s"%(str(chaineWEP[10])))
        painter.drawText(g, h, u"Start date of attack :%s"%(str(chaineWEP[3])))
        painter.drawText(i, j, u"End date of attack :%s"%(str(chaineWEP[4])))
        painter.drawText(k, l, u"Attack duration :%s seconds"%(str(chaineWEP[5])))
        painter.drawText(m, n, u"Deauthentification frames sent by suspect :%s"%(str(chaineWEP[9].strip("\n"))))
        painter.drawText(o, p, u"Broadcast data frames by suspect :%s"%(str(chaineWEP[2].strip("\n"))))
        painter.drawText(q, r, u"Initialization vector before attack :%s"%(str(chaineWEP[6].strip("\n"))))
        painter.drawText(s, t, u"Initialization vector during attack :%s"%(str(chaineWEP[7].strip("\n"))))
        painter.drawText(v, w, u"Initialization vector after attack :%s"%(str(chaineWEP[8].strip("\n"))))
        painter.drawText(sig, cachet, u"Stamp and signature of the investigator :")
        painter.end()
        del chaineWEP[:]
        # afficher le fichier pdf imprimé
        self.affiche(u"file.pdf")    
    def imprimerEVIL(self):
        # créer l'imprimante
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setOutputFileName(u"file.pdf") # => impression dans un pdf
        printer.setCreator(u"monapplication")
        printer.setDocName(u"mondocument")
        printer.setPageSize(QtGui.QPrinter.A4)
        printer.setOrientation(QtGui.QPrinter.Portrait)
        printer.setFullPage(True) # NB: incompatible avec les marges!
        resolution = printer.resolution() # en principe, c'est 1200dpi
         
        # utilitaire pour convertir mm => pixels
        mm2px = lambda mm: int(mm/25.4*resolution)
         
        # créer et démarrer l'outil de dessin
        painter = QtGui.QPainter()
        painter.begin(printer)
         
        # configurer la police de caractères
        font = QtGui.QFont()
        font.setFamily("DejaVue Sans")
        font.setPointSize(12)
        #font.setBold(True)
        font.setItalic(False)
        #font.setUnderline(True) 
        painter.setFont(font)

        # imprimer un texte au milieu de la page A4
        tit = mm2px(40)
        tit1 = mm2px(20/2)
        trg = mm2px(40)
        trd = mm2px(30/2)
        ssid= mm2px(10/2)
        ssid1= mm2px(50/2)
        a = mm2px(10/2)
        b = mm2px(70/2)
        c = mm2px(10/2)
        d = mm2px(90/2)
        e = mm2px(10/2)
        f = mm2px(110/2)
        g = mm2px(10/2)
        h = mm2px(130/2)
        i = mm2px(10/2)
        j = mm2px(150/2)
        dif=mm2px(10/2)
        dif1=mm2px(170/2)
        k = mm2px(10/2)
        l = mm2px(190/2)
        m = mm2px(10/2)
        n = mm2px(210/2)
        o = mm2px(10/2)
        p = mm2px(230/2)
        q = mm2px(10/2)
        r = mm2px(250/2)
        s = mm2px(10/2)
        t = mm2px(270/2)
        v= mm2px(10/2)
        w = mm2px(290/2)
        sig= mm2px(180/2)
        cachet = mm2px(500/2)
        painter.drawText(tit, tit1, u"Report on investigation results ( EVIL TWIN attack)")
        painter.drawText(trg, trd, u"------------------------------------------------------------------------------------")
        painter.drawText(ssid, ssid1, u"SSID :%s"%(str(chaineEVIL[12])))
        painter.drawText(a, b, u"BSSID :%s"%(str(chaineEVIL[0])))
        painter.drawText(c, d, u"BSSID EVIL TWIN :%s"%(str(chaineEVIL[15])))
        painter.drawText(e, f, u"Type of attack :%s"%(str(chaineEVIL[10])))
        painter.drawText(g, h, u"Date of creating Evil Twin :%s"%(str(chaineEVIL[7].strip("\n"))))
        painter.drawText(i, j, u"End date of Evil Twin :%s"%(str(chaineEVIL[8].strip("\n"))))
        painter.drawText(dif, dif1, u"Start date of broadcast deauthentification %s"%(str(chaineEVIL[1].strip("\n"))))
        painter.drawText(k, l, u"End date of broadcast deauthentification %s"%(str(chaineEVIL[2].strip("\n"))))
        painter.drawText(m, n, u"Moment of creating Evil Twin :%s et %s"%(str(chaineEVIL[5]),str(chaineEVIL[6].strip("\n"))))
        painter.drawText(o, p, u"Attack duration :%s secondes"%(str(chaineEVIL[9])))
        painter.drawText(q, r, u"Number of deauthentification frames broadcasted by %s :%s"%(str(chaineEVIL[12].strip("\n")),str(chaineEVIL[11].strip("\n"))))
        painter.drawText(s, t, u"Transmission channel of legitimate access point :%s"%(str(chaineEVIL[3])))
        painter.drawText(v, w, u"Transmission channel of EVIL TWIN: CH: %s"%(str(chaineEVIL[4])))
        painter.drawText(sig, cachet, u"Stamp and signature of the investigator :")
        painter.end()
        del chaineEVIL[:]
        # afficher le fichier pdf imprimé
        self.affiche(u"file.pdf")           
    def imprimerDOS(self):
        # créer l'imprimante
        printer = QtGui.QPrinter(QtGui.QPrinter.HighResolution)
        printer.setOutputFileName(u"file.pdf") # => impression dans un pdf
        printer.setCreator(u"monapplication")
        printer.setDocName(u"mondocument")
        printer.setPageSize(QtGui.QPrinter.A4)
        printer.setOrientation(QtGui.QPrinter.Portrait)
        printer.setFullPage(True) # NB: incompatible avec les marges!
        resolution = printer.resolution() # en principe, c'est 1200dpi
         
        # utilitaire pour convertir mm => pixels
        mm2px = lambda mm: int(mm/25.4*resolution)
         
        # créer et démarrer l'outil de dessin
        painter = QtGui.QPainter()
        painter.begin(printer)
         
        # configurer la police de caractères
        font = QtGui.QFont()
        font.setFamily("DejaVue Sans")
        font.setPointSize(12)
        #font.setBold(True)
        font.setItalic(False)
        #font.setUnderline(True) 
        painter.setFont(font)

        # imprimer un texte au milieu de la page A4
        titre = mm2px(30)
        titre1 = mm2px(20/2)
        trg = mm2px(30)
        trd = mm2px(30/2)
        ssid= mm2px(10/2)
        ssid1= mm2px(50/2)
        a = mm2px(10/2)
        b = mm2px(70/2)
        c = mm2px(10/2)
        d = mm2px(90/2)
        e = mm2px(10/2)
        f = mm2px(110/2)
        g = mm2px(10/2)
        h = mm2px(130/2)
        i = mm2px(10/2)
        j = mm2px(150/2)
        k = mm2px(10/2)
        l = mm2px(170/2)
        m = mm2px(10/2)
        n = mm2px(190/2)
        o = mm2px(10/2)
        p = mm2px(210/2)
        q = mm2px(10/2)
        r = mm2px(230/2)
        s = mm2px(10/2)
        t = mm2px(250/2)
        u = mm2px(10/2)
        v = mm2px(270/2)
        w = mm2px(10/2)
        x = mm2px(290/2)
        y = mm2px(10/2)
        z = mm2px(310/2)
        ab = mm2px(10/2)
        cd = mm2px(330/2)
        sig= mm2px(180/2)
        cachet = mm2px(500/2)
        painter.drawText(titre, titre1, u"Report of investigation results (DoS attack)")
        painter.drawText(trg, trd, u"-----------------------------------------------------------------------------------")
        painter.drawText(ssid, ssid1, u"SSID :%s"%(str(chaineDOS[15])))
        painter.drawText(a, b, u"BSSID :%s"%(str(chaineDOS[0])))
        painter.drawText(c, d, u"Suspect :%s"%(str(chaineDOS[2])))
        painter.drawText(e, f, u"Type of attack :%s"%(str(chaineDOS[7])))
        painter.drawText(g, h, u"Start date of WAP's broadcast deauthentification :%s"%(str(chaineDOS[3])))
        painter.drawText(i, j, u"End date of WAP's broadcast deauthentification :%s"%(str(chaineDOS[4])))
        painter.drawText(k, l, u"Start date of sending NULL subtype of data frames %s"%(str(chaineDOS[12].strip("\n"))))
        painter.drawText(m, n, u"End date of sending NULL subtype of data frames :%s"%(str(chaineDOS[13].strip("\n"))))
        painter.drawText(o, p, u"Attack duration :%s seconds"%(str(chaineDOS[6])))
        painter.drawText(q, r, u"Number of WAP's broadcast deauthentification :%s"%(str(chaineDOS[5].strip("\n"))))
        painter.drawText(s, t, u"Number of NULL subtype of data frames sent by all stations :%s"%(str(chaineDOS[8].strip("\n"))))
        painter.drawText(u, v, u"Number of NULL subtype of data frames before broadcast deauthentification  :%s"%(str(chaineDOS[9].strip("\n"))))
        painter.drawText(w, x, u"Number of NULL subtype of data frames during broadcast deauthentification :%s"%(str(chaineDOS[10].strip("\n"))))
        painter.drawText(y, z, u"Number of NULL subtype of data frames after broadcast deauthentification :%s"%(str(chaineDOS[11].strip("\n"))))
        painter.drawText(ab, cd, u"Number of NULL subtype of data frames sent by suspect :%s"%(str(chaineDOS[1].strip("\n"))))
        painter.drawText(sig, cachet, u"Stamp and signature of the investigator :")
        painter.end()
        del chaineDOS[:]
        # afficher le fichier pdf imprimé
        self.affiche(u"file.pdf")    
            
        
    def custom_show1(self,x,Duree,TypeAttaque,suspect,max,debAuth,debDes,debSendData,DatAvant,DatApres,deDesasso,finSendData,finDes,finAuth,stat,nbasso,nbr,macstation,src,nbrt,dest):
                an=Analyse()
                self.resultatAnalyse=QtGui.QDialog()
                self.ui5=Ui_Dialog1()
                self.ui5.setupUi(self.resultatAnalyse)
                self.resultatAnalyse.show()
                #Affichage des stations associes dans le tableau 1 de la fenetre resultatAnalWEP.                self.ui5.tableWidget.setColumnCount(2)
                self.ui5.tableWidget.setColumnCount(2)
                self.ui5.tableWidget.resizeRowsToContents()
                self.ui5.tableWidget.resizeColumnsToContents()
                self.ui5.tableWidget.setColumnWidth(0,150)
                self.ui5.tableWidget.setColumnWidth(1,150)
                a = QTableWidgetItem("Number of times")
                b = QTableWidgetItem("MAC address")

                j=0
                k=0
                count=0
                for st in stat:           
                    self.ui5.tableWidget.setRowCount(count+1)
                    self.ui5.tableWidget.setHorizontalHeaderItem (0, a)
                    ite0=QTableWidgetItem("%s"%(nbasso[stat.index(st)]))
                    self.ui5.tableWidget.setItem(j,0,ite0)
                    j=j+1

                    self.ui5.tableWidget.setHorizontalHeaderItem (1, b)
                    ite1=QTableWidgetItem("%s"%(st))
                    self.ui5.tableWidget.setItem(k,1,ite1)
                    k=k+1
                    count=count+1

                #Affichage dans le 2eme tableau: Nombre de tram donne envoye par chaque station.
                self.ui5.tableWidget_2.setColumnCount(2)
                self.ui5.tableWidget_2.resizeRowsToContents()
                self.ui5.tableWidget_2.resizeColumnsToContents()
                self.ui5.tableWidget_2.setColumnWidth(0,150)
                self.ui5.tableWidget_2.setColumnWidth(1,145)

                c1=QTableWidgetItem("MAC address")
                c2=QTableWidgetItem("Number ")

                i1=0
                i2=0
                cont=0
                for NbrTram in nbr:
                    self.ui5.tableWidget_2.setRowCount(cont+1)
                    
                    self.ui5.tableWidget_2.setHorizontalHeaderItem (0, c1)
                    ittem=QTableWidgetItem(str((macstation[nbr.index(NbrTram)])))
                    self.ui5.tableWidget_2.setItem(i1,0,ittem)
                    i1=i1+1

                    self.ui5.tableWidget_2.setHorizontalHeaderItem(1,c2)
                    item=QTableWidgetItem(str((NbrTram)))
                    self.ui5.tableWidget_2.setItem(i2,1,item)
                    i2=i2+1
                    cont=cont+1

                self.ui5.tableWidget_3.setColumnCount(3)
                self.ui5.tableWidget_3.resizeRowsToContents()
                self.ui5.tableWidget_3.resizeColumnsToContents()
                self.ui5.tableWidget_3.setColumnWidth(0,150)
                self.ui5.tableWidget_3.setColumnWidth(1,65)
                self.ui5.tableWidget_3.setColumnWidth(2,150)

                cc=QTableWidgetItem("Source address")
                cs=QTableWidgetItem("Number ")
                cz=QTableWidgetItem("Destination address")

                i3=0
                i4=0
                i5=0
                cntr=0
                for Srcs in src:
                    self.ui5.tableWidget_3.setRowCount(cntr+1)
                    self.ui5.tableWidget_3.setHorizontalHeaderItem (0, cc)
                    ITem1=QTableWidgetItem("%s"%(Srcs))
                    self.ui5.tableWidget_3.setItem(i3,0,ITem1)
                    i3=i3+1
                    self.ui5.tableWidget_3.setHorizontalHeaderItem (1,cs)
                    ITem2=QTableWidgetItem("%s"%(nbrt[src.index(Srcs)]))
                    self.ui5.tableWidget_3.setItem(i4,1,ITem2)
                    i4=i4+1
                    self.ui5.tableWidget_3.setHorizontalHeaderItem (2,cz)
                    ITem3=QTableWidgetItem("%s"%(dest[src.index(Srcs)]))
                    self.ui5.tableWidget_3.setItem(i5,2,ITem3)
                    i5=i5+1
                    cntr=cntr+1
               #Affichage dans le 4eme tableau: ChRonologie des activites du suspect.
                self.ui5.lineEdit_5.setText(x[1])
                station=self.ui5.lineEdit_5.text()

                self.ui5.tableWidget_4.setColumnCount(1)
                self.ui5.tableWidget_4.resizeRowsToContents()
                self.ui5.tableWidget_4.resizeColumnsToContents()
                self.ui5.tableWidget_4.setRowCount(7)
                self.ui5.tableWidget_4.setColumnWidth(0,265)

                t=QTableWidgetItem("Start date of Authentification frames")
                tt=QTableWidgetItem("Start date of Desauthentification frames")
                ttt=QTableWidgetItem("Start date of data frames")
                o=QTableWidgetItem("Start date of Disassociation frames")
                oo=QTableWidgetItem("End date of data frames")
                ooo=QTableWidgetItem("End date of Desauthentification frames")
                q=QTableWidgetItem("End date Authentification frames")
                na=QTableWidgetItem("Date")
                self.ui5.tableWidget_4.setHorizontalHeaderItem(0,na)
                self.ui5.tableWidget_4.setVerticalHeaderItem (0,t)
                IT1=QTableWidgetItem("%s"%(debAuth))
                self.ui5.tableWidget_4.setItem(0,0,IT1)

                self.ui5.tableWidget_4.setVerticalHeaderItem (1,tt)
                IT2=QTableWidgetItem("%s"%(debDes))
                self.ui5.tableWidget_4.setItem(1,0,IT2)

                self.ui5.tableWidget_4.setVerticalHeaderItem (2,ttt)
                IT3=QTableWidgetItem("%s"%(debSendData))
                self.ui5.tableWidget_4.setItem(2,0,IT3)

                self.ui5.tableWidget_4.setVerticalHeaderItem (3,o)
                IT4=QTableWidgetItem("%s"%(deDesasso))
                self.ui5.tableWidget_4.setItem(3,0,IT4)

                self.ui5.tableWidget_4.setVerticalHeaderItem (4,oo)
                IT5=QTableWidgetItem("%s"%(finSendData))
                self.ui5.tableWidget_4.setItem(4,0,IT5)

                self.ui5.tableWidget_4.setVerticalHeaderItem (5,ooo)
                IT6=QTableWidgetItem("%s"%(finDes))
                self.ui5.tableWidget_4.setItem(5,0,IT6)

                self.ui5.tableWidget_4.setVerticalHeaderItem (6,q)
                IT7=QTableWidgetItem("%s"%(finAuth))
                self.ui5.tableWidget_4.setItem(6,0,IT7)
                self.ui5.lineEdit_3.setText(str(x[11]))
                self.ui5.lineEdit_4.setText(str(x[0]))
                self.ui5.lineEdit_5.setText(str(suspect))
                self.ui5.lineEdit_6.setText(str(max)) 
                self.ui5.lineEdit_7.setText(str(x[9]))
                self.ui5.lineEdit_8.setText(str(x[10])) 
                self.ui5.lineEdit_9.setText(str(DatAvant)) 
                self.ui5.lineEdit_10.setText(str(x[6]))
                self.ui5.lineEdit_11.setText(str(x[7])) 
                self.ui5.lineEdit_12.setText(str(x[8]))
                self.ui5.lineEdit_13.setText(str(DatApres))
                self.ui5.lineEdit_14.setText(str(Duree))
                self.connect(self.ui5.pushButton, SIGNAL("clicked()"),self.imprimerWEP)
         
    def custom_show(self,bssid,NbrDesauth,suspect,DatFinDes,DatDebDes,NbrNullStat,DureeAttaqueDos,TypeAttaqueDos,NbrNull,NbrNullAvanAttak,NbrNULLduranAttak,NbrNullApresAttak,DebEnvoiNULL,FinEnvoiNULL,DureeNull,ssidAP):
       
            self.resultatAnalyse=QtGui.QDialog()
            self.ui6=Ui_Dialog2()
            self.ui6.setupUi(self.resultatAnalyse)
            self.resultatAnalyse.show() 
            self.ui6.lineEdit.setText(str(ssidAP))
            self.ui6.lineEdit_2.setText(str(bssid))
            self.ui6.lineEdit_3.setText(str(suspect))
            self.ui6.lineEdit_4.setText(str(DatDebDes)) 
            self.ui6.lineEdit_5.setText(str(DatFinDes))
            self.ui6.lineEdit_6.setText(str(DebEnvoiNULL))
            self.ui6.lineEdit_7.setText(str(DureeNull))
            self.ui6.lineEdit_8.setText(str(FinEnvoiNULL)) 
            self.ui6.lineEdit_9.setText(str(NbrNull))
            self.ui6.lineEdit_10.setText(str(NbrNullAvanAttak))
            self.ui6.lineEdit_11.setText(str(NbrNullStat)) 
            self.ui6.lineEdit_12.setText(str(TypeAttaqueDos))
            self.ui6.lineEdit_13.setText(str(DureeAttaqueDos))
            self.ui6.lineEdit_14.setText(str(NbrDesauth))
            self.ui6.lineEdit_15.setText(str(NbrNULLduranAttak))
            self.ui6.lineEdit_16.setText(str(NbrNullApresAttak))
            self.connect(self.ui6.pushButton_2, SIGNAL("clicked()"),self.imprimerDOS)

            

    def allerte(self):
        
        bssid=self.ui4.lineEdit.text()
        f=self.ui4.lineEdit_2.text()
        typeAttaque=self.ui4.comboBox.currentText()
        em=Examen()
        em.BssidSsid(f)
   
        em.ssid,em.bssid,em.canal=em.search()
        exp=r'([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})'
        if re.search(exp, bssid) is None:
            QMessageBox.warning(self,"Alert",self.trUtf8("Enter a correct BSSID \n"))
            
        elif f=="":
            QMessageBox.warning(self,"Alert",self.trUtf8("Upload a trace file \n"))
        
        elif  bssid not in em.bssid:
            QMessageBox.warning(self,"Alert",self.trUtf8("This BSSID not in trace file \n"))
        elif  typeAttaque=="--------------------":
            QMessageBox.warning(self,"Alert",self.trUtf8("You have to choose the attack before starting the analysis  \n"))
        elif typeAttaque=="DoS attack":
                 self.threadD=GenericThread(self.waiting)
                 self.disconnect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
                 self.connect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
                 self.disconnect( self, QtCore.SIGNAL("viewWaitingAnalyse()"), self.viewWaitingAnalyse )
                 self.connect( self, QtCore.SIGNAL("viewWaitingAnalyse()"), self.viewWaitingAnalyse )
                 self.threadD.start()
                
                 self.thread=GenericThread(self.methodeDOS,bssid,f)
                 self.disconnect( self, QtCore.SIGNAL("custom_show(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show ) # diconnecter le signal si il exist deja
                 self.connect( self, QtCore.SIGNAL("custom_show(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show ) 
                 self.disconnect(  self, QtCore.SIGNAL("warning()"), self.warning )
                 self.connect( self, QtCore.SIGNAL("warning()"), self.warning )   # connecter le signal
                 self.thread.start()    

        elif typeAttaque=="WEP attack":
                 self.threadW=GenericThread(self.waiting)
                 self.disconnect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
                 self.connect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
                 self.disconnect( self, QtCore.SIGNAL("viewWaitingAnalyse()"), self.viewWaitingAnalyse )
                 self.connect( self, QtCore.SIGNAL("viewWaitingAnalyse()"), self.viewWaitingAnalyse )
                 self.threadW.start()
                 
                
                 self.thread=GenericThread(self.methodeWEP,bssid,f)
                 self.disconnect( self, QtCore.SIGNAL("custom_show1(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show1 ) # diconnecter le signal si il exist deja
                 self.connect( self, QtCore.SIGNAL("custom_show1(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show1 ) 
                 self.disconnect( self, QtCore.SIGNAL("warning()"), self.warning )  
                 self.connect( self, QtCore.SIGNAL("warning()"), self.warning )   # connecter le signal
                 self.thread.start()    

             
        elif typeAttaque=="EVIL TWIN attack":
                 self.threadE=GenericThread(self.waiting)
                 self.disconnect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
                 self.connect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
                 self.disconnect( self, QtCore.SIGNAL("viewWaitingAnalyse()"), self.viewWaitingAnalyse )
                 self.connect( self, QtCore.SIGNAL("viewWaitingAnalyse()"), self.viewWaitingAnalyse )
                 self.threadE.start()
                
                 self.thread=GenericThread(self.methodeEVIL,bssid,f)
                 self.disconnect( self, QtCore.SIGNAL("custom_show2(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show2 ) # diconnecter le signal si il exist deja
                 self.connect( self, QtCore.SIGNAL("custom_show2(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show2 ) 
                 self.disconnect( self, QtCore.SIGNAL("warning()"), self.warning )  
                 self.connect( self, QtCore.SIGNAL("warning()"), self.warning )   # connecter le signal
                 self.thread.start()
           
        elif typeAttaque=="All attacks":
                 self.thread=GenericThread(self.waiting)
                 self.disconnect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
                 self.connect( self, QtCore.SIGNAL("stopaction()"), self.stopaction )
                 self.disconnect( self, QtCore.SIGNAL("viewWaitingAnalyse()"), self.viewWaitingAnalyse )
                 self.connect( self, QtCore.SIGNAL("viewWaitingAnalyse()"), self.viewWaitingAnalyse )
                 self.thread.start()
                
                 self.thread3=GenericThread(self.methodeW,bssid,f)
                 self.disconnect( self, QtCore.SIGNAL("custom_show1(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show1 ) # diconnecter le signal si il exist deja
                 self.connect( self, QtCore.SIGNAL("custom_show1(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show1 ) 
                 self.disconnect( self, QtCore.SIGNAL("warningWEP()"), self.warningWEP)  
                 self.connect( self, QtCore.SIGNAL("warningWEP()"), self.warningWEP) # connecter le signal
                 self.thread3.start()   
                 
                 self.thread1=GenericThread(self.methodeE,bssid,f)
                 self.disconnect( self, QtCore.SIGNAL("custom_show(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show ) # diconnecter le signal si il exist deja
                 self.connect( self, QtCore.SIGNAL("custom_show(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show ) 
                 self.disconnect( self, QtCore.SIGNAL("warningEVIL()"), self.warningEVIL)  
                 self.connect( self, QtCore.SIGNAL("warningEVIL()"), self.warningEVIL)    # connecter le signal
                 self.thread1.start()
                
           
               
                 self.thread2=GenericThread(self.methodeD,bssid,f)
                 self.disconnect( self, QtCore.SIGNAL("custom_show2(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show2 ) # diconnecter le signal si il exist deja
                 self.connect( self, QtCore.SIGNAL("custom_show2(PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject,PyQt_PyObject)"), self.custom_show2 ) 
                 self.disconnect( self, QtCore.SIGNAL("warningDOS()"), self.warningDOS)  
                 self.connect( self, QtCore.SIGNAL("warningDOS()"), self.warningDOS)  # connecter le signal
                 self.thread2.start()
                
  
       
                
           
    def waitingExamen(self):
        # création du QProgressDialog
        self.prog = QtGui.QProgressDialog(self.trUtf8("Examination of trace file is running... \n"), "Cancel", 0, 0, self)
        self.prog.setWindowTitle(u"Examine of trace file")
        # branchement du bouton "annuler" à la méthode 'stopaction'
        self.prog.canceled.connect(self.stopaction)
        self.action()
         
    def waiting(self):
        self.emit(QtCore.SIGNAL("viewWaitingAnalyse()"))
        
    def viewWaitingAnalyse(self):
        # création du QProgressDialog
        self.prog = QtGui.QProgressDialog(self.trUtf8("Running... \n Please wait, This might take a few minutes"), "Cancel", 0, 0, self)
        self.prog.setWindowTitle(u"Analysis of trace file")
        # branchement du bouton "annuler" à la méthode 'stopaction'
        self.prog.canceled.connect(self.stopaction)
        self.action()
    def action(self):
        self.prog.show()
 
    def stopaction(self):
        self.prog.reset()
        
class GenericThread(QtCore.QThread):
    def __init__(self, function, *args, **kwargs):
        QtCore.QThread.__init__(self)
        self.function = function
        self.args = args
        self.kwargs = kwargs

    def __del__(self):
        self.wait()
 
    def run(self):
        
        self.function(*self.args,**self.kwargs)
    
        return            
        
        
def main(args):

    a=QApplication(args)
    
    f=QMainWindow()
    c=myAppBD(f)
    f.setWindowFlags(Qt.CustomizeWindowHint|Qt.WindowMinimizeButtonHint|Qt.WindowCloseButtonHint)
    f.show()
    r=a.exec_()
    return r




if __name__ == '__main__':
    main(sys.argv)

