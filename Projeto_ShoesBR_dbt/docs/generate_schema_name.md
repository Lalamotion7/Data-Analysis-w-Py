{% docs generate_schema_name %}
## 🛠️ Macro: `generate_schema_name`
Esta macro define dinamicamente o nome do schema para cada modelo no dbt.

### 🔄 Lógica:
1. **Se `custom_schema_name` for `None`**, retorna `node.schema` (definido no `dbt_project.yml`).
2. **Se `custom_schema_name` for especificado**, usa esse valor.

### 🎯 Uso no `dbt_project.yml`:
```yaml
models:
  my_project:
    marts:
      +schema: marts  # Será aplicado automaticamente na macro
```

Essa abordagem garante flexibilidade ao organizar schemas dinamicamente.
{% enddocs %}