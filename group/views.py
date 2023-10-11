from django.shortcuts import render, redirect
from .models import Teacher
from .forms import TeacherForm


def teacher_list(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers/teacher_list.html', {'teachers': teachers})


def teacher_detail(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    return render(request, 'teachers/teacher_detail.html', {'teacher': teacher})


def teacher_create(request):
    if request.method == 'POST':
        form = TeacherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm()
    return render(request, 'teachers/teacher_form.html', {'form': form})


def teacher_update(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        form = TeacherForm(request.POST, instance=teacher)
        if form.is_valid():
            form.save()
            return redirect('teacher_list')
    else:
        form = TeacherForm(instance=teacher)
    return render(request, 'teachers/teacher_form.html', {'form': form, 'teacher': teacher})


def teacher_delete(request, pk):
    teacher = Teacher.objects.get(pk=pk)
    if request.method == 'POST':
        teacher.delete()
        return redirect('teacher_list')
    return render(request, 'teachers/teacher_confirm_delete.html', {'teacher': teacher})

