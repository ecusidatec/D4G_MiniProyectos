import unittest
from CalculadoraCuotas.calculadora_cuotas import calcular_cuota_mensual

class TestCalculos(unittest.TestCase):

    def test_calcular_cuota_mensual_12_meses(self):
        # Caso de prueba 12 meses
        monto = 11000  
        plazo = 12  # en meses
        aporte_inicial = None 
        tasa_interes_anual = 16 

        cuota_esperada = 888.26
        costo_adm_esperado = 8.26
        cuota_balon = 1.47

        cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto,
                                                                                             plazo,
                                                                                             aporte_inicial=aporte_inicial, 
                                                                                             tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=6)
        self.assertAlmostEqual(costo_adm_calculado, costo_adm_esperado, places=6)
        self.assertAlmostEqual(cuota_balon_calculado, cuota_balon, places=6)

    def test_calcular_cuota_mensual_24_meses(self):
        # Caso de prueba 24  meses
        monto = 11000  
        plazo = 24  # en meses
        aporte_inicial = None 
        tasa_interes_anual = 16 

        cuota_esperada = 479.35
        costo_adm_esperado = 8.26
        cuota_balon = 1.47

        cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto,
                                                                                             plazo,
                                                                                             aporte_inicial=aporte_inicial, 
                                                                                             tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=6)
        self.assertAlmostEqual(costo_adm_calculado, costo_adm_esperado, places=6)
        self.assertAlmostEqual(cuota_balon_calculado, cuota_balon, places=6)

                # Caso de prueba 24  meses
        monto = 30000  
        plazo = 24  # en meses
        aporte_inicial = None 
        tasa_interes_anual = 16 

        cuota_esperada = 1307.32
        costo_adm_esperado = 22.53
        cuota_balon = 4

        cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto,
                                                                                             plazo,
                                                                                             aporte_inicial=aporte_inicial, 
                                                                                             tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_calculada, cuota_esperada, places=6)
        self.assertAlmostEqual(costo_adm_calculado, costo_adm_esperado, places=6)
        self.assertAlmostEqual(cuota_balon_calculado, cuota_balon, places=6)


    def test_calcular_cuota_mensual_48_meses(self):
        # Caso de prueba 48 meses
        monto = 11000  
        plazo = 48  # en meses
        aporte_inicial = None 
        tasa_interes_anual = 16 

        cuota_total_esperada = 287.18

        cuota_calculada, costo_adm_calculado, cuota_balon_calculado = calcular_cuota_mensual(monto,
                                                                                             plazo,
                                                                                             aporte_inicial=aporte_inicial, 
                                                                                             tasa_interes_anual=tasa_interes_anual)

        self.assertAlmostEqual(cuota_calculada+costo_adm_calculado+cuota_balon_calculado, cuota_total_esperada, places=6)

if __name__ == '__main__':
    unittest.main()
