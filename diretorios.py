"MÓDULO DIRETORIOS"

import os
import shutil
import glob

def filtra_arq(dir, extensao):
	return glob.glob(os.path.join(dir,extensao))

def cria_diretorio(caminho):
	os.makedirs(caminho)
	return
	
def move_arq(caminho, arquivo):
	shutil.move(caminho,arquivo)
