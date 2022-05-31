from genericpath import exists
from itertools import count
import os
import pdb
from string import punctuation
import math
import numpy as np


current_directory = os.getcwd()
path = current_directory +"/Texts/"
os.chdir(path)



#funcao que le o documento recebido
def readDoc (file):
    with open(file) as outputfile:
        text = outputfile.read()
        return text

#funcao para tokenizar o documento
def tokenize(file):
    return file.split()

#funcao que remove stopwords do documento
def remove_stopwords(document):
    tokens_filtered= [word for word in document if not word in stopwords ]
    return tokens_filtered

#funcao que remove pontuacao do documento
def remove_punctuation(document):
    output = []
    
    for word in document:
        for letter in word:
            if letter in punctuation:
                word = word.replace(letter,"")   
        output.append(word)
    return output

#funcao filtro que realiza a remocao das stopwords e pontuacoes do documento e ja o retorna todo em letra minuscula
def filter(document):
    
    output = []
    
    for word in document:
        output.append(word.lower())
      
    filter = remove_punctuation(output)
    filter = remove_stopwords(filter)
    
    return filter
    
#funcao que cria o dicionario e organiza os indices invertidos dentro do mesmo
def makeDictionary(document):
    
    terms = []
    Dict = {}
    
    #separo todas as palavras de todos os documentos em um vetor 
    for doc in document:
        for word in doc:
            if word not in terms:
                terms.append(word)
                
    
    #for que realiza a busca das palavras em cada documento e cria um indice dessa palavra que salva os documentos onde ela apareceu
    for word in terms:
        aux = []
        i = 1 
        for doc in document:  
            for letter in doc:
                if word == letter:
                    if i not in aux:
                        aux.append(i)
            i+=1
        Dict[word] = aux        
        
            
    return(Dict)

def makeMatrix(document):
    
    terms = []
    
    #separo todas as palavras individuais do documento em um novo vetor
    for doc in document:
        for word in doc:
            if word not in terms:
                terms.append(word)
    
    #crio uma nova matriz de zeros do tipo object
    term_document = np.zeros( (len(terms)+1 , len(document)+1), dtype=np.object_)
    
    #i controla as linhas da matriz, enquanto y controla as colunas da matriz para preencher a primeira linha com os nomes dos documentos
    i = 1
    y = 0
    for word in terms:
        while y < 6:
            if y == 0:
                term_document[0][y] = 'Documents: '
                y+=1
            term_document[0][y] = "Doc "+ str(y)
            y+=1
        term_document[i][0] = word
        
        i+=1
        
     #for que realiza a filtragem termo-documento de cada palavra dentro de cada documento
    y=1
    for word in document:
        i = 1
        for letter in word:
            x = 1
            while x < len(terms)+1:
                if letter == term_document[x][0]:
                    term_document[x][y] += 1
                x+=1
            i +=1    
        y+=1
        
        
    return term_document

def tfIdf(document):
    Dict = makeDictionary(document)
    matrix = makeMatrix(document)
    
    i = 0
    aux = {}
    
    tfidf_matrix = np.zeros( (len(Dict)+1 , len(document)+1), dtype=np.object_)
    
    #i controla as linhas da matriz, enquanto y controla as colunas da matriz para preencher a primeira linha com os nomes dos documentos
    i = 1
    y = 0
    for word in Dict:
        while y < len(document)+1:
            if y == 0:
                tfidf_matrix[0][y] = 'Documents: '
                y+=1
            tfidf_matrix[0][y] = "Doc "+ str(y)
            y+=1
        tfidf_matrix[i][0] = word
        
        i+=1
    
    
    #for que utiliza da matriz termo-documento para pegar a frequencia do termo em cada documento, enquanto também usa o indice invertido para saber a frequencia de documentos em que o termo aparece
    #... e depois de realizar o calculo tf-idf insere na nova matriz tf-idf
    y = 1
    for doc in document:
        for word in Dict:
            x = 1
            while x < len(Dict)+1:
                if word == tfidf_matrix[x][0]:
                    count = int(matrix[x][y])
                    if count == 0:
                        tf_idf = 0
                    else:
                        tf_idf = (1 + math.log(count, 10)) * math.log((len(document) / len(Dict[word])), 10)
                    tf_idf =np.around(tf_idf, decimals=2)
                    tfidf_matrix[x][y] = tf_idf
                x+=1
        y+=1
        
    print(tfidf_matrix)
                    
            
             
    
            
    

#funcao que le diversos documentos de um determinado diretorio e ja as tokeniza totalmente (removendo stopwords, pontuacoes e deixando em letra minuscula)
def readCollection():
    i = 0
    docs = []
    
    for file in sorted(os.listdir()):
        if file.endswith('.txt'):
            file_path =f"{path}{file}"
            output = readDoc(file_path)
            output = tokenize(output)
            output = filter(output)
        docs.append(output) 
        i+=1
    return docs            
    
#optei por deixar o documento das stopwords e pontuacao global pois assim poderia acessa-lo de qualquer funcao
stopwords = readDoc(current_directory + "/Filters/stopwords_ptbr.txt")
stopwords = tokenize(stopwords)
    
punctuation = readDoc(current_directory +"/Filters/punctuation.txt")
#punctuation = tokenize(punctuation)

def main():
    
    #newFile recebe uma lista dos documentos do diretorio ja totalmente tokenizados (sem stopword, pontuacao e tudo em minusculo)
    newFile = readCollection()
    
    x=1
    for doc in newFile:
        print("Documento", x, ":", doc)
        x+=1
    print("\n")
    
    tfIdf(newFile)


if __name__ == "__main__":
    main()
