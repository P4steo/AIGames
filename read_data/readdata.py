import pandas as p

route_definitions = p.read_csv('datasets/route_definitions.csv')

print(route_definitions.to_string())