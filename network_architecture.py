import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import pandas as pd
from utils import create_expanding_section

def display():
    st.title("Network Architecture of Genesis Bloom")
    st.markdown("""
    Genesis Bloom's network architecture consists of three interconnected layers that work together
    to create a resilient, adaptive, and intelligent system. Each layer serves distinct functions
    while maintaining integration with the others.
    """)
    
    # Create layered network visualization
    st.markdown("## Three-Layer Architecture Visualization")
    create_network_visualization()
    
    # Layer descriptions
    st.markdown("## Layer Details")
    
    layers = {
        "Root Layer": {
            "description": "Local mesh nodes with basic access (open internet, solar/kinetic powered). Resilient to blackout, disaster, or collapse.",
            "details": """
            ### Root Layer
            
            The Root Layer forms the foundation of Genesis Bloom, consisting of local mesh networks that maintain
            basic connectivity and essential functions even during extreme conditions. This layer prioritizes
            resilience and accessibility over advanced features.
            
            #### Key Characteristics:
            - **Local Mesh Networking**: Distributed connection points that can operate independently of central infrastructure
            - **Energy Independence**: Powered by solar, kinetic, and other renewable sources with minimal requirements
            - **Disaster Resilience**: Designed to maintain function during blackouts, natural disasters, or infrastructure collapse
            - **Basic Access Guarantee**: Ensures fundamental connectivity for all participants regardless of resources
            
            #### Technical Implementation:
            - Low-power mesh network protocols (LoRa, Meshtastic, etc.)
            - Minimal computing requirements enabling deployment on diverse hardware
            - Local caching of essential data and services
            - Simple, text-based interfaces for low-bandwidth scenarios
            - Hardware designs optimized for repair and longevity
            
            #### Root Layer Services:
            - Essential messaging and coordination
            - Basic identity verification
            - Local resource exchange facilitation
            - Emergency alerts and response coordination
            - Minimal viable healthcare and educational resources
            """
        },
        "Bloom Layer": {
            "description": "Mid-tier cooperative cloud—handles storage, semantic consensus, and model updates.",
            "details": """
            ### Bloom Layer
            
            The Bloom Layer provides mid-tier infrastructure that connects local networks into a wider ecosystem,
            enabling richer services and broader coordination while maintaining cooperative governance. This layer
            balances functionality with distributed control.
            
            #### Key Characteristics:
            - **Cooperative Cloud**: Distributed storage and computing resources governed by participant communities
            - **Semantic Consensus**: Agreement mechanisms for meaning and interpretation across diverse contexts
            - **Model Propagation**: Distribution of updated AI models, protocols, and system improvements
            - **Regional Coordination**: Connection of local networks into broader regional systems
            
            #### Technical Implementation:
            - Distributed storage systems with erasure coding for redundancy
            - Federated semantic databases and knowledge graphs
            - Incremental model update protocols for efficient synchronization
            - Cross-cultural translation and interpretation services
            - Regional consensus mechanisms with cultural adaptation
            
            #### Bloom Layer Services:
            - Rich media sharing and collaboration
            - Distributed computing for complex modeling
            - Cross-community resource coordination
            - Cultural exchange and translation
            - Intermediate governance processes
            - Health and environmental monitoring
            """
        },
        "Ouroboros Layer": {
            "description": "Meta-reflection layer for system introspection, guided by AI-coach collectives and \"mystic coders.\"",
            "details": """
            ### Ouroboros Layer
            
            The Ouroboros Layer serves as the meta-cognitive function of Genesis Bloom, enabling the system to
            observe, analyze, and improve itself. This layer focuses on long-term patterns, ethical considerations,
            and evolution of the entire ecosystem.
            
            #### Key Characteristics:
            - **System Introspection**: Continuous analysis of Genesis Bloom's own operations and impacts
            - **AI-Coach Collectives**: Hybrid human-AI teams focused on system evolution and wisdom
            - **Mystic Coding**: Integration of diverse wisdom traditions with technical development
            - **Meta-Reflection**: Capacity to consider multiple paradigms and longer timeframes
            
            #### Technical Implementation:
            - System-wide telemetry and health monitoring
            - Long-term pattern recognition across all network activities
            - Multi-paradigmatic modeling frameworks
            - Contemplative computing interfaces for deep analysis
            - Ethical impact assessment protocols
            
            #### Ouroboros Layer Services:
            - Long-term trend analysis and forecasting
            - System evolution guidance
            - Ethical framework development and refinement
            - Cross-paradigm translation and integration
            - Deep anomaly detection and response
            - Wisdom tradition integration and application
            """
        }
    }
    
    # Create tabs for each layer
    tabs = st.tabs(list(layers.keys()))
    
    # Populate each tab with content
    for i, (layer, content) in enumerate(layers.items()):
        with tabs[i]:
            st.markdown(f"### {layer}")
            st.markdown(f"**{content['description']}**")
            st.markdown(content['details'])
    
    # Layer interactions and information flow
    st.markdown("## Layer Interactions and Information Flow")
    st.markdown("""
    The three layers of Genesis Bloom are not isolated tiers but rather form a continuous,
    interconnected system with information and resources flowing in multiple directions.
    """)
    
    create_expanding_section(
        "Bottom-Up Information Flow",
        """
        Data flows from the Root Layer upward, providing real-world feedback:
        
        1. **Root Layer** captures local conditions, needs, and activities through direct interaction
        2. **Bloom Layer** aggregates and analyzes patterns across multiple local networks
        3. **Ouroboros Layer** identifies long-term trends and systemic implications
        
        This bottom-up flow ensures the system remains grounded in lived reality and responsive to
        actual conditions rather than abstract models.
        """
    )
    
    create_expanding_section(
        "Top-Down Intelligence Flow",
        """
        Insights and improvements flow from the Ouroboros Layer downward:
        
        1. **Ouroboros Layer** develops systemic improvements and ethical frameworks
        2. **Bloom Layer** adapts these insights to regional and cultural contexts
        3. **Root Layer** implements practical applications in local environments
        
        This top-down flow enables the system to evolve while respecting local autonomy and adaptation.
        """
    )
    
    create_expanding_section(
        "Horizontal Coordination",
        """
        Each layer also facilitates horizontal coordination between peers:
        
        - **Root Layer**: Local mesh networks connect neighboring communities
        - **Bloom Layer**: Regional networks enable broader resource sharing and coordination
        - **Ouroboros Layer**: Global ethical frameworks and wisdom traditions are integrated
        
        This horizontal coordination creates resilience through diversity and redundancy.
        """
    )
    
    create_expanding_section(
        "Cross-Layer Integration Example: Climate Adaptation",
        """
        In responding to climate change:
        
        1. **Root Layer** captures local environmental changes through sensors and community reports
        2. **Bloom Layer** identifies regional patterns and coordinates resource sharing for adaptation
        3. **Ouroboros Layer** analyzes long-term trends and develops systemic adaptation strategies
        4. These strategies flow back down to the Bloom Layer for regional implementation
        5. Local Root Layer nodes implement specific adaptations suited to their context
        6. Successful adaptations are shared horizontally at each layer
        
        This multi-directional flow creates a learning system that combines immediate response
        with long-term transformation.
        """
    )


