<div class="flex flex-col items-start justify-center h-full"
v-click="1"
v-motion
:initial="{ opacity: 0 }"
:enter="{ opacity: 1}"
:duration="1000"
>
````md magic-move {at:2, lines: false}
```python
def load_file_function(file_ext: str) -> Callable:
```

```python
def load_file_function(file_ext: str) -> Callable:

  if file_ext == ".csv":
    return pandas.read_csv
  else:
    raise KeyError("File extension not supported")
```

```python
def load_file_function(file_ext: str) -> Callable:

  if file_ext == ".csv":
    return pandas.read_csv
  elif file_ext == ".parquet":
    return pandas.read_parquet
  else:
    raise KeyError("File extension not supported")
```

```python
def load_file_function(file_ext: str) -> Callable:

  if file_ext == ".csv":
    return pandas.read_csv
  elif file_ext == ".parquet":
    return pandas.read_parquet
  elif file_ext == "pickle":
    return pandas.read_pickle
  else:
    raise KeyError("File extension not supported")
```

```python
def load_file_function(file_ext: str) -> Callable:

  if file_ext == ".csv":
    return pandas.read_csv
  elif file_ext == ".parquet":
    return pandas.read_parquet
  elif file_ext == "pickle":
    return pandas.read_pickle
  elif file_ext == ".xlsx":
    return padas.read_excel
  else:
    raise KeyError("File extension not supported")
```

```python
def load_file_function(file_ext: str) -> Callable:

  if file_ext == ".csv":
    return pandas.read_csv
  elif file_ext == ".parquet":
    return pandas.read_parquet
  elif file_ext == "pickle":
    return pandas.read_pickle
  elif file_ext == ".xlsx":
    return padas.read_excel
  elif file_ext == ".html":
    return pandas.read_html
  elif file_ext == ".json":
    return pandas.read_json
  elif file_ext == ".xml":
    return pandas.read_xml
  elif file_ext == ".sql":
    return pandas.read_sql
  elif file_ext == ".feather":
    return pandas.read_feather
  else:
    raise KeyError("File extension not supported")
```
````
</div>