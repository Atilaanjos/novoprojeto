import unittest

from projetoia import calcular_valor_final


class TestCalcularValorFinal(unittest.TestCase):
    def test_desconto_pix_10_porcento(self):
        preco = 100.0
        pagamento = "Pix"
        parcelas = 1
        desconto = 0.10

        valor_final, desconto_aplicado, juros_aplicado = calcular_valor_final(
            preco, pagamento, parcelas, desconto
        )

        self.assertAlmostEqual(valor_final, 90.0, places=2)
        self.assertEqual(desconto_aplicado, 0.10)
        self.assertEqual(juros_aplicado, 0.0)

    def test_desconto_dinheiro_10_porcento(self):
        preco = 200.0
        pagamento = "Dinheiro"
        parcelas = 1
        desconto = 0.10

        valor_final, desconto_aplicado, juros_aplicado = calcular_valor_final(
            preco, pagamento, parcelas, desconto
        )

        self.assertAlmostEqual(valor_final, 180.0, places=2)
        self.assertEqual(desconto_aplicado, 0.10)
        self.assertEqual(juros_aplicado, 0.0)

    def test_cartao_sem_juros_ate_10_parcelas(self):
        preco = 150.0
        pagamento = "Cartão"
        parcelas = 10
        desconto = 0.0

        valor_final, desconto_aplicado, juros_aplicado = calcular_valor_final(
            preco, pagamento, parcelas, desconto
        )

        self.assertAlmostEqual(valor_final, 150.0, places=2)
        self.assertEqual(desconto_aplicado, 0.0)
        self.assertEqual(juros_aplicado, 0.0)

    def test_cartao_com_juros_acima_de_10_parcelas(self):
        preco = 150.0
        pagamento = "Cartão"
        parcelas = 12
        desconto = 0.0

        valor_final, desconto_aplicado, juros_aplicado = calcular_valor_final(
            preco, pagamento, parcelas, desconto
        )

        self.assertAlmostEqual(valor_final, 153.0, places=2)
        self.assertEqual(desconto_aplicado, 0.0)
        self.assertEqual(juros_aplicado, 0.02)


if __name__ == "__main__":
    unittest.main()
