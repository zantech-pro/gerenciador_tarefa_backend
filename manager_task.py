#Imports
import csv
from datetime import datetime
import os
import time
from os.path import exists

global secrete
secrete = 0

def welcome():
    print('\n')
    print(' Bem-vindo ao Gestor de Tarefas '.center(50,'#'))
    print('Pressione 1 para continuar')
    print('Pressione 2 para sair')
    try:
        acao = int(input('\nDigite aqui >>> '))

        if acao == 1:
            os.system('cls')
            menu_principal()
        elif acao == 2:
            print('Programa terminado')
            time.sleep(1.2)
            exit()
        elif acao == 2025:
            global secrete
            secrete = 1717
            menu_principal()
        else:
            print('opção Invalida, vamos reiniciar...')
            time.sleep(2)
            os.system('cls')
            welcome()
    except Exception as error:
        print(f'Você digitou algum valor invalido, vamos iniciar a aplicação - Tela Welcome\n Mensagem de erro: {error}')
        time.sleep(1.2)
        os.system('cls')
        welcome()

def menu_principal():
    print('\n')
    print(' Menu Principal'.center(50,'#'))
    print('-'*50)
    print('1 - Visualizar Tarefas')
    print('2 - Criar Tarefas')
    print('3 - Sobre')
    print('4 - Sair')

    try:
        acao = int(input('\nDigite aqui >>> '))

        if acao == 1:
            os.system('cls')
            acoes_tarefa(options='view')
        elif acao == 2:
            os.system('cls')
            acoes_tarefa(options='create')
        elif acao == 3:
            os.system('cls')
            sobre()
        elif acao == 4:
            print('Programa esta sendo encerrado...')
            time.sleep(1.2)
            exit()
        else:
            print('opção Invalida, vamos reiniciar...')
            time.sleep(2)
            os.system('cls')
            menu_principal()

    except Exception as error:
        print(f'Você digitou algum valor invalido, vamos iniciar a aplicação - menu principal\n Mensagem de erro: {error}')
        time.sleep(1.5)
        os.system('cls')
        menu_principal()


def sobre():
    print('\n')
    print(' Sobre'.center(50,'#'))
    print('-'*50)
    print('''O Gestor de Tarefas é um programa em backend, 
          e com frontend via prompt, com objetivo do usuario registrar suas tarefas e acompanhar seus status.
          Projeto idealizado pela Zantech, visite nosso site: zantech.com.br ou
          Nos contacte por email em dev@zantech.com.br\n''')
    try:
        acao = int(input('\nDigite aqui 1 para voltar ao menu anterior >>> '))

        if acao == 1:
            os.system('cls')
            menu_principal()
        else:
            print('opção Invalida, vamos reiniciar...')
            time.sleep(2)
            os.system('cls')
            menu_principal()
    except Exception as error:
        print(f'Você digitou algum valor invalido, vamos iniciar a aplicação - Tela Sobre\n Mensagem de erro: {error}')
        time.sleep(1.2)
        os.system('cls')
        menu_principal()

