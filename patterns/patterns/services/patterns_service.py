import math

from pattern_galery.models import PatternEntry


def get_pattern_page(page_number, patterns_per_page):  # paginacja rekordow wzorow
    patterns_begin_index = page_number * patterns_per_page
    patterns_page = PatternEntry.objects.all().order_by('added_date')[
                    patterns_begin_index:patterns_begin_index + patterns_per_page]
    return patterns_page


def get_pattern_grid(patterns_list, patterns_per_row):  # zwrot listy list tak jak na stronie
    result = []
    current_row = []

    for pattern in patterns_list:
        current_row.append(pattern)
        if len(current_row) >= patterns_per_row:
            result.append(current_row.copy())
            current_row.clear()
    if current_row:
        result.append(current_row.copy())
    return result


def get_total_pages_count(patterns_per_page):  # calkowita liczba podstron
    pages_count = math.ceil(PatternEntry.objects.count() / patterns_per_page)
    return pages_count
