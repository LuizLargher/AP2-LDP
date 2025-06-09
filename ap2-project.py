#MATRIZES
tarefa_pendente = [
]
tarefa_concluido = [
]


#GLOBAL NUM
num = 1


#VISUALIZAR TAREFAS NO GERAL
def ver_tarefas():
   global num
   opcao = int(input('\n1) Tarefas pendentes\n2)Tarefas concluidas\n//Escolha: '))
   if opcao == 1:
       ver_tarefas_pendentes()
   elif opcao == 2:
       ver_tarefas_concluido()
   else:
       print('Erro, opção inválida. Tente novamente!')


#VISUALIZAR TAREFAS PENDENTES
def ver_tarefas_pendentes():
   global num
   for i in tarefa_pendente:
       print(f'\nTarefa número {num}:\n{i}\n')
       num += 1
   num = 1


#VISUALIZAR TAREFAS CONCLUIDAS
def ver_tarefas_concluido():
   global num
   for i in tarefa_concluido:
       print(f'\n Tarefa número {num}:\n{i}\n')
       num += 1
   num = 1


#ADICIONAR
def adicionar_tarefa(tarefa_pendente):
   script = input('\n//Descrição da tarefa: ')
   relevance = int(input('\n//De 1 a 5, sendo 5, o mais relevante.\n//Qual é o nível de relevância da tarefa: '))
   time = int(input('\n//Qual o tempo estimado para essa tarefa: '))
   tarefa = (f'Descrição: {script}.\nRelevância: {relevance}.\nTempo: {time} minutos.')
   tarefa_pendente.append(tarefa)
   print('\nA tarefa foi adicionada com sucesso!\n')


#REMOVER
def remover_tarefa():
   global num
   opcao = int(input('\n1) Tarefas pendentes\n2)Tarefas concluidas\n//Escolha: '))
   if opcao == 1:
       ver_tarefas_pendentes()
       indice = int(input('\n//Qual deseja remover: ')) - 1
       for i in range(len(tarefa_pendente)):
           if 0 <= indice < len(tarefa_pendente):
               tarefa_pendente.pop(indice)
       print('\nA tarefa foi removida com sucesso!\n')
   elif opcao == 2:
       ver_tarefas_concluido()
       indice = int(input('\n//Qual deseja remover: ')) - 1
       for i in range(len(tarefa_concluido)):
           if 0 <= indice < len(tarefa_concluido):
               tarefa_concluido.pop(indice)
       print('\nA tarefa foi removida com sucesso!\n')


#CONCLUIR
def concluir_tarefa():
   global num
   ver_tarefas_pendentes()
   try:
       indice = int(input('\n//Digite o número da tarefa que deseja concluir: ')) - 1
       if 0 <= indice < len(tarefa_pendente):
           item = tarefa_pendente.pop(indice)
           tarefa_concluido.append(item)
           print('\nA tarefa foi concluída com sucesso!\n')
       else:
           print("\nNúmero inválido.")
   except ValueError:
       print('\nErro, opção inválida. Tente novamente!\n')


#EDITAR
def editar_tarefa(tarefa_pendente):
   ver_tarefas_pendentes()
   indice = int(input("\nDigite o número da tarefa que deseja editar: ")) -1
   if indice < 0 or indice >= len(tarefa_pendente):
       print('Erro, opção inválida. Tente novamente!')
   script = input('\n//Nova descrição da tarefa: ')
   relevance = int(input('\n//De 1 a 5, sendo 5 o mais relevante.\n//Novo nível de relevância: '))
   time = int(input('\n//Novo tempo estimado (em minutos): '))
   nova_tarefa = (f'Descrição: {script}.\nRelevância: {relevance}.\nTempo: {time} minutos.')
   tarefa_pendente[indice] = nova_tarefa
   print("\nA tarefa foi atualizada com sucesso!\n")


#MENU
def menu():
   global num
   while True:
       mode = int(input('Gerenciador de Tarefas\n1) Adicionar terefa\n2) Editar tarefa\n3) Excluir tarefa\n4) Concluir tarefa\n5) Visualizar tarefas\n6) Sair do gerenciador\nEscolha: '))
       if mode == 1:
           adicionar_tarefa(tarefa_pendente)
       elif mode == 2:
           editar_tarefa(tarefa_pendente)
       elif mode == 3:
           remover_tarefa()
       elif mode == 4:
           concluir_tarefa()
       elif mode == 5:
           ver_tarefas()
       elif mode == 6:
           exit()
       else:
           print('\nErro, opção inválida. Tente novamente!\n')


menu()
