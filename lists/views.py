from django.shortcuts import redirect, render
from lists.models import Item

def home_page(request):
    return render(request, 'home.html')

def view_list(request, list_id):
    my_list = List.objects.get(id=list_id)
    return render(request, 'list.html', {'list': my_list})

def new_list(request):
    my_list = List.objects.create()
    Item.objects.create(text=request.POST['item_text'], list=my_list)
    return redirect(f'/lists/{my_list.id}/')

def add_item(request, list_id):
    list_ = List.objects.get(id=list_id)
    Item.objects.create(text=request.POST['item_text'], list=list_)
    return redirect(f'/lists/{list_.id}/')

def view_list(request, list_id):
    list_ = List.objects.get(id=list_id)
    error = None

    if request.method == 'POST':
        try:
            item = Item(text=request.POST['item_text'], list=list_)
            item.full_clean()
            item.save()
            return redirect(f'/lists/{list_.id}/')
        except ValidationError:
            error = "You can't have an empty list item"

    return render(request, 'list.html', {'list': list_, 'error': error})