import os
from playwright.sync_api import sync_playwright

class PlaywrightRenderer:
    """
    Motor de Renderização Nativo usando Playwright.
    Compila o HTML/CSS e captura a imagem final do Pôster (1080x1350).
    """

    def __init__(self, viewport_width: int = 1080, viewport_height: int = 1350):
        self.viewport_width = viewport_width
        self.viewport_height = viewport_height

    def render_to_png(self, html_content: str, output_path: str, base_dir: str = None) -> str:
        """
        Renderiza uma string HTML em um arquivo PNG.
        
        :param html_content: Código HTML a ser renderizado.
        :param output_path: Caminho completo para salvar o PNG.
        :param base_dir: Diretório base para resolver dependências relativas (como tokens.css).
        :return: O caminho do arquivo PNG gerado.
        """
        # Garante que o diretório de destino exista
        os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)

        with sync_playwright() as p:
            browser = p.chromium.launch(headless=True)
            page = browser.new_page(
                viewport={"width": self.viewport_width, "height": self.viewport_height},
                device_scale_factor=2 # Alta resolução (Retina)
            )
            
            # Se houver um diretório base (ex: design_system), escrevemos o HTML nele para que os assets carreguem
            temp_file = None
            if base_dir and os.path.isdir(base_dir):
                temp_file = os.path.join(base_dir, "_temp_render.html")
                with open(temp_file, "w", encoding="utf-8") as f:
                    f.write(html_content)
                
                # Usa file:// URI
                page.goto(f"file://{os.path.abspath(temp_file)}")
                # Aguarda recursos (imagens de fundo, css) carregarem
                page.wait_for_load_state("networkidle")
            else:
                page.set_content(html_content)
                page.wait_for_load_state("networkidle")
                
            page.screenshot(path=output_path, type="png")
            # Save HTML next to PNG for debugging
            html_path = output_path.replace(".png", ".html")
            with open(html_path, "w", encoding="utf-8") as f:
                f.write(html_content)
                
            browser.close()
            
            # Limpeza do arquivo temporário
            if temp_file and os.path.exists(temp_file):
                os.remove(temp_file)

        return output_path
