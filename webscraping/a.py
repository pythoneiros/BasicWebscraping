#!/usr/bin/env python
# -*- coding: utf-8 -*-

import urllib2
from bs4 import BeautifulSoup
import sys	

def pega_link():
  """
    Extrai os links de uma página
  """
  try:
    html_doc = urllib2.urlopen(sys.argv[1]).read()

    soup = BeautifulSoup(html_doc, 'html.parser')

    links =  soup.find_all('a')

    for link in links:
      print link.get('href')

  except IndexError:
    print "Informe um parâmetro (site alvo)"
  except ValueError:
    print "Informe um parâmetro no formato http://www.site.com"
   
if __name__ == '__main__':
  pega_link()
