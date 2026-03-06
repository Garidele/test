import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

pos = {
    1: (-3,  1), 2: (-4, -1), 3: (-2, -1),
    4: ( 0,  1), 5: (-1, -1), 6: ( 1, -1),
    7: ( 3,  1), 8: ( 2, -1), 9: ( 4, -1),
}

original_edges = [
    (1,3),(3,2),(2,1),
    (4,5),(5,6),(6,4),
    (7,9),(9,8),(8,7),
]

added_within = [
    (1,2),(2,3),(3,1),
    (4,6),(6,5),(5,4),
    (7,8),(8,9),(9,7),
]

scc1_to_scc2 = [(u,v) for u in [1,2,3] for v in [4,5,6]]
scc1_to_scc3 = [(u,v) for u in [1,2,3] for v in [7,8,9]]
scc2_to_scc3 = [(u,v) for u in [4,5,6] for v in [7,8,9]]
added_between = scc1_to_scc2 + scc1_to_scc3 + scc2_to_scc3

G = nx.DiGraph()
G.add_nodes_from(range(1, 10))
G.add_edges_from(original_edges)
G.add_edges_from(added_within)
G.add_edges_from(added_between)

node_colors = {1:'#4C9BE8', 2:'#4C9BE8', 3:'#4C9BE8',
               4:'#E8844C', 5:'#E8844C', 6:'#E8844C',
               7:'#4CE87A', 8:'#4CE87A', 9:'#4CE87A'}
colors = [node_colors[n] for n in G.nodes()]

fig, ax = plt.subplots(figsize=(14, 8))
ax.set_facecolor('#1e1e2e')
fig.patch.set_facecolor('#1e1e2e')

nx.draw_networkx_edges(G, pos, edgelist=added_between,
    edge_color='#888888', alpha=0.35, arrows=True, arrowsize=12,
    connectionstyle='arc3,rad=0.15', width=0.8, ax=ax)

nx.draw_networkx_edges(G, pos, edgelist=added_within,
    edge_color='white', alpha=0.7, arrows=True, arrowsize=15,
    style='dashed', connectionstyle='arc3,rad=0.25', width=1.5, ax=ax)

nx.draw_networkx_edges(G, pos, edgelist=original_edges,
    edge_color='yellow', alpha=1.0, arrows=True, arrowsize=20,
    connectionstyle='arc3,rad=0.1', width=2.5, ax=ax)

nx.draw_networkx_nodes(G, pos, node_color=colors, node_size=800, ax=ax)
nx.draw_networkx_labels(G, pos, font_color='white', font_size=13, font_weight='bold', ax=ax)

legend_handles = [
    mpatches.Patch(color='#4C9BE8', label='SCC₁  {1, 2, 3}'),
    mpatches.Patch(color='#E8844C', label='SCC₂  {4, 5, 6}'),
    mpatches.Patch(color='#4CE87A', label='SCC₃  {7, 8, 9}'),
    mpatches.Patch(color='yellow',  label='Original arcs (9)'),
    mpatches.Patch(color='white',   label='Added within-SCC arcs (9)'),
    mpatches.Patch(color='#888888', label='Added between-SCC arcs (27)'),
]
ax.legend(handles=legend_handles, loc='lower center', ncol=2,
          facecolor='#2e2e3e', labelcolor='white', fontsize=10, framealpha=0.9)

ax.set_title('Directed Graph – Original + 36 Added Arcs\n(3 SCCs preserved)',
             color='white', fontsize=15, pad=12)
ax.axis('off')
plt.tight_layout()
plt.savefig('graph_sccs.png', dpi=150, bbox_inches='tight')
print("Saved as graph_sccs.png")
