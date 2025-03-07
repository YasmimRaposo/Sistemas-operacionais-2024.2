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

## Explicação do copilot:<br>

**Entendendo a Eficiência \(E\) em Sistemas de Tempo Compartilhado**

A eficiência \(E\) mede o uso produtivo do processador em comparação com o tempo total, incluindo trocas de contexto.

**Fórmula**
\[
E = \frac{tq \cdot (1 - p/100)}{tq + ttc}
\]

**Onde:**
- \(tq\): Quantum de tempo alocado para cada processo.
- \(ttc\): Tempo gasto na troca de contexto.
- \(p\): Percentual do quantum gasto em entrada/saída.

---

### **Explicação**
1. **Numerador** (\(tq \cdot (1 - p/100)\)):
   - Representa o tempo efetivo que o processador utiliza para tarefas úteis.
   - \((1 - p/100)\) ajusta o quantum disponível, removendo o tempo dedicado às operações de I/O.

2. **Denominador** (\(tq + ttc\)):
   - Inclui o tempo total que o processador dedica, somando o quantum disponível e o tempo gasto nas trocas de contexto.

---
#### **Exemplo 1**:
**Parâmetros**:
- \(tq = 10ms\), \(ttc = 2ms\), \(p = 20\%\).

**Cálculo**:
- Tempo útil: \(10 \cdot (1 - 0,2) = 8ms\).
- Tempo total: \(10 + 2 = 12ms\).
- Eficiência:
\[
E = \frac{8}{12} = 0,666 \, (ou \, 66,6\%)
\]

---

### **Fatores que Influenciam a Eficiência**
1. **Quantum maior (\(tq\))**:
   - Aumenta a eficiência, pois reduz o impacto relativo do \(ttc\).
2. **Troca de contexto lenta (\(ttc\))**:
   - Diminui a eficiência, já que mais tempo é desperdiçado.
3. **Percentual alto de I/O (\(p\))**:
   - Reduz a eficiência, pois mais tempo do quantum é gasto em operações não produtivas.

### **03. Explique o que é, para que serve e como funciona a técnica de aging.**<br>
É uma técnica de (envelhecimento) que aumenta a prioridade da tarefa proporcionalmente ao tempo que ela está aguardando o processador, evitando, assim, a inanição de tarefas de baixa prioridade.

### **04. No algoritmo de envelhecimento definido na Seção 6.4.6, o que seria necessário modificar para suportar uma escala de prioridades negativa?**<br>
Para suportar prioridades negativas, o fator de envelhecimento deve diminuir a prioridade dinâmica ao invés de aumentá-la. Assim, tarefas que esperam aumentam sua prioridade com valores mais baixos até serem executadas.<br>

### **05. Enunciado:**<br>
![image](https://github.com/user-attachments/assets/4ed7bad2-1fe0-4296-b554-ba55def506c9)

### **06. Enunciado:**<br>

![image](https://github.com/user-attachments/assets/117f523f-5c8e-4c2a-9903-6e198404b0e0)

