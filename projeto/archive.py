# ----- AUTORES ----- # 
# Brenda Alexsandra Januario     - 194832
# Felipe Carreiro Marchi         - 196695
# Pedro Henrique Bernini Silva   - 204575

# ----- BIBLIOTECAS ----- # 
import sys

# ----- ARGS LINHA DE COMANDO ----- # 
qtdArgumentos = len(sys.argv)
arquivador = sys.argv[2]
comando = sys.argv[1]
arquivos = []

for i in range(3, qtdArgumentos):
    arquivos.append(sys.argv[i])
    
def printArquivos() :
    string = ""
    for el in arquivos :
        string += el + ", "
    return string


# ----- CRIAR ARQUIVADOR COM ARQUIVOS ----- # 
def criar() :    
    cont = 0
    try :
        open(arquivador, 'r+b')
        print("A CRIACAO FALHOU!")
        print("Ja existe um arquivador de mesmo nome neste local.")
        print("")
        
    except FileNotFoundError :
        archive = open(arquivador, 'w+b')

        for arq in arquivos :
            qtdBytes = 0  
            
            try :      
                conteudo = (open(arq, 'r+b').read())
                
                for byte in conteudo :
                    qtdBytes += 1
        
                # INSERIR
                nome = arq
                tamanho = qtdBytes            
                novoArquivo = str.encode(nome) + str.encode("|") + str.encode(str(tamanho)) + str.encode("|") + conteudo         
                archive.write(novoArquivo)
                cont += 1
                
            except FileNotFoundError :
                print("UMA INSERCAO FALHOU!")
                print("Nao existe o arquivo '", arq ,"' neste local.")
                print("")
            
            

        archive.close()
        
        print("ARQUIVADOR CRIADO COM SUCESSO!")
        print("O arquivador '", arquivador ,"' foi criado com", cont ,"arquivo(s).")
        print("")
        

# ----- INSERIR UM ARQUIVO ----- # 
def inserir() :
    try :
        open(arquivador, 'r+b')        
        archive = open(arquivador, 'a+b')
        
        for arq in arquivos :
            qtdBytes = 0 
            
            if arq in lista() :
                print("A INSERCAO FALHOU!")
                print("Ja existe o arquivo '", arq ,"' neste arquivador.")  
                print("")              
                return
                
            else :
                try : 
                    conteudo = (open(arq, 'r+b').read())
                    
                    for byte in conteudo :
                        qtdBytes += 1
                    
                    # INSERIR
                    nome = arq
                    tamanho = qtdBytes            
                    novoArquivo = str.encode(nome) + str.encode("|") + str.encode(str(tamanho)) + str.encode("|") + conteudo         
                    archive.write(novoArquivo)
                
                except FileNotFoundError :
                    print("A INSERCAO FALHOU!")
                    print("Nao existe o arquivo '", arq ,"' neste local.")
                    print("")
                
        archive.close()
        
        print("INSERIDO COM SUCESSO!")
        print("O arquivo '", arq ,"' foi inserido no arquivador.")
        print("")
        
    except FileNotFoundError :
        print("A INSERCAO FALHOU!")
        print("Nao existe o arquivador '", arquivador ,"' neste local.")
        print("")


# ----- LISTAR ARQUIVOS DO ARQUIVADOR ----- # 
def lista() :
    try :    
        listaNomes = []
        archive = open(arquivador, 'r+b')
        caractere = archive.read(1).decode("utf-8")
        
        while(caractere != '') :
            
            # PEGA NOME
            nome = ""
            while(caractere != '|') :
                nome += caractere
                caractere = archive.read(1).decode("utf-8")                
            listaNomes.append(nome)
                    
            # PEGA QTDBYTES   
            qtdBytes = "" 
            caractere = archive.read(1).decode("utf-8")
            while(caractere != '|') :
                qtdBytes += caractere
                caractere = archive.read(1).decode("utf-8")
                
            # PULA CONTEUDO         
            archive.read(int(qtdBytes))
            caractere = archive.read(1).decode("utf-8")
                         
        archive.close()
        
        # RETORNAR LISTA DE NOMES
        return listaNomes
        
            
    except FileNotFoundError :
        print("A LISTAGEM FALHOU!")
        print("Nao existe o arquivador '", arquivador ,"' neste local.")
        print("")
        

