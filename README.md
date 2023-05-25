# stage_controller
Este arquivo fornece instruções sobre como executar o código no seu ambiente local.

## Pré-requisitos
- Linguagem de programação: [Python 3]
- Versão Ubunto: [20.04]
- Versão do ROS: [Noetic]

## Comandos para executar o programa 
### Preparando ambiente do ROS
1. Em um terminal, navegue para o repositório catkin_ws:
```sheel
$ cd catkin_ws/
```
2. Inicialize e configure o ambiente:
```sheel
~/catkin_ws$ source devel/setup.bash 
```
3. Copila os pacotes baixados( executar esse comando só quando baixa o pacote, não e necessário executar toda vez que executa a simulação):
```sheel
~/catkin_ws$ catkin_make
```
### Deixando o arquivo executavel
4. Vamos navegar até a pasta de /scripts para isso vamos executar o seguinte comando:
```sheel
~/catkin_ws$ cd src/stage_controller/scripts/
```
5. Depois disso vamos executar o comando que deixa o arquivo stage_controller.py executavel:

```sheel
~/src/stage_controller/scripts/$ chmod +x stage_controller.py
```
### Rodando Simulação
6. Inicialize o ros:
```sheel
~/catkin_ws$ roscore
```
7. Em outro terminal sem fechar o primeiro execute os comandos 1 e 2 para carregar o ambiente e en seguida execute o seguinte comando para abrir a janela de simulação:
```sheel
~/catkin_ws$ roslaunch stage_controller launcher.launch
```
Assim vai abrir a janela a seguir: 
![Screenshot from 2023-05-24 13-16-06](https://github.com/jardelprad0/stage_controller/assets/61805544/6bb63beb-8d87-40d5-b465-5792dfd39e88)

8. Com isso feito vamos abrir outro terminal e executar os comandos 1 e 2, depois vamos executar nosso codigo para fazer o robo se movimentar:
```sheel
~/catkin_ws$ rosrun stage_controller stage_controller.py
```

## Pronto! Seu robô esta se movendo até o 'target' definido no código :)

### Link do Vídeo  : https://youtu.be/XEvFqXbvWAI
