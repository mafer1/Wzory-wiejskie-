from django.shortcuts import render


def browse_view(request):
    return render(request, "patterns/gallery.html")
