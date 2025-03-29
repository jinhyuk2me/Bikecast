import osmnx as ox

# 예: 서울 자전거도로
G = ox.graph_from_place("Seoul, South Korea", network_type='bike')

# 좌표 추출
edges = ox.graph_to_gdfs(G, nodes=False)
for _, row in edges.iterrows():
    print(row['geometry'])  # 자전거도로 선형 정보
