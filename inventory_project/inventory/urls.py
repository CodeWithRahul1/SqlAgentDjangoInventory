from django.urls import path
from .views import query_sql_agent, chatbot_page  # Import chatbot_page

urlpatterns = [
    path("query/", query_sql_agent, name="query_sql_agent"),  # API for chatbot queries
    path("chatbot/", chatbot_page, name="chatbot_page"),  # Chatbot UI page
]
