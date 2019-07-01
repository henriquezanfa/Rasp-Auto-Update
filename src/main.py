#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Script baseado em:
# https://medium.com/@johngrant/updating-distributed-raspberrypis-with-automatic-code-updates-3336aa0bcca1

import sh
from sh import git
import time
import os, sys

tempoDeChecagem = 60
diretorioGit = "/SEU/DIRETORIO/"

def checandpAtualizacoes(diretorio):
    print("Comparando versão local com a remota em: " + diretorio)

    # Pegando a versão mais recente
    git("--git-dir=" + diretorio + ".git/", "--work-tree=" + diretorio, "fetch", "origin", "master", _out_bufsize=0, _tty_in=True)               
    
    time.sleep(1)   
    print("Checando o status do diretório...")
    statusCheck = git("--git-dir=" + diretorio + ".git/", "--work-tree=" + diretorio, "status")

    # Resposta do git ao realizar um fetch
    if "Your branch is up-to-date" in statusCheck:
        print("Diretório atualizado.")
        return False
    else:
        print("Atualizações disponíveis")
        return True

def contagemRegressiva(t):
    while t:
        mins, secs = divmod(t, 60)
        tempoFormatado = '{:02d}:{:02d}'.format(mins, secs)
        print(tempoFormatado)
        sys.stdout.write("\033[F")
        time.sleep(1)
        t -= 1

    print("00:00")

if __name__ == "__main__":
    while True:
        print("\n************************ Checando se há atualizações ************************")                                                     
    
        if checandpAtualizacoes(diretorioGit):
            print("Atualizando código...")
            resetCheck = git("--git-dir=" + diretorioGit + ".git/", "--work-tree=" + diretorioGit, "reset", "--hard", "origin/master")
            print(str(resetCheck)) 
                                                                                                                                                                
        print("Checagem completa! \nAguardando " + str(tempoDeChecagem) + " segundos para a próxima atualização")
        contagemRegressiva(tempoDeChecagem)