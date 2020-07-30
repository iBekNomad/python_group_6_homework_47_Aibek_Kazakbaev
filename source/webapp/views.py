from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseNotAllowed
from django.utils.timezone import make_naive

from webapp.models import QuickMemo
from .forms import MemoForm


def index_view(request):
    data = QuickMemo.objects.all()
    return render(request, 'index.html', context={
        'memos': data
    })


def memo_view(request, pk):
    memo = get_object_or_404(QuickMemo, pk=pk)
    context = {'memo': memo}
    return render(request, 'memo_view.html', context)


def memo_create_view(request):
    if request.method == "GET":
        form = MemoForm()
        return render(request, 'memo_create.html', context={
            'form': form
        })
    elif request.method == 'POST':
        form = MemoForm(data=request.POST)
        if form.is_valid():
            memo = QuickMemo.objects.create(
                description=form.cleaned_data['description'],
                text=form.cleaned_data['text'],
                status=form.cleaned_data['status'],
                execution_date=form.cleaned_data['execution_date']
            )
            return redirect('memo_view', pk=memo.pk)
        else:
            return render(request, 'memo_create.html', context={'form': form})
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def memo_update_view(request, pk):
    memo = get_object_or_404(QuickMemo, pk=pk)
    if request.method == "GET":
        form = MemoForm(initial={
            'description': memo.description,
            'text': memo.text,
            'status': memo.status,
            'execution_date': memo.execution_date
        })
        return render(request, 'memo_update.html', context={
            'form': form,
            'memo': memo
        })
    elif request.method == 'POST':
        form = MemoForm(data=request.POST)
        if form.is_valid():
            memo.description = form.cleaned_data['description']
            memo.text = form.cleaned_data['text']
            memo.status = form.cleaned_data['status']
            memo.execution_date = form.cleaned_data['execution_date']
            memo.save()
            return redirect('memo_view', pk=memo.pk)
        else:
            return render(request, 'memo_update.html', context={
                'memo': memo,
                'form': form
            })
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])


def memo_delete_view(request, pk):
    memo = get_object_or_404(QuickMemo, pk=pk)
    if request.method == 'GET':
        return render(request, 'memo_delete.html', context={'memo': memo})
    elif request.method == 'POST':
        memo.delete()
        return redirect('index')
    else:
        return HttpResponseNotAllowed(permitted_methods=['GET', 'POST'])
