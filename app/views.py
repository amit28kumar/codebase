from django.shortcuts import render_to_response, RequestContext
from .models import Item
from rest_framework.views import APIView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
import ast
from rest_framework import status
from rest_framework.response import Response
from datetime import datetime, date


class AppView(APIView):

    @method_decorator(login_required)
    def get(self, request, format=None):
        try:
            due_date = self.request.GET.get('date', None)
            month_data = self.request.GET.get('month', None)
            week_date = self.request.GET.get('week', None)
            if due_date:
                tasks = Item.objects.filter(due_date=datetime.strptime(str(due_date),"%Y-%m-%d"))
            elif month_data:
                time_list = month_data.split('-')
                year = datetime.strptime(str(time_list[0]), "%Y").year
                month = datetime.strptime(str(time_list[1]), "%m").month
                tasks = Item.objects.filter(due_date__year=year,
                                            due_date__month=month)
            elif week_date:
                week_list = week_date.split('-')
                week = str(week_list[1])[1:]
                year = datetime.strptime(str(week_list[0]), "%Y").year
                tasks = []
                for task in Item.objects.all():
                    if int(task.due_date.isocalendar()[1]) == int(week):
                        tasks.append(task)
            else:
                tasks = Item.objects.all()
            todo_listing = []
            for task in tasks:
                todo_dict = {}
                todo_dict['id'] = task.id
                todo_dict['title'] = task.title
                todo_dict['priority'] = task.priority
                todo_dict['due_date'] = task.due_date
                todo_dict['state'] = task.state
                if task.due_date.date() < date.today() and task.state in [1,2]:
                    todo_dict['color'] = True
                else:
                    todo_dict['color'] = False
                todo_listing.append(todo_dict)
            return render_to_response('status_report.html',
                                      { 'todo_listing':todo_listing ,
                                        'count':tasks.count, 'user':
                                            request.user},
                                      context_instance=RequestContext(request))
        except Exception as exp:
            import traceback
            traceback.print_exc()
            return Response({'message': exp.message},
                            status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, format=None):
        try:
            data = request.data
            params = {'title':data.get('title'),
                      'due_date': data.get('due_date'),
                      'priority': data.get('priority'),
                      'state': data.get('state')}
            obj, created = Item.objects.update_or_create(**params)
            return Response(status=status.HTTP_200_OK)

        except Exception as exp:
            import traceback
            traceback.print_exc()
            return Response({'message': exp.message},
                            status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, pk=None):
        try:
            parameter = request.body
            if '=' in parameter:
               parameter = parameter.split('=')
               if parameter[0] == "state":
                   task = Item.objects.filter(id=pk).update(state=parameter[1])
               else:
                   task = Item.objects.filter(id=pk).update(priority=parameter[1])
            else:
                raise Exception("Invalid Updation")
            return Response(status=status.HTTP_200_OK)
        except Exception as exp:
            import traceback
            traceback.print_exc()
            return Response({'message': exp.message},
                            status=status.HTTP_400_BAD_REQUEST)



