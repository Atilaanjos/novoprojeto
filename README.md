# Projeto AI-Driven Software Engineering

Aluno: Átila dos Anjos Paulo

## Objetivo do Projeto

Este projeto foi desenvolvido com o objetivo de demonstrar como ferramentas de Inteligência Artificial podem auxiliar no desenvolvimento de software,
aumentando a produtividade da equipe, melhorando a qualidade do código e automatizando processos de teste.

O projeto consiste em um sistema simples de loja desenvolvido em Python, capaz de calcular descontos e juros de acordo com a forma de pagamento 
escolhida pelo cliente.



## Análise do Problema

A empresa do cenário proposto enfrentava dificuldades para equilibrar velocidade de desenvolvimento e qualidade do software.
Quando a equipe acelerava a entrega de funcionalidades, a quantidade de bugs aumentava. Quando priorizava testes e revisões, os prazos deixavam de ser 
cumpridos.

Os principais problemas identificados foram:

* Desenvolvimento lento devido à escrita manual de código repetitivo.
* Baixa cobertura de testes automatizados.
* Descoberta tardia de erros durante QA ou em produção.
* Falta de padronização nas implementações dos desenvolvedores.



## Uso da Inteligência Artificial

Durante o desenvolvimento foi utilizado o GitHub Copilot como assistente de programação.

Inicialmente o sistema possuía apenas a seleção de produtos. Utilizando um prompt em linguagem natural, foi solicitado ao Copilot que adicionasse uma 
regra de desconto de 10% para pagamentos realizados em dinheiro ou PIX e que solicitasse a forma de pagamento antes da finalização da compra.

Posteriormente, o código foi reorganizado em funções para melhorar a manutenção e permitir a criação de testes automatizados.

O uso do Copilot acelerou o desenvolvimento, reduziu o tempo gasto com tarefas repetitivas e auxiliou na organização do código.



## Testes Automatizados

Foram desenvolvidos testes automatizados para validar as principais regras de negócio do sistema:

* Desconto de 10% para pagamento em dinheiro.
* Desconto de 10% para pagamento via PIX.
* Pagamento em cartão sem juros até 10 parcelas.
* Pagamento em cartão com juros acima de 10 parcelas.
* Tratamento de métodos de pagamento inválidos.

Os testes ajudam a garantir que futuras alterações não quebrem funcionalidades já implementadas.



## Automação com GitHub Actions

Foi configurado um workflow utilizando GitHub Actions para executar automaticamente os testes sempre que uma alteração é enviada ao repositório.

Essa automação proporciona:

* Feedback rápido sobre erros.
* Maior confiabilidade nas entregas.
* Redução de falhas em produção.
* Maior produtividade da equipe.



## Caso Real

Diversas empresas utilizam ferramentas de IA para acelerar o desenvolvimento de software. Um exemplo é o próprio GitHub, 
que divulgou estudos mostrando que desenvolvedores utilizando GitHub Copilot conseguem concluir tarefas de programação mais rapidamente 
quando comparados a equipes sem assistência de IA.

Além disso, empresas de tecnologia utilizam GitHub Actions para automatizar testes, integração contínua (CI) e validações antes da publicação de novas 
versões dos sistemas.



## Tecnologias Utilizadas

* Python
* Git
* GitHub
* GitHub Copilot
* GitHub Actions
* unittest



## Conclusão

O projeto demonstrou como a combinação entre Inteligência Artificial e automação pode contribuir para um fluxo de desenvolvimento mais eficiente.
O uso do GitHub Copilot auxiliou na implementação das funcionalidades e dos testes, enquanto o GitHub Actions garantiu a execução automática das validações, 
aumentando a qualidade e a confiabilidade do software.
