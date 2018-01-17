# paloAlto_api

#### Ejemplos de uso:

##### Obtener api_key:
```python
get_api_key(URL, 'username', 'password')
```

##### Inicializar objeto:
```
URL = 'https://192.168.1.1/api/?'
API_KEY = 'Loremipsumdolorsitametconsecteturadipiscingelitseddoeiusmodtempor'

api = Paloalto_api(URL, API_KEY)
```

##### Descastivar verificación de certificado HTTPS:
```python
api.set_https_verify(False)

```
##### Usar proxy:
```python
proxies = {
    'http': 'socks5://127.0.0.1:1081',
    'https': 'socks5://127.0.0.1:1081'
}
api.set_proxy(proxies)  

```

##### Obtener XML del estado del dispositivo:
```python
api.get_config()
```

##### Obtener XML de una dirección:
```python
api.get_address("Direccion_1")
```

##### Crear un objeto de tipo dirección:
```python
api.create_address("Direccion_2", "192.168.1.1/32", "Descripcion")
```

##### Eliminar objeto de tipo dirección:  
```python
api.delete_objet("Direccion_1")
```

##### Añadir dirección a grupo    
Crea el grupo si no existe    
```python
api.add_group_address("Grupo_1", "Direccion_1")
```

### TODO:
 - [ ] Añadir resto de opciones de la API
 - [ ] Documentar metodos
 - [ ] Aplicar check antes de borrar un objeto
 - [ ] Eliminar un objeto con dependencias
