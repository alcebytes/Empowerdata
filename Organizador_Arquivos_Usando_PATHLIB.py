import random
from pathlib import Path


#Gera vários arquivos temporários e diferentes extensões.
extensoes = ['.jpg', '.jpeg', '.png', '.wepb', '.gif', '.docx', '.xlsx', '.pptx',
             '.pdf', '.rar', '.zip', '.mp4', '.mp3', '.py', '.ipynb', '.txt']  # 16 tipos de arquivos


# Caminho do diretório
dir_ = Path(r'.\desktop\my_downloads')


#Verificando a existência de um diretório
if dir_.is_dir():
    print('\nPasta já existe', dir_)
else:
    #Criando um novo diretório
    dir_.mkdir()
    print(f'\nDiretório "{dir_}" criado com sucesso..!')


# Gerando arquivos temporarios
print('\nGerando arquivos testes..!\n')
for n in random.sample(range(1,101), 7):
    for ext in extensoes:
        Path(dir_/f"file_0{n}{ext}").touch()
print('Arquivos testes criados com sucesso..!\n')


# Listando arquivos dentro de um diretório:
print('listando arquivos da pasta"', dir_, '":\n')
extensoes_encontradas = set()
for file_ in dir_.glob('*.*'): #glob mostra apenas os arquivos do diretório
    print(file_.name, end=', ')
    ext_file =  file_.name.partition('.')[2]
    extensoes_encontradas.add(ext_file) # adicionando extensões num set()

r = input('\n\nDeseja organizar todos seus arquivos [ s/n ], pressione <enter> para continuar.')

# Criando novos diretórios
print('\n\nOrganizando arquivos, criando novos diretórios por extensão..!\n')
for extensao in extensoes_encontradas:
    if Path(dir_/extensao).exists():
        pass
    else:
        Path(dir_/extensao).mkdir()


# movendo arquivos para suas respectivas pastas
for file_ in dir_.glob('*.*'): #rglob mostra tanto arquivos como sub-diretório
    pasta_destino = file_.name.rsplit('.')[1]  # novo caminho da pasta
    de = file_
    para = Path.joinpath(dir_, pasta_destino, file_.name)
    Path( de ).replace( para )

#rename  - move arquivos, é não substitui arquivos existente
#replace - move arquivos, é substitui arquivos existente
    
print("\nDE....: PASTA ATUAL\n  >>>", str(dir_).upper())
print("\nPARA..: NOVAS PASTAS\n  >>>", str(extensoes_encontradas).upper())

print("\n\nArquivos Organizados com sucesso..!\n\n")
