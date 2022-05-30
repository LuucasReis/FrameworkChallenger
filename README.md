# FrameworkChallenger
Desafio técnico para montar um menu com acesso a 3 janelas que devem conter uma tabelas que liste as informações contidas na API https://jsonplaceholder.typicode.com/

Criei uma interface gráfica de login/cadastro utilizando a biblioteca PyQt5 para acessar a janela de menu, com 3 tabelas (ToDos, Postagens e albuns) contendo as informações da API requisitada criada através da biblioteca Tkinter. 

.1º JANELA
----------


![1_tela_fw](https://user-images.githubusercontent.com/102496835/171066236-baaeebe7-3d59-486d-82bf-cb5a7ca0f72c.jpg)

- GUI de autenticação utilizando um login e uma senha para poder acessar a janela que contém as tabelas.

.2º JANELA
----------

![2_tela_fw](https://user-images.githubusercontent.com/102496835/171066370-f794c9d2-f16a-4112-9023-b163f18d81aa.jpg)

- Tela de cadastro simples, apenas com senha e confirmação de senha (Caso não sejam iguais, não sera possível concluir o cadastro)

3º JANELA
---------

![3_tela_fw](https://user-images.githubusercontent.com/102496835/171066556-2514fd25-9e73-4bbc-a676-e9cbbf284fd7.jpg)

- Tela do desafio que contém as 3 tabelas. Cada um dos botões abre uma nova janela para apresentar a tabela, sem fechar a janela do desafio, além de possuir um botão para logout, que redireciona para a 1º tela (requisitos do desafio)
- As tabelas contém dados falsos, e a partir disso, criei apenas um filtro pela id (que se diferencia em cada dado) e um botão de selecionar pelo próprio mouse para obter os dados nos blocos.
