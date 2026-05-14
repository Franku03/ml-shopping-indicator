def predict_purchase_intention(data: dict) -> float:
    """
    Aquí eventualmente cargaremos el modelo de Keras/Scikit-learn.
    Por ahora, simulamos una probabilidad basada en la duración de la visita.
    """
    # Lógica dummy temporal
    if data["product_related"] > 10 and data["page_value"] > 20:
        return 0.85 # 85% de probabilidad de compra
    return 0.15 # 15% de probabilidad