from cog import BasePredictor, Input, Path
import traceback
from sklearn.cluster import MiniBatchKMeans  # ✅ Isso resolve o bug

class Predictor(BasePredictor):
    def predict(self, audio_path: Path = Input(...)):
        try:
            # Seu código RVC ou outro aqui...
            return "Modelo rodou com sucesso!"
        except Exception:
            return traceback.format_exc()
