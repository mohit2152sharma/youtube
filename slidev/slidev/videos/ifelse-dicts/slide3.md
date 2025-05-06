<FancyArrow v-click="[3, 8]" 
  v-motion
  :initial="{opacity: 0}"
  :enter="{opacity: 1}"
  :duration="500"
  z-10 x2="275" y2="138" arc="0.2" q1="[data-id=file_ext]" pos1="bottom"  color="orange" roughness="1" width="1" pos2="top"></FancyArrow>
<FancyArrow v-click="[6, 8]"
  v-motion
  :initial="{opacity: 0}"
  :enter="{opacity: 1}"
  :duration="500"
  z-10 x1="180" y1="138" x2="180" y2="360" arc="-0.7" pos1="bottom"  color="teal" roughness="1" width="1" pos2="top"></FancyArrow>

<div
  class="flex flex-col items-center justify-center gap-y-2">
<div
  v-click="[1,8]"
  v-motion
  :initial="{opacity: 0}"
  :enter="{opacity: 1}"
>
<pre><code data-id=file_ext>file_ext</code></pre>
</div>

<div v-click="2" 
  v-motion
  :initial="{opacity: 0}"
  :enter="{opacity: 1}"
  class="w-3/4">
````md magic-move {at: 3, lines: false}

```python  {*|*|3}
{
  ".csv",
  ".parquet",
  ".pickle",
  ".xlsx",
  ".html",
  ".json",
  ".xml",
  ".sql",
  ".feather"
}
```

```python {3,14,15,16,17,18,19,20,21,22,23,24|3,14,15,16,17,18,19,20,21,22,23,24|3,16}
{
  ".csv",
  ".parquet",
  ".pickle",
  ".xlsx",
  ".html",
  ".json",
  ".xml",
  ".sql",
  ".feather"
}


{
  pandas.read_csv,
  pandas.read_parquet,
  pandas.read_pickle,
  pandas.read_xlsx,
  pandas.read_html,
  pandas.read_json,
  pandas.read_xml,
  pandas.read_sql,
  pandas.read_feather
}
```

```python
{
  ".csv"            ->           pandas.read_csv, 
  ".parquet"        ->           pandas.read_parquet,
  ".pickle"         ->           pandas.read_pickle,
  ".xlsx"           ->           pandas.read_xlsx,
  ".html"           ->           pandas.read_html,
  ".json"           ->           pandas.read_json,
  ".xml"            ->           pandas.read_xml,
  ".sql"            ->           pandas.read_sql,
  ".feather"        ->           pandas.read_feather
}
```

```python
{
  ".csv"            :           pandas.read_csv, 
  ".parquet"        :           pandas.read_parquet,
  ".pickle"         :           pandas.read_pickle,
  ".xlsx"           :           pandas.read_xlsx,
  ".html"           :           pandas.read_html,
  ".json"           :           pandas.read_json,
  ".xml"            :           pandas.read_xml,
  ".sql"            :           pandas.read_sql,
  ".feather"        :           pandas.read_feather
}
```

```python
{
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
```

```python
file_ext_to_function = {
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

file_ext_to_function["csv"]
```

```python
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
    raise ValueError(f"Unsupported file extension: {file_ext}")
```
````
</div>

</div>
