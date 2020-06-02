def abrr_number(number, decimals=0):

    scales = {
        pow(10, 24): "Y",  # Septillón / Cuatrillón
        pow(10, 21): "Z",  # Se10tillón / Mil trillones
        pow(10, 18): "E",  # Quintillón / Trillón
        pow(10, 15): "P",  # Cuatrillón / Mil billones
        pow(10, 12): "T",  # Trillón / Billón
        pow(10, 9): "G",  # Billón / Millardo
        pow(10, 6): "M",  # Millón
        pow(10, 3): "k",  # Mil / Millar
        pow(10, 2): "h",  # Cien / Centena
        pow(10, 1): "da",  # Diez / Decena
    }

    if not number in range(min(scales), max(scales)):
        return f"{number}"

    for digit, symbol in scales.items():
        minimum = int("9" * str(digit).count("0"))
        maximum = int(str(minimum) + "999")

        if number in range(minimum, maximum):
            return f"{number / digit:.{decimals}f} {symbol}"
abrr_number(1000000)
abrr_number(10000)

