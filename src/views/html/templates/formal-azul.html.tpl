<!DOCTYPE html>
<html lang="es">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Presupuesto - {{ project_name }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            color: #333;
        }

        h1 {
            color: #24488a;
        }

        table {
            width: 100%;
            border-collapse: collapse;
            margin: 20px 0;
        }

        th,
        td {
            border: 1px solid #ddd;
            padding: 5px;
            text-align: center;
        }

        th {
            background-color: #24488a;
            color: white;
        }

        tr:nth-child(even) {
            background-color: #f2f2f2;
        }

        .total {
            font-weight: bold;
            margin-top: 20px;
        }
    </style>
</head>

<body>
    <h1>Proyecto {{ project_name }}</h1>

    <h2>Presupuesto</h2>

    <table>
        <thead>
            <tr>
                <th>Concepto</th>
                <th>Cantidad</th>
                <th>Costo</th>
            </tr>
        </thead>
        <tbody>
            {% for item in items -%}
            <tr>
                <td>{{ item.name }}</td>
                <td>{{ item.quantity }}</td>
                <td>{{ "$" ~ item.cost if item.cost and item.cost_visible else "-" }}</td>
            </tr>
            {% endfor %}
        </tbody>
    </table>

    <div class="total">
        Total: ${{ total }}
    </div>
</body>

</html>