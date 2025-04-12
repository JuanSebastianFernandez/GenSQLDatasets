import numpy as np
import random
import unicodedata
import os

random.seed(42)

def createListDate(start_date: str, finish_date: str, n: int = 10):

    start = np.datetime64(start_date)
    finish = np.datetime64(finish_date)
    
    days_range = (finish - start).astype(int)

    random_days = [random.randint(0, days_range) for _ in range(n)]
    dates = [str(start + np.timedelta64(days, 'D')) for days in random_days]
    
    return dates

def createData(*all_list, extension: int = 50, pay_attention: bool = False, 
               have_present: dict = {}, primary_keys: list = []):
    
    data = set()
    primary_key_set = set()  # Para rastrear las claves primarias únicas
    attention_dict = {}
    
    if pay_attention:
        for key, value in have_present.items():
            att_list = []

            for this_data in value["data_attention"]:
                selected_values = [this_data[column] for column in value["columns_attention"]]
                att_list.append(tuple(selected_values)) 
                
            attention_dict[key] = att_list
            
    while len(data) < extension:
        
        register = [random.choice(onde_list) for onde_list in all_list]
        
        if pay_attention:
            for key, list_values in attention_dict.items():
                random_list = random.choice(list_values)

                for position, value in zip(have_present[key]["position_data"], random_list):
                    register.insert(position, value)

        # Extraer la combinación de clave primaria
        primary_key_values = tuple(register[i] for i in primary_keys)

        # Si la clave primaria ya existe, no se agrega el registro
        if primary_key_values not in primary_key_set:
            data.add(tuple(register))
            primary_key_set.add(primary_key_values)  # Agregar clave primaria al set

    return sorted(data)

def createTextInsert(data:list, name_database:str, features:list[str]):
    sql_text = "INSERT ALL\n"

    for values in data:
        formatted_values = []
        
        for value in values:
            if isinstance(value, str):
                if len(value) == 10 and value[4] == '-' and value[7] == '-':
                    formatted_values.append(f"TO_DATE('{value}', 'YYYY-MM-DD')")
                else:
                    formatted_values.append(f"'{value}'")
            else:
                formatted_values.append(str(value))
        
        sql_text += f"    INTO {name_database} ({', '.join(features)}) VALUES ({', '.join(formatted_values)})\n"

    sql_text += "SELECT * FROM DUAL;\n"
    
    return sql_text

def createDoc(document_name: str, sql_text: str):
    folder_name = "data_generated"
    
    # Asegurar que la carpeta existe
    os.makedirs(folder_name, exist_ok=True)
    
    # Crear la ruta completa del archivo
    file_path = os.path.join(folder_name, f"{document_name}.txt")
    
    # Guardar el archivo en la carpeta especificada
    with open(file_path, "w", encoding="utf-8") as file:
        file.write(sql_text)
        print(f"Los datos han sido guardados en {file_path}")


def quite_tildes(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )