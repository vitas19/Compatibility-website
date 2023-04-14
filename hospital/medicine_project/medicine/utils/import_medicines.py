import pandas as pd
from models import Medicine

# assume the Excel file has columns 'name', 'description', and 'price'
df = pd.read_excel('mysite\prueba.xlsx')

# iterate over rows in the DataFrame and create Medicine objects
for _, row in df.iterrows():
    medicines = Medicine(
        medicine=row[0],
        name=row[1],
        group=row[2],
        recomendation=row[3],
        code=row[4],
        observations=row[5],
        bibliography=row[6]
    )
    medicines.save()


medicines = Medicine.objects.all()
print(medicines)