#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import sqlite3 as sql # MySQLdb
import nltk, re, sys, os, math
from collections import Counter
from numpy import linalg as LA
import numpy as np
from math import sqrt, pow
from bottle import route, run, template, static_file, debug, request, abort, HTTPResponse
import json
import random
"""
#
# Calculo de distancia con
# Algoritmo de manhattan
# 
"""
def manhattan(item, tf_idf):
  result = {}
  for _id in tf_idf:
    k = 0
    suma = 0.
    for j in tf_idf[_id]:
      suma += abs(j - item[k])
      k += 1
    result[_id] = suma
  return result
"""
#
# Calculo de distancia con
# Algoritmo canberra
# 
"""
def canberra(item, tf_idf):
  result = {}
  for _id in tf_idf:
    k = 0
    suma = 0.
    numerador = 0.
    denominador = 0.
    for j in tf_idf[_id]:
      try:
        numerador = abs(j - item[k])
        denominador = j + item[k]
        suma += numerador/denominador
      except:
        suma += 0
      k += 1
    result[_id] = suma
  return result
"""
#
# Calculo de distancia con
# Algoritmo Squared Cord
# 
"""
def cord(item, tf_idf):
  result = {}
  for _id in tf_idf:
    k = 0
    number = 0.
    suma = 0.
    for j in tf_idf[_id]:
      number = sqrt(j) - sqrt(item[k])
      suma += pow(number, 2)
      k += 1
    result[_id] = suma
  return result
"""
#
# Calculo de distancia con
# Algoritmo Squared Chi-squered
# 
"""
def chiSquared(item, tf_idf):
  result = {}
  for _id in tf_idf:
    k = 0
    suma = 0.
    number = 0.
    denominador = 0.
    numerador = 0.
    for j in tf_idf[_id]:
      try:
        number = j - item[k]
        numerador = pow(number, 2)
        denominador = j + item[k]
        suma += numerador/denominador
      except:
        suma +=0
      k += 1
    result[_id] = suma
  return result

def token(files):
  fi = open('stopwords.es.txt', 'r')
  stop_words = fi.readlines()
  data = files.lower()
  tokens = nltk.word_tokenize(data)
  final_tok = []
  for j in tokens:
    try:
      if stop_words.index(j) >= 0:
        pass
    except:
      final_tok.append(j)
    
  nonPunct = re.compile('.*[\W+\w+].*')
  filtered = [w for w in final_tok if nonPunct.match(w)]
  counts = Counter(filtered)
  token = counts.items()

  return token #, len(counts)