#Funções de Crud
def acoes_tarefa(**options):

    if exists('base_csv.csv'):
        if options['options'] == 'view':
            ler_dados = view_data()

            if len(ler_dados) > 1:
                print(' Visualizar Tarefas '.center(50, '#'))
                print('-' * 50)

                #Algorimo de ordenação pela coluna Status
                lista_ordenada = []
                lista_ordernada_ativa = []

                for num, dado in enumerate(ler_dados):
                    if dado[1] == 'Novo':
                        lista_ordenada.append(num)

                for num, dado in enumerate(ler_dados):
                    if dado[1] == 'Em Andamento':
                        lista_ordenada.append(num)

                for num, dado in enumerate(ler_dados):
                    if dado[1] == 'Há Vencer':
                        lista_ordenada.append(num)

                for num, dado in enumerate(ler_dados):
                    if dado[1] == 'Vencido':
                        lista_ordenada.append(num)

                for num, dado in enumerate(ler_dados):
                    if dado[1] != 'Vencido' and dado[1] != 'Há Vencer' and dado[1] != 'Em Andamento' and dado[1] != 'Novo' and dado[0] != 'id':
                        lista_ordenada.append(num)

                for item in lista_ordenada:
                    lista_ordernada_ativa.append(ler_dados[item])
                lista_ordernada_ativa.insert(0, ler_dados[0])
                # Fim do Algorimo de ordenação pela coluna Status

                for num, dado in enumerate(lista_ordernada_ativa):
                    #['id', 'status', 'criado_em', 'prazo', 'criado_por', 'descricao', 'modicado_em', 'prazo_restante']
                    if num == 0:
                        print(str(dado[0]).capitalize().center(4, ' '), '|',
                              str(dado[1]).capitalize().center(12, ' '), '|',
                              str(dado[2]).capitalize().center(19, ' '), '|',
                              str(dado[3]).capitalize().center(7, ' '), '|',
                              str(dado[6]).capitalize().center(19, ' '), '|',
                              str(dado[7]).capitalize().center(28, ' '), '|',
                              str(dado[4]).capitalize().center(35, ' '), '|',
                              str(dado[5]).capitalize().center(60, ' '), '|')
                    else:


                        print(str(dado[0]).capitalize().center(4, ' '), '|',
                              str(dado[1]).capitalize().center(12, ' '), '|',
                              str(dado[2]).capitalize().center(19, ' '), '|',
                              str(dado[3]).capitalize().center(7, ' '), '|',
                              str(dado[6]).capitalize().center(19, ' '), '|',
                              str(dado[7]).capitalize().center(28, ' '), '|',
                              str(dado[4]).capitalize().center(35, ' '), '|',
                              str(dado[5]).capitalize().center(60, ' '), '|')
                try:
                    print('Opções:')
                    print('   1 - Concluir Tarefa')
                    print('   2 - Alterar Tarefa')
                    print('   3 - Deletar Tarefa')
                    print('   4 - Voltar ao menu anterior')

                    acao = int(input('\nDigite aqui a opção >>> '))
                    if acao == 4:
                        os.system('cls')
                        menu_principal()

                    if acao not in [1, 2, 3, 4]:
                        print('Opção invalida, vamos reiniciar o menu...')
                        time.sleep(1.2)
                        os.system('cls')
                        menu_principal()

                    id_linha = int(input('\nDigite o ID da tarefa a receber a ação escolhida anterior \n(Ou Digite "0" Zero para retornar ao menu inicial) >>> '))

                    if id_linha == 0:
                        print('Cancelando operação...')
                        time.sleep(1.2)
                        os.system('cls')
                        menu_principal()
                    elif acao == 1:
                        acoes_tarefa(options='alter', status='concluido', id=id_linha)
                    elif acao == 2:
                        alterar_dados_tarefa(comando='alter', id=id_linha)
                        os.system('cls')
                        menu_principal()
                    elif acao == 3:
                        deletar_dados_tarefa(comando='delete', id=id_linha)
                        os.system('cls')
                        menu_principal()

                    else:
                        print('opção Invalida, vamos reiniciar...')
                        time.sleep(2)
                        os.system('cls')
                        menu_principal()
                except Exception as error:
                    print(f'Você digitou algum valor invalido, vamos iniciar a aplicação - View\n Mensagem de Erro: {error}')
                    time.sleep(1.2)
                    os.system('cls')
                    menu_principal()


            else:
                print(' Visualizar Tarefas '.center(50, '#'))
                print('-'*50)
                print('Não há Tarefas')

            try:
                acao = int(input('Digite aqui 1 para voltar ao menu anterior >>> '))

                if acao == 1:
                    os.system('cls')
                    menu_principal()
                else:
                    print('opção Invalida, vamos reiniciar...')
                    time.sleep(2)
                    os.system('cls')
                    menu_principal()
            except Exception as error:
                print(f'Você digitou algum valor invalido, vamos iniciar a aplicação 002 - view - {error}')
                time.sleep(1.2)
                os.system('cls')
                menu_principal()

        elif options['options'] == 'create':

            print(' Criar tarefa '.center(50, '#'))
            print('-'*50)


            lista_id = []
            with open('base_csv.csv', 'r', encoding='utf-8') as f:
                ler_dados = csv.reader(f, delimiter='|')
                for linha in ler_dados:
                    lista_id.append(linha[0])

            if len(lista_id) > 0:



                print(' Preencha formulario da tarefa: '.center(50, ' '))
                print('-'*50)

                try:
                    prazo = int(input('Prazo: '))
                    criado_por = input('Autor (Seu nome): ')
                    descricao = input('Descrição: ')


                    acao = int(input('Para Adicionar Nova Tarefa digite 1 (ou 2 para voltar) >>> '))


                    if acao == 1:


                        status = 'Novo'
                        criando_em = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
                        modificado_em = '---'
                        prazo_restante = '---'

                        if len(lista_id) > 1:
                            if lista_id[0] == 'id':
                                del lista_id[0]
                            lista_id.sort()
                            id_tarefa = int(lista_id[-1]) + 1
                        else:
                            id_tarefa = 1

                        with open('base_csv.csv', 'a+', newline='', encoding='utf-8') as file:
                            add_tarefa = csv.writer(file, delimiter='|')
                            add_tarefa.writerow([id_tarefa, status, criando_em, prazo, criado_por, descricao, modificado_em, prazo_restante])
                        print('Tarefa criada com sucesso!')
                        time.sleep(1.5)
                        menu_principal()

                    else:
                        print('opção Invalida, vamos reiniciar...')
                        time.sleep(2)
                        os.system('cls')
                        menu_principal()
                except Exception as error:
                    print(f'Você digitou algum valor invalido, vamos iniciar a aplicação 001 - create- {error}')
                    print(error)
                    time.sleep(1.2)
                    os.system('cls')
                    menu_principal()
            else:
                try:
                    with open('base_csv.csv', 'w', newline='', encoding='utf-8') as file:
                        writer = csv.writer(file, delimiter='|')

                        # Criar apenas o cabeçalho
                        writer.writerow(
                            ['id', 'status', 'criado_em', 'prazo', 'criado_por', 'descricao', 'modicado_em',
                             'prazo_restante'])
                    print('Base de Dados Criado com sucesso!!! Reiniciaremos o menu')
                    time.sleep(1.5)
                    os.system('cls')
                    menu_principal()
                except Exception as error:
                    print(f'Deu um erro inesperado, estaremos reinciado o menu; descrição do erro: {error}')
                    time.sleep(2.5)
                    os.system('cls')
                    menu_principal()


        elif options['options'] == 'alter' and options['status'] == 'concluido':
            alter_dados = view_data()
            for num, dados in enumerate(alter_dados):
                if num == 0:
                    continue
                else:
                    if int(dados[0]) == int(options['id']):
                        if alter_dados[num] != 'Concluido':
                            alter_dados[num][1] = 'Concluido'
                            alter_dados[num][6] = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
            try:
                with open('base_csv.csv', 'w', newline='', encoding='utf-8') as file:
                    add_tarefa = csv.writer(file, delimiter='|')
                    for linha in alter_dados:
                        add_tarefa.writerow(linha)
                print('Tarefa alterada com sucesso!')
            except Exception as error:
                print(f'Algo inexperado ocorreu, estamos reinicializando... descrição do erro {error}')
                time.sleep(1.5)
                os.system('cls')
                menu_principal()



    else:
        try:
            with open('base_csv.csv', 'w', newline='', encoding='utf-8') as file:
                writer = csv.writer(file, delimiter='|')

                #Criar apenas o cabeçalho
                writer.writerow(['id', 'status', 'criado_em', 'prazo', 'criado_por', 'descricao', 'modicado_em', 'prazo_restante'])
            print('Base de Dados Criado com sucesso!!! Reiniciaremos o menu')
            time.sleep(1.5)
            os.system('cls')
            menu_principal()
        except Exception as error:
            print(f'Deu um erro inesperado, estaremos reiniciado o menu; descrição do erro: {error}')
            time.sleep(2.5)
            os.system('cls')
            menu_principal()

