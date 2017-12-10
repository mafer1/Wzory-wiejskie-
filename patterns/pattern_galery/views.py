from django.http import Http404
from django.shortcuts import render

from patterns.services import patterns_service, config_service, utils_service


def browse_view(request):
    if 'current-page' in request.GET:  # parametr url obecnej srony
        current_page = utils_service.parse_int_or_default(request.GET['current-page'], 0)
    else:
        current_page = 0
    total_pages_count = patterns_service.get_total_pages_count(config_service.PATTERNS_PER_PAGE)

    if current_page > total_pages_count:  # ktos zepsul i wpisal dziwna podstrone
        raise Http404("Nie ma takiej strony!")

    # wzorki na tej podstronie i ich siatka
    patterns_in_current_page = list(patterns_service.get_pattern_page(current_page, config_service.PATTERNS_PER_PAGE))
    patterns_in_current_page_grid = patterns_service.get_pattern_grid(patterns_in_current_page,
                                                                      config_service.PATTERNS_PER_ROW)
    return render(request, "patterns/gallery.html",
                  context={'patterns_grid': patterns_in_current_page_grid,  # to potem leci do szablonu .html
                           'previous_page': current_page,
                           'current_page_human_readable': current_page + 1,
                           'next_page': current_page + 2,
                           'total_pages': total_pages_count})
