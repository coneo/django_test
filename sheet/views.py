# Create your views here.

from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import NameForm

from django_tables2 import SingleTableView
from .tables import PersonTable

def get_name(request):
    # 如果form通过POST方法发送数据
    if request.method == 'POST':
        # 接受request.POST参数构造form类的实例
        form = NameForm(request.POST)
        #table = PersonTable([{"age": 31, "name": "aaa"}, {"age": 34, "name": "bbb"}])
        table = PersonTable([{"age": request.POST['data_head'], "name": request.POST['data_content']}
            , {"age": 34, "name": "bbb"}
            , {"age": 34, "name": "bbb"}
            , {"age": 34, "name": "bbb"}
            , {"age": 34, "name": "bbb"}
            , {"age": 34, "name": "bbb"}
            ])
        # print(request.POST)
        # 验证数据是否合法
        # if form.is_valid():

    # 如果是通过GET方法请求数据，返回一个空的表单
    else:
        form = NameForm()
        table = PersonTable([])

    return render(request, 'name.html', {'form': form, 'table': table})
