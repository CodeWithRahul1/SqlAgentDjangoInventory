# from .sql_agent import process_query  # Correct import

# from rest_framework.decorators import api_view
# from rest_framework.response import Response

# @api_view(["POST"])
# def query_sql_agent(request):
#     """
#     Accepts a user query and returns only the response from SQL Agent.
#     """
#     user_query = request.data.get("query", "")

#     if not user_query:
#         return Response({"error": "Query parameter is missing"}, status=400)

#     response = process_query(user_query)

#     return Response(response)

from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .sql_agent import agent_executor

def chatbot_page(request):
    return render(request, "chatbot.html")  # Add "inventory/" to template path

@csrf_exempt
def query_sql_agent(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            query = data.get("query", "")
            response = agent_executor.run(query)
            return JsonResponse({"response": response})
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)

    return JsonResponse({"error": "Invalid request"}, status=400)
