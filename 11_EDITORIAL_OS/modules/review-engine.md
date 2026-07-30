# Review Engine (Crítica Automática)

O **Review Engine** é o ciclo de validação obrigatório de qualquer peça de conteúdo gerada pelo EOS. Nada é publicado sem o aval de toda a equipe de agentes.

## 🔄 Fluxo de Aprovação em Cascata

A peça passa pelos agentes na seguinte ordem (Sequence Pipeline):

1. **Editor-Chefe:** Verifica coesão narrativa e continuidade com o `Memory Engine`.
2. **Diretor Criativo:** Verifica originalidade, choque estético e ausência de clichês.
3. **Estrategista de Marca:** Verifica o alinhamento com os pilares fundamentais da High House.
4. **Copy & Consistência:** Refina vocabulário (remove adjetivação vazia e exclamações desnecessárias).
5. **Diretor de Arte & UX:** Avalia se a composição visual ou HTML/CSS atende aos critérios do Design System.

## ❌ Ciclo de Reprovação e Loop

Se **QUALQUER** agente rejeitar a peça, o processo é interrompido, e um relatório (Feedback Log) é gerado na pasta `logs_and_docs/`.

O relatório de falha deve conter:
- **Agente Reprovador:** (Ex: Diretor Criativo)
- **Motivo da Reprovação:** (Ex: "A imagem proposta parece muito renderizada por IA genérica. Parece plástico. Precisamos de textura analógica.")
- **Ação de Correção:** (Ex: "Substituir a geração por um layout puramente tipográfico consumindo nosso arquivo CSS de Design System.")

A Criação deve processar a correção e reiniciar o Review Engine do passo 1.

## ✅ Crivo de Alta Exigência
A IA não tem pressa. É preferível que o Review Engine fique em loop por 5 interações consertando detalhes de sombra, contraste ou vocabulário do que publicar um material que desvalorize o "Premium Feeling" da marca.
