#!/usr/bin/env python
# -*- coding: utf-8 -*- 

import MySQLdb as sql
import nltk, re, sys 
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
def manhattan(arrA, desc, bow):
  suma = 0.0
  tok = token(desc)
  letterTok, letterTokFrec = [], []
    
  for i in tok:
    letterTok.append(i[0])
    letterTokFrec.append(i[1])

  arrB = [0]*len(bow)
  for i in letterTok:
    if i in bow:
      pos = bow.index( i )
      arrB[pos] += 1

  k = 0
  for j in arrA:
    suma += abs(j - arrB[k])
    k += 1
  return suma
"""
#
# Calculo de distancia con
# Algoritmo canberra
# 
"""
def canberra(arrA, arrB, bow):
  suma = 0.0
  numerador = 0.0
  denominador = 0.0
  tok = token(arrB)
  letterTok, letterTokFrec = [], []

  for i in tok:
    letterTok.append(i[0])
    letterTokFrec.append(i[1])

  num = [0]*len(bow)
  for i in letterTok:
    if i in bow:
      pos = bow.index( i )
      num[pos] += 1

  k = 0
  for j in arrA:
    try:
      numerador = abs(j - num[k])
      denominador = j + num[k]
      suma += numerador/denominador
    except:
      suma += 0
      k += 1
  return suma
"""
#
# Calculo de distancia con
# Algoritmo Squared Cord
# 
"""
def cord(arrA, arrB, bow):
  suma = 0.0
  number = 0.0
  tok = token(arrB)
  letterTok, letterTokFrec = [], []
  
  for i in tok:
    letterTok.append(i[0])
    letterTokFrec.append(i[1])

  num = [0]*len(bow)
  for i in letterTok:
    if i in bow:
      pos = bow.index( i )
      num[pos] += 1

  k = 0
  for j in arrA:
    number = sqrt(j) - sqrt(num[k])
    suma += pow(number, 2)
    k += 1
  return suma
"""
#
# Calculo de distancia con
# Algoritmo Squared Chi-squered
# 
"""
def chiSquared(arrA, arrB, bow):
  suma = 0.0
  numerador = 0.0
  denominador = 0.0
  number = 0.0
  tok = token(arrB)
  letterTok, letterTokFrec = [], []

  for i in tok:
    letterTok.append(i[0])
    letterTokFrec.append(i[1])

  num = [0]*len(bow)
  for i in letterTok:
    if i in bow:
      pos = bow.index( i )
      num[pos] += 1

  k = 0
  for j in arrA:
    try:
      number = j - num[k]
      numerador = pow(number, 2)
      denominador = j + num[k]
      suma += numerador/denominador
    except:
      suma +=0
  return suma

