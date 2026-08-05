import os
from eos.infrastructure.renderer import PlaywrightRenderer

class PublicationExporter:
    """
    Handles the side-effects of rendering HTML to PNG and saving text captions to disk.
    Isolates these side-effects from the Orchestrator.
    """
    def __init__(self, output_dir: str):
        self.output_dir = output_dir
        self.renderer = PlaywrightRenderer()
        
        # Na arquitetura atual o design_system fica em 05_IMPLEMENTACAO/design_system
        self.design_system_dir = os.path.abspath(os.path.join(self.output_dir, "../design_system"))

    def export(self, collection_id: str, poster_num: str, html_content: str, caption: str) -> tuple[str, str]:
        """
        Exports the rendered HTML as PNG and the caption as TXT.
        Returns the absolute paths to the generated files (png_path, txt_path).
        """
        collection_path = os.path.join(self.output_dir, collection_id)
        os.makedirs(collection_path, exist_ok=True)
        
        png_path = os.path.join(collection_path, f"poster_{poster_num}.png")
        txt_path = os.path.join(collection_path, f"poster_{poster_num}_caption.txt")
        
        print(f"[EXPORTER] Renderizando {png_path} via Playwright...")
        self.renderer.render_to_png(html_content, png_path, base_dir=self.design_system_dir)
        
        with open(txt_path, "w", encoding="utf-8") as f:
            f.write(caption)
            
        return png_path, txt_path
