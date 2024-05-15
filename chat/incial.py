# [vamos criar um chat simples e juntamente um site, tudo isso usando a biblioteca Flet]

import flet as ft

# [criar a função princiapl, o que vai acontecer quando o usuário entrar no site]

# {


def main(pagina):  # como parametro a pagina, ois é a pagina que o usuário está e vai abrir #primeiro criamos os elementos e depois adcionamos

    # (a ordem dos elementos importa, o que for criado primeiro vai aparecer primeiro)

    # adciobar um elemento usamos "ft.", o text é o texto que vai aparecer na tela
    titulo = ft.Text("hashzap")

    titulo_janela = ft.Text("Bem vindo ao hashzap")
    # È um label(rotulo), ou seja, uma sugestão de texto que vai aparecer no campo de texto
    campo_nome_usuario = ft.TextField(label="Digite seu nome de usuário")

    chat = ft.Column()  # é uma coluna de mensagens (para as mensagens aparecerem uma embaixo da outra), ou seja, é uma string vazia

# {
    # TUNEL DE COMINICAÇÃO ENTRE DOIS DISPOSITIVOS - duas etapas = 1º função que vai ser executada para todo mundo ao mesmo tempo
    # criar uma função para enviar a mensagem
    def enviar_mensagem_tunel(mensagem):
        # criar um texto, o texto que vai aparecer é a mensagem
        texto_chat = ft.Text(mensagem)
        # adcionar a mensagem dentro do chat,"controls" é uma lista de elementos que vão aparecer na tela (controles do chat), o "append" é para adcionar um elemento na lista
        chat.controls.append(texto_chat)
        pagina.update()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
        # TUNEL DE COMINICAÇÃO ENTRE DOIS DISPOSITIVOS - duas etapas = 2º criar o tunel de comunicação dentro do seu site
    # criar um tunel de comunicação "pubsub", o "subscribe" é para se inscrever em um canal de comunicação, o "enviar_mensagem_tunel" é a função que vai ser executada
    pagina.pubsub.subscribe(enviar_mensagem_tunel)
# }

# {
    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value  # pegar o valor do campo de mensagem
        nome_usuario = campo_nome_usuario.value  # pegar o valor do campo de mensagem

        # texto dinamico (o que vai ser exibido na tela), o f é para indicar que é um texto dinamico (formatar), o {} é para indicar que é uma variavel, o nome_usuario é a variavel que vai ser exibida, o : é para separar o nome do usuário da mensagem, o texto_mensagem é a mensagem que vai ser exibida/ o quue SÓ estiver entre "" é estatico, ou seja, não muda
        mensagem = f"{nome_usuario}: {texto_mensagem}"
        # enviar a mensagem para todo mundo, o "send_all" é para enviar a mensagem para todo mundo, o "mensagem" é a mensagem que vai ser enviada
        pagina.pubsub.send_all(mensagem)

        # depois de enviar a mensagem, o campo de mensagem vai ficar vazio
        campo_mensagem.value = ""
        pagina.update()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # o "on_submit" é o evento que vai acontecer quando o usuário apertar "enter", ou seja, quando ele enviar a mensagem, o evento que vai acontecer é a função "enviar_mensagem
    campo_mensagem = ft.TextField(
        label="Digite sua mensagem", on_submit=enviar_mensagem)
    # criar um botão, o texto que vai aparecer no botão é "Enviar mensagem"
    botao_enviar_mensagem = ft.ElevatedButton(
        "Enviar mensagem", on_click=enviar_mensagem)
# }

# {
    # criar uma linha, ou seja, os elementos vão aparecer um ao lado do outro, passamos uma lista com os elementos que vão aparecer na linha
    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])

    def entrar_chat(evento):
        pagina.remove(titulo)  # remover o titulo da pagina
        pagina.remove(botao_iniciar)  # remover o botão da pagina
        janela.open = False  # fechar a janela

        pagina.add(chat)  # adcionar o chat na pagina
        pagina.add(linha_mensagem)
        # mensagem que vai aparecer quando o usuário entrar no chat
        mensagem = (f"{campo_nome_usuario.value}: entrou no chat")
        pagina.pubsub.send_all(mensagem)  # enviar a mensagem para todo mundo
        pagina.update()
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # criar um botão, o texto que vai aparecer no botão é "Entrar"
    botao_entrar = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)
# }

    # criar uma janela de alerta ("Alert"=caixa de pop-up, Dialog= o tipo, tem varios tipos), nela tem que ter 3 parametros title, contnet e buttons/ actions = lista de botoes obrigatoriamente tem que estar entre "[]"
    janela = ft.AlertDialog(title=titulo_janela,
                            content=campo_nome_usuario, actions=[botao_entrar])

# {
    # (obrigatoriamente toda função associada a um botão tem que ter o parametro "evento", já que vai haver uma enteração com o usuário)Toda função vem antes do botão

    def iniciar_chat(evento):  # vamos criar tudo o que vai acontecer quando clicarmos no botão
        # usamos "dialog" porque é o nome do tipo da janela, e passamos a janela que criamos
        pagina.dialog = janela
        # toda janela é fechada então temos que usar o "open=True" para abrir a janela
        janela.open = True
        pagina.update()  # atualizar a pagina para aparecer as alterações
# -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
    # criar um botão, on_click é o evento que vai acontecer quando o botão for clicado
    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)
# }
    # (NÃO USAMOS O "pagina.add()" PARA ADICIONAR A JANELA, POIS ELA VAI SER ADICIONADA QUANDO O BOTÃO FOR CLICADO, OU SEJA, VAI APARCER EM CIMA DE TUDO, NÃO DE BAIXO).

    pagina.add(titulo)  # adcionar o titulo na pagina
    pagina.add(botao_iniciar)  # adcionar o botão na pagina
    # }


# rodar o aplocativo, passando a função main como parametro
ft.app(main, view=ft.WEB_BROWSER)

# para deixar disponivel internet vai ter que fazer um deploy, ou seja, colocar o site na internet - vai no site do flet e depois documentação e lá eles ensinam
# intranet é a internet local, ou seja, só quem está conectado na mesma rede que você pode acessar, para disponilizar para todo mundo tem que colocar em um servidor onde todo mundo vai estar conectado na mesma rede
