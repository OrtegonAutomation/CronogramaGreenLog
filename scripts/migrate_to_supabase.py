import json
import requests

# Datos de Supabase (Públicos proporcionados por el usuario)
SUPABASE_URL = "https://rmfpwdmxnffurnxkevvi.supabase.co"
SUPABASE_KEY = "sb_publishable_H3VjmfuU9ht15xxrvBJsVQ_OQqQQLrN"

def migrate_data():
    # Cargar datos locales
    try:
        with open('data/cronograma_data.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        print("Error: cronograma_data.json no encontrado.")
        return

    config = data.get("config", {})
    actividades = data.get("actividades", [])

    headers = {
        "apikey": SUPABASE_KEY,
        "Authorization": f"Bearer {SUPABASE_KEY}",
        "Content-Type": "application/json",
        "Prefer": "resolution=merge-duplicates"
    }

    # 1. Migrar Config
    print("Migrando Configuración...")
    # Buscamos si ya existe el ID 1 o insertamos
    res_cfg = requests.post(
        f"{SUPABASE_URL}/rest/v1/config",
        headers=headers,
        json={
            "id": 1,
            "fecha_inicio": config.get("fecha_inicio"),
            "cliente": config.get("cliente"),
            "proyecto": config.get("proyecto")
        }
    )
    if res_cfg.status_code in [200, 201, 204]:
        print("[OK] Configuración migrada.")
    else:
        print(f"[ERROR] Config: {res_cfg.text}")

    # 2. Migrar Actividades
    print(f"Migrando {len(actividades)} actividades...")
    
    # Preparar datos para Supabase
    bulk_data = []
    for i, act in enumerate(actividades):
        bulk_data.append({
            "id": act["id"],
            "fase": act.get("fase"),
            "actividad": act["actividad"],
            "tipo": act["tipo"],
            "semana_inicio": act.get("semana_inicio"),
            "duracion": act.get("duracion"),
            "responsable": act.get("responsable"),
            "porcentaje": act.get("porcentaje", 0),
            "estado": act.get("estado", "Pendiente"),
            "color": act.get("color"),
            "orden": i + 1
        })

    # Insertar en bloques (Supabase REST API permite bulk insert)
    res_acts = requests.post(
        f"{SUPABASE_URL}/rest/v1/actividades",
        headers=headers,
        json=bulk_data
    )

    if res_acts.status_code in [200, 201, 204]:
        print(f"[OK] {len(actividades)} actividades migradas exitosamente.")
    else:
        print(f"[ERROR] Actividades: {res_acts.text}")

if __name__ == "__main__":
    migrate_data()
