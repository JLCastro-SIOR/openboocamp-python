import time

hora_sistema = time.localtime()
hora = hora_sistema.tm_hour
hora_mexico = hora - 6

if hora_mexico >= 19:
  print("Es hora de ir a casa")
else:
  horas_faltan = 19 - hora_mexico
  print("Faltan " + str(horas_faltan)+" horas para ir a casa.")