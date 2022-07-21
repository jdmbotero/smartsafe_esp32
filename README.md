# smartsafe_esp32

Para la conexión a internet y al proyecto de firebase, se necesita un archivo de configuración llamado localdata.json con la siguiente estructura:

```json
{
    "firestore": {
        "projectId": "",
        "apiKey": "",
        "email": "",
        "password": ""
    },
    "wifi": {
        "SSD": "",
        "password": ""
    }
}
```
