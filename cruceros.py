import numpy as np
from Data import cruceros_data
from functions import createData, createListDate, createTextInsert, createDoc


#----------------------------------- Cruceros -----------------------------------------

data_cruceros = createData(cruceros_data.CRUCEROS, 
                  cruceros_data.COMPANIAS, 
                  cruceros_data.PAISES, 
                  np.arange(1800, 2801, 50), 
                  np.arange(2000, 2025), 
                  cruceros_data.CATEGORIAS_CRUCEROS, 
                  extension=50,
                  primary_keys=[0,1])      

sql_text_cruceros = createTextInsert(data_cruceros, 
                                     "CRUCEROS", 
                                     ["NOMBRE", 
                                      "COMPANIA", 
                                      "PAIS_REGISTRO", 
                                      "CAPACIDAD", 
                                      "ANO_CONSTRUCCION", 
                                      "CATEGORIA"])

createDoc("cruceros", sql_text_cruceros)

#-------------------------------- Itinerarios -----------------------------------------

dates_itinerarios = createListDate("2025-01-01", "2026-12-31", 100)

data_itinerarios = createData(cruceros_data.PUERTOS_SALIDA, 
                              dates_itinerarios, 
                              cruceros_data.DESTINOS_CRUCEROS, 
                              np.arange(1, 11), 
                              extension=100,
                              pay_attention=True, 
                              have_present={"cruceros": {
                                  "data_attention": data_cruceros, 
                                  "columns_attention": [0,1], 
                                  "position_data": [0,1]
                              }},
                              primary_keys=[0,1,3])

sql_text_itinerarios = createTextInsert(data_itinerarios,
                                        "ITINERARIOS",
                                        ["NOMBRE_CRUCERO",
                                         "COMPANIA",
                                         "PUERTO_SALIDA",
                                         "FECHA_SALIDA",
                                         "DESTINOS",
                                         "DURACION"])
createDoc("itinerarios", sql_text_itinerarios)

#-------------------------------- Pasajeros -----------------------------------------

passports = [f"P{str(i).zfill(4)}" for i in range(1, 501)]

birthdays = createListDate("1950-01-01", "2024-12-31", 100)

data_pasajeros = createData(passports,
                            cruceros_data.NOMBRES_USUARIOS,
                            cruceros_data.PAISES,
                            birthdays,
                            extension=150,
                            primary_keys=[0])

sql_text_pasajeros = createTextInsert(data_pasajeros,
                                      "PASAJEROS",
                                      ["PASAPORTE",
                                       "NOMBRE_COMPLETO",
                                       "NACIONALIDAD",
                                       "FECHA_NACIMIENTO"])

createDoc("pasajeros", sql_text_pasajeros)

#-------------------------------- Reservas -----------------------------------------

reservations_date = createListDate("2009-01-01", "2025-03-31", 100)

data_reservas = createData(reservations_date,
                           cruceros_data.ESTADOS,
                           extension=200,
                           pay_attention=True,
                           have_present={"pasajeros":{
                                            "data_attention": data_pasajeros, 
                                            "columns_attention":[0], 
                                            "position_data":[0]
                                            },
                                         "itinerarios":{
                                            "data_attention": data_itinerarios, 
                                            "columns_attention":[0,1,3], 
                                            "position_data":[1,2,3]
                                             
                                         }},
                           primary_keys=[0,1,2,3])

sql_text_reservas = createTextInsert(data_reservas,
                                     "RESERVAS",
                                     ["PASAPORTE",
                                      "NOMBRE_CRUCERO",
                                      "COMPANIA",
                                      "FECHA_SALIDA",
                                      "FECHA_RESERVA",
                                      "ESTADO"])

createDoc("reservas", sql_text_reservas)