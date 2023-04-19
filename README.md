# pytest_requests

Exemples de com crear tests automàtics amb Python. Usem les llibreries
- Pytest (general) 
- Requests (per a testejar API’s).
- Flask (pels 3 últims tests, crear la nostra pròpia API)

### Instal·lació.

Les 3 llibreries les trobareu a pip i a Anaconda (totes al canal -c anaconda)

```
conda -n <ENTORN> install -c anaconda <LLIBRERIA>
```

```
pip install -U <LLIBRERIA>
```

### Codi pytestdemo.py

- Els 2 primers tests són sobre una funció inventada (dins d'aligner.py)
- Els 3 mètodes entremig provem Requests a API's externes.
- Els 3 últims els provem en un web service creat per nosaltres amb Flask, el seu codi es troba a la carpeta /app5
