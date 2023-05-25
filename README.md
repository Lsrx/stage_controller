# stage_controller
Este arquivo fornece instruções sobre como executar o código no seu ambiente local.

## Pré-requisitos
- Linguagem de programação: [Python 3]
- Versão Ubuntu: [20.04]
- Versão do ROS: [Noetic]

## Comandos báicos
### Preparando o ambiente ROS
1. Abra o terminal e navegue para o repositório catkin_ws:

```sheel
$ cd catkin_ws/
```
2. Realize a iniciacao e configuracao do ambiente através da seguinte linha:

```sheel
~/catkin_ws$ source devel/setup.bash 
```
3. Atraves do comando catkin_make vamos realizar a compilacao dos pacotes para nossa primeira execucao (depois da primeira nao precisa fazer mais)

```sheel
~/catkin_ws$ catkin_make
```
### Gerando o executavel do script
4. Acesse a pasta de scripts e execute o comando:

```sheel
~/catkin_ws$ cd src/stage_controller/scripts/
```
5. Utilize a seguinte linha de codigo para transformar o arquivo .py em um arquivo executavel:

```sheel
~/src/stage_controller/scripts/$ chmod +x stage_controller.py
```
### Realizando a simulacao

6. Primeiro vamos inicializar o ROS core:

```sheel
~/catkin_ws$ roscore
```

7. Abra outro terminal e inicialize o ROS com stage_controler atraves do lancher (lembrar que nao se deve fechar os terminais abertos):
```sheel
~/catkin_ws$ roslaunch stage_controller launcher.launch
```

8. Abra outra janela de terminal e execute o stage_controler com o codigo desenvolvido:
```sheel
~/catkin_ws$ rosrun stage_controller stage_controller.py
```

9. O robo se movera ate o goal (destino) designado via codigo, para alterar o goal voce deve realizar a pausa do ultimo terminal e modificar o script stage_controller.py com o goal desejado. Apos isso salve o codigo e repita a passo 8.

## Ate o momento nao consegui recordar o teste no meu computador dado que a VM nao esta aguentando gravar o video (nao ha memoria suficiente para rodar o ROS e gravar tela numa VM).