def token(files):
  stop_words = [
    "se", "su", "lo", "en" ,"una", "por", "es", "muy", "las", "al", "del", "la", "los", "el", "y", "a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the", ";", ")", "(", ".", "?", "&", ":", ","
  ]
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
  print str(item) + " " + user
  db = sql.connect(host="localhost", # host
                     user="root", # username
                     passwd="root", # password
                     db="virmuseum", # name of the db
                     ) 

  cur = db.cursor() 
  # we retraive the description of the items set
  cur.execute("SELECT description FROM items")

  globalWords = []
  descript = cur.fetchall()
  bag_of_word = []

  # we meke a bag of word
  text = ""
  for row in descript:
    text += row[0] + " "
  tok = token(text.rstrip())
  for i in tok:
    word = i[0].replace(".", "")
    if word in bag_of_word:
      pass
    else:
      bag_of_word.append(word)

  matrix = []
  # here we define the matrix of occurency
  for row in descript:
    matrix_row = [0]*len(bag_of_word)
    tok = token(row[0].rstrip())
    for j in tok:
      word = j[0].replace(".", "")
      pos = bag_of_word.index( word )
      if word in bag_of_word:
        matrix_row[pos] += j[1]
      else:
        matrix_row[pos] = 0
    matrix.append(matrix_row)

  print "########################################################################################"
  print "########################################################################################"
  print
  print "Item seleccionado: " + str(item+1)
  row = descript[item]
  cur.execute("SELECT name FROM hierarchies WHERE id = (SELECT id_hierarchy FROM items WHERE id = %s)", item+1)
  hierarchy = cur.fetchall()[0][0]
  print "Jerarquia: " + hierarchy
  print "Usuario: " + user
  print
  print "########################################################################################"
  print "########################################################################################"
  cur.execute("SELECT id FROM items WHERE id_hierarchy = (SELECT id FROM hierarchies WHERE name = %s) AND id != %s", (hierarchy, item+1))
  items_by_hierarchy = cur.fetchall()
  if len(items_by_hierarchy) == 0:
    return json.dumps({"elements":0, "error": "true", "msg": "no existen resultados para esta jerarquia"}) 
    

  # here we choose the method to calculate the distance between items
  final_result = {}
  i = 0
  med = 0.0
  med = float("{0:.2f}".format(random.random()))
  print med
  for item_bag_temp in matrix:
    if med >= 0.0 and med < 0.25:
      print "Metrica: Manhattan"
      final_result[str(i+1)] = manhattan(item_bag_temp, row[0], bag_of_word)
    elif med >= 0.25 and med < 0.5:
      print "Metrica: Canberra"
      final_result[str(i+1)] = canberra(item_bag_temp, row[0], bag_of_word)
    elif med >= 0.5 and med < 0.75:
      print "Metrica: Squared cord"
      final_result[str(i+1)] = cord(item_bag_temp, row[0], bag_of_word)
    elif med >= 0.75 and med <= 1.0:
      print "Metrica: Squared Chi-squered"
      final_result[str(i+1)] = chiSquared(item_bag_temp, row[0], bag_of_word)
    else:
      print "error en la eleccion, metodo no existe"
      print "opciones:"
      print "\tman"
      print "\tcan"
      print "\tcord"
      print "\tchi"
      break
      sys.exit()
    i += 1

  # we organize the result in diferenct way
  # ascendent
  rec_asc = sorted(final_result.items(), key=lambda x: (x[1], x[0]))
  # decendent
  rec_desc = sorted(final_result.items(), key=lambda x: (-x[1], x[0]))

  if user == "adulto":
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

    print "Con filtro jerarquico:"
    i = len(final_recommend_id_herarchy)
    j = 0
    while j < 10:
      if j == i:
        break
      print "Item " + str(final_recommend_id_herarchy[j])
      j += 1
    print

    print "Recomendacion final para adulto:"
    final_response = {}
    final_response['order'] = 'desc'
    count = 0
    for i in final_recommend_id:
      cur.execute("SELECT visible FROM items WHERE id = %s", (i))
      visible = cur.fetchall()

      if visible[0][0] == 1:
        cur.execute("SELECT url, data_type FROM data_streams WHERE id_item = %s AND id_role = (SELECT id FROM roles WHERE id = (SELECT id_role FROM users WHERE name = %s));", (i, user))
        data_stream = cur.fetchall()
        print i + " -> " + str(data_stream)
        if len(data_stream) > 0:
          count += 1
          data_stream_response = {}
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
  if user == "niño":
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
      cur.execute("SELECT visible, visits FROM items WHERE id = %s", (i))
      visible = cur.fetchall()
      if visible[0][0] == 1:
        cur.execute("SELECT url, data_type FROM data_streams WHERE id_item = %s AND id_role = (SELECT id FROM roles WHERE id = (SELECT id_role FROM users WHERE name = %s));", (i, user))
        data_stream = cur.fetchall()
        print i + " -> " + str(data_stream)
        if len(data_stream) > 0:
          count += 1
          data_stream_response = {}
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

