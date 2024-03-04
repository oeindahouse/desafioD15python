def emc(**masas):

    """
    _Funcion Einstein E=mc*2_
    funcion que calcula el valor de la energia en base a la masa y la constante vel luz
    params: {kwargs} : (masa1 = valor, masa2 = valor)

    :return: _resultado valor de energia como lista de diccionario_
    :rtype: _float_
    """

    c= 300000
    resultado = [{k:v, 'energia':v*c**2} for k, v in masas.items()]
    return resultado

print(emc(masa1=1000, masa2= 2000, masa3= 3000))


# def osea(elevar,base):
#     """
#     osea _summary_

#     _extended_summary_

#     :param elevar: _description_
#     :type elevar: _type_
#     :param base: _description_
#     :type base: _type_
#     """
#     pass 