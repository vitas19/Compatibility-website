# views.py
import pandas as pd
from django.shortcuts import render, get_object_or_404
from .models import Medicine
from django.http import JsonResponse
import openpyxl
from openpyxl.styles import Color



def dropdown(request):
    # Read medicine data from Excel file
    medicine_data = pd.read_excel(r'mysite\lista_farmacos.xlsx')
    third_column = medicine_data.iloc[:, 2]
    print(third_column[0],type(third_column[0]))

     # extract values from first column
    medicines = [str(med).strip() for med in medicine_data.iloc[:, 0] if isinstance(med, str)]


    medicines.sort()

    # pass values to template context
    context = {'medicines': medicines}

    # Render the template with the medicine data
    return render(request, 'video.html', context)


def medicine_results(request):
    name = request.GET.get('medicine')
    #print(name)
    medicine_name = name.lstrip()
    medicine_name = medicine_name.rstrip()
    #print(name)
    #print(medicine_name)

    #print(Medicine.objects.all())
    if len(Medicine.objects.all()) == 0:
        # assume the Excel file has columns 
        medicine_data = pd.read_excel(r'mysite\lista_farmacos.xlsx')
        print("ENTRA")
        # iterate over rows in the DataFrame and create Medicine objects
        for _, row in medicine_data.iterrows():
            medicine = Medicine(
                name= row[0].strip().replace("\n",""),
                donation = row[1],
                days = row[2],
                observations= row[3],
                bibliography= row[4])
            
            medicine.save()

    # Perform a query to get the matching medicine object
    d_styles = {
        "Aceptar": {"st1": "background-color:green !important",
                    "st2": "background-color: #ACE4AA !important"},
        "Rechazar": {"st1": "background-color: #C00000 !important",
                    "st2": "background-color: #eb5e5e8a !important"},
        "Aceptar pero con precaución (ver observaciones)": {"st1": "background-color:orange !important",
                    "st2": "background-color:#ffbe5d !important"},
        "Depende (ver observaciones)": {"st1": "background-color:orange !important",
                    "st2": "background-color:#ffbe5d !important"},
        "Aceptar, excepto si es para plasmaferesis, esperar 2 días": {"st1": "background-color:orange !important",
                    "st2": "background-color:#ffbe5d !important"},
        "Si, con condiciones (ver observaciones)": {"st1": "background-color:orange !important",
                    "st2": "background-color:#ffbe5d !important"},
        "Si, con restricciones (ver observaciones)": {"st1": "background-color:orange !important",
                    "st2": "background-color:#ffbe5d !important"},
        "CONSULTE CON SU MÉDICO": {"st1": "background-color:orange !important",
                    "st2": "background-color:#ffbe5d !important"}
    }
    try:
        print(medicine_name)
        results = Medicine.objects.filter(name = medicine_name.strip())[0]
        b = results.bibliography
        b = results.bibliography[results.bibliography.find("http"):]
        b = b.split(",")
        new_list = []
        for e in b:
            s_2 = e.split(" ")
            for e2 in s_2:
                if "http" in e2:
                    new_list.append(e2)
        
            
    except Medicine.DoesNotExist:
        results = None

    #print(results)

    # Pass the results to the template
    context = {'result': results, "bibliography": new_list, "style_server": d_styles[results.donation.strip()]}

    return render(request, 'medicine_results.html', context)

