# jezeli value da sie sparsowac do liczby calkowitej to ja zwroc jesli nie to zwroc domyslna wartosc
def parse_int_or_default(value, default_value):
    try:
        result = int(value)
    except ValueError:
        result = default_value
    return result
