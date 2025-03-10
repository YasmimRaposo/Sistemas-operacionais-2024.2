# Experimentos com Servidor HTTP
- **Aluno**: [Yasmim Fernandes de oliveira Raposo](https://github.com/YasmimRaposo)
- Matrícula: 20231014040007
#### Cenários:
- Apenas 1 cliente
- 2 clientes simultâneos
- 5 clientes simultâneos
- 10 clientes simultâneos

#### Análise:
- Analisar e explicar o comportamento do cliente e do servidor sem thread e com Threads para cada um dos 4 casos acima.

#### Análise:
- Analisar e explicar o comportamento do cliente e do servidor com thread para cada um dos 4 casos acima.
- Se houver diferença no funcionamento dos servidores sem e com threads, analisar a diferença.

## Adições para Análise de Requisições

Para realizar uma análise detalhada do comportamento do servidor e dos clientes, foram adicionadas funcionalidades de medição de tempo no código. Especificamente, o módulo `time` do Python foi utilizado para registrar o tempo de início e fim de cada requisição.

## Análise dos Resultados

### Servidor HTTP sem Thread:

1. **1 cliente**: Aproximadamente 0.0034 segundos para completar a requisição.
2. **2 clientes simultâneos**:
   - Cliente 1: 0.0042 segundos
   - Cliente 2: 0.0044 segundos
3. **5 clientes simultâneos**:
   - Clientes 1 e 2: 0.0034 segundos
   - Cliente 3: 0.0057 segundos
   - Cliente 4: 0.0038 segundos
   - Cliente 5: 0.0055 segundos
4. **10 clientes simultâneos**:
   - Cliente 1: 0.0036 segundos
   - Cliente 2: 0.0055 segundos
   - Cliente 3: 0.0067 segundos
   - Cliente 4: 0.0039 segundos
   - Cliente 5: 0.0069 segundos
   - Cliente 6: 0.0039 segundos
   - Cliente 7: 0.0101 segundos
   - Cliente 8: 0.0060 segundos
   - Cliente 9: 0.0107 segundos
   - Cliente 10: 0.0025 segundos

### Servidor HTTP com Thread:

1. **1 cliente**: Tempo de Resposta: 0.0035 segundos
2. **2 clientes simultâneos**:
   - Cliente 1: 0.0047 segundos
   - Cliente 2: 0.0046 segundos
3. **5 clientes simultâneos**: Entre 0.0046 a 0.0055 segundos
4. **10 clientes simultâneos**:
   - Cliente 1: 0.0074 segundos
   - Cliente 2: 0.0083 segundos
   - Cliente 3: 0.0088 segundos
   - Cliente 4: 0.0085 segundos
   - Cliente 5: 0.0106 segundos
   - Cliente 6: 0.0096 segundos
   - Cliente 7: 0.0091 segundos
   - Cliente 8: 0.0138 segundos
   - Cliente 9: 0.0108 segundos
   - Cliente 10: 1.0170 segundos

## Comparação

### Escalabilidade:
- **Servidor sem Thread**: Eficiente para um pequeno número de clientes simultâneos. À medida que o número de clientes aumenta, a variação no tempo de resposta se torna maior.
- **Servidor com Thread**: : Gerencia múltiplas conexões simultâneas de maneira eficaz até um certo ponto. No entanto, observamos um aumento significativo no tempo de resposta para o 10º cliente (1.0170 segundos), indicando que pode haver sobrecarga devido à criação e gerenciamento de muitas threads.

### Uso de Recursos:
- **Servidor sem Thread**: Consome menos recursos, mas pode haver um aumento na latência com um número maior de clientes simultâneos.
- **Servidor com Thread**: Aumenta o consumo de recursos (CPU e memória) com a criação e gerenciamento de múltiplas threads, mas gerencia melhor múltiplas requisições até certo limite.

### Latência:
- **Servidor sem Thread**: Latência inicial baixa, mas pode aumentar significativamente com um grande número de clientes.
- **Servidor com Thread**: Latência inicial baixa e relativamente estável, até enfrentar problemas de sobrecarga com um grande número de conexões.

## Conclusão:
- Ambos os servidores apresentam tempos de resposta rápidos e eficientes para um pequeno número de clientes.
- O servidor com thread pode enfrentar problemas de sobrecarga com um grande número de conexões.
- O servidor sem thread pode apresentar variações na latência com o aumento do número de clientes, mas tende a consumir menos recursos.

> Pra rodar, no terminal digite o servidor que deseja iniciar, "python server_comThread.py" ou "python server_semThread". Posteriormente, em outro terminal digite "python cliente.py"

