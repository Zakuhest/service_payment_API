#  Service Payment API
- ## Proyecto Unidad 5

## Hecho por:
- ## Cristian Diaz C.

## Tipo de proyecto:

Individual o grupal máximo de 2 personas.
#
## Funcionalidades a desarrollar:

Realizar el versionamiento basado en la tarea desarrollada:

- Versión 1: lo desarrollado el viernes 16 de diciembre.

- Versión 2: lo solicitado en el proyecto.
#
## Modelos:

Services
- Id
- Name
- Description
- Logo

Payment_user
- Id
- User_id
- Service_id
- Amount
- PaymentDate
- ExpirationDate

Expired_payments
- Id
- Payment_user_id
- Penalty_fee_amount

User
- Id
- Email
- Username
- Password
#
-> Para la parte del login deben hacer uso de <code>simpleJWT</code>, y debe contar con las mismas funcionalidades que el login desarrollado en sesiones anteriores.

-> La API deberá contar con el CRUD para todos los modelos presentados.

-> Deben crear roles para el uso de la API:
- Anónimo: No puede acceder a la API
- Usuario normal: Puede realizar POST de los pagos y hacer GET de todas las vistas.
- Admin: Tiene acceso al CRUD de todas las vistas.

-> La vista creada para el modelo de servicios debe ser estática, por lo que debe contar únicamente con el método GET.

-> La vista creada para el modelo <code>Expired_payments</code>, sólo debe admitir GET y POST

-> Añadir Paginación de 100 resultados por página.

-> Añadir filtro de búsqueda en <code>Payment_user</code> para los campos de fecha de pago y fecha de expiración.

-> Si la fecha de pago supera a la fecha de expiración, se debe crear un registro automático en <code>Expired_payments</code>.

-> Implementar Throttling para la vista de pagos con 1000 request por día y las demás de 2000 por día. Para las pruebas realizar con 3 y 7 respectivamente.

-> Generar la documentación de toda su API.

#
## Notas:
<strong>Cuenta admin: </strong>

- Email: admin@mail.com
- Password: 12345678
- Generar token y refresh en url: "/api/payment/login/"

<strong>Para todas las cuentas: </strong>

Es necesario loguearse (POST) en url "/api/payment/login/", para obtener el token y refresh. O actualizar token con el refresh (POST) en url "api/payment/refresh/".
#
## Deploy Railway:
- Documentación de API: https://servicepaymentapi-production.up.railway.app/api/redoc/
