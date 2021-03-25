from pydantic import BaseModel
from image2vec import Img2Vec
import base64, os

class VectorImagePayload(BaseModel):
  id: str
  image: str

class ImageVectorizer:
  img2vec: Img2Vec

  def __init__(self):
    self.img2vec = Img2Vec()

  def vectorize(self, id: str, image: str):
    filepath = self.saveImage(id, image)
    vector = self.img2vec.get_vec(filepath)
    self.removeFile(filepath)
    return vector

  def saveImage(self, id: str, image: str):
    try:
      filepath = id
      file_content = base64.b64decode(image)
      with open(filepath, "wb") as f:
        f.write(file_content)
      return filepath
    except Exception as e:
      print(str(e))
      return ""

  def removeFile(self, filepath: str):
    if os.path.exists(filepath):
      os.remove(filepath)
