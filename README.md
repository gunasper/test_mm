# MaxMilhas - Teste desenvolvedor Python

Este teste tem como objetivo demonstrar habilidades do candidato com Python3, desenvolvimento de APIS RESTful, boas práticas de desenvolvimento, conhecimentos em banco de dados, etc.
Para simplificar processos de instalação e deploy, foi criado um makefile contendo os comandos que devem ser utilizados para criação do ambiente de desenvolvimento e/ou produção.

Este arquivo README está separado em 4 sessões, a saber: Decisões de Projeto, Dependências, Makefile, TODO.

## Decisões de Projeto
Embora a descrição da vaga sugira que a MaxMilhas use Django como principal framework, este é um framework síncrono. Para torná-lo assíncrono, pode-se usar a biblioteca Celery para tarefas assíncronas. Entretanto, existe um web framework Python nativamente assíncrono chamado Tornado http://www.tornadoweb.org/en/stable/. O Tornado foi desenvolvido para contornar o problema C10k https://en.wikipedia.org/wiki/C10k_problem, que envolve lidar e escalonar 10 mil conexões simultâneas. Embora 10 mil conexões não seja o mesmo que 10 mil requisições por segundo, comparado ao Django, o Tornado consegue lidar muito mais rapidamente com entrega de conteúdo, principalmente para requisições RESTful envolvendo IO. O seguinte comparativo corrobora as informações acima: http://klen.github.io/py-frameworks-bench/.

O ponto negativo de usar-se o Tornado ao invés do Django é a falta de um ORM nativo e a gerência de bancos de dados provida pelo Django. Porém, para este projeto, isso pode ser considerado como uma coisa boa, pois permite demonstrar conhecimento em SQL e bancos de dados, tanto do ponto de vista de web services quanto de infraestrutura.

O banco de dados escolhido, para fins de demonstração, foi o MySQL. Porém, para projetos maiores que visem escalabilidade deve-se pensar em utilizar bancos de dados NoSQL (como o AWS DynamoDB ou Apache Cassandra ou MongoDB). AWS Aurora ou PostgreSQL podem ser alternativas, caso queiramos manter uma estrutura SQL. Pensando numa arquitetura de micro-serviços, o banco de dados NÃO vem configurado junto à aplicação. Optei por subir, em minha conta AWS, uma instância configurada com o MySQL. Embora isso não seja a prática ideal, servirá para demonstrar o conceito.

Devido ao prazo ser critério de exclusão, não está sendo entregue uma interface de comunicação com a API. A ideia inicial era utilizar algum template HTML seguindo o Material Design. Foi inicializado o desenvolvimento, mas como o projeto estava longe de se tornar funcional, o código HTML/JavaScript/CSS não está anexado nesse projeto. Entretanto, segue, junto ao projeto, o projeto da view para comunicação com a API.

#### Estrutura do Projeto
O projeto está estruturado em 4 pastas principais: conf, docs, max_milhas, scripts. Cada pasta possui um README apropriado explicando suas funcionalidades.

> A pasta max_milhas contém o projeto em si e é dividida em 5 subpastas: 
* commons
* handlers
* models
* views
* tests. 

app.py contém a aplicação a ser executada. routes.py contém as rotas disponíveis em nossa API. 

#### Tratamento de Erro:
Em commons/erros.py é possível encontrar os erros que a aplicação está preparada para lidar. Cada erro possui um código interno, uma mensagem padronziada e o status code a ser retornado. Um handler será capaz de entender a classe de erro e disponibilizar ao cliente informações sobre como tratá-lo.

#### Rotas disponíveis:
Uma vez que essa é uma demonstração, a API encontra-se em versão 0. Assim, todas as rotas devem ser prececidas do parâmetro v0.

v0/status: entrega informações do servidor;
v0/cpfs: CRUD do CPFs;
v0/cpfs/{cpf_number}: informações sobre um determinado CPF.

#### Testes automatizados:
Novamente, devido ao prazo, não foi criada uma rotina de testes automatizados. Porém, usando a biblioteca nosetests do Python é fácil integrar os testes no Tornado.

#### Log
Ao ser inicializado, um arquivo chamado max.log é criado no diretório raiz, contendo o Log da aplicação.

#### Docker
Para gerar imagem e container, respectivamente, deve-se usar os seguintes comandos:

`sudo docker build --rm -t mmimage . --build-arg build=123`

`sudo docker rm -f mmcontainer; sudo docker run -e LANG=C.UTF-8 -p 5000:5000 --name="mmcontainer" -d mmimage;`

## Dependências
O projeto foi implementado e testado utilizando Python 3.5.3. Para assegurar máxima compatibilidade, sugere-se fortemente o uso de um virtualenv para executar o projeto e suas dependências.

Para instalar o Python3.5.3 deve-se:
```
cd /tmp && wget https://www.python.org/ftp/python/3.5.3/Python-3.5.3.tar.xz && tar xvf Python-3.5.3.tar.xz && cd Python-3.5.3
./configure
make -j4
sudo make altinstall
```
Dependências do Python3.5 estão listadas no arquivo "requirements" e podem ser instaladas usando o `python3.5 -m pip install -r requirements` ou o Makefile, como explicado abaixo.

## Makefile:

#### make deps
Instala todas as dependências listadas no arquivo requirements para execução do projeto. Note que, idealmente, esse comando deve ser executado dentro do ambiente virtual para evitar problemas de versionamento em outros projetos.

#### make run
Inicializa nossa aplicação e a coloca para escutar a porta 5000 do localhost.

#### make tests
Executa testes automatizados.

#### make docker
Cria um container Docker para disponibilizar a aplicação.

#### make clear
Removes .pyc cache files.

## TODO
* Instruções de como criar um virtualenv;
* Caso seja de interesse, seria possível disponibilizar este log externamente no futuro;
* Aumentar cobertura de testes;
* Pensar e decidir qual melhor banco de dados a ser usado em nossos sistema e como/onde disponibilizá-lo.
* Implementação de segurança da API: autenticação usando JWT e SSL.
* Váriáveis de ambiente: a fim de simplificar o desenvolvimento, informações de login no banco de dados encontram-se HARDCODED. Devemos alterar isso para variáveis de ambientes e/ou separa ambientes dev/produção.

## Read the docs
Tornado Stable Version:
http://www.tornadoweb.org/en/stable/