def view_data():
    ler_dados = list()
    try:
        with open('base_csv.csv', 'r', newline='', encoding='utf-8') as file:
            reader = csv.reader(file, delimiter='|')
            for row in reader:
                ler_dados.append(row)

        for item in ler_dados:
            if item[0] == 'id':
                pass
            else:
                data_hora_atual = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())

                #Data e Hora de criação
                data_criacao = item[2].split(' ')[0].split('/')
                hora_criacao = item[2].split(' ')[1].split(':')
                #Data e hora atual
                data_atual = data_hora_atual.split(' ')[0].split('/')
                hora_atual = data_hora_atual.split(' ')[1].split(':')

                #Sliptando e usando Datetime para subtração das datas
                data_criacao_ajustada = datetime(int(data_criacao[2]),
                                                 int(data_criacao[1]),
                                                 int(data_criacao[0]),
                                                 int(hora_criacao[0]),
                                                 int(hora_criacao[1]),
                                                int(hora_criacao [0]))

                data_atual_ajustada = datetime(int(data_atual[2]),
                                               int(data_atual[1]),
                                               int(data_atual[0]),
                                               int(hora_atual[0]),
                                               int(hora_atual[1]),
                                               int(hora_atual [0]))

                diferenca2 = str(data_atual_ajustada - data_criacao_ajustada)

                if ',' in diferenca2:
                    diferenca2 = diferenca2.split(',')
                    diferencaDias = diferenca2[0].split(' ')[0]
                    diferencaHoras = diferenca2[1]
                    diferencaHoras = diferencaHoras.split(':')

                    # Regra de negocio numero 1 - Alternar status mediante periodo de data/hora exceto quando já estiver com status de concluido
                    dias = int(diferencaDias)
                    horas = int(diferencaHoras[0])
                    minutos = int(diferencaHoras[1])

                    dias_em_horas_em_min = (((dias * 24) + horas) * 60) + minutos   # horas em min

                    if item[1] != 'Concluido' and item[1] != 'Deletado':

                        if dias_em_horas_em_min >= 360 and horas_em_min < (int(item[3] * 24) * 60):
                            item[1] = 'Em Andamento'
                        elif dias_em_horas_em_min >= ((int(item[3] * 24) * 60) / 3):
                            item[1] = 'Há Vencer'
                        elif dias_em_horas_em_min > (int(item[3] * 24) * 60):
                            item[1] = 'Vencido'
                        else:
                            pass

                        # Regra de negocio numero 2 - prazo restante é um decremente de prazo
                        prazo_em_min = (int(item[3]) * 24) * 60
                        diferenca_em_min = (((dias * 24) + horas) * 60) + minutos
                        decremento_prazo = prazo_em_min - diferenca_em_min
                else:

                    diferencaHoras = diferenca2.split(':')
                    horas = diferencaHoras[0]
                    minutos = diferencaHoras[1]

                    # Regra de negocio numero 1 - Alternar status mediante periodo de data/hora exceto quando já estiver com status de concluido

                    horas_em_min = (int(horas) * 60) + int(minutos) #horas em min

                    if item[1] != 'Concluido' and item[1] != 'Deletado':
                        if horas_em_min >= 360 and horas_em_min < (int(item[3] * 24) * 60):
                            item[1] = 'Em Andamento'
                        elif horas_em_min >= ((int(item[3] * 24) * 60) / 3):
                            item[1] = 'Há Vencer'
                        elif horas_em_min > (int(item[3] * 24) * 60):
                            item[1] = 'Vencido'
                        else:
                            pass

                    if item[1] != 'Concluido' or item[1] != 'Deletado':
                        # Regra de negocio numero 2 - prazo restante é um decremente de prazo
                        prazo_em_min = (int(item[3]) * 24) * 60
                        diferenca_em_min = (int(horas) * 60) + int(minutos)
                        decremento_prazo = prazo_em_min - diferenca_em_min

                        #Algoritomo de extração de dias, horas, e min, de um data convertida totalmente em min
                        prazo_desc = decremento_prazo
                        count_dias = 0
                        count_horas = 0
                        count_minutos = 0
                        while prazo_desc >= 1440:
                            prazo_desc -= 1440
                            count_dias += 1
                        while prazo_desc >= 60 and prazo_desc < 1440:
                            prazo_desc -= 60
                            count_horas += 1
                        while prazo_desc > 0 and prazo_desc < 60:
                            prazo_desc -= 1
                            count_minutos += 1

                        if count_dias > 0 and count_horas > 0 and count_minutos > 0:
                            item[7] = f'{count_dias} dias {count_horas} horas, {count_minutos} minutos'
                        elif count_dias == 0 and count_horas == 0 and count_minutos == 0:
                            item[7] = f'Carregando...'
                        elif count_dias > 0 and count_horas > 0 and count_minutos == 0:
                            item[7] = f'{count_dias} dias {count_horas} horas'
                        elif count_dias > 0 and count_horas == 0 and count_minutos == 0:
                            item[7] = f'{count_dias} dias'
                        elif count_dias == 0 and count_horas == 0 and count_minutos > 0:
                            item[7] = f'{count_minutos} minutos'
                        elif count_dias == 0 and count_horas > 0 and count_minutos == 0:
                            item[7] = f'{count_horas} horas'
                        elif count_dias >  0 and count_horas == 0 and count_minutos == 0:
                            item[7] = f'{count_dias} dias'
                        elif count_dias ==  0 and count_horas > 0 and count_minutos > 0:
                            item[7] = f'{count_horas} horas, {count_minutos} minutos'
                        else:
                            item[7] = f'---'
            #removendo da visualização os Deletados
            if secrete != 1717:
                novalista = []

                for linhas in ler_dados:
                    if linhas[0] == 'id':
                        novalista.append(linhas)
                    elif linhas[1] == 'Deletado':
                        pass
                    else:
                        novalista.append(linhas)

        with open('base_csv.csv', 'w', newline='', encoding='utf-8') as file:
            alterar = csv.writer(file, delimiter='|')

            for row in ler_dados:
                alterar.writerow(row)



    except Exception as error:
        print(f'Deu um erro inesperado, estaremos reiniciado o menu; descrição do erro: {error}')
        time.sleep(2.5)
        os.system('cls')
        menu_principal()

    if secrete == 1717:
        return ler_dados
    else:
        return novalista

