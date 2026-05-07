# Documento de Requisitos e Regras de Negócio

## 1. Introdução
Este documento descreve as funcionalidades e restrições do sistema de gestão para a rede de cinemas, visando centralizar o controle de filmes, sessões e registro de público.

## 2. Requisitos Funcionais (RF)
Os requisitos funcionais descrevem o que o sistema deve fazer.

| ID | Descrição |
|:---|:---|
| **RF01** | O sistema deve permitir o cadastro de filmes (título, duração, gênero, elenco e diretor). |
| **RF02** | O sistema deve permitir o cadastro de unidades de cinema com sua respectiva capacidade. |
| **RF03** | O sistema deve permitir a criação de sessões, vinculando um filme a um cinema e horário. |
| **RF04** | O sistema deve permitir o registro da quantidade de público ao final de cada sessão. |
| **RF05** | O sistema deve fornecer a totalização de público por filme e por cinema. |
| **RF06** | O sistema deve permitir a consulta de informações detalhadas dos filmes (elenco e diretores). |

## 3. Regras de Negócio (RN)
As regras de negócio são as condições e restrições de operação do sistema.

* **RN01 - Intervalo entre Sessões:** Deve haver um intervalo mínimo de 20 minutos entre o fim de uma sessão e o início da próxima na mesma sala.
* **RN02 - Limite de Lotação:** O público registrado em uma sessão não pode ultrapassar a capacidade máxima informada no cadastro do cinema.
* **RN03 - Integridade de Dados:** Não é permitida a exclusão de um filme que possua sessões vinculadas no histórico.
* **RN04 - Unicidade de Sessão:** Não podem existir duas sessões simultâneas no mesmo cinema utilizando o mesmo espaço/sala.

## 4. Requisitos Não Funcionais (RNF)
* **RNF01:** O sistema deve utilizar persistência em banco de dados local (SQLite).
* **RNF02:** A aplicação deve ser estruturada seguindo o padrão de camadas (MVC + Service + Repository).
