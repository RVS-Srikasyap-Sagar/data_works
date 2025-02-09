import re
from typing import Any, Dict


class InputValidator:
    @staticmethod
    def validate_email(email: str) -> bool:
        pattern = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        return re.match(pattern, email) is not None

    @staticmethod
    def validate_sql_query(query: str) -> bool:
        forbidden_keywords = ['delete', 'drop', 'alter', 'insert', 'update']
        return not any(kw in query.lower() for kw in forbidden_keywords)

    @staticmethod
    def sanitize_input(input_str: str) -> str:
        """Basic input sanitization for task parameters"""
        return input_str.strip().replace('\0', '')

    @staticmethod
    def validate_task_params(params: Dict[str, Any]) -> None:
        """Validate parameters for task execution"""
        if 'path' in params:
            from app.core.security import validate_path
            validate_path(params['path'])

        if 'sql' in params:
            if not InputValidator.validate_sql_query(params['sql']):
                raise ValueError("Invalid SQL query")