# ----- EXTRAIR UM ARQUIVO ----- # 
def extrair() :
    try :    
        nome = ""
        archive = open(arquivador, 'r+b')
        caractere = archive.read(1).decode("utf-8")
        
        while(caractere != '' and nome != arquivos[0]) :
            
            # PEGA NOME
            nome = ""
            while(caractere != '|') :
                nome += caractere
                caractere = archive.read(1).decode("utf-8")
                        
            # PEGA QTDBYTES
            qtdBytes = ""
            caractere = archive.read(1).decode("utf-8")
            while(caractere != '|') :
                qtdBytes += caractere
                caractere = archive.read(1).decode("utf-8")
            
            # PEGA CONTEUDO            
            conteudo = archive.read(int(qtdBytes))
            caractere = archive.read(1).decode("utf-8")
            
        archive.close()
        
        # EXTRAIR
        if (nome == arquivos[0]) :
            arq = open(nome,'w+b')
            arq.write(conteudo)
            arq.close()
            
            print("EXTRAIDO COM SUCESSO!")
            print("O arquivo '", arquivos[0] ,"' foi extraido do arquivador.")
            print("")
            
        else :
            print("A EXTRACAO FALHOU!")
            print("Nao existe o arquivo '", arquivos[0] ,"' neste arquivador.")
            print("")        
        
                        
    except FileNotFoundError :
        print("A EXTRACAO FALHOU!")
        print("Nao existe o arquivador '", arquivador ,"' neste local.")
        print("")
        
    
# ----- REMOVER UM ARQUIVO ----- # 
def remover() :
    try :
        nome = ""
        archive = open(arquivador, 'r+b')
        caractere = archive.read(1).decode("utf-8")
        

        while(caractere != '' and nome != arquivos[0]) :
            
            # PEGA POSICAO INICIAL DO ARQUIVO
            posicaoInicial = archive.tell() - 1
            
            # PEGA NOME
            nome = ""
            while(caractere != '|') :
                nome += caractere
                caractere = archive.read(1).decode("utf-8")
                        
            # PEGA QTDBYTES
            qtdBytes = ""
            caractere = archive.read(1).decode("utf-8")
            while(caractere != '|') :
                qtdBytes += caractere
                caractere = archive.read(1).decode("utf-8")
            
            # PULA CONTEUDO            
            archive.read(int(qtdBytes))
            
            # PEGA POSICAO FINAL DO ARQUIVO
            posicaoFinal = archive.tell()
            
            caractere = archive.read(1).decode("utf-8")
        
        archive.close()
        
        # REMOVER
        if (nome == arquivos[0]) :
            
            # SALVAR CONTEUDO PERSISTENTE DO ARQUIVADOR
            archive = open(arquivador, 'r+b')
            archive.seek(posicaoFinal)
            conteudoPersistente =  archive.read()
            archive.close()
            
            # REMOVER ARQUIVO DO ARQUIVADOR
            archive = open(arquivador, 'a+b')
            archive.truncate(posicaoInicial)
            archive.close()
            
            # RESTAURAR ARQUIVOS PERSISTENTES NO ARQUIVADOR
            archive = open(arquivador, 'a+b')
            archive.seek(posicaoInicial)
            archive.write(conteudoPersistente)
            archive.close()            
            
            print("REMOVIDO COM SUCESSO!")
            print("O arquivo '", arquivos[0] ,"' foi removido do arquivador.")
            print("")
            
        else :
            print("A REMOCAO FALHOU!")
            print("Nao existe o arquivo '", arquivos[0] ,"' neste arquivador.")
            print("")
                    
    except FileNotFoundError :
        print("A REMOCAO FALHOU!")
        print("Nao existe o arquivador '", arquivador ,"' neste local.")
        print("")
        

# --- FUNCAO PRINCIPAL --- #
if(comando == "-c") :
    arquivosRepetidos = False
    for arq in arquivos :
        if (arquivos.count(arq) > 1) :
            arquivosRepetidos = True
            
    if(arquivosRepetidos == False) :
        criar()
    else :
        print("ARQUIVOS COM NOMES REPETIDOS!")
        print("Tente: arquivador -l <archive.arq>")
        print("")
    
elif(comando == "-l") :
    if (qtdArgumentos == 3) :
        print("LISTAGEM CONCLUIDA. ARQUIVOS ENCONTRADOS:")
        for el in lista() :
            print(el)        
        print("")
    else :
        print("NUMERO DE ARGUMENTOS INVALIDOS!")
        print("Tente: arquivador -l <archive.arq>")      
        print("")
    
elif(qtdArgumentos == 4) :
    if(comando == "-i") :
        inserir()
    elif(comando == "-e") :
        extrair()    
    elif(comando == "-r") :
        remover()
else :
    print("NUMERO DE ARGUMENTOS INVALIDOS!")
    print("Tente: arquivador", comando ,"<archive.arq> <arq>")


