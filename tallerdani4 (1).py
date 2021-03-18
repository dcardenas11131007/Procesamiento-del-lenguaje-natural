#!/usr/bin/env python
# coding: utf-8

# In[ ]:





# In[1]:


import re
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from nltk.tokenize import RegexpTokenizer

datos = pd.read_csv('C:/Users/dcard/OneDrive/Documentos/Procesamiento_del_lenguaje_Natural/Archivo_taller.csv')
datos


# In[2]:


def textoRegex(quitartildes):
    a = quitartildes.replace("á", "a")
    e = a.replace("é", "e")
    i = e.replace("í", "i")
    o = i.replace("ó", "o")
    u = o.replace("ú", "u")
    return u

textosintilde = []
for texto in datos['Locución'].values:  # Recorrer todos los datos en locución
    textominuscula = texto.lower()  # Convertir en minuscula
    textosololetras = re.sub(r"[\W\d]", " ", textominuscula) # Dejar sólo letras
    textosintilde.append(textoRegex(textosololetras))   #Agregar los textos en diccionario
    
    
datos['Preprocesamiento'] = textosintilde
#textosintilde
datos


# In[ ]:


print(datos['Preprocesamiento'])


# In[3]:


datos['Preprocesamiento'] = datos.to_string()
tokenizer = RegexpTokenizer(r'\w+')
tokens = tokenizer.tokenize(datos['Preprocesamiento'])
print(datos['Preprocesamiento'])


# In[15]:


import nltk  
nltk.download('punkt')
nltk.download('stopwords') # Esta línea se corre sólo la primera vez

from nltk.corpus import stopwords
stop_words = stopwords.words('spanish')
#stop_words = set(stopwords.words('spanish')
#stop_words = stop_words.update(set(['deb','co','https','rt','dr','lv','me', 'le', 'da', 'mi', 'su', 'ha', 'he', 'ya', 'un', 'una', 'es','del', 'las', 'los', 'en', 'que', 'y', 'la','de',]))
texto = [palabra for palabra in textosintilde if palabra not in stop_words]
texto


# In[ ]:





# In[ ]:


# BONUS Punto 4: 😜

- `[2pt]` ¿A qué pertenecen los dialogos de ese archivo? 

Temporada 16, ep 8 South Park :)

