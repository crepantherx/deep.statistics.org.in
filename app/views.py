from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect, JsonResponse, HttpResponseNotFound, HttpResponseServerError
from django.conf import settings
from django.views.decorators.csrf import ensure_csrf_cookie, csrf_exempt
from django.views.decorators.http import require_http_methods
from django.middleware.csrf import get_token
from .forms import RegistrationForm, LoginForm

import logging
import json
import csv
import os

logger = logging.getLogger(__name__)

def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # Log the user in after registration
            login(request, user)
            messages.success(request, 'Registration successful!')
            return redirect('home')
    else:
        form = RegistrationForm()
    return render(request, 'app/register.html', {'form': form})

from django.http import HttpResponseRedirect
from django.conf import settings

import logging

logger = logging.getLogger(__name__)

def login_view(request):
    try:
        if request.method == 'POST':
            form = LoginForm(data=request.POST)
            if form.is_valid():
                user = form.get_user()
                login(request, user)
                request.session.save()
                messages.success(request, 'Logged in successfully!')
                
                frontend_url = settings.FRONTEND_URL
                logger.info(f"Redirecting to frontend: {frontend_url}")
                return HttpResponseRedirect(frontend_url)
            else:
                messages.error(request, 'Invalid username or password.')
                logger.warning("Invalid login attempt")
        else:
            form = LoginForm()
        return render(request, 'app/login.html', {'form': form})
    except Exception as e:
        logger.error(f"Error in login_view: {str(e)}")
        messages.error(request, 'An error occurred during login.')
        return render(request, 'app/login.html', {'form': LoginForm()})

@require_http_methods(['POST'])
def logout_view(request):
    try:
        logout(request)
        request.session.flush()
        messages.success(request, 'Logged out successfully!')
        
        login_url = settings.LOGIN_URL
        logger.info(f"Redirecting to login: {login_url}")
        return HttpResponseRedirect(login_url)
    except Exception as e:
        logger.error(f"Error in logout_view: {str(e)}")
        return JsonResponse({'error': 'Internal server error'}, status=500)

def profile_view(request):
    return render(request, 'app/profile.html')

def home(request):
    return render(request, 'app/home.html')

def about(request):
    return render(request, 'app/about.html')

def services(request):
    return render(request, 'app/services.html')

def careers(request):
    return render(request, 'app/careers.html')

def legal(request):
    return render(request, 'app/legal.html')

import os
from django.conf import settings

def demo(request):
    csv_path = os.path.join(settings.BASE_DIR, 'static', 'temperature_data.csv')

    # Process the CSV into a list of yearly temperature arrays
    temperature_data = []
    current_year = None
    year_data = []

    with open(csv_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            year = int(row['Year'])
            anomaly = float(row['Anomaly'])
            if current_year != year:
                if year_data:
                    temperature_data.append(year_data)
                year_data = []
                current_year = year
            year_data.append(anomaly)
        if year_data:  # Append the last year
            temperature_data.append(year_data)

    # Pass the data to the template
    context = {
        'temperature_data': temperature_data,
        'start_year': 1850  # Adjust based on your data
    }
    return render(request, 'app/demo.html', context)

def pricing(request):
    return render(request, 'app/pricing.html')

import json
import csv

from django.http import HttpResponseNotFound, HttpResponseServerError

def custom_404_view(request, exception):
    return HttpResponseNotFound('<h1>404 - Page Not Found</h1><p>The page you requested does not exist.</p>')

def custom_500_view(request):
    return HttpResponseServerError('<h1>500 - Server Error</h1><p>An error occurred on the server. Please try again later.</p>')


# def chart(request):
#     csv_path = '/Users/crepantherx/PycharmProjects/testing.statistics.org.in/static/temperature_data.csv'
#
#     # Process the CSV into a list of yearly temperature arrays
#     temperature_data = []
#     current_year = None
#     year_data = []
#
#     with open(csv_path, 'r') as file:
#         reader = csv.DictReader(file)
#         for row in reader:
#             year = int(row['Year'])
#             anomaly = float(row['Anomaly'])
#             if current_year != year:
#                 if year_data:
#                     temperature_data.append(year_data)
#                 year_data = []
#                 current_year = year
#             year_data.append(anomaly)
#         if year_data:  # Append the last year
#             temperature_data.append(year_data)
#
#     # Pass the data to the template
#     context = {
#         'temperature_data': temperature_data,
#         'start_year': 1850  # Adjust based on your data
#     }
#     return render(request, 'app/chart.html', context)


# from .utils.chart_generator import generate_charts

import csv
from django.shortcuts import render
from django.contrib import messages
from .forms import CSVUploadForm

#
# def upload_csv_view(request):
#     if request.method == 'POST':
#         form = CSVUploadForm(request.POST, request.FILES)
#         if form.is_valid():
#             try:
#                 csv_file = request.FILES['csv_file']
#                 decoded_file = csv_file.read().decode('utf-8').splitlines()
#                 reader = csv.reader(decoded_file)
#
#                 headers = next(reader, None)  # Read the header row
#                 if not headers:
#                     messages.error(request, "CSV file is empty or missing headers.")
#                     return render(request, 'app/upload_csv.html', {'form': form})
#
#                 data = list(reader)  # Read the rest of the file
#                 if not data:
#                     messages.error(request, "CSV file contains no data.")
#                     return render(request, 'app/upload_csv.html', {'form': form})
#
#                 # Identify numerical and categorical columns
#                 numerical_columns = []
#                 categorical_columns = []
#                 for i, col in enumerate(zip(*data)):
#                     try:
#                         [float(value) for value in col]  # Attempt to convert all values to float
#                         numerical_columns.append(headers[i])
#                     except ValueError:
#                         categorical_columns.append(headers[i])
#
#                 charts = generate_charts(data, headers)
#
#                 return render(request, 'app/upload_csv.html', {
#                     'form': form,
#                     'numerical_columns': charts['numerical_columns'],
#                     'categorical_columns': charts['categorical_columns'],
#                     'any_columns': charts['any_columns']
#                 })
#             except Exception as e:
#                 messages.error(request, f"Error: {str(e)}")
#                 return render(request, 'app/upload_csv.html', {'form': form})
#     else:
#         form = CSVUploadForm()
#     return render(request, 'app/upload_csv.html', {'form': form})

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import ensure_csrf_cookie
from django.middleware.csrf import get_token
from django.views.decorators.http import require_http_methods

@ensure_csrf_cookie
@csrf_exempt
@require_http_methods(['GET'])
def auth_check(request):
    try:
        logger.info("Auth check request received")
        logger.info(f"Session ID: {request.session.session_key}")
        logger.info(f"Is authenticated: {request.user.is_authenticated}")
        
        if request.user.is_authenticated:
            logger.info(f"User authenticated: {request.user.username}")
            return JsonResponse({
                'user': {
                    'username': request.user.username,
                    'email': request.user.email
                }
            })
        else:
            logger.warning("User not authenticated")
            return JsonResponse({'error': 'Unauthorized'}, status=401)
    except Exception as e:
        logger.error(f"Error in auth_check: {str(e)}")
        return JsonResponse({'error': 'Internal server error'}, status=500)

@require_http_methods(['POST'])
def logout_view(request):
    logout(request)
    request.session.flush()  # Clear the session completely
    messages.success(request, 'Logged out successfully!')
    if settings.DEBUG:
        return HttpResponseRedirect('http://localhost:5173/login')
    return HttpResponseRedirect('https://deep.statistics.org.in/login/')