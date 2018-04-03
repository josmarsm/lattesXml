# encoding: utf-8
import sys, os
import json
import zipfile
import time
import datetime

import xml.etree.ElementTree as ET

import xlwt
import re
import xml.dom.minidom
import xlsxwriter

reload(sys)
sys.setdefaultencoding('utf8')

MYDIR = os.path.dirname(__file__)


def getPesquisador():
  with open('pesquisadores.json') as f:
    data = json.load(f)
    pesquisador=[]
    for x in data['Professores']:
      id_pesquisador = x['id']
      pesquisador.append(id_pesquisador)
  return pesquisador


def getCurriculo():
  pesquisador = getPesquisador()
  for id_pesquisador in pesquisador:
    print id_pesquisador
    documento = (r'Lattes_Docentes_PGCC/' + id_pesquisador + '.xml')
    #print (documento)
    tree = ET.parse(documento)
    #print (tree)
    root = tree.getroot()
    #print (root)
    print (root.tag, root.attrib)
    print ('---')

getCurriculo()
