# Desafio DIO - Sistema Bancário em Python

## Repositório: desafio-sysbank-python

Desafio proposto para o Bootcamp **NTT DATA - Engenharia de Dados com Python**


###Objetivo
	Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato

###Requisitos
	1-) Operação de depósito:
	    Deve ser possível depositar valores positivos para a minha conta bancária. A v1 do projeto trabalha apenas com 1 usuário, dessa forma não precisamos nos preocupar em identificar qual é o número da agência e conta bancária. Todos os depósitos devem ser armazenados em uma variável e exibidos na operação de extrato.

	2-) Operação de saque:
	    O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possivel sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

	3-) Operação de extrato:
	    Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: __Não foram realizadas movimentações.__
	    Os valores devem ser exibidos utilizando o formato __R$ XXX.XX__ (Exemplo: 1500.45 => R$ 1500.45)
	    