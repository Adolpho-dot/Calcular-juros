print("Bem-vindos a loja do Adolpho Evaristo Corrêa Neto")
valorDoPedido = float(input("Entre com o valor do pedido: "))
quantidadeParcelas = int(input("Entre com a quantidade de parcelas: "))

#Verifica a quantidade de parcelas e define a taxa de juros correspondente
if quantidadeParcelas < 4:
    juros = 0.0
elif 4 <= quantidadeParcelas < 6:
    juros = 0.04
elif 6 <= quantidadeParcelas < 9:
    juros = 0.08
elif 9 <= quantidadeParcelas < 13:
    juros = 0.16
else:
    juros = 0.32
    
#Calcula o valor da parcela e o valor total do parcelado
valorDaParcela = (valorDoPedido * (1 + juros)) / quantidadeParcelas
valorTotalParcelado = valorDaParcela * quantidadeParcelas

#Exibe os resultados da parcela e o valor total utilizando duas casas decimais após a virgula
print(f"O valor das parcelas é de: R$ {valorDaParcela:.2f}")
print(f"O valor Total Parcelado é de: R$ {valorTotalParcelado:.2f}")
