# Рачунарска интелигенција

## Инсталација

За управљање пројектом и библиотекама користи се `uv`.
Потребно је прво њега инсталирати, па након клонирања репозиторијума покренути синхронизацију.

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
git clone https://github.com/MATF-RI/Materijali-sa-vezbi.git
cd Materijali-sa-vezbi
uv sync
```
На овај начин ће аутоматски бити преузета одговарајућа верзија Python-a (3.11), креирано виртуелно окружење и инсталиране све потребне библиотеке.

За инсталацију CPLEX-a, потребно је улоговати се са факултетским мејлом на https://www.ibm.com/academic/ и у одељку Data Science преузети ILOG CPLEX optimisation studio 22.1.1 (можда ће бити потребно allow popups и вероватно је лакше изабрати http него download director).
Да би се ова потпуна верзија CPLEX-a повезала са пројектом, потребно је покренути:
```bash
uv run python make_full.py /opt/ibm/ILOG/CPLEX_Studio2211
```
Ово је подразумевана путања, замените је својом уколико сте приликом инсталације изабрали неку другу.