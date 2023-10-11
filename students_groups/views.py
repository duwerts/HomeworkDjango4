from django.shortcuts import render, redirect
from .models import Group
from .forms import GroupForm


def add_student_to_group(request, group_id):
    group = Group.objects.get(pk=group_id)

    if request.method == 'POST':
        form = GroupForm(request.POST, instance=group)
        if form.is_valid():
            form.save()
            return redirect('group_list')

    form = GroupForm(instance=group)
    return render(request, 'students/add_student_to_group.html', {'form': form, 'group': group})