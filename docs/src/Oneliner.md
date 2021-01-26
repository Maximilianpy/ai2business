<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/macros/oneliner.py#L45)</span>

### Search


```python
ai2business.macros.oneliner.Search(*args, **kwargs)
```


Collection of `oneliner` for searching.


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/macros/oneliner.py#L48)</span>

### four_step_trendsearch


```python
Search.four_step_trendsearch(
    keyword_list,
    timeframe="today 5-y",
    language="en-US",
    category=0,
    timezone=360,
    country="",
    property_filter="",
    resolution="COUNTRY",
    **kwargs
)
```


four step search

A four step search includes:

1. Overtime
2. By regions
3. By related topics
4. By related queries

Arguments:
    keyword_list (list): Keyword-list with the items to search for.
    timeframe (str, optional): Time frame, respectively, period to search for.
    Defaults to "today 5-y".
    language (str, optional): Search language. Defaults to "en-US".
    category (int, optional): Define a specific [search category](https://github.com/pat310/google-trends-api/wiki/Google-Trends-Categories). Defaults to 0.
    timezone (int, optional): [Search timezone](https://developers.google.com/maps/documentation/timezone/overview). Defaults to 360.
    country (str, optional): The country, where to search for. Defaults to "".
    property_filter (str, optional): Property filer of the search; only in news, images, YouTube, shopping. Defaults to "".
    resolution (str, optional): The resolution / zoom-factor, where to search for. Defaults to "COUNTRY".

Returns:
    dict: Dictionary with the keys: 'interest_over_time', 'interest_by_region', 'related_topics', 'related_queries' and its dataframes.


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/macros/oneliner.py#L113)</span>

### Plot


```python
ai2business.macros.oneliner.Plot(*args, **kwargs)
```


Collection of `oneliner` for plotting.


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/macros/oneliner.py#L116)</span>

### plotdata


```python
Plot.plotdata(
    df,
    plot_type="lineplot",
    dark_mode=False,
    grid=False,
    figsize=(12, 8),
    dpi=300,
    save_fig=True,
    show_fig=False,
    x_label=None,
    y_label=None,
    hue=None,
    palette=None,
    folder=None,
    **kwargs
)
```


Plotting all pandas dataframes as `oneliner`.

!!! warning
    All defined functions of`ai2business.visualization.data_visualization` will be
    called via `getattr`, so be sure that the `class DataVisualization` function
    is typed correctly.

Args:
    df (pd.DataFrame): [description]
    plot_type (str, optional): [description]. Defaults to "lineplot".
    dark_mode (bool, optional): [description]. Defaults to False.
    grid (bool, optional): [description]. Defaults to False.
    figsize (tuple, optional): [description]. Defaults to (12, 8).
    dpi (int, optional): [description]. Defaults to 300.
    save_fig (bool, optional): [description]. Defaults to True.
    show_fig (bool, optional): [description]. Defaults to False.
    x_label (str, optional): [description]. Defaults to None.
    y_label (str, optional): [description]. Defaults to None.
    hue (str, optional): [description]. Defaults to None.
    palette (Union[str, list, dict], optional): [description]. Defaults to None.
    folder (str, optional): [description]. Defaults to None.


----

