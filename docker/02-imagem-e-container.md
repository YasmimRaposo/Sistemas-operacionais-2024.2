# códigos da aula de 14/02

## Cliente e servidor em python

### Servidor HTTP
`servidor-http.py`

```python
import http.server

# Definir o conteúdo HTML fixo
html_fixo = """
<!DOCTYPE html>
<html>
<head>
    <title>Servidor HTTP Multithread</title>
</head>
<body>
    <h1>Olá, mundo!</h1>
    <p>Este é um servidor HTTP multithread em Python.</p>
</body>
</html>
"""

class MeuManipulador(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Imprimir informações da requisição no console
        print(f"Requisição recebida de: {self.client_address}")
        print(f"Caminho solicitado: {self.path}")
        print("Cabeçalhos da requisição:")
        for nome, valor in self.headers.items():
            print(f"{nome}: {valor}")

        # Enviar resposta de código 200
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        # Enviar o conteúdo HTML fixo
        self.wfile.write(html_fixo.encode("utf-8"))

# Definir o endereço e a porta do servidor
endereco = ("", 8000)

# Criar o servidor
with http.server.HTTPServer(endereco, MeuManipulador) as httpd:
    print("Servidor HTTP rodando na porta 8000...")
    # Manter o servidor rodando
    httpd.serve_forever()

```

### Cliente HTTP com Threads
`cliente-http.py`

```python
import http.client
from concurrent.futures import ThreadPoolExecutor

def fazer_requisicao_get(id):
    print(f'### thread id {id} - Iniciou')
    # Conectar ao servidor localhost na porta 8000
    conexao = http.client.HTTPConnection("localhost", 8000)
    print(f'### thread id {id} - Abriu conexão')

    # Fazer a requisição GET
    conexao.request("GET", f"/{id}")
    print(f'### thread id {id} - Enviou requisição')

    # Obter a resposta
    resposta = conexao.getresponse()

    # Ler o conteúdo da resposta
    # conteudo = resposta.read()

    # Imprimir o status e o conteúdo da resposta
    print(f"Status ({id}): {resposta.status}")
    print(f"Motivo ({id}): {resposta.reason}")
    # print("Conteúdo:")
    # print(conteudo.decode("utf-8"))

    # Fechar a conexão
    conexao.close()
    print(f'### thread id {id} - Terminou')

# Chamar a função para fazer a requisição GET
# fazer_requisicao_get()

# Usar ThreadPoolExecutor para gerenciar threads
# with ThreadPoolExecutor(max_workers=2) as executor:
#     futuro1 = executor.submit(fazer_requisicao_get, 1)
#     futuro2 = executor.submit(fazer_requisicao_get, 2)

#     futuro1.result()
#     futuro2.result()

futuro = [0] * 10
with ThreadPoolExecutor(max_workers=10) as executor:
    for thread_id in range(10):
        futuro[thread_id] = executor.submit(fazer_requisicao_get, thread_id)

    for thread_id in range(10):
        futuro[thread_id].result()

```

## Construindo com docker

### Servidor Docker
1. Colocar o arquivo Servidor HTTP `servidor-http.py` e o arquivo Dockerfile abaixo no mesmo diretório (pasta)
2. Executar o comando `docker build -t http-server-python .` para **construir** a **imagem**
3. Executar o comando `docker run -p 3000:8000 --name servidor http-server-python` para executar o **container**
   - Executar o comando noutro terminal `docker stop servidor` para **parar** o **container**
   - Para executar o container novamente, em um terminal executar `docker start servidor`

`Dockerfile`

```
# Usar uma imagem base do Python
FROM python:3-slim

# Definir o diretório de trabalho no contêiner
WORKDIR /app

# Copiar o script Python para o contêiner
COPY servidor-http.py .

# Expor a porta 8000
EXPOSE 8000

# Executar o script Python
CMD ["python", "servidor-http.py"]

```

### Cliente Docker

segunda-feira 17/02
