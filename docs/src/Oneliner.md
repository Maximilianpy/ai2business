<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/macros/oneliner.py#L22)</span>

### TrendSearch


```python
ai2business.macros.oneliner.TrendSearch(*args, **kwargs)
```


Here is collection of *oneliner* for trend search.

!!! example "What is an *oneliner*?"

    Oneliner is a function that can be executed in one line and contains all essential
    parameters. No further introductions are needed.

## A four step search is searching:

    1. Overtime
    2. By regions
    3. By related topics
    4. By related queries


----

<span style="float:right;">[[source]](https://github.com/ai2business/ai2business/blob/main/ai2business/macros/oneliner.py#L38)</span>

### four_step_search


```python
TrendSearch.four_step_search(
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

A four step search is searching:

1. Overtime
2. By regions
3. By related topics
4. By related queries

Args:
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

