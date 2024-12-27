# Sistema de Recomendación de Productos

Este sistema es una solución para recomendar productos personalizados a los usuarios según su historial de compras y preferencias. Incluye una API REST para gestionar productos y usuarios, generar recomendaciones, y manejar la autenticación.

## Características

- Gestión de productos (crear, consultar, actualizar, eliminar).
- Gestión de usuarios (crear, consultar, actualizar, eliminar).
- Recomendaciones basadas en preferencias e historial.
- Filtro por precio y categoría en las recomendaciones.
- Simulación de autenticación con JWT.
- Documentación interactiva con Swagger.

## Requisitos

- Python 3.8 o superior.
- Pip (para instalar dependencias).

## Instalación

1. Clona el repositorio:
   ```bash
   git clone <URL_DEL_REPOSITORIO>
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd sistema_recomendacion
   ```
3. Crea un entorno virtual y actívalo:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows: venv\Scripts\activate
   ```
4. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

## Ejecución

1. Inicia el servidor:
   ```bash
   uvicorn main:app --reload
   ```
2. Accede a la API en tu navegador:
   - Documentación interactiva: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Documentación alternativa: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

## Uso

### Crear un Usuario
Método: POST  
URL: `/users/`  
Body:
```json
{
    "id": 1,
    "name": "Juan Perez",
    "email": "juan.perez@example.com",
    "preferences": ["Electronics"]
}
```

### Crear un Producto
Método: POST  
URL: `/products/`  
Body:
```json
{
    "id": 1,
    "name": "Laptop",
    "description": "Portátil de alta gama",
    "category": "Electronics",
    "price": 1500.00,
    "stock": 5
}
```

### Actualizar un Producto
Método: PUT  
URL: `/products/{product_id}`  
Body:
```json
{
    "name": "Laptop Pro",
    "description": "Portátil mejorado",
    "category": "Electronics",
    "price": 2000.00,
    "stock": 3
}
```

### Eliminar un Producto
Método: DELETE  
URL: `/products/{product_id}`

### Actualizar un Usuario
Método: PUT  
URL: `/users/{user_id}`  
Body:
```json
{
    "name": "Juan Actualizado",
    "email": "juan.actualizado@example.com",
    "preferences": ["Books"]
}
```

### Eliminar un Usuario
Método: DELETE  
URL: `/users/{user_id}`

### Obtener Recomendaciones
Método: GET  
URL: `/recommendations/{user_id}?max_price=2000`  

## Casos de Prueba

- **Usuario sin historial:** Se recomiendan los productos más populares.
- **Usuario con preferencias:** Se recomiendan productos de las categorías favoritas.
- **Filtros:** Funciona el filtrado por precio y categoría.

## Estructura del Proyecto

- `main.py`: Punto de entrada principal.
- `api/`: Módulos de la API para usuarios, productos y recomendaciones.
  - `products.py`: Gestión de productos.
  - `users.py`: Gestión de usuarios.
  - `recommendations.py`: Algoritmo y recomendaciones.
  - `auth.py`: Simulación de autenticación.
- `models.py`: Modelos de datos para usuarios y productos.
- `requirements.txt`: Lista de dependencias.

## Mejoras Futuras

- Integrar una base de datos relacional como PostgreSQL.
- Implementar autenticación JWT real.
- Añadir sistema de feedback para las recomendaciones.