def alterar_dados_tarefa(comando, id):
    alter_dados = view_data()
    sinalero = 0

    if comando == 'alter':
        for num, dados in enumerate(alter_dados):
            if num == 0:
                continue
            else:
                if int(dados[0]) == int(id):
                    print('Você pode altera os campos: ')
                    print(f'Prazo atua é : {dados[3]}')
                    prazo_novo = int(input('Informo o novo prazo aqui ou digite 0 (zero) para manter o atual>>>'))

                    if prazo_novo == 0:
                        pass
                    else:
                        alter_dados[num][3] = prazo_novo
                        alter_dados[num][6] = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
                        print('Prazo alterado com sucesso!!!')
                        sinalero += 1

                    print(f'Prazo atua é : {dados[5]}')
                    descricao_novo = input('Informo a nova Descrição aqui ou aperte <<Enter>> para manter o valor atual >>>')

                    if descricao_novo == '':
                        continue
                    else:
                        alter_dados[num][5] = descricao_novo
                        alter_dados[num][6] = time.strftime('%d/%m/%Y %H:%M:%S', time.localtime())
                        print('Descrição alterado com sucesso!!!')
                        sinalero += 1

    if sinalero != 0:
        try:
            with open('base_csv.csv', 'w', newline='', encoding='utf-8') as file:
                add_tarefa = csv.writer(file, delimiter='|')
                for dados in alter_dados:
                    add_tarefa.writerow(dados)
            print('Tarefa alterada com sucesso!')
            time.sleep(1.5)
            os.system('cls')
            menu_principal()
        except Exception as error:
            print(f'Algo inesperado ocorreu, estamos reinicializando... descrição do erro {error}')
            time.sleep(1.5)
            os.system('cls')
            menu_principal()

