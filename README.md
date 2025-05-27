# Desafio-Bandeiras-de-Cartão

Este é um programa em Python que valida números de cartões de crédito usando o algoritmo de Luhn e identifica a bandeira do cartão com base em seu número.

Funcionalidades
Validação de números de cartão de crédito usando o algoritmo de Luhn

Identificação automática da bandeira do cartão

Suporte para as seguintes bandeiras:

Visa (16 dígitos)

Mastercard (12 dígitos)

American Express (12 dígitos)

Diners Club (12 dígitos)

Discover (12 dígitos)

JCB (12 dígitos)

Voyager (12 dígitos)

Hipercard (12 dígitos)

Aura (12 dígitos)

Algoritmo de Luhn
O validador implementa o algoritmo de Luhn (também conhecido como "módulo 10"), que é o método padrão para validação de números de cartão de crédito:

Os dígitos são processados da direita para a esquerda

Dígitos em posições pares são multiplicados por 2

Se o resultado for maior que 9, soma-se os dígitos

A soma total deve ser divisível por 10 para ser válido

Padrões de identificação de bandeiras
Cada bandeira tem um padrão específico de identificação baseado nos primeiros dígitos:

Bandeira	Dígitos	Padrão de início
Visa	16	4
Mastercard	12	51-55 ou 2221-2720
American Express	12	34 ou 37
Diners Club	12	300-305, 36 ou 38
Discover	12	6011, 644-649 ou 65
JCB	12	3528-3589
Voyager	12	8699
Hipercard	12	384100, 606282 ou 637095
Aura	12	50
Observações
Este programa é apenas para fins educacionais

Não armazenamos nenhum dado do cartão

A validação pelo algoritmo de Luhn não significa que o cartão existe ou está ativo
