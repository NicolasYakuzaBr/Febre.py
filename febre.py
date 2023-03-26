while True:

    print('\nVocê está com febre?')
    temp = float(input('informe sua temperatura: '))
    
    if temp >= 36.2 and temp <= 37.2:
        print('\nNormal')
    elif temp > 37.2 and temp <= 37.9:
        print('\nAumento ligeiro de temperatura!')
    elif temp > 37.9 and temp <= 38.4:
        print('\nFebre')
    elif temp > 38.4:
        print('\nVocê está com febre alta!! Corra imediatamente para um hospital próximo!')
    elif temp <= 35 and temp >= 1:
        print('\nHipotermia')
    if temp <= 0:
        print('Programa Finalizado!')
        break
    
