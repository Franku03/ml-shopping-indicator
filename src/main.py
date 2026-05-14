from fastapi import FastAPI, HTTPException
from src.dtos.schemas import SessionDataDTO, PredictionResponseDTO
from src.services.connect_to_model_service import predict_purchase_intention

# Inicializamos la app
app = FastAPI(
    title="API Predictiva de E-commerce",
    description="Detecta intención de compra en tiempo real",
    version="1.0"
)

@app.post("/predict", response_model=PredictionResponseDTO)
async def get_prediction(session: SessionDataDTO):
    try:
        # 1. Convertimos el DTO a un diccionario de Python
        features = session.model_dump()

        # 2. Se lo pasamos al modelo matemático
        probabilidad = predict_purchase_intention(features)

        # 3. Lógica de negocio para formatear la respuesta
        is_buyer = probabilidad >= 0.5
        clasificacion = "Compra" if is_buyer else "No Compra"

        # 4. Generar el "Human readable entry"
        if probabilidad >= 0.8:
            mensaje = f"El usuario presenta un {probabilidad * 100:.0f}% de probabilidades, es una venta casi segura."
        elif probabilidad >= 0.5:
            mensaje = f"El usuario presenta un {probabilidad * 100:.0f}% de probabilidades. Podría comprar si se le ofrece un incentivo."
        else:
            mensaje = f"El usuario presenta un {probabilidad * 100:.0f}% de probabilidades. Es un visitante casual de momento."

        return PredictionResponseDTO(
            clasificacion=clasificacion,
            probabilidad=probabilidad,
            mensaje=mensaje
        )

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error en el servidor de ML: {str(e)}")
@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}
