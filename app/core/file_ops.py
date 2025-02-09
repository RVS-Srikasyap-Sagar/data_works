import json
import re
from pathlib import Path
from typing import Any, Dict, List


class FileOps:
    @staticmethod
    def read_file(path: str) -> str:
        """Read file content with path validation"""
        from app.core.security import validate_path
        validate_path(path)

        try:
            with open(path, 'r', encoding='utf-8') as f:
                return f.read()
        except FileNotFoundError:
            raise
        except Exception as e:
            raise IOError(f"Error reading file: {str(e)}")

    @staticmethod
    def write_file(path: str, content: str) -> None:
        """Write content to file with path validation"""
        from app.core.security import validate_path
        validate_path(path)

        try:
            Path(path).parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'w', encoding='utf-8') as f:
                f.write(content)
        except PermissionError:
            raise
        except Exception as e:
            raise IOError(f"Error writing file: {str(e)}")

    @staticmethod
    def read_json(path: str) -> Dict[str, Any]:
        content = FileOps.read_file(path)
        return json.loads(content)

    @staticmethod
    def write_json(path: str, data: Dict[str, Any]) -> None:
        FileOps.write_file(path, json.dumps(data, indent=2))

    @staticmethod
    def extract_markdown_headers(content: str) -> List[str]:
        """Extract first occurrence of H1 headers from markdown content"""
        return re.findall(r'^#\s+(.+)$', content, flags=re.MULTILINE)
