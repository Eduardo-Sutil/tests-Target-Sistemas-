sp = 67836.43
rj = 36678.66
mg = 29229.88
es = 27165.48
outros = 19849.53

soma_faturamento = sp + rj + mg + es + outros

percentual_faturamento_sp = round((sp * 100)/soma_faturamento)
percentual_faturamento_rj = round((rj * 100/soma_faturamento))
percentual_faturamento_mg = round((mg * 100/soma_faturamento))
percentual_faturamento_es = round((es * 100/soma_faturamento))
percentual_faturamento_outros = round((outros * 100/soma_faturamento))

print(f'Percentual do faturamento mensal de SP: {percentual_faturamento_sp}%')
print(f'Percentual do faturamento mensal do RJ: {percentual_faturamento_rj}%')
print(f'Percentual do faturamento mensal de MG: {percentual_faturamento_mg}%')
print(f'Percentual do faturamento mensal do ES: {percentual_faturamento_es}%')
print(f'Percentual do faturamento mensal dos outros estados: {percentual_faturamento_outros}%')
