""" Tomar los archivos descargados en el modulo ingest_data leyendolos como excel dependiendo su extension (xls o xlsx), eliminando las filas superiores que no tienen
datos, entre el año 1995-2000 los archivos xlsx las tres primeras filas no tienen datos, entre 2000-2015 archivos xlsx las dos primeras filas no tienen datos, entre 2016 y 2017 los archivos xls
as dos primeras filas no tienen datos y entre 2019 y 2021 trae informacion en todas las filas. Se seleccionan las 25 primeras columnas que corresponden a la fecha y a las horas"""

def transform_data():
    
    """Transforme los archivos xls a csv.

    Transforme los archivos data_lake/landing/*.xls a data_lake/raw/*.csv. Hay
    un archivo CSV por cada archivo XLS en la capa landing. Cada archivo CSV
    tiene como columnas la fecha en formato YYYY-MM-DD y las horas H00, ...,
    H23.

    """
    import pandas as pd
    
    for num in range(1995, 2022):        
        if num in range(1995, 2000):
            data_csv = pd.read_excel('data_lake/landing/{}.xlsx'.format(num), header=3)
            data_csv = data_csv.iloc[:, 0:25]
            data_csv.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']       
            data_csv.to_csv('data_lake/raw/{}.csv'.format(num),index=None)
        elif(num in range(2000, 2016)):
            data_csv = pd.read_excel('data_lake/landing/{}.xlsx'.format(num), header=2)
            data_csv = data_csv.iloc[:, 0:25]
            data_csv.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            data_csv.to_csv('data_lake/raw/{}.csv'.format(num),index=None)
        elif(num in range(2016, 2018)):
            data_csv = pd.read_excel('data_lake/landing/{}.xls'.format(num), header=2)
            data_csv = data_csv.iloc[:, 0:25]
            data_csv.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            data_csv.to_csv('data_lake/raw/{}.csv'.format(num), index=None)
        else:
            data_csv = pd.read_excel('data_lake/landing/{}.xlsx'.format(num), header=0)
            data_csv = data_csv.iloc[:, 0:25]
            data_csv.columns = ['Fecha', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10','11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']             
            data_csv.to_csv('data_lake/raw/{}.csv'.format(num), index=None)
    return
    raise NotImplementedError("Implementar esta función")


if __name__ == "__main__":
    import doctest
    transform_data()
    doctest.testmod()
