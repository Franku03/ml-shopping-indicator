from pydantic import BaseModel, Field


class SessionDataDTO(BaseModel):
    # Atributos de navegación (Ejemplo de algunos de los 10 numéricos)
    administrative: int = Field(ge=0, description="Páginas administrativas visitadas")
    administrative_duration: float = Field(ge=0.0)
    informational: int = Field(ge=0)
    product_related: int = Field(ge=0)

    # Métricas de Google Analytics
    bounce_rate: float = Field(ge=0.0, le=1.0)
    exit_rate: float = Field(ge=0.0, le=1.0)
    page_value: float = Field(ge=0.0)

    # Atributos Categóricos (Ejemplo)
    special_day: float = Field(ge=0.0, le=1.0)
    visitor_type: str = Field(description="New_Visitor o Returning_Visitor")
    weekend: bool
    month: str


class PredictionResponseDTO(BaseModel):
    clasificacion: str
    probabilidad: float
    mensaje: str