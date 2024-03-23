# Autom-RelatorioComissao
 Este código é um script de automação para abrir um arquivo do LibreOffice Calc (Funciona também no Excel), atualizar os dados nele, salvar as alterações e fechar o arquivo. Aqui está uma descrição passo a passo do que ele faz:

1. Importa os módulos necessários: `os` para interagir com o sistema operacional, `time` para adicionar pausas entre as operações, e `pyautogui` para controlar o mouse e o teclado.

2. Define o caminho do arquivo do LibreOffice Calc a ser manipulado.

3. Usa `os.startfile(caminho_arquivo)` para abrir o arquivo especificado no LibreOffice Calc.

4. Espera alguns segundos usando `time.sleep(4)` para permitir que o LibreOffice Calc seja aberto completamente.

5. Clica na opção "DADOS" na barra de ferramentas do Calc usando `pyautogui.click(x=410, y=46)`.

6. Espera mais alguns segundos (`time.sleep(2)`) para garantir que a janela de "DADOS" seja aberta e, em seguida, clica na opção "ATUALIZAR TODOS" usando `pyautogui.click(x=426, y=91)`.

7. Espera 30 segundos (`time.sleep(5)`) para que os dados sejam atualizados.

8. Salva a planilha usando `pyautogui.hotkey('ctrl', 's')` (atalho para salvar) e espera um pouco (`time.sleep(2)`) para a janela de salvar aparecer. Em seguida, pressiona Enter (`pyautogui.press('enter')`) para confirmar a ação de salvar.

9. Espera mais um pouco (`time.sleep(2)`) antes de fechar o arquivo usando o atalho `pyautogui.hotkey('ctrl', 'q')`.

10. Por fim, imprime uma mensagem indicando que o arquivo foi atualizado, salvo e fechado com sucesso.

Este script automatiza o processo de atualização de dados em uma planilha de Relatorio de Comissão e salva as alterações feitas.
