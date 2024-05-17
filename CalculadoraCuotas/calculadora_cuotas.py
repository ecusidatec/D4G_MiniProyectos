import numpy_financial as npf

def calcular_cuota_mensual(monto, plazo, tasa_interes_anual=16, cuota_balon_porcentaje=1, \
                           aporte_inicial=None, aporte_inicial_porcentaje=10, \
                            seguro_porcentaje=0.75):
    if aporte_inicial is None:
        aporte_inicial = monto*(aporte_inicial_porcentaje/100)

    cuota_balon = (monto*(cuota_balon_porcentaje/100))
    # Monto del préstamo después del aporte inicial
    monto_prestamo = monto - aporte_inicial - cuota_balon 
    
    # Convertir tasa anual a mensual y de porcentaje a decimal
    tasa_interes_mensual = (tasa_interes_anual) / 12 / 100  
    tasa_seguro_anual = seguro_porcentaje*0.87/0.84*(1+(tasa_interes_anual/100))

    # Calcular la cuota mensual
    if tasa_interes_mensual > 0:
        cuota_mensual = npf.pmt(tasa_interes_mensual, plazo, -monto_prestamo)
    else:
        # Si la tasa de interés es 0%, la fórmula del pago mensual es simplemente el préstamo dividido entre el número de meses
        cuota_mensual = monto_prestamo / plazo

    return round(cuota_mensual, 2), \
        round((monto*(tasa_seguro_anual/100)/12), 2), \
        round((tasa_interes_mensual*cuota_balon),2)
