# import pandas as pd
# import altair as alt
# data = pd.DataFrame({'Categories': ['Cloting',
#                                     'Electronics',
#                                     'Furniture',
#                                     'Health',
#                                     'Kitchen'],
#                      'Sales': [110, 343, 201, 120, 278]})
# print(data)
# a = alt.Chart(data).mark_bar().encode(
#     x='Categories',
#     y='Sales'
# )

# wide_form = pd.DataFrame({'Year': [2018, 2019, 2020],
#                           'Clothing': [110, 101, 129],
#                           'Furniture': [201, 184, 195],
#                           'Health': [120, 132, 133]})
# print(wide_form)
# base = alt.Chart(wide_form)
# bar = base.mark_line().encode(
#     x='Year:O',
#     y='Furniture:Q',
#     color='Category:N').properties(
#     height=400,
#     width=600,
#     title='Furniture by year'
# )
# print(bar)

import altair as alt
import pandas_practice as pd
from vega_datasets import data
# # data.world_110m()['objects']['countries']
# contries = alt.topo_feature(data.world_110m.url, 'countries')
# print(contries)
# alt.Chart(contries, width=600).mark_geoshape(fill='skyblue', stroke='grey').project('ortographic')
# world_offices = pd.DataFrame({'City': ['Tokio', 'Santiago'],
#                               'Latitude': [35.65, -33.45],
#                               'Longitude': [139.84, -70.67],
#                               'NumEmployees': [20,67]})
# print(world_offices)
# background = alt.Chart(countries, width=600).mark_geoshape(fill='skyblue', stroke='grey', opacity= 0.4).project('equirectangular')
