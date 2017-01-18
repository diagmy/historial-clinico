from .models import Item

def del_tasks(request, deleted_items):
    # Delete selected items
    for item_id in deleted_items:
        i = Item.objects.get(id=item_id)
        messages.success(request, "Item \"{i}\" deleted.".format(i=i.title))
        i.delete()