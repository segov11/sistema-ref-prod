from fastapi import FastAPI
from api import users, products, recommendations, auth

app = FastAPI(title="Sistema de Recomendación de Productos")

# Incluir los routers
def include_routers():
    app.include_router(products.router, prefix="/products", tags=["Products"])
    app.include_router(users.router, prefix="/users", tags=["Users"])
    app.include_router(recommendations.router, prefix="/recommendations", tags=["Recommendations"])
    app.include_router(auth.router, tags=["Auth"])

include_routers()

# Documentación Swagger disponible en /docs


