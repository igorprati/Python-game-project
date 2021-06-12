# Python Game Project
 Este projeto foi desenvolvido ao final do <b>Módulo I</b> do Curso de Programação da <a href='https://blueedtech.com.br/'>Blue Edtech 💙</a>
 
 ## Objetivos do projeto
 Deveríamos fazer um jogo de ficção interativa em linguagem Python utilizando os recursos de laço de repetição, estruturas condicionais, programação orientada a objetos, funções. Neste tipo de jogo, é simulado a rotina de uma pessoa onde ela pode interagir com o ambiente e objetos através de comandos no teclado, gerando modificações ao curso de suas escolhas. 
 
 <img src='https://i.imgur.com/ToeprUy.jpg' width='300px'></img>
 
 # Programmer Life Simulator
 ```
 #### REGRAS ####
 
 - Cada ação gasta uma quantidade de energia, avança o tempo e poderá (ou não) gastar dinheiro.
 - O personagem não poderá executar uma ação caso essa ultrapasse 24h do dia ou 0 de energia.
 - O peronagem não poderá trabalhar até que consiga status de "Programador Júnior", que é obtido estudando.
 - A cada vez que estuda, recebe 0.5 exp e será considerado "Programador Júnior" ao alcançar 2.0 exp.
 - Poderá restaurar energia comprando itens ou ir dormir para iniciar o próximo dia.
 
 ```
 ## O início
 Para começar, vamos entender antes o que dita o andamento do nosso jogo. Ou seja, o que nos informa se estamos progredindo ou não. <br><br>
  <img src='https://i.imgur.com/61dDwQ0.png' width='300px'></img>
  
 Nosso personagem possui basicamente 2 atributos **iniciais**:
 
 - ⚡Energia: 100
 - 💵 Dinheiro: 100

 
 O dia começa em:

 - 📆 Dia: 01
 - ⌚ Hora: 06:00 a.m

 
## Menu inicial
Existe um menu inicial no qual você poderá escolher o que quer fazer. Lembrando que todas as opções irão alterar sua Energia ou Dinheiro ou (Experiência no trabalho/estudo) mas falaremos disso depois.
- São 5 ações iniciais que o personagem é capaz de tomar. São elas:
```
 Estudar
 Trabalhar
 Restaurar energia
 Ir ao banco
 Dormir
 ```
<img src='https://i.imgur.com/raamBqR.png' width='300px'></img>

## Menu Estudar
Para este menu, o personagem possui 02 (duas) opções:

- Estudar HTML
- Estudar Java
```
A cada vez que estuda, o status do personagem muda para:
```
- -15 energia
- +0.5 experiência nos estudos
- Horário avança 3h


 


