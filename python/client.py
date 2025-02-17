import http.client
import concurrent.futures
import time ##adicionando biblioteca time pra saber tempo de resposta para cada requisição


def fazer_requisicao_get():
    inicio = time.time()
    # Conectar ao servidor localhost na porta 8000
    conexao = http.client.HTTPConnection("localhost", 8000)

    # Fazer a requisição GET
    conexao.request("GET", "/")

    # Obter a resposta
    resposta = conexao.getresponse()

    # Ler o conteúdo da resposta
    conteudo = resposta.read()
    fim = time.time()
    tempo_de_resposta = fim - inicio

    # Imprimir o status e o conteúdo da resposta
    print(f"Status: {resposta.status}")
    print(f"Motivo: {resposta.reason}")
    print("Conteúdo:")
    print(conteudo.decode("utf-8"))
    print(f"Tempo de Resposta: {tempo_de_resposta:.4f} segundos")

    # Fechar a conexão
    conexao.close()

def main(num_clients):
    with concurrent.futures.ThreadPoolExecutor(max_workers=num_clients) as executor:
        futures = [executor.submit(fazer_requisicao_get) for _ in range(num_clients)]
        for i, future in enumerate(concurrent.futures.as_completed(futures)):
            try:
                future.result()
                print(f"Cliente {i+1} completou a requisição.")
            except Exception as e:
                print(f"Cliente {i+1} gerou uma exceção: {e}")

if __name__ == '__main__':
    num_clients = 10
    main(num_clients)
