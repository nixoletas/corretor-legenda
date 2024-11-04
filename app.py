def corrigir_acentuacao(legenda):

    # Caracteres incorretos a serem corrigidos
    correcoes = {
        "Ã©": "é",
        "Ãº": "ú",
        "Ã¢": "â",
        "Ãª": "ê",
        "Ã³": "ó",
        "Ã§": "ç",
        "Ã£": "ã",
        "Ã´": "ô",
        "nhÃ£":"nhã",
        "quÃª":"quê",
        "Ã§":"ç",
        "Ãµ": "õ",
        "Ã­": "í",
        "Ã¡": "á",
        "Ã‡": "Ç",
        "Ã‰": "É",
        "ÃŠ": "Ê",
        "Ã”": "Ô"
    }
    
    # Aplicar correções para cada erro
    for erro, correcao in correcoes.items():
        legenda = legenda.replace(erro, correcao)
    
    return legenda

# Ler o conteúdo do arquivo legenda.srt, corrigir e salvar em legenda_corrigida.srt
def processar_arquivo_srt(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as file:
        legenda = file.read()
    
    legenda_corrigida = corrigir_acentuacao(legenda)
    
    with open(output_file, 'w', encoding='utf-8') as file:
        file.write(legenda_corrigida)
    
    print(f"Arquivo corrigido salvo como {output_file}")

# Executar a função de processamento
processar_arquivo_srt('legenda.srt', 'legenda_corrigida.srt')
