# Ejercicio 8: Escribir un programa que almacene la cadena de caracterres "contraseña" en una
# variable, pregunte al usuario por la contraseña e imprima por pantalla si la contraseña introducida
# por el usuario coincide con la guardada en la variable sin tener en cuenta mayusculas y minusculas

print("\n\t.:VALIDACIÓN DE CONTRASEÑA:.")
contraseña = "contraseña"
contra = input("Ingrese la contraseña: ")
if contra.upper() == contraseña.upper():
    print("La contraseña es correcta\n")
else: 
    print("La contraseña es incorrecta\n")