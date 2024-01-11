Tabla: categoria
Empty DataFrame
Columns: [id, nombre]
Index: []

Tabla: producto
Empty DataFrame
Columns: [id, nombre, marca, categoria_id, precio_unitario]
Index: []

Tabla: sucural
Empty DataFrame
Columns: [id, nombre, direccion]
Index: []

Tabla: stock
Empty DataFrame
Columns: [id, sucursal_id, producto_id, cantidad]
Index: []

Tabla: cliente
Empty DataFrame
Columns: [id, nombre, telefono]
Index: []

Tabla: orden
Empty DataFrame
Columns: [id, cliente_id, sucursal_id, fecha, total]
Index: []

Tabla: item
Empty DataFrame
Columns: [id, orden_id, producto_id, cantidad, monto_ventas]
Index: []