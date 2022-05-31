from itertools import count
import os
import pdb
from string import punctuation
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

#funcao que realiza a criação da matriz termo-documento    
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
        
        
    print(term_document)
                     

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

#funcao para procurar um termo especifico dentro da colecao de documentos
def searchTerm(file, term):
    
    i = 1
    output = []
    
    #for para separar os documentos onde o termo foi encontrado e atribuilos a uma nova lista
    for word in file:
        count = 0

        str_match = [s for s in word if term in s];
        count = len(str_match)
        
        if(count > 0):
            output.append(word)
            
    # separa os documentos da lista e informa quantas vezes o termo pesquisado aparece em cada um dos documentos       
    print("Documentos onde o termo", term, "foi encontrado: \n")
    for word in output:
        str_match = [s for s in word if term in s];
        count = len(str_match)
        print("Documento", i,":" ,word,"\n")
        print("O termo", term, "foi apareceu ", count, "vez(es)\n\n")
        i+=1
            
    
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
    
    makeMatrix(newFile) 


if __name__ == "__main__":
    main()
