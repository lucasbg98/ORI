from genericpath import exists
from itertools import count
import os
import pdb
from string import punctuation

from numpy import where


current_directory = os.getcwd()
path =r"/home/lucas/Documents/Projects/ORI/Texts/"
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
        
            
    return Dict
                       

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

#funcao que retorna o dicionario na chave onde o termo foi passado
def returnDict(file, term):
    
    Dict = makeDictionary(file)
    return Dict[term]

#funcao que realiza a busca booleana
def booleanSearch(file, term):
    
    i = 0
    output = []
    
    # for que busca a palavra 'and' ou 'or' e realiza a comparação logica entre a palavra na frente e a palavra atrás da posição da condição logica em questao
    for word in term:
        if word == "ands":
            output.append(set(returnDict(file, term[i-1])) & set(returnDict(file,term[i+1])))
        elif word == "or":
            output.append(set(returnDict(file, term[i-1])) | set(returnDict(file,term[i+1])))
        i+=1                  
    print(output)    
            
            
    
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
    
    print("Insira a busca:\n Observacao: utilize operandos and ou or nas buscas Ex:'arara and loura' ")
    term = []
    term = input()
    
    term = tokenize(term)
    term = filter(term)
    
    booleanSearch(newFile, term)
    
    
    
    
    
    


if __name__ == "__main__":
    main()
