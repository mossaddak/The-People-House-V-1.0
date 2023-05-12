from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from .serializer import(
    NewsLetterSerializer
)
from .models import(
     ElectionStart
)
from datetime import datetime
import calendar


# Create your views here.
class NewsLetterView(APIView):
    
    def post(self, request):
        data = request.data
        serializer = NewsLetterSerializer(data=data)
        if not serializer.is_valid():
            return Response(
                    {
                        'message':"something Went Wrong",
                        'data':serializer.errors
                    },status = status.HTTP_400_BAD_REQUEST
                )
        else:
            serializer.save()
            return Response(
                {
                    'data':serializer.data,
                    'message':"Thank you for contact us."
                }
            )
        

class ElectionStartView(APIView):
    def get(self, request):
        election_start = ElectionStart.objects.last().date
        datetime_str = election_start.strftime("%Y-%m-%d %H:%M:%S")
        datetime_obj = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")

        year, week_num, weekday = datetime_obj.isocalendar()
        response = {
            'full_date': datetime_obj,
            'year': year,
            'month': datetime_obj.month,
            'week': week_num,
            # 'weekday': weekday,
            # 'minute': datetime_obj.minute,
            # 'second': datetime_obj.second

        }
        return Response(response) 