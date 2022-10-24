from ejemplo.models import Familiar

Familiar(nombre="Pedro", direccion="Libertad 1856", numero_pasaporte=124512).save()
Familiar(nombre="Emiliano", direccion="21 de Septiembre 908", numero_pasaporte=458697).save()
Familiar(nombre="Ximena", direccion="Pedro Berro 578", numero_pasaporte=197346).save()
Familiar(nombre="Marcela", direccion="18 de Julio 1542", numero_pasaporte=341645).save()

print("Se cargo con éxito los usuarios de pruebas")
