# iliketrains-odoo17

Este módulo de Odoo gestiona los servicios de tren, incluyendo proveedores, billetes, rutas, estaciones y pagos. A continuación se detallan las funcionalidades y partes del código.

## Modelos

### `train_provider.py`
Define el modelo `train.provider` que representa a los proveedores de servicios de tren.

- `name`: Nombre del proveedor (obligatorio).
- `code`: Código identificador del proveedor.
- `website`: Sitio web del proveedor.
- `active`: Estado activo/inactivo del proveedor (por defecto, activo).
- `notes`: Notas adicionales.
- `ticket_ids`: Relación uno a muchos con los billetes (`train.ticket`).

### `train_ticket.py`
Define el modelo `train.ticket` que representa a los billetes de tren.

- `name`: Referencia del billete (obligatorio).
- `ticket_code`: Código identificador único del billete.
- `employee_id`: Relación con el empleado (`hr.employee`) que posee el billete (obligatorio).
- `provider_id`: Relación con el proveedor (`train.provider`) (obligatorio).
- `route_id`: Relación con la ruta (`train.route`) (obligatorio).
- `travel_date`: Fecha de viaje (obligatorio).
- `price`: Precio del billete (obligatorio).
- `currency_id`: Moneda del precio del billete.
- `state`: Estado del billete (`draft`, `confirmed`, `reimbursed`, `cancelled`).
- `ticket_file`: Archivo del billete.
- `ticket_filename`: Nombre del archivo del billete.
- `payment_id`: Relación con la factura (`train.payment`).
- `invoice_number`: Número de factura relacionado.
- `invoice_date`: Fecha de la factura relacionada.
- `invoice_file`: Archivo de la factura.
- `invoice_filename`: Nombre del archivo de la factura.
- `notes`: Notas adicionales.

#### Mensajes de validación:
- `_check_price_positive`: Asegura que el precio del billete sea mayor que cero.

### `train_route.py`
Define el modelo `train.route` que representa las rutas de tren.

- `name`: Nombre de la ruta (obligatorio).
- `departure_station_id`: Estación de salida (obligatorio).
- `arrival_station_id`: Estación de llegada (obligatorio).
- `duration`: Duración estimada de la ruta en horas.
- `distance`: Distancia de la ruta en kilómetros.

#### Mensajes de validación:
- `_check_stations_different`: Asegura que las estaciones de salida y llegada sean diferentes.

### `train_station.py`
Define el modelo `train.station` que representa las estaciones de tren.

- `name`: Nombre de la estación (obligatorio).
- `location`: Ubicación de la estación (obligatorio).

### `train_payment.py`
Define el modelo `train.payment` que representa los registros de facturas de billetes.

- `name`: Referencia de la factura (obligatorio).
- `provider_id`: Proveedor relacionado (obligatorio).
- `invoice_date`: Fecha de la factura (obligatorio).
- `due_date`: Fecha de vencimiento.
- `total_amount`: Importe total de la factura.
- `ticket_ids`: Relación uno a muchos con los billetes (`train.ticket`) incluidos en la factura.
- `state`: Estado de la factura (`draft`, `validated`, `paid`).
- `payment_date`: Fecha de pago.
- `payment_reference`: Referencia del pago.
- `notes`: Notas adicionales.

## Instalación

Para instalar este módulo en tu instancia de Odoo, sigue estos pasos:
1. Clona este repositorio en tu directorio de addons de Odoo.
2. Reinicia el servidor de Odoo.
3. Ve a la interfaz de Odoo y actualiza la lista de aplicaciones.
4. Busca "iliketrains" y haz clic en "Instalar".

## Contribuciones

Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull request.

## Licencia

Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.