def create_network_visualization():
    """Create a visualization of the three-layer network architecture"""
    
    # Create an interactive Plotly visualization of the layered network
    
    # Define node characteristics for each layer
    layers = {
        "Ouroboros Layer": {"color": "rgba(153, 102, 255, 0.8)", "y": 3, "size": 15, "count": 6},
        "Bloom Layer": {"color": "rgba(75, 192, 192, 0.8)", "y": 2, "size": 12, "count": 10},
        "Root Layer": {"color": "rgba(255, 159, 64, 0.8)", "y": 1, "size": 8, "count": 16}
    }
    
    # Generate nodes for each layer
    nodes_x = []
    nodes_y = []
    nodes_text = []
    nodes_size = []
    nodes_color = []
    
    # Generate random but evenly spread x positions
    for layer_name, layer_data in layers.items():
        count = layer_data["count"]
        y = layer_data["y"]
        size = layer_data["size"]
        color = layer_data["color"]
        
        for i in range(count):
            # Create evenly spaced nodes with some random variation
            x = (i / (count - 1)) * 2 - 1  # Scale to -1 to 1
            x += np.random.normal(0, 0.05)  # Add small random offset
            
            nodes_x.append(x)
            nodes_y.append(y)
            nodes_text.append(f"{layer_name} Node")
            nodes_size.append(size)
            nodes_color.append(color)
    
    # Instead of combining all edges, we'll create separate traces for different types of edges
    # This allows proper coloring and better hover text
    
    # List to store all edge traces
    edge_traces = []
    
    # Connect Root to Bloom (upward connections)
    for i in range(layers["Root Layer"]["count"]):
        root_idx = i
        # Connect to nearest Bloom nodes
        for j in range(2):  # Each Root node connects to 2 Bloom nodes
            bloom_idx = layers["Root Layer"]["count"] + (i + j) % layers["Bloom Layer"]["count"]
            
            # Create a trace for this upward connection
            edge_trace = go.Scatter(
                x=[nodes_x[root_idx], nodes_x[bloom_idx], None],
                y=[nodes_y[root_idx], nodes_y[bloom_idx], None],
                line=dict(width=1.5, color='rgba(150, 150, 150, 0.7)'),
                hoverinfo='text',
                text=f"Root→Bloom: Information flow from local to regional",
                mode='lines',
                showlegend=False
            )
            edge_traces.append(edge_trace)
    
    # Connect Bloom to Ouroboros (upward connections)
    for i in range(layers["Bloom Layer"]["count"]):
        bloom_idx = layers["Root Layer"]["count"] + i
        # Connect to nearest Ouroboros nodes
        ouro_idx = layers["Root Layer"]["count"] + layers["Bloom Layer"]["count"] + (i % layers["Ouroboros Layer"]["count"])
        
        # Create a trace for this upward connection
        edge_trace = go.Scatter(
            x=[nodes_x[bloom_idx], nodes_x[ouro_idx], None],
            y=[nodes_y[bloom_idx], nodes_y[ouro_idx], None],
            line=dict(width=1.5, color='rgba(150, 150, 150, 0.7)'),
            hoverinfo='text',
            text=f"Bloom→Ouroboros: Pattern recognition and system analysis",
            mode='lines',
            showlegend=False
        )
        edge_traces.append(edge_trace)
    
    # Create horizontal connections within Root Layer (mesh network)
    for i in range(layers["Root Layer"]["count"]):
        for j in range(i+1, min(i+4, layers["Root Layer"]["count"])):
            # Create a trace for this Root Layer connection
            edge_trace = go.Scatter(
                x=[nodes_x[i], nodes_x[j], None],
                y=[nodes_y[i], nodes_y[j], None],
                line=dict(width=1, color='rgba(255, 159, 64, 0.5)'),
                hoverinfo='text',
                text=f"Root Layer mesh connection: Local community cooperation",
                mode='lines',
                showlegend=False
            )
            edge_traces.append(edge_trace)
    
    # Bloom Layer connections
    bloom_start = layers["Root Layer"]["count"]
    bloom_end = bloom_start + layers["Bloom Layer"]["count"]
    for i in range(bloom_start, bloom_end):
        for j in range(i+1, min(i+4, bloom_end)):
            # Create a trace for this Bloom Layer connection
            edge_trace = go.Scatter(
                x=[nodes_x[i], nodes_x[j], None],
                y=[nodes_y[i], nodes_y[j], None],
                line=dict(width=1, color='rgba(75, 192, 192, 0.5)'),
                hoverinfo='text',
                text=f"Bloom Layer connection: Regional coordination and resource sharing",
                mode='lines',
                showlegend=False
            )
            edge_traces.append(edge_trace)
    
    # Ouroboros Layer connections (fully connected)
    ouro_start = bloom_end
    ouro_end = ouro_start + layers["Ouroboros Layer"]["count"]
    for i in range(ouro_start, ouro_end):
        for j in range(i+1, ouro_end):
            # Create a trace for this Ouroboros Layer connection
            edge_trace = go.Scatter(
                x=[nodes_x[i], nodes_x[j], None],
                y=[nodes_y[i], nodes_y[j], None],
                line=dict(width=1, color='rgba(153, 102, 255, 0.5)'),
                hoverinfo='text',
                text=f"Ouroboros Layer connection: System introspection and meta-analysis",
                mode='lines',
                showlegend=False
            )
            edge_traces.append(edge_trace)
            
    # Create legend traces (invisible traces just for the legend)
    root_legend = go.Scatter(
        x=[None], y=[None],
        line=dict(width=1, color='rgba(255, 159, 64, 0.8)'),
        mode='lines',
        name="Root Layer Connections",
        showlegend=True
    )
    
    bloom_legend = go.Scatter(
        x=[None], y=[None],
        line=dict(width=1, color='rgba(75, 192, 192, 0.8)'),
        mode='lines',
        name="Bloom Layer Connections",
        showlegend=True
    )
    
    ouroboros_legend = go.Scatter(
        x=[None], y=[None],
        line=dict(width=1, color='rgba(153, 102, 255, 0.8)'),
        mode='lines',
        name="Ouroboros Layer Connections",
        showlegend=True
    )
    
    vertical_legend = go.Scatter(
        x=[None], y=[None],
        line=dict(width=1.5, color='rgba(150, 150, 150, 0.7)'),
        mode='lines',
        name="Cross-Layer Connections",
        showlegend=True
    )
    
    # Create the figure
    fig = go.Figure()
    
    # Add all edge traces
    for trace in edge_traces:
        fig.add_trace(trace)
    
    # Add legend traces
    fig.add_trace(root_legend)
    fig.add_trace(bloom_legend)
    fig.add_trace(ouroboros_legend)
    fig.add_trace(vertical_legend)
    
    # Add nodes
    fig.add_trace(go.Scatter(
        x=nodes_x, y=nodes_y,
        mode='markers',
        marker=dict(
            size=nodes_size,
            color=nodes_color,
            line=dict(width=1, color='rgb(50,50,50)')
        ),
        text=nodes_text,
        hoverinfo='text',
        name="Nodes",
        showlegend=False
    ))
    
    # Add layer labels
    for layer_name, layer_data in layers.items():
        fig.add_annotation(
            x=-1.2,
            y=layer_data["y"],
            text=layer_name,
            showarrow=False,
            font=dict(size=14)
        )
    
    # Update layout with improved legend
    fig.update_layout(
        showlegend=True,
        hovermode='closest',
        margin=dict(b=10,l=10,r=10,t=10),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.3, 1.1]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.8, 3.2]),
        height=500,
        plot_bgcolor='rgba(255,255,255,0.8)',
        legend=dict(
            yanchor="top",
            y=0.99,
            xanchor="left",
            x=0.01,
            bgcolor="rgba(255, 255, 255, 0.7)",
            bordercolor="rgba(0, 0, 0, 0.2)",
            borderwidth=1
        )
    )
    
    st.plotly_chart(fig, use_container_width=True)
    
    # Add legend explaining the visualization
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("""
        **Root Layer** 
        <span style='color: rgb(255, 159, 64);'>●</span> Local mesh network
        """, unsafe_allow_html=True)
    with col2:
        st.markdown("""
        **Bloom Layer** 
        <span style='color: rgb(75, 192, 192);'>●</span> Cooperative cloud
        """, unsafe_allow_html=True)
    with col3:
        st.markdown("""
        **Ouroboros Layer** 
        <span style='color: rgb(153, 102, 255);'>●</span> Meta-reflection system
        """, unsafe_allow_html=True)
