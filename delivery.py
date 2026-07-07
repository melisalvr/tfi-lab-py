total_pedido = 0.0
cant_pedidos_dia = 0
recaudacion_diaria = 0.0


def mostrar_menu():
    """Muestra las opciones del sistema por pantalla."""
    print("--------------------------------")
    print("      SISTEMA DE PEDIDOS        ")
    print("--------------------------------")
    print("1. Agregar producto al pedido")
    print("2. Cobrar pedido actual")
    print("3. Ver estadísticas del día")
    print("4. Salir")
    print("--------------------------------")


def agregar_al_pedido():
    """Muestra categorías, luego productos (8 por categoría), pide cantidad y suma al carrito."""
    global total_pedido

    # 1. Menú principal de categorías
    print("\n--- Categorías ---")
    print("1. Comidas")
    print("2. Bebidas")
    print("3. Postres")
    categoria = input("Elija una categoría (1-3): ")

    precio_item = 0.0

    # 2. Condicionales anidados según la categoría
    if categoria == "1":
        print("\n--- Comidas ---")
        print("1. Hamburguesa completa - $5000")
        print("2. Pizza especial - $7000")
        print("3. Lomo completo - $8500")
        print("4. Docena de empanadas - $6000")
        print("5. Milanesa con papas fritas - $6500")
        print("6. Sandwich de bondiola - $7500")
        print("7. Tarta de jamón y queso - $4000")
        print("8. Ensalada César - $4500")
        prod = input("Elija el producto (1-8): ")

        if prod == "1":
            precio_item = 5000.0
        elif prod == "2":
            precio_item = 7000.0
        elif prod == "3":
            precio_item = 8500.0
        elif prod == "4":
            precio_item = 6000.0
        elif prod == "5":
            precio_item = 6500.0
        elif prod == "6":
            precio_item = 7500.0
        elif prod == "7":
            precio_item = 4000.0
        elif prod == "8":
            precio_item = 4500.0
        else:
            print("Error: Producto no válido.")

    elif categoria == "2":
        print("\n--- Bebidas ---")
        print("1. Gaseosa 1L - $2000")
        print("2. Agua mineral 1L - $1500")
        print("3. Cerveza artesanal 1L - $3500")
        print("4. Limonada natural - $1800")
        print("5. Agua saborizada 1.5L - $2200")
        print("6. Gaseosa 500ml - $1200")
        print("7. Vino tinto de la casa - $4000")
        print("8. Jugo de naranja exprimido - $1600")
        prod = input("Elija el producto (1-8): ")

        if prod == "1":
            precio_item = 2000.0
        elif prod == "2":
            precio_item = 1500.0
        elif prod == "3":
            precio_item = 3500.0
        elif prod == "4":
            precio_item = 1800.0
        elif prod == "5":
            precio_item = 2200.0
        elif prod == "6":
            precio_item = 1200.0
        elif prod == "7":
            precio_item = 4000.0
        elif prod == "8":
            precio_item = 1600.0
        else:
            print("Error: Producto no válido.")

    elif categoria == "3":
        print("\n--- Postres ---")
        print("1. Helado 1/4 kg - $3000")
        print("2. Flan mixto - $2500")
        print("3. Porción de Chocotorta - $3500")
        print("4. Tiramisú - $3200")
        print("5. Brownie con helado - $3800")
        print("6. Ensalada de frutas - $2000")
        print("7. Cheesecake de frutos rojos - $4000")
        print("8. Volcán de chocolate - $4500")
        prod = input("Elija el producto (1-8): ")

        if prod == "1":
            precio_item = 3000.0
        elif prod == "2":
            precio_item = 2500.0
        elif prod == "3":
            precio_item = 3500.0
        elif prod == "4":
            precio_item = 3200.0
        elif prod == "5":
            precio_item = 3800.0
        elif prod == "6":
            precio_item = 2000.0
        elif prod == "7":
            precio_item = 4000.0
        elif prod == "8":
            precio_item = 4500.0
        else:
            print("Error: Producto no válido.")

    else:
        print("Error: Categoría no válida.")

    # 3. Lógica de Cantidad y Subtotales
    if precio_item > 0:
        cantidad_str = input("Ingrese la cantidad que desea: ")

        if cantidad_str.isdigit() and int(cantidad_str) > 0:
            cantidad = int(cantidad_str)
            subtotal = precio_item * cantidad

            total_pedido = total_pedido + subtotal

            print(
                f"\n¡Se agregaron {cantidad} unidad(es)! Subtotal del ítem: ${subtotal}"
            )
            print(f"Total parcial del pedido: ${total_pedido}")
        else:
            print(
                "\nError: La cantidad no es válida. Debe ingresar un número entero positivo."
            )


def cobrar_pedido():
    """Cobra el pedido, aplica descuentos/recargos, actualiza estadísticas y reinicia el carrito."""
    global total_pedido
    global cant_pedidos_dia
    global recaudacion_diaria

    if total_pedido == 0:
        print(
            "\nError: No hay productos en el pedido actual. Agregue productos primero."
        )
    else:
        print("\n--- Medios de Pago ---")
        print("1. Efectivo (10% de descuento)")
        print("2. Tarjeta (10% de recargo)")
        metodo = input("Elija el medio de pago (1-2): ")

        if metodo == "1":
            descuento = total_pedido * 0.10
            total_final = total_pedido - descuento
            print(f"\nDescuento aplicado: -${descuento}")
        elif metodo == "2":
            recargo = total_pedido * 0.10
            total_final = total_pedido + recargo
            print(f"\nRecargo aplicado: +${recargo}")
        else:
            total_final = total_pedido
            print("\nMedio de pago no reconocido. Se cobrará el precio de lista.")

        print("--------------------------------")
        print(f"Total a pagar: ${total_final}")
        print("¡Gracias por su compra!")
        print("--------------------------------")

        cant_pedidos_dia = cant_pedidos_dia + 1
        recaudacion_diaria = recaudacion_diaria + total_final

        total_pedido = 0.0


def mostrar_estadisticas():
    """Muestra la cantidad de pedidos y la recaudación total del día."""
    print("--------------------------------")
    print("      ESTADÍSTICAS DEL DÍA      ")
    print("--------------------------------")
    print(f"Pedidos completados: {cant_pedidos_dia}")
    print(f"Dinero recaudado: ${recaudacion_diaria}")
    print("--------------------------------")

    input("Presione Enter para continuar...")


def main():
    """Motor principal del sistema."""
    while True:
        mostrar_menu()
        opcion = input("Elija una opción (1-4): ")

        if opcion == "1":
            agregar_al_pedido()
        elif opcion == "2":
            cobrar_pedido()
        elif opcion == "3":
            mostrar_estadisticas()
        elif opcion == "4":
            print("\nCerrando el sistema. ¡Hasta luego!")
            break
        else:
            print("\nError: Opción no válida. Ingrese un número del 1 al 4.")


main()
