# Implementação de tarefas

## Informações gerais

- Capítulo: [Implementação de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-05.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Yasmim Fernandes de O. Raposo
- matrícula: 20231014040007

## Respostas dos exercícios
### **1. Explique o que é, para que serve e o que contém um TCB - Task Control Block**<br>

Uma estrutura de dados importantíssima em um sistema operacional. Ele é responsável por armazenar todas as informações relevantes sobre uma tarefa ou processo em execução, funcionando como um "cartão de identidade" para cada tarefa. Dessa maneira, ele permite que o sistema operacional gerencie e monitore o estado e o progresso de todas as tarefas de maneira eficaz. Além disso, destaca-se o seu conteúdo:
- Identificador do Processo (PID): Número único que diferencia cada tarefa no sistema.<br>
- Estado da Tarefa: Indica se a tarefa está "Pronta", "Executando" ou "Suspensa".<br>
- Contador de Programa: Mostra a próxima instrução a ser executada pela tarefa.<br>
- Contexto de Execução: Inclui registradores e ponteiros de pilha, permitindo que a tarefa seja retomada de onde parou.
Permissões de Acesso e Recursos Utilizados: Informações sobre memória alocada, arquivos abertos e prioridades de escalonamento.<br>
<br>

### 2. Desenhe o diagrama de tempo da execução do código a seguir, informe qual a saída do programa na tela (com os valores de x) e calcule a duração aproximada de sua execução.<br>

![image](https://github.com/user-attachments/assets/9e434c9d-5d03-45a5-b599-471916c3fff7)

1. O programa começa com `x = 0`.  
2. A função `fork()` cria novos processos. No total, quatro processos são gerados ao final.  
3. Cada processo incrementa `x++`, pausando com `sleep(5)` e usando `wait(0)` para sincronização.  
4. No final, todos os processos imprimem `x = 2`.  

**Saída Final**:
```
Valor de x: 2
Valor de x: 2
Valor de x: 2
Valor de x: 2
```

O tempo total estimado de execução do programa é de 10 segundos, resultado de duas chamadas sleep(5) em todos os processos, enquanto as chamadas wait() garantem a sincronização entre pai e filhos

### **3. Indique quantas letras “X” serão impressas na tela pelo programa abaixo quando for executado com a seguinte linha de comando: “a.out 4 3 2 1”. O comando a.out resulta da compilação do programa a seguir:**<br>
![image](https://github.com/user-attachments/assets/639a8fdb-4230-4a3a-b39a-f442c2fe8e8c)

ERRO DE SEGMENTATION FAULT


### **4. O que são threads e para que servem?**<br>

Threads são as menores unidades de execução dentro de um processo, permitindo a realização de várias tarefas simultaneamente. Elas compartilham recursos como memória e arquivos, mas possuem seu próprio contador de programa, registradores e pilha. Isso melhora a eficiência e a performance do sistema, especialmente em processadores multicore, otimizando o uso dos recursos e permitindo que programas respondam mais rapidamente.<br>

### **5. Quais as principais vantagens e desvantagens de threads em relação a processos?**<br>
Threads oferecem vantagens em desempenho e compartilhamento de recursos, permitindo comunicação e sincronização rápidas com menor sobrecarga. Elas podem ser criadas, trocadas e encerradas mais rapidamente que processos, ideais para tarefas paralelas. No entanto, o compartilhamento de recursos pode comprometer a segurança e estabilidade, exigindo sincronização cuidadosa para evitar problemas de concorrência. Threads são vantajosas para desempenho e compartilhamento de dados, enquanto processos são melhores para isolamento e segurança.<br>

### **6. Forneça dois exemplos de problemas cuja implementação multi-thread não tem desempenho melhor que a respectiva implementação sequencial.**<br>

#### 1. Cálculos Estritamente Sequenciais:

- Algoritmos com forte dependência sequencial, como a sequência de Fibonacci recursiva, não se beneficiam de multi-threading.
- Cada termo depende do cálculo dos termos anteriores, criando dependências que não podem ser paralelizadas sem custos extras de sincronização.
- O overhead de gerenciar múltiplas threads torna a abordagem multi-thread menos eficiente que a execução sequencial.

#### Leitura e Escrita de Arquivos com I/O Limitado:

- Sistemas dependentes de operações de I/O (entrada e saída) são limitados pela velocidade do disco.
- Adicionar threads não melhora o desempenho em sistemas I/O-bound, pois o tempo de busca e entrega dos dados pelo disco é o fator limitante.
- Acesso simultâneo pode piorar o desempenho, criando gargalos devido à competição pelo mesmo recurso de I/O.

### **7. Associe as afirmações a seguir aos seguintes modelos de threads: many-to-one (N:1); one-to-one (1:1); many-to-many (N:M).**<br>


> Lembrete: 
> N:1 -> N threads do processo mapeadas em uma thread de núcleo.
> 1:1 -> Cada thread do processo mapeada em uma thread de núcleo.
> N:M -> N threads do processo mapeadas em M (< N) threads de núcleo.<br>

- a. Tem a implementação mais simples, leve e eficiente<br>
Resposta: (N:1)<br>
- b. Multiplexa os threads de usuário em um pool de threads de núcleo<br>
Resposta:(N:M)<br>
- c. Pode impor uma carga muito pesada ao núcleo<br>
Resposta:(1:1)<br>
- d. Não permite explorar a presença de várias CPUs pelo mesmo processo<br>
Resposta:(N:1)<br>
- e. Permite uma maior concorrência sem impor muita carga ao núcleo<br> 
Resposta:(N:M)<br>
- f. Geralmente implementado por bibliotecas<br>
Resposta:(N:1)<br>
- g. É o modelo implementado no Windows NT e seus sucessores<br>
Resposta: (1:1)<br>
- h. Se um thread bloquear, todos os demais têm de esperar por ele<br>
Resposta: (N:1)<br>
- i. Cada thread no nível do usuário tem sua correspondente dentro do núcleo<br>
Resposta: (1:1)<br>
- j. É o modelo com implementação mais complexa<br>
Resposta:(N:M)<br>

### **8.Considerando as implementações de threads N:1 e 1:1 para o trecho de código a seguir, a) desenhe os diagramas de execução, b) informe as durações aproximadas de execução e c) indique a saída do programa na tela. Considere a operação sleep() como uma chamada de sistema (syscall). A chamada thread_create cria uma nova thread, thread_exit encerra a thread corrente e thread_join espera o encerramento da thread informada como parâmetro**
![image](https://github.com/user-attachments/assets/18f1c8a7-4461-4677-a1d3-2ee85c024020)

Explicação gemini:

O código cria threads tA, tB e tC, executando threadBody (incrementa x, dorme, imprime x e y).

Implementação N:1
Execução: Sequencial, uma thread por vez.
Duração: ~32 unidades de tempo.
Saída:
x: 1, y: 1
x: 1, y: 2
x: 1, y: 3
Implementação 1:1
Execução: Threads concorrentes.
Duração: ~13 unidades de tempo.
Saída: (Ordem variável)
x: 1, y: 1
x: 1, y: 2
x: 1, y: 3
Observações
y é global, x é local.
N:1 é mais lento, 1:1 é mais rápido devido à concorrência.
