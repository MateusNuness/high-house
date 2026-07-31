import re
from pathlib import Path

class MarkdownContextLoader:
    """
    Abstração para localizar, carregar e versionar contextos de agentes (prompts) escritos em Markdown.
    
    Hierarquia de carregamento:
    1. Contexto dedicado em 04_AGENT_CONTEXTS/<slug>_context.md (preferencial)
    2. Bloco correspondente em 04_AGENT_SPECIFICATIONS.md (fallback)
    
    Isso permite que agentes com contextos mais ricos (ex: Brand Guardian) tenham
    arquivos dedicados, enquanto os demais continuam usando o documento monolítico.
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
    def _role_to_slug(cls, role_name: str) -> str:
        """Converte 'Brand Guardian Agent' → 'brand_guardian'."""
        slug = role_name.lower().replace(" agent", "").strip()
        return slug.replace(" ", "_")

    @classmethod
    def load(cls, role_name: str) -> str:
        """
        Carrega o contexto do agente. Primeiro tenta um arquivo dedicado em
        04_AGENT_CONTEXTS/, depois faz fallback para 04_AGENT_SPECIFICATIONS.md.
        
        role_name: Nome do agente (ex: 'Research Agent', 'Brand Guardian Agent').
        """
        root = cls._find_project_root()
        
        # 1. Tentar carregar contexto dedicado
        slug = cls._role_to_slug(role_name)
        context_path = root / "11_EDITORIAL_OS" / "04_AGENT_CONTEXTS" / f"{slug}_context.md"
        
        if context_path.exists():
            with open(context_path, "r", encoding="utf-8") as f:
                return f.read().strip()
        
        # 2. Fallback: parsear do documento monolítico
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
