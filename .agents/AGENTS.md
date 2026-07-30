# Regras do Projeto High House

Estas regras definem o comportamento estrito de todos os agentes trabalhando no repositório da High House. 
Elas não podem ser violadas.

## Regra de Ouro do README.md e Governança

1. **Atualização Contínua do README.md:** Sempre que a estrutura de diretórios, a arquitetura de agentes, ou um macroprocesso for alterado, o arquivo `README.md` raiz DEVE ser atualizado para refletir a nova topologia. Nenhuma alteração estrutural está completa sem a atualização do README.
2. **Tom de Voz Documental (Zero Fluff):** O `README.md` e toda documentação gerada no repositório devem seguir um tom institucional, rigoroso e objetivo.
   - **Proibido:** Uso de linguagem de assistente, aconselhamentos, jargões conversacionais (ex: "Aqui está o documento", "Você deve fazer isso", "Recomendo que").
   - **Estratégia e Operação:** Escrita impessoal (3ª pessoa) documentando fatos, fluxos e decisões tomadas.
   - **Fundação da Marca:** Uso da 1ª pessoa do plural ("nós") APENAS em manifestos e declarações de posicionamento público da marca.
3. **Mapeamento Arquitetural:** O README.md sempre deve conter a Árvore de Diretórios (`🗂️ Estrutura e Arquitetura do Repositório`) atualizada perfeitamente em sincronia com o estado real do repositório. Nunca remova seções essenciais durante uma atualização.
4. **Versionamento Autônomo:** Toda atualização, incluindo a modificação do README, deve ser finalizada com a esteira Git:
   - Verificar proteção via `.gitignore`
   - `git add .`
   - `git commit` utilizando Conventional Commits (ex: `docs: atualiza arquitetura do EOS no README`)
   - `git push` para sincronizar na nuvem.