def deletar_dados_tarefa(comando, id):
    alter_dados = []
    with open('base_csv.csv', 'r', newline='', encoding='utf-8') as file:
        ler_dados = csv.reader(file, delimiter='|')
        for row in ler_dados:
            alter_dados.append(row)

    sinalero = 0

    if comando == 'delete':
        for num, dados in enumerate(alter_dados):
            if num == 0:
                continue
            else:
                if int(dados[0]) == int(id):
                    print('Você tem certeza que quer deletar a tarefa? ')
                    acao_novo = int(input('Digite 1 para deletar e 0 para retornar ao menu inicial>>> '))

                    if acao_novo == 0:
                        menu_principal()
                    elif acao_novo == 1:
                        alter_dados[num][1] = 'Deletado'
                        print('Registro deletado com sucesso!!!')
                        sinalero += 1

    if sinalero != 0:
        try:
            with open('base_csv.csv', 'w', newline='', encoding='utf-8') as file:
                add_tarefa = csv.writer(file, delimiter='|')
                for dados in alter_dados:
                    add_tarefa.writerow(dados)
            print('Ação concluida com sucesso!')
            time.sleep(1.5)
            os.system('cls')
            menu_principal()

        except Exception as error:
            print(f'Algo inesperado ocorreu, estamos reinicializando... descrição do erro {error}')
            time.sleep(1.5)
            os.system('cls')
            menu_principal()


#started program
welcome()
