from .models import Mineral
from .forms import SearchForm


def get_first_letters(request):
    all_first_letters = []
    names = Mineral.objects.values('name')
    for mineral in names:
        if mineral['name'][0] not in all_first_letters:
            all_first_letters.append(mineral['name'][0])
    return {'letters': all_first_letters}


def get_groups(request):
    group_list = []
    groups = Mineral.objects.order_by().values('group').distinct()
    for group in groups:
        group_list.append(group['group'])
    group_list.sort()
    return {'group_list': group_list}


def search_form(request):
    form = SearchForm()
    return {'form': form}
