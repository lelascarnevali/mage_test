import io
import pandas as pd
import requests

@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://api.openbrewerydb.org/v1/breweries'
    per_page = 200  # Número de resultados por página
    page = 1  # Número da página inicial
    df_list = []  # Lista para armazenar os DataFrames de cada página

    while True:
        # Construir a URL com o parâmetro da página atual
        page_url = f'{url}?per_page={per_page}&page={page}'

        # Fazer a requisição para a página atual
        response = requests.get(page_url)

        # Verificar se a requisição foi bem-sucedida
        if response.status_code == 200:
            # Ler os dados JSON em um DataFrame
            df = pd.read_json(io.StringIO(response.text))

            # Adicionar o DataFrame à lista
            df_list.append(df)

            # Verificar se há mais páginas a serem carregadas
            if len(df) < per_page:
                break  # Saír do loop se não houver mais páginas
            else:
                page += 1  # Incrementar o número da página
        else:
            print(f'Error: Failed to retrieve data from page {page}')
            break

    # Concatenar todos os DataFrames da lista em um único DataFrame
    df_all = pd.concat(df_list, ignore_index=True)

    return df_all


