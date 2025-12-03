from pathlib import Path

class FileService:
  def readFile(self, relativePath: str) -> str:
    # Current file: src/utils/FileService.py
    # .parent = src/utils
    # .parent.parent = src
    # .parent.parent.parent = Project Root
    basePath = Path(__file__).resolve().parent.parent.parent
    filePath = basePath / relativePath
    
    try:
      with open(filePath, "r", encoding="utf-8") as f:
        return f.read()
    except FileNotFoundError:
      # Return empty JSON list as fallback
      return "[]"