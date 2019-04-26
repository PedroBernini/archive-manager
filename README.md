# Archive Manager
Programa arquivador, ou seja, um gerenciador de archives.

## Descrição do Software
O software é um "arquivo de arquivos", ou seja, é um arquivo que contém uma coleção de outros
arquivos em uma estrutura que torna possível recuperar individualmente cada arquivo nele
armazenado. Um arquivador (archiver) é um programa que permite criar e modificar archives, bem
como extrair arquivos de um archive.

Foi desenvolvido na linguagem de programação Python e é funcional no terminal do Linux. Veja abaixo os comandos reservados para cada caso de uso:
- Comando "-c" está reservado para a criação de um novo archive;
- Comando "-i" está reservado para a inserção de um arquivo dentro de um archive;
- Comando "-l" está reservado para listar os arquivos contidos dentro de um archive;
- Comando "-e" está reservado para a extração de um arquivo contido em um archive;
- Comando "-r" está reservado para a remoção de um arquivo contido em um archive.

## Instruções para compilar/executar
A pasta projeto contém o arquivo archive.py. Mova-se até esta pasta via terminal Linux e
insira o seguinte comando :
**$ python3 archive.py \<comando> \<archive.arq> \<arq1> \<arq2> ...**

Onde:
- \<comando> representa um dos 5 comandos reservados para cada caso de uso;
- \<archive.arq> representa o nome do arquivador e sua extensão;
- \<arq1> \<arq2> ... representa um conjunto de arquivos que irão fazer parte do caso de
uso.

Observação:
- Os arquivos passados por parâmetros também devem ter extensão, e devem ser
colocados dentro do diretório do projeto antes de sua execução.

## Desenvolvedores
- [Brenda Alexsandra](https://github.com/brendajanuario)
- [Felipe Marchi](https://github.com/felipemarchi)
- [Pedro Bernini](https://github.com/PedroBernini)
