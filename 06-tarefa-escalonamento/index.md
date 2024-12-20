# Escalonamento de tarefas

## Informações gerais

- Capítulo: [Escalonamento de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-06.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Yasmim Fernandes de Oliveira Raposo
- matrícula: 20231014040007

## Respostas dos exercícios

### **01. Explique o que é escalonamento round-robin, dando um exemplo.**<br>
O escalonamento Round-Robin (RR) é um método preemptivo que aloca o processador a cada tarefa por um período fixo chamado quantum. Se a tarefa não terminar nesse tempo, ela volta para a fila de prontas e o processador passa para a próxima. Isso garante um uso justo do processador. 
Vantagem:<br>
cada processo recebe uma fatia de tempo da CPU de forma justa.<br>

Desvantagem:<br>
trocas de contexto podem diminuir a eficiência, principalmente se a fatia de tempo de CPU for curta.<br>

Impacto:<br>
Desempenho, pois frequentemente gera um overhead devido às trocas de contexto.<br>

Exemplo:<br>
Jogos Multiplayer: Em um servidor de jogos multiplayer, cada jogador recebe uma fatia de tempo de processamento de forma justa.

### **02. Considere um sistema de tempo compartilhado com valor de quantum tq e duração da troca de contexto ttc. Considere tarefas de entrada/saída que usam em média p% de seu quantum de tempo cada vez que recebem o processador. Defina a eficiência E do sistema como uma função dos parâmetros tq, ttc e p. A eficiência E mede o uso efetivo do processador comparado ao tempo total, incluindo trocas de contexto. A eficiência é:**

[...]

### **03. Explique o que é, para que serve e como funciona a técnica de aging.**<br>
É uma técnica de (envelhecimento) que aumenta a prioridade da tarefa proporcionalmente ao tempo que ela está aguardando o processador, evitando, assim, a inanição de tarefas de baixa prioridade.

### **04. No algoritmo de envelhecimento definido na Seção 6.4.6, o que seria necessário modificar para suportar uma escala de prioridades negativa?**<br>
Para suportar prioridades negativas, o fator de envelhecimento deve diminuir a prioridade dinâmica ao invés de aumentá-la. Assim, tarefas que esperam aumentam sua prioridade com valores mais baixos até serem executadas.<br>

### **05. Enunciado:**<br>
![image](https://github.com/user-attachments/assets/4ed7bad2-1fe0-4296-b554-ba55def506c9)

### **06. Enunciado:**<br>

![image](https://github.com/user-attachments/assets/117f523f-5c8e-4c2a-9903-6e198404b0e0)

