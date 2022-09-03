from copy import deepcopy
from typing import Union, Optional, List

import numpy as np
import matplotlib.pyplot as plt

from dhg.structure.graphs import Graph, DiGraph, BiGraph
from dhg.structure.hypergraphs import Hypergraph

from .layout import force_layout, bipartite_force_layout
from .utils import draw_vertex, draw_line_edge, draw_circle_edge

from .defaults import (
    default_style,
    default_size,
    default_strength,
    default_bipartite_style,
    default_bipartite_size,
    default_bipartite_strength,
    default_hypergraph_style,
    default_hypergraph_strength,
)


def draw_graph(
    g: "Graph",
    e_style: str = "line",
    v_label: Optional[List[str]] = None,
    v_size: Union[float, list] = 1.0,
    v_color: Union[str, list] = "r",
    v_line_width: Union[str, list] = 1.0,
    e_color: Union[str, list] = "gray",
    e_fill_color: Union[str, list] = "whitesmoke",
    e_line_width: Union[str, list] = 1.0,
    font_size: int = 1.0,
    font_family: str = "sans-serif",
    push_v_strength: float = 1.0,
    push_e_strength: float = 1.0,
    pull_e_strength: float = 1.0,
    pull_center_strength: float = 1.0,
):
    assert e_style in ["line", "circle"], "e_style must be 'line' or 'circle'"
    assert g.num_e > 0, "g must be a non-empty structure"
    fig, ax = plt.subplots(figsize=(6, 6))
    num_v, e_list = g.num_v, deepcopy(g.e[0])
    # default configures
    v_color, e_color, e_fill_color = default_style(g.num_v, g.num_e, v_color, e_color, e_fill_color)
    v_size, v_line_width, e_line_width, font_size = default_size(num_v, e_list, v_size, v_line_width, e_line_width)
    (push_v_strength, push_e_strength, pull_e_strength, pull_center_strength,) = default_strength(
        num_v, e_list, push_v_strength, push_e_strength, pull_e_strength, pull_center_strength,
    )
    # layout
    v_coor = force_layout(num_v, e_list, push_v_strength, None, pull_e_strength, pull_center_strength)

    if e_style == "line":
        draw_line_edge(
            ax, v_coor, v_size, e_list, False, e_color, e_line_width,
        )
    elif e_style == "circle":
        draw_circle_edge(
            ax, v_coor, v_size, e_list, e_color, e_fill_color, e_line_width,
        )

    draw_vertex(
        ax, v_coor, v_label, font_size, font_family, v_size, v_color, v_line_width,
    )

    plt.xlim((0, 1.0))
    plt.ylim((0, 1.0))
    plt.axis("off")

    fig.tight_layout()


def draw_digraph(
    g: "DiGraph",
    e_style: str = "line",
    v_label: Optional[List[str]] = None,
    v_size: Union[float, list] = 1.0,
    v_color: Union[str, list] = "r",
    v_line_width: Union[str, list] = 1.0,
    e_color: Union[str, list] = "gray",
    e_line_width: Union[str, list] = 1.0,
    font_size: int = 1.0,
    font_family: str = "sans-serif",
    push_v_strength: float = 1.0,
    push_e_strength: float = 1.0,
    pull_e_strength: float = 1.0,
    pull_center_strength: float = 1.0,
):
    assert e_style in ["line"], "e_style must be 'line'"
    assert g.num_e > 0, "g must be a non-empty structure"
    fig, ax = plt.subplots(figsize=(6, 6))
    num_v, e_list = g.num_v, deepcopy(g.e[0])
    # default configures
    v_color, e_color, _ = default_style(g.num_v, g.num_e, v_color, e_color, None)
    v_size, v_line_width, e_line_width, font_size = default_size(num_v, e_list, v_size, v_line_width, e_line_width)
    (push_v_strength, push_e_strength, pull_e_strength, pull_center_strength,) = default_strength(
        num_v, e_list, push_v_strength, push_e_strength, pull_e_strength, pull_center_strength,
    )
    # layout
    v_coor = force_layout(num_v, e_list, push_v_strength, None, pull_e_strength, pull_center_strength)

    if e_style == "line":
        draw_line_edge(
            ax, v_coor, v_size, e_list, True, e_color, e_line_width,
        )
    else:
        raise ValueError("e_style must be 'line'")

    draw_vertex(
        ax, v_coor, v_label, font_size, font_family, v_size, v_color, v_line_width,
    )

    plt.xlim((0, 1.0))
    plt.ylim((0, 1.0))
    plt.axis("off")

    fig.tight_layout()


