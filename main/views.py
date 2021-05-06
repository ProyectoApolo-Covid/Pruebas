from django.shortcuts import render
from pathlib import Path
import numpy as np
import requests
import pandas
import datetime

def home(request):
    return render(request, 'index.html')
# Create your views here.
