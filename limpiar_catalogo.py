import csv

input_file = 'extra-addons/mi_modulo_test/data/catalogo.csv'
output_file = 'extra-addons/mi_modulo_test/data/catalogo_limpio.csv'

# Mapeo: Nombre en Square -> Nombre técnico en Odoo
mapeo = {
    'Nombre del artículo': 'name',
    'Descripción': 'description_sale',
    'Precio': 'list_price',
    'SKU': 'default_code'
}

with open(input_file, mode='r', encoding='utf-8') as infile:
    reader = csv.DictReader(infile)
    
    with open(output_file, mode='w', encoding='utf-8', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=mapeo.values())
        writer.writeheader()
        
        for row in reader:
            # Creamos una nueva fila con solo los datos que queremos
            new_row = {mapeo[key]: row[key] for key in mapeo if key in row}
            
            # Limpieza básica de precio (quitar símbolos de moneda si los hay)
            if 'list_price' in new_row:
                new_row['list_price'] = new_row['list_price'].replace('$', '').replace(',', '').strip()
            
            writer.writerow(new_row)

print(f"✅ ¡Hecho! Catálogo limpio guardado en {output_file}")

