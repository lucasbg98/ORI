from itertools import count
import os
import pdb

path =r"/home/lucas/Documentos/ORI/Texts/"
os.chdir(path)


#funcao que le o documento recebido
def readDoc (file):
    with open(file) as outputfile:
        text = outputfile.read()
        return text

#funcao para tokenizar o documento
def tokenize(file):
    return file.split()

#funcao que le diversos documentos de um determinado diretorio e ja as tokeniza
def readCollection():

    i = 0
    docs = []
    
    for file in sorted(os.listdir()):
        if file.endswith('.txt'):
            file_path =f"{path}{file}"
            output = readDoc(file_path)
            output = tokenize(output)
        docs.append(output) 
        i+=1
    return docs

#funcao para procurar um termo especifico dentro do documento
def searchTerm(file, term):

    str_match = [s for s in file if term in s];
    count = len(str_match)
    
    print("O termo" ,term , "aparece" , count ,"vez(es)")
    

def main():

    #newFile recebe uma lista dos documentos do diretorio ja tokenizados
    newFile = readCollection()

    print("Digite o numero indicado para escolher o documento desejado:\n1- Arara Loura\n2- Lara Arara\n3- Rato Rapido\n4- Rato Roma\n5-Tigres Trigo")

    x = input()
    x = int(x)

    if x > 5:
        print("Valor invalido");
        return 0;
    
    #atribuo a file o valor do documento selecionado pelo usuario
    file = newFile[x-1]
    print(file)

    print("Digite o termo que deseja procurar dentro desse documento")
    term = input()
    
    searchTerm(file, term)


if __name__ == "__main__":
    main()