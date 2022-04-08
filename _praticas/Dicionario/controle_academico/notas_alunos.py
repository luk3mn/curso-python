# Criar um programa que verifica a situação de um aluno matriculado
# em uma certa faculdade:
# - nome, código(auto), idade, sexo, curso, media, situação: 'aprov/reprov'
# - Media para aprovação: 8
# - Opções de entrada:
#   _Exibir alunos
#   _Alunos Aprovados
#   _Alunos Reprovados
#   _Adicionar aluno
#   _Excluir Alunos
#   _Colocar um codigo do aluno que é gerado automaticamente como a chave

from _praticas.Dicionario.controle_academico.func_academic import *

# alunos={}
alunos = {
  "121": ["Renan", "121", "25", "Masculino", "Engenharia", str(6.7), "Reprovado"],
  "122": ["Miya", "122", "23", "Feminino", "Psicologia", str(10.0), "Aprovado"],
  "123": ["Lucas", "123", "24", "Masculino", "TADS", str(8.7), "Aprovado"]
}
opcao = perguntar()
while opcao == 'A' or opcao == 'P' or opcao == 'R' or opcao == 'L':
    if opcao == 'A':
        adicionar(alunos)
    if opcao == 'P':
        pesquisar(alunos)
    if opcao == 'R':
        remover(alunos)
    if opcao == 'L':
        listar_cursos(alunos)
    opcao = perguntar()
