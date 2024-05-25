import math
from datetime import datetime,timedelta


#################################### Variable configurables ########################################################################

IPC_3 = 3533.2 # IPC Diciembre
IPC_2 = 4261.5 # IPC Enero

RIPTE_3 = 55356.61 # Ripte Diciembre
RIPTE_2 = 63468.76	 # Ripte Enero

Dias_mes = 31 # Marzo

Primer_dia_ejemplo = "03/04/2024"

ICL_0 = 9.308

Cantidad_dias_a_imprimir = 20
####################################################################################################################################
####################################################################################################################################
####################################################################################################################################

def get_date_object(date_string):
  """
  This function parses a date string in the format MM/DD/YYYY and returns a datetime object.
  """
  try:
    # "%m/%d/%Y" specifies the format (month/day/year)
    date_object = datetime.strptime(date_string, "%m/%d/%Y")
    return date_object.date()  # Return only the date part
  except ValueError:
    print("Invalid date format. Please use MM/DD/YYYY.")
    return None


Factor_actualización_base = (0.5*(IPC_2/IPC_3)+0.5*(RIPTE_2/RIPTE_3))
Factor_actualización = math.pow(Factor_actualización_base, (1/Dias_mes))


print("Factor de actualización: ", Factor_actualización)

print("Valor inicial, correspondiente al día ", Primer_dia_ejemplo, ":", ICL_0)

print("Imprimiendo sucesión de valores:")

date_object = get_date_object(Primer_dia_ejemplo)

print("Primer día: ", ICL_0)

ICLt = ICL_0 # Primera iteración
new_day=date_object

for dias in range(Cantidad_dias_a_imprimir):
    ICLt = ICLt*Factor_actualización
    new_day = new_day+ timedelta(days=1)
    print("Dia: ", new_day, ": ", ICLt)