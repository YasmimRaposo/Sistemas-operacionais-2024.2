# Conceito de tarefas

## Informações gerais

- Capítulo: [Conceito de tarefas](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-04.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Yasmim Fernandes de Oliveira Raposo
- matrícula: 20231014040007

## Respostas dos exercícios

## Questões sobre Sistemas Operacionais

### 1. O que significa time-sharing e qual a sua importância em um sistema operacional?<br>
Significa compartilhamento de tempo. Desse modo, o time-sharing maximiza o uso do recursos ao definir um prazo de processamento.<br>

### 2. Como e com base em que critérios é escolhida a duração de um quantum de processamento?<br>
A duração do quantum depende muito do tipo de sistema operacional e a partir disso os criterios incluem tempo de resposta, eficiência e tipo de aplicação. <br>
### 3. Considerando o diagrama de estados dos processos apresentado na figura a seguir, complete o diagrama com a transição de estado que está faltando (t6) e apresente o significado de cada um dos estados e transições.<br>
![image](https://github.com/user-attachments/assets/5309ae06-9a34-4787-a4c5-d8bf79fa6ad9)


Nova E1: A tarefa está sendo criada e carregada em memória.

Nova -> Pronto(t5): a tarefa termina de ser carregada em memória.

Pronta E5 -> A tarefa está em memória, aguardando o processador.

Pronto -> Executando(t4): A transição ocorre quando a tarefa é escolhida pelo escalonador para ser executado.

Executando E3 -> A tarefa está sendo executada pelo processador.

Executando -> Suspensa(t2): O processo passa para espera enquanto aguarda a conclusão de um evento solicitado. Geralmente, acontece quando um recurso não está disponível.

Suspensa E4 -> A tarefa está aguardando dados externos ou sincronização.

Suspensa -> Pronto(t3): O processo passa para pronto quando solicitado e atendido ou o recurso esperado é concedido.

Executando → Terminada(t1): ocorre quando a tarefa encerra sua execução

Terminada E2 -> A tarefa foi concluída e pode ser removida da memória.

### 4. Indique se cada uma das transições de estado de tarefas a seguir definidas é possível ou não. Se a transição for possível, dê um exemplo de situação na qual ela ocorre (N: Nova, P: Pronta, E: Executando, S: Suspensa, T: Terminada).

- **E → P**: Possível. Exemplo: quando a tarefa executando atinge o limite de tempo do quantum de processamento<br>
- **E → S**: Possível.  Exemplo: quando a tarefa em execução solicita um recurso indisponível no momento
- **S → E**: Não possível. 
- **P → N**: Não possível. 
- **S → T**: Possível. Exemplo: a tarefa em estado suspenso possui um erro ou é forçada a encerrar sua execução por conta de um comando do sistema.
- **E → T**: Possível. Exemplo: a tarefa completa sua execução ou é encerrada por conta de erro.
- **N → S**: Não é possível.
- **P → S**: Não é possivel.

### 5. Relacione as afirmações abaixo aos respectivos estados no ciclo de vida das tarefas (N: Nova, P: Pronta, E: Executando, S: Suspensa, T: Terminada):

- [ N ] O código da tarefa está sendo carregado.
- [ P ] As tarefas são ordenadas por prioridades.
- [ E ] A tarefa sai deste estado ao solicitar uma operação de entrada/saída.
- [ T ] Os recursos usados pela tarefa são devolvidos ao sistema.
- [ P ] A tarefa vai a este estado ao terminar seu quantum. 
- [ P ] A tarefa só precisa do processador para poder executar.
- [ ? ] O acesso a um semáforo em uso pode levar a tarefa a este estado.
- [ E ] A tarefa pode criar novas tarefas.
- [ E ] Há uma tarefa neste estado para cada processador do sistema.
- [ S ] A tarefa aguarda a ocorrência de um evento externo.


