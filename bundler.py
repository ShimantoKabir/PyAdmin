import os

# Name of the output file
OUTPUT_FILE = "project-code.txt"

# Folders to skip (add any others you want to ignore)
IGNORE_DIRS = {
  '.git', '.venv', 'venv', 'env', '__pycache__', 
  '.idea', '.vscode', 'node_modules', 'dist', 'build'
}

# File extensions to skip (images, binaries, databases)
IGNORE_EXTENSIONS = {
  '.pyc', '.png', '.jpg', '.jpeg', '.gif', 
  '.svg', '.ico', '.db', '.sqlite', '.log', '.pot'
}

def is_text_file(filename):
  """Check if a file is likely a text file based on extension."""
  return not any(filename.endswith(ext) for ext in IGNORE_EXTENSIONS)

def generate_bundle():
  # Get the absolute path of the current directory to match your format
  base_path = os.path.abspath(".")
  
  with open(OUTPUT_FILE, 'w', encoding='utf-8') as outfile:
    # Walk through the directory tree
    for root, dirs, files in os.walk("."):
      # Modify 'dirs' in-place to skip ignored directories
      dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
      
      for file in files:
        # Don't include the script itself or the output file
        if file == "bundler.py" or file == OUTPUT_FILE:
          continue
        
        if not is_text_file(file):
          continue

        # Create the full path
        relative_path = os.path.join(root, file)
        absolute_path = os.path.abspath(relative_path)
        
        try:
          with open(relative_path, 'r', encoding='utf-8') as infile:
            content = infile.read()
            
            # WRITE THE HEADER EXACTLY AS YOU REQUESTED
            outfile.write(f"file path: {absolute_path}\n")
            outfile.write(content)
            outfile.write("\n\n") # Add spacing between files
            
            print(f"Added: {file}")
        except Exception as e:
          print(f"Skipping {file} (Read Error: {e})")

  print(f"\nSuccessfully generated: {OUTPUT_FILE}")

if __name__ == "__main__":
  generate_bundle()