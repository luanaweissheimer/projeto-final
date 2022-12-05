'''PROGRAMA QUE CRIA PASTAS E MOVE OS ARQUIVOS CONFORME SUA EXTENSÃO
DATA: 03/12/2022
AUTOR: LUANA WEISSHEIMER
VERSÃO : 0.0.1'''


#ENTRADA
#IMPORTAÇÃO DE BIBLIOTECAS
import diretorios


#PROCESSAMENTO E SAIDA
def main():
    dir_projeto = 'C:/users/Luana/Documents/UFRGS/PROGRAMACAO/PROJETO'
    dir_planilha = 'C:/users/Luana/Documents/UFRGS/PROGRAMACAO/PROJETO/PLANILHAS'
    dir_document = 'C:/users/Luana/Documents/UFRGS/PROGRAMACAO/PROJETO/DOCUMENTOS' 

    diretorios.cria_diretorio(dir_planilha)
    diretorios.cria_diretorio(dir_document)

    #LISTA DE ARQUIVOS
    files_xlsx = diretorios.filtra_arq(dir_projeto,"*.xlsx")
    files_docx = diretorios.filtra_arq(dir_projeto,"*.docx")
                  
    for file in files_xlsx:
        diretorios.move_arq(file,dir_planilha)
    
    for file in files_docx:
        diretorios.move_arq(file,dir_document)

main()
