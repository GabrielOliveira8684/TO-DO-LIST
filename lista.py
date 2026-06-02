import os
import platform
import json

def salvar_dados(tarefas):
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, indent=4, ensure_ascii=False)

try:
    with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
        tarefas = json.load(arquivo)
except FileNotFoundError:
    tarefas = {
        'Completas': [],
        'Incompletas': []
    }

contador = 0

while True:
    try:
        if platform.system() == 'Windows':
            os.system('cls')
        else:
            os.system('clear')

        print("""
    =================================
            GERENCIADOR DE TAREFAS     
    =================================
    1 - Adicionar Nova Tarefa
    2 - Listar Todas as Tarefas
    3 - Excluir Tarefa
    4 - Marcar Tarefa Como Concluída
    5 - Sair
    =================================
    """)
        
        escolha = int(input('Escolha uma opção (1-5): '))
        
        if escolha not in [1, 2, 3, 4, 5]:
            print('\nNúmero inválido! Pressione Enter para continuar...')
            input()
        elif escolha == 1:
            contador += 1
            nova_tarefa = input('\nDigite a tarefa: ')
            tarefas['Incompletas'].append(nova_tarefa.capitalize())
            salvar_dados(tarefas)
            print('\nTarefa adicionada com sucesso! Pressione Enter...')
            input()
            
        elif escolha == 2:
            print('\nTarefas Incompletas: ')
            for i, tarefa_in in enumerate(tarefas['Incompletas']):
                print(f'{i + 1} - {tarefa_in}')
            print('\nTarefas Completas: ')
            for j, tarefa_com in enumerate(tarefas['Completas']):
                print(f'{j + 1} - {tarefa_com}')
            print('\nPressione Enter para voltar ao menu...')
            input()
            
        elif escolha == 3:
            if not tarefas['Completas'] and not tarefas['Incompletas']:
                print('\nLista de tarefas vazia! Pressione Enter...')
                input()
            else:
                qual = int(input('''
        Remover de qual lista: 

        1 - Incompletas
        2 - Completas

        Digite aqui: '''))
                
                if qual not in [1, 2]:
                    print('\nOpção inválida! Pressione Enter...')
                    input()
                    continue
                elif qual == 1:
                    print('\nTarefas Incompletas: ')
                    for i, tarefa_in in enumerate(tarefas['Incompletas']):
                        print(f'{i + 1} - {tarefa_in}')
                        
                    remover = int(input('\nQual deseja retirar: '))
                    if remover <= 0:
                        print('\nEscolha um número válido! Pressione Enter...')
                        input()
                        continue
                    tarefas['Incompletas'].pop(remover - 1)
                    salvar_dados(tarefas)
                    print('\nTarefa removida com sucesso! Pressione Enter...')
                    input()
                else:
                    print('\nTarefas Completas: ')
                    for j, tarefa_com in enumerate(tarefas['Completas']):
                        print(f'{j + 1} - {tarefa_com}')
                        
                    remover = int(input('\nQual deseja retirar: '))
                    if remover <= 0:
                        print('\nEscolha um número válido! Pressione Enter...')
                        input()
                        continue
                    tarefas['Completas'].pop(remover - 1)
                    salvar_dados(tarefas)
                    print('\nTarefa removida com sucesso! Pressione Enter...')
                    input()
                    
        elif escolha == 4:
            if not tarefas['Incompletas']:
                print('\nLista de tarefas incompletas vazia! Pressione Enter...')
                input()
            else:
                print('\nTarefas Incompletas: ')
                for i, tarefa_in in enumerate(tarefas['Incompletas']):
                    print(f'{i + 1} - {tarefa_in}')
                    
                concluir = int(input('\nQual tarefa foi concluída: '))
                if concluir <= 0:
                    print('\nEscolha um número válido! Pressione Enter...')
                    input()
                    continue
                concluida = tarefas['Incompletas'].pop(concluir - 1)
                tarefas['Completas'].append(concluida)
                salvar_dados(tarefas)
                print('\nTarefa marcada como concluída! Pressione Enter...')
                input()
                
        elif escolha == 5:
            break
            
    except ValueError:
        print('\nEscolha um número válido! Pressione Enter...')
        input()
    except IndexError:
        print('\nEscolha um número que esteja na lista! Pressione Enter...')
        input()

print('\nSaída concluída e dados salvos com sucesso!')