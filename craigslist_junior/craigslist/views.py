from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Item
from .forms import CategoryForm, ItemForm

# Create your views here.

def category_list(request):
    categories = Category.objects.all()
    return render(request, 'craigslist/category_list.html', {'categories': categories})

def category_items(request, category_id):
    category = Category.objects.get(id=category_id)
    items = category.items.all()
    return render(request, 'craigslist/category_items.html', {'category': category, 'items': items})

def item_detail(request, category_id, item_id):
    category = Category.objects.get(id=category_id)
    item = Item.objects.get(id=item_id)
    return render(request, 'craigslist/item_detail.html', {'category': category, 'item': item, 'type_of_request': 'detail'})

def new_category(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_items', category.id)
    else:
        form = CategoryForm()
    return render(request, 'new_category.html', {'form': form, 'action': 'Add', 'type_of_request': 'New-Cat'})

def new_item(request, category_id):
    category = Category.objects.get(id=category_id)
    form = ItemForm(initial={"category": category})
    
    if request.method == "POST":
        form = ItemForm(request.POST, initial={"category": category})
        try:
            if form.is_valid():
                item = form.save(commit=False)
                item.save()
                return redirect('item_detail',category. id, item.id)
        except:
            return HttpResponse("You've enteredinvalid item details, please try again!") 

    return render(request, 'new_item.html', {'form': form, 'category': category, 'action': 'Add', 'type_of_request': 'New-Item'})

def edit_category(request, category_id):
    category = Category.objects.get(id=category_id)
    if request.method == "POST":
        form = CategoryForm(request.POST, instance=category)
        if form.is_valid():
            category = form.save(commit=False)
            category.save()
            return redirect('category_items', category.id)
    else:
        form = CategoryForm(instance=category)
    return render(request, 'new_category.html', {'form': form, 'action': 'Update', 'type_of_request': 'New-Cat'})

def edit_item(request, category_id, item_id):
    category = Category.objects.get(id=category_id)
    item = Item.objects.get(id=item_id)
    
    if request.method == "POST":
        form = ItemForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save(commit=False)
            item.save()
            return redirect('item_detail', category_id=category.id, item_id=item.id)
    else:
        form = ItemForm(instance=item)

    return render(request, 'new_item.html', {'form': form, 'category': category, 'action': 'Update', 'type_of_request': 'Update-Item'})

def delete_category(request, category_id):
    category = Category.objects.get(id=category_id)
    category.delete()
    return redirect('category_list')

def delete_item(request, category_id, item_id):
    category = Category.objects.get(id=category_id)
    item = Item.objects.get(id=item_id)
    item.delete()
    return redirect('category_items', category.id)