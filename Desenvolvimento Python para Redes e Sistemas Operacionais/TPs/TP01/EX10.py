#Os comandos os.exec* e os.spawn* são bastante parecidos. No entanto, eles apresentam uma diferença em suas execuções. Aponte qual é está diferença.

print("Resposta:")
print("Spawn cria um processo. A entrada e a saída dos processos são conectadas para esperar para uso pelos outros comandos: enviar, esperar e interagir.")
print("Exec cria um subprocesso em tcl. Em geral, o tcl é suspenso até que o subprocesso seja concluído. No entanto, pode-se criar o subprocesso em segundo plano (usando & como o último argumento) e se conectar a entrada e a saída corretamente, tcl pode interagir com o subprocesso. Isso é muito desajeitado e é exatamente o tipo de interação que o expect foi projetado para lidar suavemente.")
