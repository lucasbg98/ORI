from itertools import count
import os
import pdb
from string import punctuation

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
    return (" ").join(tokens_filtered)

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
    filter = remove_stopwords(document)
    filter = remove_punctuation(document)
    
    output = []
    
    for word in filter:
        output.append(word.lower())
        
    return output
    


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

def main():
    
    #newFile recebe uma lista dos documentos do diretorio ja totalmente tokenizados (sem stopword, pontuacao e tudo em minusculo)
    newFile = readCollection()

    print("Digite o termo que deseja procurar dentro da colecao de documentos")
    term = input()
    
    searchTerm(newFile, term) 


if __name__ == "__main__":
    main()
