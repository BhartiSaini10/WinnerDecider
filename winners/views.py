import csv
import random

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from django.http import HttpResponse


class WinnerDecider():
    '''
        This class is used to take comma separated names as an input in an input box and select 5 random winners
        from them and export the result in a csv.
    '''

    @classmethod
    def write_csv(cls, winners: list):
        with open("/tmp/winners.csv", 'w', newline='') as csv_file:
            writer = csv.writer(csv_file)
            writer.writerow(["Winners"])
            for winner in winners:
                writer.writerow([winner])

    @classmethod
    def select_winners(cls, names_str=""):
        if not names_str:
            names_str = input("Enter the name")
        names = names_str.split(',')
        if len(names) < 5:
            return "Please enter at least 5 names."
        winners = random.sample(names, 5)
        cls.write_csv(winners)


class GetTopFiveWinners(APIView):
    def get(self, request):
        '''
            This is used to take comma separated names as an input in an input box
        '''
        return render(request, 'select_winners.html')

    def post(self, request):
        '''
            This is used to select 5 random winners from the input names and export the result in a csv
        '''
        names_str = request.data.get('names', "")
        if not names_str:
            return Response(data="No names entered. Please try again.", status=status.HTTP_400_BAD_REQUEST)
        result = WinnerDecider.select_winners(names_str)
        if isinstance(result, str):
            return Response(data=result, status=status.HTTP_400_BAD_REQUEST)
        winners_file = open("/tmp/winners.csv", "r")
        response = HttpResponse(winners_file, content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename={}'.format("winners.csv")
        return response
