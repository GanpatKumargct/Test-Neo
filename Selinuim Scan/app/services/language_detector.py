from pathlib import Path
from collections import Counter

EXT_TO_LANG = {
    ".py": "python",
    ".java": "java",
    ".js": "javascript",
    ".ts": "javascript",
    ".cs": "csharp",
    ".kt": "kotlin",
}

def detect_language(root_path: Path) -> str:
    """
    Scans the directory for source file extensions and returns the most frequent language.
    Defaults to 'python' if no matches found.
    """
    counts = Counter()
    for ext in EXT_TO_LANG.keys():
        for _ in root_path.rglob(f"*{ext}"):
            counts[EXT_TO_LANG[ext]] += 1
    
    if not counts:
        return "python"
    
    return counts.most_common(1)[0][0]