def draw_bigraph(
    g: "BiGraph",
    e_style: str = "line",
    u_label: Optional[List[str]] = None,
    u_size: Union[float, list] = 1.0,
    u_color: Union[str, list] = "m",
    u_line_width: Union[str, list] = 1.0,
    v_label: Optional[List[str]] = None,
    v_size: Union[float, list] = 1.0,
    v_color: Union[str, list] = "r",
    v_line_width: Union[str, list] = 1.0,
    e_color: Union[str, list] = "gray",
    e_line_width: Union[str, list] = 1.0,
    u_font_size: float = 1.0,
    v_font_size: float = 1.0,
    font_family: str = "sans-serif",
    push_u_strength: float = 1.0,
    push_v_strength: float = 1.0,
    push_e_strength: float = 1.0,
    pull_e_strength: float = 1.0,
    pull_u_center_strength: float = 1.0,
    pull_v_center_strength: float = 1.0,
):
    assert e_style in ["line"], "e_style must be 'line'"
    assert g.num_e > 0, "g must be a non-empty structure"
    fig, ax = plt.subplots(figsize=(6, 6))
    num_u, num_v, e_list = g.num_u, g.num_v, deepcopy(g.e[0])
    # default configures
    u_color, v_color, e_color, _ = default_bipartite_style(num_u, num_v, g.num_e, u_color, v_color, e_color, None)
    (u_size, u_line_width, v_size, v_line_width, e_line_width, u_font_size, v_font_size,) = default_bipartite_size(
        num_u, num_v, e_list, u_size, u_line_width, v_size, v_line_width, e_line_width, u_font_size, v_font_size,
    )
    (
        push_u_strength,
        push_v_strength,
        push_e_strength,
        pull_e_strength,
        pull_u_center_strength,
        pull_v_center_strength,
    ) = default_bipartite_strength(
        num_u,
        num_v,
        e_list,
        push_u_strength,
        push_v_strength,
        push_e_strength,
        pull_e_strength,
        pull_u_center_strength,
        pull_v_center_strength,
    )
    # layout
    u_coor, v_coor = bipartite_force_layout(
        num_u,
        num_v,
        e_list,
        push_u_strength,
        push_v_strength,
        None,
        pull_e_strength,
        pull_u_center_strength,
        pull_v_center_strength,
    )

    # preprocess
    e_list = [(u, v + num_u) for u, v in e_list]
    if e_style == "line":
        draw_line_edge(
            ax, np.vstack([u_coor, v_coor]), u_size + v_size, e_list, False, e_color, e_line_width,
        )
    else:
        raise ValueError("e_style must be 'line'")

    draw_vertex(
        ax,
        np.vstack([u_coor, v_coor]),
        u_label + v_label if u_label is not None and v_label is not None else None,
        u_font_size + v_font_size,
        font_family,
        u_size + v_size,
        u_color + v_color,
        u_line_width + v_line_width,
    )

    plt.xlim((0, 1.0))
    plt.ylim((0, 1.0))
    plt.axis("off")

    fig.tight_layout()


def draw_hypergraph(
    g: "Hypergraph",
    e_style: str = "circle",
    v_label: Optional[List[str]] = None,
    v_size: Union[float, list] = 1.0,
    v_color: Union[str, list] = "r",
    v_line_width: Union[str, list] = 1.0,
    e_color: Union[str, list] = "gray",
    e_fill_color: Union[str, list] = "whitesmoke",
    e_line_width: Union[str, list] = 1.0,
    font_size: float = 1.0,
    font_family: str = "sans-serif",
    push_v_strength: float = 1.0,
    push_e_strength: float = 1.0,
    pull_e_strength: float = 1.0,
    pull_center_strength: float = 1.0,
):
    assert e_style in ["circle"], "e_style must be 'circle'"
    assert g.num_e > 0, "g must be a non-empty structure"
    fig, ax = plt.subplots(figsize=(6, 6))

    num_v, e_list = g.num_v, deepcopy(g.e[0])
    # default configures
    v_color, e_color, e_fill_color = default_hypergraph_style(g.num_v, g.num_e, v_color, e_color, e_fill_color)
    v_size, v_line_width, e_line_width, font_size = default_size(num_v, e_list, v_size, v_line_width, e_line_width)
    (push_v_strength, push_e_strength, pull_e_strength, pull_center_strength,) = default_hypergraph_strength(
        num_v, e_list, push_v_strength, push_e_strength, pull_e_strength, pull_center_strength,
    )
    # layout
    v_coor = force_layout(num_v, e_list, push_v_strength, push_e_strength, pull_e_strength, pull_center_strength)
    if e_style == "circle":
        draw_circle_edge(
            ax, v_coor, v_size, e_list, e_color, e_fill_color, e_line_width,
        )
    else:
        raise ValueError("e_style must be 'circle'")

    draw_vertex(
        ax, v_coor, v_label, font_size, font_family, v_size, v_color, v_line_width,
    )

    plt.xlim((0, 1.0))
    plt.ylim((0, 1.0))
    plt.axis("off")

    fig.tight_layout()