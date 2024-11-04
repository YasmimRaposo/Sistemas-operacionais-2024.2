# Arquiteturas de Sistemas Operacionais

## Informações gerais

- Capítulo: [Arquitetura de SO](https://wiki.inf.ufpr.br/maziero/lib/exe/fetch.php?media=socm:socm-03.pdf)
- Disciplina: *sistemas operacionais*
- Livro: [Sistemas Operacionais: Conceitos e Mecanismos](https://wiki.inf.ufpr.br/maziero/doku.php?id=socm:start)

## Aluno

- nome: Yasmim Fernandes de Oliveira Raposo
- matrícula: 20231014040007

## Respostas dos exercícios

**1. Monte uma tabela com os benefícios e deficiências mais relevantes das principais
arquiteturas de sistemas operacionais.**

| Característica | Monolítico | Micronúcleo | Híbrido |
|---|---|---|---|
| **Vantagens** | Simplicidade de implementação, eficiente para tarefas comuns, boa integração entre componentes. | Alta modularidade, mais seguros, mais portáveis. | Combina o melhor dos dois mundos, boa performance e flexibilidade. |
| **Desvantagens** | Dificuldade de adicionar novos recursos, menos seguros, menos portáveis. | Sobrecarga de comunicação entre processos, pode ser menos eficiente para tarefas simples. | Complexidade de design e implementação. |

**2. O Linux possui um núcleo similar com o da figura 3.1, mas também possui
“tarefas de núcleo” que executam como os gerentes da figura 3.2. Seu núcleo é
monolítico ou micronúcleo? Por quê?**

Monolítico, pois apresenta diversas funcionalidades, desde gerenciamento de processos e memória até interação com dispositivos de hardware. 

**3. Sobre as afirmações a seguir, relativas às diversas arquiteturas de sistemas
operacionais, indique quais são incorretas, justificando sua resposta:**<br>

**(a) Uma máquina virtual de sistema é construída para suportar uma aplicação
escrita em uma linguagem de programação específica, como Java.**<br>
Incorreto. O objetivo da máquina é emular o computador, independente da linguagem.<br>

**(b) Um hipervisor convidado executa sobre um sistema operacional hospedeiro.**<br>
Sim. Ação mostrada na imagem 3.4<br>

**(c) Em um sistema operacional micronúcleo, os diversos componentes do
sistema são construídos como módulos interconectados executando dentro
do núcleo.**<br>
Incorreto. A característica principal desse sistema é a mínima quantidade de código executando em modo kernel.

**(d) Núcleos monolíticos são muito utilizados devido à sua robustez e facilidade
de manutenção.**<br>
Incorreto. Na verdade, o núcleo monolítico é considerado complexo e frágil.<br>

**(e) Em um sistema operacional micronúcleo, as chamadas de sistema são
implementadas através de trocas de mensagens.**<br>
Sim. Ocorre troca de mensagens entre aplicações. 