############## main block ##############
@route('/recommend/get', method='POST')
def recommend():
  item = int(request.forms.get('item_id')) # item to compare
  # TODO: med its gonna be a random value to determinate the metric for distance calc
  user = request.forms.get('user') # user who trigger the recommendation
  os.system('clear')
  print str(item) + " " + user
  db = sql.connect('db/virmuseum')
  # db = sql.connect(host="localhost", # host
  #                    user="root", # username
  #                    passwd="root", # password
  #                    db="virmuseum", # name of the db
  #                    ) 

  cur = db.cursor() 
  # we retraive the description of the items set
  cur.execute("SELECT id, description FROM items WHERE hierarchy_id = (SELECT hierarchy_id FROM items WHERE id = :item)", {'item': item+1})
  # cur.execute("SELECT id, description FROM items")
  globalWords = []
  descript = cur.fetchall()
  descript_dict = {}
  i = 0
  for j in descript:
    descript_dict[j[0]] = j[1]
  
  bag_of_word = []

  # we meke a bag of word
  text = ""

  j = 0
  for i in descript_dict:
    text += descript_dict[i] + " "
    j += 1;
  tok = token(text.rstrip())
  for i in tok:
    word = i[0].replace(".", "")
    if word in bag_of_word:
      pass
    else:
      bag_of_word.append(word)

  matrix = {}
  
  # here we define the matrix of occurency
  # this matrix is our matrix for term frecuency Fij
  for i in descript_dict:
    matrix_row = [0]*len(bag_of_word)
    tok = token(descript_dict[i].rstrip())
    for j in tok:
      word = j[0].replace(".", "")
      pos = bag_of_word.index( word )
      if word in bag_of_word:
        matrix_row[pos] += j[1]
      else:
        matrix_row[pos] = 0
    matrix[i] = matrix_row
  
  print "########################################################################################"
  print "########################################################################################"
  print
  print "Item seleccionado: " + str(item+1)
  try:
    item_seen = descript_dict[item+1]
  except:
    return json.dumps({'elements' : 0})
  
  cur.execute("SELECT name FROM hierarchies WHERE id = (SELECT hierarchy_id FROM items WHERE id = :item)", {'item' : item+1})
  hierarchy = cur.fetchall()[0][0]
  print "Jerarquia: " + hierarchy
  print "Usuario: " + user
  print
  print "########################################################################################"
  print "########################################################################################"
  cur.execute("SELECT id FROM items WHERE hierarchy_id = (SELECT id FROM hierarchies WHERE name = :name) AND id != :id", {'name' : hierarchy, 'id' : item+1})
  items_by_hierarchy = cur.fetchall()
  if len(items_by_hierarchy) == 0:
    return json.dumps({"elements":0, "error": "true", "msg": "no existen resultados para esta jerarquia"}) 
    

  # here we choose the method to calculate the distance between items

  # here we need calculate relative frecuency
  relative_frecuency_term = {}
  for _id in matrix:
    try:
      divi = (1./max(matrix[_id]))
    except:
      divi = 0.
    row = [i*divi for i in matrix[_id]]
    relative_frecuency_term[_id] = row

  # Here we need calculate IDF values
  IDF = {}
  for _id in matrix:
    row = [0. if i == 0 else 1. for i in matrix[_id]]
    IDF[_id] = row

  # generate the vetor prom for IDF
  vector_IDF = [0]*len(bag_of_word)
  for _id in IDF:
    i = 0
    for j in IDF[_id]:
      vector_IDF[i] += j
      i += 1
  count_item = len(matrix)
  final_vector_IDF = [math.log10(count_item/i) for i in vector_IDF]

  # After calculate those matrix we need calculte TF-IDF before use the metric
  TF_IDF = {}
  for _id in relative_frecuency_term:
    i = 0
    TF_IDF_ROW = []
    for col_rel in relative_frecuency_term[_id]:
      TF_IDF_ROW.append(final_vector_IDF[i]*col_rel)
      i += 1
    TF_IDF[_id] = TF_IDF_ROW

  # now, we know the item that the user see
  tok = token(item_seen)
  letterTok = []
  for i in tok:
    letterTok.append(i[0])

  arr_item_seen = [0.]*len(bag_of_word)
  for i in letterTok:
    if i in bag_of_word:
      pos = bag_of_word.index( i )
      arr_item_seen[pos] += 1.

  max_arr_item_seen = max(arr_item_seen)
  final_arr_item_seen = [0.]*len(bag_of_word)
  i = 0
  for j in arr_item_seen:
    final_arr_item_seen.append((j/max_arr_item_seen)*final_vector_IDF[i])
    i += 1
  # at this point we use de metric for distance
  med = 0.0
  med = float("{0:.2f}".format(random.random()))
  del TF_IDF[item+1]
  if med >= 0.0 and med < 0.25:
    print "Metrica: Manhattan"
    final_result = manhattan(final_arr_item_seen, TF_IDF)
  elif med >= 0.25 and med < 0.5:
    print "Metrica: Canberra"
    final_result = canberra(final_arr_item_seen, TF_IDF)
  elif med >= 0.5 and med < 0.75:
    print "Metrica: Squared cord"
    final_result = cord(final_arr_item_seen, TF_IDF)
  elif med >= 0.75 and med <= 1.0:
    print "Metrica: Squared Chi-squered"
    final_result = chiSquared(final_arr_item_seen, TF_IDF)
  
  # we organize the result in diferenct way
  # ascendent
  rec_asc = sorted(final_result.items(), key=lambda x: (x[1], x[0]))
  # decendent
  rec_desc = sorted(final_result.items(), key=lambda x: (-x[1], x[0]))

  if user == "adult":
    user = "adulto"
    print "Resultados mas diversos:"
    final_recommend_id = []
    for i in rec_desc:
      if str(item+1) != i[0]:
        final_recommend_id.append(i[0])

    print "Sin filtro jerarquico:"
    i = len(final_recommend_id)
    j = 0
    while j < 10:
      if j == i:
        break
      print "Item " + str(final_recommend_id[j])
      j += 1
    print

    j = 0
    final_recommend_id_herarchy = []
    for i in final_recommend_id:
      if str(items_by_hierarchy[j][0]) == i:
        final_recommend_id_herarchy.append(i)

    print "Recomendacion final para adulto:"
    final_response = {}
    final_response['order'] = 'desc'
    count = 0
    for i in final_recommend_id:
      cur.execute("SELECT visible FROM items WHERE id = :id", {'id':i})
      visible = cur.fetchall()

      if visible[0][0] == 1:
        cur.execute("SELECT url, data_type FROM data_streams WHERE item_id = :item_id AND role_id = (SELECT id FROM roles WHERE id = (SELECT role_id FROM users WHERE name = :name));", {'item_id':i, 'name':user})
        data_stream = cur.fetchall()
        cur.execute("SELECT name, cientific_name FROM items WHERE id = :id", {'id':i}) #  (SELECT name FROM hierarchies WHERE id = (SELECT hierarchy_id FROM items WHERE id = :id)) as hierarchy 
        name = cur.fetchall()
        print str(i) + " -> " + str(data_stream)
        if len(data_stream) > 0:
          count += 1
          data_stream_response = {}
          data_stream_response['name'] = name[0][0]
          data_stream_response['cientific_name'] = name[0][1]
          for ds in data_stream:
            data_stream_response['url'] = ds[0]
            data_stream_response['type'] = ds[1]
          final_response[i] = data_stream_response
    
    if count > 0:
      final_response['elements'] = count
      return json.dumps(final_response)
    else:
      return json.dumps({'elements' : 0})

  ###################### resultados mas parecidos #############################
  if user == "child":
    print "Resultados mas parecidos:"
    final_recommend_id = []
    for i in rec_asc:
      if str(item+1) != i[0]:
        final_recommend_id.append(i[0])

    print "Sin filtro jerarquico:"
    i = len(final_recommend_id)
    j = 0
    while j < 10:
      if j == i:
        break
      print "Item " + str(final_recommend_id[j])
      j += 1
    print

    j = 0
    final_recommend_id_herarchy = []
    for i in final_recommend_id:
      if str(items_by_hierarchy[j][0]) == i:
        final_recommend_id_herarchy.append(i)

    print "Con filtro jerarquico:"
    i = len(final_recommend_id_herarchy)
    j = 0
    while j < 10:
      if j == i:
        break
      print "Item " + str(final_recommend_id_herarchy[j])
      j += 1
    print

    print "Recomendacion final para niño:"
    final_response = {}
    final_response['order'] = 'desc'
    count = 0

    for i in final_recommend_id:
      cur.execute("SELECT visible, visits FROM items WHERE id = :id", {'id':i})
      visible = cur.fetchall()
      if visible[0][0] == 1:
        cur.execute("SELECT url, data_type FROM data_streams WHERE item_id = :item_id AND role_id = (SELECT id FROM roles WHERE id = (SELECT role_id FROM users WHERE name = :name));", {'item_id':i, 'name':user})
        data_stream = cur.fetchall()
        cur.execute("SELECT name, cientific_name, (SELECT name FROM hierarchies WHERE id = (SELECT hierarchy_id FROM items WHERE id = :id)) as hierarchy FROM items WHERE id = :id", {'id':i})
        name = cur.fetchall()
        print i + " -> " + str(data_stream)
        if len(data_stream) > 0:
          count += 1
          data_stream_response = {}
          data_stream_response['name'] = name[0][0]
          data_stream_response['cientific_name'] = name[0][1]
          data_stream_response['hierarchy'] = name[0][2]
          for ds in data_stream:
            data_stream_response['url'] = ds[0]
            data_stream_response['type'] = ds[1]
          final_response[i] = data_stream_response
    
    if count > 0:
      final_response['elements'] = count
      return json.dumps(final_response)
    else:
      return json.dumps({'elements' : 0})

try:
  debug(True)
  run(host='0.0.0.0', port=3001, quiet=True) # reloader=True, 
except (KeyboardInterrupt, SystemExit):
  print "lee el readme en una de esas se solucionan tus problemas"
  sys.exit()

# TODO: insert the results into the db
# we need save this values into the db
#for i in globalWords:
#  print i + " -> " + str(globalWords[i])
# for row in descript:
#   print row[0]
#   try:
#     cur.execute("""INSERT INTO terms (term, count) VALUES (%s,%s)""", (i, globalWords[i]) )
#     db.commit()
#     print "commiting"
#   except:     
#     db.rollback()

# cur.execute("SELECT term FROM terms")

# for row in cur.fetchall():
#   print row[0]

