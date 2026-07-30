import re
from pathlib import Path

class MarkdownContextLoader:
    """
    Abstração para localizar, carregar e versionar contextos de agentes (prompts) escritos em Markdown.
    Lê a fonte de verdade absoluta (04_AGENT_SPECIFICATIONS.md) para evitar duplicação de informações.
    """
    
    @staticmethod
    def _find_project_root() -> Path:
        current = Path.cwd()
        while current != current.parent:
            if (current / "11_EDITORIAL_OS").exists():
                return current
            if current.name == "11_EDITORIAL_OS":
                return current.parent
            current = current.parent
        return Path.cwd()

    @classmethod
    def load(cls, role_name: str) -> str:
        """
        Carrega o bloco correspondente ao agente dentro do 04_AGENT_SPECIFICATIONS.md.
        role_name: Nome do agente (ex: 'Research Agent').
        """
        root = cls._find_project_root()
        spec_path = root / "11_EDITORIAL_OS" / "04_AGENT_SPECIFICATIONS.md"
        
        if not spec_path.exists():
            raise FileNotFoundError(f"Arquivo mestre de especificações não encontrado: {spec_path}")
            
        with open(spec_path, "r", encoding="utf-8") as f:
            content = f.read()
            
        # Regex para capturar desde '### X.X {Role Name}' até o próximo '###' ou fim do arquivo
        pattern = re.compile(rf"(### \d+\.\d+ {re.escape(role_name)}.*?)(?=\n### |\Z)", re.DOTALL)
        match = pattern.search(content)
        
        if not match:
            raise ValueError(f"Contexto para o agente '{role_name}' não encontrado no documento de especificações.")
            
        return match.group(1).strip()
