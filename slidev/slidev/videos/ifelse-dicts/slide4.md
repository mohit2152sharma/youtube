<div v-click="1" 
  v-motion
  :initial="{opacity: 0}"
  :enter="{opacity: 1}"
  class="grid grid-cols-2 gap-x-2">

<div>
```python {*}{lines: false}
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
</div>

<div>
```python {*}{lines: false}
def load_file_function(file_ext: str) -> Callable:
  file_ext_to_function: dict[str, Callable] = {
    ".csv" : pandas.read_csv, 
    ".parquet" : pandas.read_parquet,
    ".pickle" : pandas.read_pickle,
    ".xlsx": pandas.read_xlsx,
    ".html": pandas.read_html,
    ".json": pandas.read_json,
    ".xml": pandas.read_xml,
    ".sql": pandas.read_sql,
    ".feather": pandas.read_feather
  }
  try:
    return file_ext_to_function[file_ext]
  except KeyError:
    raise KeyError(f"Unsupported file extension: {file_ext}")
```
</div>

</div>



