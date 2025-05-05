import streamlit as st
import networkx as nx
import numpy as np
import pandas as pd
import plotly.graph_objects as go
import time
import random
from utils import create_expanding_section
from database import store_simulation_result, get_all_simulation_results, get_simulation_result

def display():
    st.title("Interactive Genesis Bloom Simulation")
    st.markdown("""
    This simulation demonstrates how the components of Genesis Bloom interact in various scenarios.
    Observe how information flows through the system, how resources are allocated, and how the network
    responds to different challenges. The simulation will also generate practical use cases based on the results.
    """)
    
    # Create tabs for simulation and history
    tab1, tab2 = st.tabs(["Run Simulation", "Simulation History"])
    
    with tab1:
        # Simulation explanation
        st.markdown("""
        ## How This Simulation Works
        
        This interactive model represents a simplified version of Genesis Bloom's components and their interactions.
        Each node represents a different part of the system, and connections show information and resource flows.
        
        The simulation demonstrates three key aspects of Genesis Bloom:
        1. **Network Resilience**: How the system maintains functionality when components fail
        2. **Resource Allocation**: How resources flow to where they're needed most
        3. **Collective Intelligence**: How information propagates and leads to system adaptation
        """)
        
        # Simulation controls
        st.markdown("## Simulation Controls")
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            scenario = st.selectbox(
                "Select scenario:",
                ["Normal Operation", "Resource Scarcity Event", "Node Failure", "Governance Challenge"]
            )
        
        with col2:
            speed = st.slider("Simulation Speed", min_value=1, max_value=10, value=5)
            speed_factor = 0.2 / speed  # Convert to delay time
        
        with col3:
            if "simulation_running" not in st.session_state:
                st.session_state.simulation_running = False
                st.session_state.simulation_step = 0
            
            if st.button("Start/Reset Simulation"):
                st.session_state.simulation_running = True
                st.session_state.simulation_step = 0
                st.rerun()
        
        # Create placeholders for simulation visualization and status
        simulation_viz = st.empty()
        simulation_status = st.empty()
        simulation_metrics = st.empty()
        
        # Run simulation if active
        if st.session_state.simulation_running:
            run_simulation(scenario, speed_factor, simulation_viz, simulation_status, simulation_metrics)
        else:
            simulation_status.info("Click 'Start Simulation' to begin the demonstration")
        
        # Additional explanation based on scenario
        st.markdown("## Scenario Details")
        
        scenario_details = {
            "Normal Operation": """
                Under normal operating conditions, Genesis Bloom demonstrates:
                
                - Regular information flow between all system components
                - Balanced resource distribution according to needs
                - Continuous low-level adaptation and learning
                - Stable governance processes with distributed decision-making
                
                This represents the baseline functioning of the system when no significant
                challenges or disruptions are present.
            """,
            "Resource Scarcity Event": """
                During a resource scarcity event, Genesis Bloom activates:
                
                - Need detection through PSI Nodes and Harmonic Resource Mesh
                - BloomKernel AI optimization to identify efficient resource allocation
                - SpiralDAO emergency prioritization protocols
                - Chain of Trust verification of all resource transfers
                - Sentinel Layer monitoring for resource capture or hoarding
                
                This scenario demonstrates how the system ensures basic needs are met
                even when total resources are constrained.
            """,
            "Node Failure": """
                When nodes fail or become compromised, Genesis Bloom demonstrates:
                
                - Automatic detection of failures through heartbeat protocols
                - Rerouting of network traffic around damaged nodes
                - Resource reallocation to compensate for lost capacity
                - Sentinel Layer investigation of potential attacks
                - Self-healing protocols to repair or replace damaged components
                
                This scenario demonstrates the system's resilience in the face of
                both accidental failures and deliberate attacks.
            """,
            "Governance Challenge": """
                During governance challenges such as contentious decisions, Genesis Bloom activates:
                
                - SpiralDAO deliberation processes with increased participation
                - Sentinel Layer monitoring for manipulation or capture attempts
                - BloomKernel AI modeling of various outcome scenarios
                - PSI Node representation of diverse perspectives
                - Ouroboros Layer ethical review of decision processes
                
                This scenario demonstrates how the system handles complex governance
                situations that involve competing values or interests.
            """
        }
        
        st.markdown(scenario_details[scenario])
        
        # Educational insights from the simulation
        st.markdown("## Key Insights from This Simulation")
        
        create_expanding_section(
            "Emergent Intelligence",
            """
            The simulation demonstrates how intelligence emerges from the interactions of simpler components.
            No single node contains the complete "intelligence" of Genesis Bloom; rather, it emerges from:
            
            - Pattern recognition across distributed data sources
            - Feedback loops between sensing and action
            - Multi-level processing from local to global
            - Evolutionary selection of successful adaptations
            
            This emergent intelligence allows the system to respond to novel situations without
            requiring explicit programming for every possible scenario.
            """
        )
        
        create_expanding_section(
            "Resilience Through Redundancy",
            """
            Genesis Bloom's resilience comes from strategic redundancy:
            
            - Multiple nodes can perform similar functions
            - Information is stored across distributed locations
            - Decision-making processes have multiple pathways
            - Resources can flow through alternative routes
            
            Unlike inefficient redundancy that simply duplicates everything, Genesis Bloom
            uses strategic redundancy focused on critical functions and likely failure points.
            """
        )
        
        create_expanding_section(
            "Balance of Autonomy and Coordination",
            """
            The simulation reveals how Genesis Bloom balances local autonomy with global coordination:
            
            - Nodes make independent decisions based on local information
            - Coordination emerges through shared protocols rather than central control
            - Higher-level patterns influence but don't dictate local actions
            - System-wide goals are achieved without centralized management
            
            This balance allows for both efficient response to local conditions and
            coherent action at the system level.
            """
        )


def run_simulation(scenario, speed_factor, viz_placeholder, status_placeholder, metrics_placeholder):
    """Run the interactive simulation based on the selected scenario"""
    
    # Create placeholder for use cases
    if "use_cases_placeholder" not in st.session_state:
        st.session_state.use_cases_placeholder = st.empty()
    
    # Simulation parameters based on scenario
    params = {
        "Normal Operation": {
            "node_failure_rate": 0.005,
            "resource_growth_rate": 0.02,
            "resource_consumption_rate": 0.018,
            "information_flow_rate": 0.08,
            "governance_challenge_rate": 0.01
        },
        "Resource Scarcity Event": {
            "node_failure_rate": 0.008,
            "resource_growth_rate": 0.005,
            "resource_consumption_rate": 0.025,
            "information_flow_rate": 0.1,
            "governance_challenge_rate": 0.03
        },
        "Node Failure": {
            "node_failure_rate": 0.05,
            "resource_growth_rate": 0.015,
            "resource_consumption_rate": 0.02,
            "information_flow_rate": 0.12,
            "governance_challenge_rate": 0.025
        },
        "Governance Challenge": {
            "node_failure_rate": 0.008,
            "resource_growth_rate": 0.018,
            "resource_consumption_rate": 0.018,
            "information_flow_rate": 0.15,
            "governance_challenge_rate": 0.08
        }
    }
    
    # Initialize or get network from session state
    if st.session_state.simulation_step == 0:
        G = initialize_network()
        node_status = {node: "healthy" for node in G.nodes()}
        node_resources = {node: 100 for node in G.nodes()}
        metrics_history = {
            "steps": [],
            "healthy_nodes": [],
            "total_resources": [],
            "information_flow": [],
            "governance_consensus": []
        }
    else:
        G = st.session_state.network
        node_status = st.session_state.node_status
        node_resources = st.session_state.node_resources
        metrics_history = st.session_state.metrics_history
    
    # Simulation step
    if st.session_state.simulation_step < 100:  # Run for 100 steps maximum
        # Update simulation state
        G, node_status, node_resources, metrics = update_simulation(
            G, node_status, node_resources, params[scenario]
        )
        
        # Store updated state
        st.session_state.network = G
        st.session_state.node_status = node_status
        st.session_state.node_resources = node_resources
        
        # Update metrics history
        metrics_history["steps"].append(st.session_state.simulation_step)
        metrics_history["healthy_nodes"].append(metrics["healthy_nodes"])
        metrics_history["total_resources"].append(metrics["total_resources"])
        metrics_history["information_flow"].append(metrics["information_flow"])
        metrics_history["governance_consensus"].append(metrics["governance_consensus"])
        st.session_state.metrics_history = metrics_history
        
        # Update visualization
        visualize_network(G, node_status, node_resources, viz_placeholder)
        
        # Update status message based on simulation events
        status_message = get_status_message(scenario, st.session_state.simulation_step, metrics)
        status_placeholder.info(status_message)
        
        # Display metrics
        display_metrics(metrics_history, metrics_placeholder)
        
        # Increment step
        st.session_state.simulation_step += 1
        
        # Add delay based on speed factor
        time.sleep(speed_factor)
        
        # Rerun to continue simulation
        st.rerun()
    else:
        # Simulation complete
        status_placeholder.success("Simulation complete! Click 'Start/Reset Simulation' to run again.")
        
        # Final visualization
        visualize_network(G, node_status, node_resources, viz_placeholder)
        
        # Final metrics
        display_metrics(metrics_history, metrics_placeholder)
        
        # Generate use cases
        use_cases = generate_use_cases(scenario, G, node_status, node_resources, metrics_history)
        st.session_state.use_cases_placeholder.markdown(use_cases)
        
        # Store simulation results in the database (with error handling)
        try:
            simulation_id = store_simulation_result(
                scenario=scenario,
                steps=st.session_state.simulation_step,
                metrics_history=metrics_history,
                use_cases_markdown=use_cases
            )
            if simulation_id:
                st.success(f"Simulation results saved to database (ID: {simulation_id}).")
            else:
                st.warning("Could not save results to database, but simulation completed successfully.")
        except Exception as e:
            st.warning(f"Simulation completed successfully, but results could not be saved to database: {str(e)}")
            # Continue without database saving


def initialize_network():
    """Create the initial network for the simulation"""
    
    G = nx.DiGraph()
    
    # Add nodes for each component type
    component_counts = {
        "NovaChain": 5,
        "BloomKernel": 4,
        "PSI Node": 8,
        "Resource Mesh": 6,
        "SpiralDAO": 5,
        "Sentinel": 3
    }
    
    node_id = 0
    for component, count in component_counts.items():
        for i in range(count):
            G.add_node(node_id, component_type=component, layer="")
            node_id += 1
    
    # Assign layers to nodes (for visualization)
    for node in G.nodes():
        component = G.nodes[node]["component_type"]
        if component in ["NovaChain", "Resource Mesh"]:
            G.nodes[node]["layer"] = "Root"
        elif component in ["BloomKernel", "SpiralDAO"]:
            G.nodes[node]["layer"] = "Bloom"
        else:  # PSI Node or Sentinel
            if node % 3 == 0:  # Distribute PSI nodes across layers
                G.nodes[node]["layer"] = "Bloom"
            elif node % 3 == 1:
                G.nodes[node]["layer"] = "Ouroboros"
            else:
                G.nodes[node]["layer"] = "Root"
    
    # Create connections between components based on system architecture
    nodes_list = list(G.nodes())
    for i in range(len(nodes_list)):
        # Each node connects to 3-5 other nodes
        num_connections = random.randint(3, 5)
        possible_targets = list(range(len(nodes_list)))
        possible_targets.remove(i)  # Remove self from targets
        targets = random.sample(possible_targets, min(num_connections, len(possible_targets)))
        
        for target in targets:
            # Add weighted edge
            weight = random.uniform(0.5, 1.0)
            G.add_edge(i, target, weight=weight)
    
    return G


def update_simulation(G, node_status, node_resources, params):
    """Update simulation state for one step"""
    
    # Extract parameters
    node_failure_rate = params["node_failure_rate"]
    resource_growth_rate = params["resource_growth_rate"]
    resource_consumption_rate = params["resource_consumption_rate"]
    information_flow_rate = params["information_flow_rate"]
    governance_challenge_rate = params["governance_challenge_rate"]
    
    # Process node failures and recoveries
    for node in G.nodes():
        if node_status[node] == "healthy":
            # Chance of failure
            if random.random() < node_failure_rate:
                node_status[node] = "failing"
        elif node_status[node] == "failing":
            # Failing nodes might recover or become compromised
            if random.random() < 0.3:
                node_status[node] = "healthy"
            elif random.random() < 0.2:
                node_status[node] = "compromised"
        elif node_status[node] == "compromised":
            # Compromised nodes might be repaired
            if random.random() < 0.1:
                node_status[node] = "healthy"
    
    # Process resource changes
    for node in G.nodes():
        component_type = G.nodes[node]["component_type"]
        
        # Resource generation
        if component_type == "Resource Mesh" and node_status[node] != "compromised":
            node_resources[node] += random.uniform(5, 15) * resource_growth_rate
        
        # Resource consumption
        node_resources[node] -= random.uniform(1, 5) * resource_consumption_rate
        
        # Minimum resource level
        node_resources[node] = max(node_resources[node], 0)
    
    # Resource distribution based on need
    for i in range(5):  # Multiple passes to simulate flow
        resource_nodes = sorted(node_resources.items(), key=lambda x: x[1], reverse=True)
        for donor_node, resource in resource_nodes:
            if resource > 120 and node_status[donor_node] != "compromised":
                # Find most needy connected node
                needy_nodes = []
                for target in G.successors(donor_node):
                    if node_resources[target] < 80 and node_status[target] != "compromised":
                        needy_nodes.append((target, node_resources[target]))
                
                if needy_nodes:
                    # Sort by need level
                    needy_nodes.sort(key=lambda x: x[1])
                    target = needy_nodes[0][0]
                    
                    # Transfer resources
                    transfer_amount = random.uniform(5, 15)
                    node_resources[donor_node] -= transfer_amount
                    node_resources[target] += transfer_amount
    
    # Calculate metrics
    metrics = {}
    
    # Count healthy nodes
    healthy_count = sum(1 for status in node_status.values() if status == "healthy")
    metrics["healthy_nodes"] = healthy_count / len(node_status) * 100
    
    # Total resources
    metrics["total_resources"] = sum(node_resources.values())
    
    # Information flow (simulated)
    metrics["information_flow"] = min(100, sum(G.edges[e]["weight"] for e in G.edges()) * information_flow_rate)
    
    # Governance consensus (simulated)
    base_consensus = 85  # Base level
    challenge_effect = random.uniform(0, 30) * governance_challenge_rate
    recovery_effect = healthy_count / len(node_status) * 15
    metrics["governance_consensus"] = min(100, max(0, base_consensus - challenge_effect + recovery_effect))
    
    return G, node_status, node_resources, metrics


def visualize_network(G, node_status, node_resources, placeholder):
    """Visualize the current state of the network"""
    
    # Create Plotly figure
    fig = go.Figure()
    
    # Define node colors based on status
    colors = {
        "healthy": "rgba(75, 192, 192, 0.8)",
        "failing": "rgba(255, 159, 64, 0.8)",
        "compromised": "rgba(255, 99, 132, 0.8)"
    }
    
    # Define layer positions
    layer_y = {
        "Root": 1,
        "Bloom": 2,
        "Ouroboros": 3
    }
    
    # Create a positions dictionary
    pos = {}
    for node in G.nodes():
        layer = G.nodes[node]["layer"]
        component = G.nodes[node]["component_type"]
        
        # Position nodes within their layer, with some component-based clustering
        component_offset = {
            "NovaChain": -0.6,
            "BloomKernel": -0.2,
            "PSI Node": 0.2,
            "Resource Mesh": 0.6,
            "SpiralDAO": 0.0,
            "Sentinel": 0.4
        }.get(component, 0)
        
        # Add some random variation
        random_offset = random.uniform(-0.2, 0.2)
        
        # Calculate position
        layer_count = sum(1 for n in G.nodes() if G.nodes[n]["layer"] == layer)
        layer_position = list(G.nodes()).index(node) % layer_count
        
        x = -1 + (2 * layer_position / max(1, layer_count - 1)) + component_offset + random_offset
        y = layer_y[layer] + random.uniform(-0.2, 0.2)
        
        pos[node] = (x, y)
    
    # Create individual edge traces for better visualization
    for edge in G.edges():
        x0, y0 = pos[edge[0]]
        x1, y1 = pos[edge[1]]
        
        # Calculate resource flow for visualization
        source_resources = node_resources[edge[0]]
        target_resources = node_resources[edge[1]]
        flow = max(0, (source_resources - target_resources) / 100)
        
        # Skip low-flow edges for clarity
        if flow < 0.1:
            continue
        
        # Determine source and target node details for hover information
        source_component = G.nodes[edge[0]]["component_type"]
        target_component = G.nodes[edge[1]]["component_type"]
        source_status = node_status[edge[0]]
        target_status = node_status[edge[1]]
        
        # Create curved edges for better visualization
        cx = (x0 + x1) / 2
        cy = (y0 + y1) / 2 + 0.1
        
        # Edge color based on flow with proper formatting for Plotly
        edge_color = f"rgba(150, 150, 150, {min(1.0, flow + 0.2)})"
        
        # Edge width based on flow
        edge_width = 1 + (flow * 2)
        
        # Hover text
        hover_text = f"Flow: {source_component} → {target_component}<br>"
        hover_text += f"Resource transfer: {int(flow * 10)}<br>"
        hover_text += f"Source status: {source_status}<br>"
        hover_text += f"Target status: {target_status}"
        
        # Add individual edge trace
        fig.add_trace(go.Scatter(
            x=[x0, cx, x1, None],
            y=[y0, cy, y1, None],
            mode='lines',
            line=dict(width=edge_width, color=edge_color),
            hoverinfo='text',
            text=hover_text,
            showlegend=False
        ))
    
    # Add nodes
    node_x = []
    node_y = []
    node_colors = []
    node_sizes = []
    node_text = []
    
    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)
        
        # Node color based on status
        node_colors.append(colors[node_status[node]])
        
        # Node size based on resources
        size = max(10, min(30, node_resources[node] / 10))
        node_sizes.append(size)
        
        # Node text for hover info
        component = G.nodes[node]["component_type"]
        layer = G.nodes[node]["layer"]
        status = node_status[node]
        resources = int(node_resources[node])
        
        node_text.append(f"{component} (ID: {node})<br>Layer: {layer}<br>Status: {status}<br>Resources: {resources}")
    
    # Add node trace
    fig.add_trace(go.Scatter(
        x=node_x, y=node_y,
        mode='markers',
        marker=dict(
            size=node_sizes,
            color=node_colors,
            line=dict(width=1, color='rgb(50,50,50)')
        ),
        text=node_text,
        hoverinfo='text'
    ))
    
    # Update layout
    fig.update_layout(
        showlegend=False,
        hovermode='closest',
        margin=dict(b=10, l=10, r=10, t=10),
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[-1.2, 1.2]),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False, range=[0.8, 3.2]),
        height=600,
        plot_bgcolor='rgba(255,255,255,0.8)'
    )
    
    # Add layer labels
    for layer, y in layer_y.items():
        fig.add_annotation(
            x=-1.1,
            y=y,
            text=layer,
            showarrow=False,
            font=dict(size=14)
        )
    
    # Display in placeholder
    placeholder.plotly_chart(fig, use_container_width=True)


def display_metrics(metrics_history, placeholder):
    """Display simulation metrics over time"""
    
    if not metrics_history["steps"]:
        return
    
    # Create a metrics visualization with improved readability
    fig = go.Figure()
    
    # Add traces with hover templates to show exact values
    fig.add_trace(go.Scatter(
        x=metrics_history["steps"],
        y=metrics_history["healthy_nodes"],
        mode='lines+markers',
        name='Healthy Nodes (%)',
        line=dict(color='rgba(75, 192, 192, 0.8)', width=2),
        marker=dict(size=6, color='rgba(75, 192, 192, 1.0)'),
        hovertemplate='Step: %{x}<br>Healthy Nodes: %{y:.1f}%<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=metrics_history["steps"],
        y=[r/100 for r in metrics_history["total_resources"]],  # Scale for visibility
        mode='lines+markers',
        name='Resources (÷100)',
        line=dict(color='rgba(255, 159, 64, 0.8)', width=2),
        marker=dict(size=6, color='rgba(255, 159, 64, 1.0)'),
        hovertemplate='Step: %{x}<br>Resources: %{y:.1f} × 100<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=metrics_history["steps"],
        y=metrics_history["information_flow"],
        mode='lines+markers',
        name='Information Flow',
        line=dict(color='rgba(54, 162, 235, 0.8)', width=2),
        marker=dict(size=6, color='rgba(54, 162, 235, 1.0)'),
        hovertemplate='Step: %{x}<br>Info Flow: %{y:.1f}<extra></extra>'
    ))
    
    fig.add_trace(go.Scatter(
        x=metrics_history["steps"],
        y=metrics_history["governance_consensus"],
        mode='lines+markers',
        name='Governance Consensus',
        line=dict(color='rgba(153, 102, 255, 0.8)', width=2),
        marker=dict(size=6, color='rgba(153, 102, 255, 1.0)'),
        hovertemplate='Step: %{x}<br>Consensus: %{y:.1f}%<extra></extra>'
    ))
    
    # Current step indicator - vertical line at current step
    current_step = max(metrics_history["steps"]) if metrics_history["steps"] else 0
    fig.add_vline(
        x=current_step, 
        line_width=2, 
        line_dash="dash", 
        line_color="rgba(0, 0, 0, 0.5)",
        annotation_text="Current Step",
        annotation_position="top right"
    )
    
    # Update layout with improved formatting
    fig.update_layout(
        title=dict(
            text='System Metrics Over Time',
            font=dict(size=18)
        ),
        xaxis_title='Simulation Step',
        yaxis_title='Value',
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.02,
            xanchor="right",
            x=1,
            bgcolor="rgba(255, 255, 255, 0.8)",
            bordercolor="rgba(0, 0, 0, 0.2)",
            borderwidth=1
        ),
        height=350,  # Slightly taller for better visibility
        margin=dict(l=20, r=20, t=60, b=30),
        hovermode="x unified",  # Show all traces for a given x value
        plot_bgcolor='rgba(245, 245, 245, 0.5)',  # Light background
        xaxis=dict(
            gridcolor='rgba(200, 200, 200, 0.2)',
            showgrid=True
        ),
        yaxis=dict(
            gridcolor='rgba(200, 200, 200, 0.2)',
            showgrid=True
        )
    )
    
    # Display the chart
    placeholder.plotly_chart(fig, use_container_width=True)
    
    # Display the current metrics values as text below the chart
    if metrics_history["steps"]:
        last_idx = len(metrics_history["steps"]) - 1
        col1, col2, col3, col4 = placeholder.columns(4)
        
        col1.metric(
            "Healthy Nodes", 
            f"{metrics_history['healthy_nodes'][last_idx]:.1f}%",
            delta=f"{metrics_history['healthy_nodes'][last_idx] - metrics_history['healthy_nodes'][max(0, last_idx-10)]:.1f}%"
        )
        
        col2.metric(
            "Total Resources", 
            f"{metrics_history['total_resources'][last_idx]:.0f}",
            delta=f"{metrics_history['total_resources'][last_idx] - metrics_history['total_resources'][max(0, last_idx-10)]:.0f}"
        )
        
        col3.metric(
            "Information Flow", 
            f"{metrics_history['information_flow'][last_idx]:.1f}",
            delta=f"{metrics_history['information_flow'][last_idx] - metrics_history['information_flow'][max(0, last_idx-10)]:.1f}"
        )
        
        col4.metric(
            "Governance Consensus", 
            f"{metrics_history['governance_consensus'][last_idx]:.1f}%",
            delta=f"{metrics_history['governance_consensus'][last_idx] - metrics_history['governance_consensus'][max(0, last_idx-10)]:.1f}%"
        )


def get_status_message(scenario, step, metrics):
    """Generate scenario-specific status messages based on simulation state"""
    
    # Common beginning for all messages
    message = f"Simulation Step: {step} | "
    
    # Add health status
    health_percent = metrics["healthy_nodes"]
    if health_percent > 90:
        message += "Network Health: Excellent | "
    elif health_percent > 70:
        message += "Network Health: Good | "
    elif health_percent > 50:
        message += "Network Health: Fair | "
    else:
        message += "Network Health: Critical | "
    
    # Add scenario-specific messages
    if scenario == "Normal Operation":
        if step < 10:
            message += "System initializing and establishing baseline connections."
        elif step < 30:
            message += "Normal operation patterns stabilizing across all components."
        elif step < 50:
            message += "Resource distribution flowing according to standard parameters."
        elif step < 70:
            message += "Governance processes maintaining system integrity and adaptation."
        else:
            message += "Long-term operational patterns demonstrating system stability. Use cases are being generated."
    
    elif scenario == "Resource Scarcity Event":
        if step < 10:
            message += "Resource pressure detected in multiple nodes."
        elif step < 30:
            message += "BloomKernel optimizing resource allocation priorities."
        elif step < 50:
            message += "Harmonic Resource Mesh redistributing available resources to critical needs."
        elif step < 70:
            message += "SpiralDAO activating emergency resource protocols."
        else:
            message += "System adapting to sustained resource constraints. Use cases are being generated."
    
    elif scenario == "Node Failure":
        if step < 10:
            message += "Detecting compromised nodes in the network."
        elif step < 30:
            message += "Rerouting critical functions around failing components."
        elif step < 50:
            message += "Sentinel Layer analyzing failure patterns for potential attacks."
        elif step < 70:
            message += "Self-healing protocols activating to restore network integrity."
        else:
            message += "Network adaptation stabilizing after significant node failures. Use cases are being generated."
    
    elif scenario == "Governance Challenge":
        if step < 10:
            message += "Governance challenge detected in SpiralDAO components."
        elif step < 30:
            message += "Multiple conflicting governance proposals under evaluation."
        elif step < 50:
            message += "BloomKernel modeling potential outcomes of governance options."
        elif step < 70:
            message += "Consensus-building processes activating across all layers."
        else:
            message += "Governance resolution pathways stabilizing as consensus emerges. Use cases are being generated."
    
    return message


def generate_use_cases(scenario, G, node_status, node_resources, metrics_history):
    """Generate practical use cases based on simulation results"""
    
    # Get final metrics
    if metrics_history["steps"]:
        final_step = max(metrics_history["steps"])
        health_percent = metrics_history["healthy_nodes"][metrics_history["steps"].index(final_step)]
        total_resources = metrics_history["total_resources"][metrics_history["steps"].index(final_step)]
        information_flow = metrics_history["information_flow"][metrics_history["steps"].index(final_step)]
        governance_consensus = metrics_history["governance_consensus"][metrics_history["steps"].index(final_step)]
    else:
        return "Run a simulation to generate use cases."
    
    markdown = "## Real-World Use Cases\n\n"
    markdown += "Based on this simulation, here are practical applications where Genesis Bloom could address real-world challenges:\n\n"
    
    # Scenario-specific use cases
    if scenario == "Normal Operation":
        markdown += "### Healthy System Applications\n\n"
        
        markdown += "**1. Community Energy Grid**\n"
        markdown += "- **Challenge:** Traditional energy grids are centralized, brittle, and inefficient\n"
        markdown += "- **Genesis Bloom Solution:** A neighborhood-level energy sharing network where excess solar power is automatically traded between homes\n"
        markdown += "- **Components Used:** NovaChain tracks energy credits, Resource Mesh optimizes distribution, PSI Nodes represent individual homes\n\n"
        
        markdown += "**2. Learning Ecosystem Platform**\n"
        markdown += "- **Challenge:** Educational resources are unevenly distributed and often paywalled\n"
        markdown += "- **Genesis Bloom Solution:** Global knowledge-sharing platform that connects teachers, students and resources dynamically\n"
        markdown += "- **Components Used:** BloomKernel matches learning needs with resources, SpiralDAO ensures quality standards, Sentinel Layer prevents manipulation\n\n"
    
    elif scenario == "Resource Scarcity Event":
        markdown += "### Resource Optimization Applications\n\n"
        
        markdown += "**1. Drought Response System**\n"
        markdown += "- **Challenge:** Water scarcity affecting multiple communities with competing needs\n"
        markdown += "- **Genesis Bloom Solution:** Intelligent water allocation system that adapts to changing conditions while ensuring basic needs are met\n"
        markdown += "- **Components Used:** Resource Mesh tracks water availability, BloomKernel models optimal usage, SpiralDAO governs allocation priorities\n\n"
        
        markdown += "**2. Supply Chain Resilience Network**\n"
        markdown += "- **Challenge:** Disruptions in global supply chains causing critical shortages\n"
        markdown += "- **Genesis Bloom Solution:** Adaptive supply network that reroutes resources based on need, finds alternatives, and distributes fairly\n"
        markdown += "- **Components Used:** NovaChain verifies resource transfers, PSI Nodes represent participating businesses, Sentinel Layer prevents hoarding\n\n"
    
    elif scenario == "Node Failure":
        markdown += "### Resilience Applications\n\n"
        
        markdown += "**1. Disaster Response Coordination**\n"
        markdown += "- **Challenge:** Communication breakdowns during natural disasters hamper rescue efforts\n"
        markdown += "- **Genesis Bloom Solution:** Mesh network that maintains critical communications even when infrastructure fails\n"
        markdown += "- **Components Used:** Root Layer provides local connectivity, Sentinel Layer prioritizes emergency communications, Resource Mesh allocates aid\n\n"
        
        markdown += "**2. Cyber-Resilient Financial System**\n"
        markdown += "- **Challenge:** Centralized financial systems vulnerable to attacks and technical failures\n"
        markdown += "- **Genesis Bloom Solution:** Distributed financial network that maintains integrity even when multiple nodes are compromised\n"
        markdown += "- **Components Used:** NovaChain provides transaction verification, PSI Nodes protect individual accounts, Sentinel Layer detects attack patterns\n\n"
    
    elif scenario == "Governance Challenge":
        markdown += "### Collaborative Decision-Making Applications\n\n"
        
        markdown += "**1. Urban Planning Platform**\n"
        markdown += "- **Challenge:** City development decisions often fail to represent diverse resident needs\n"
        markdown += "- **Genesis Bloom Solution:** Participatory urban planning system that balances competing interests and models outcomes\n"
        markdown += "- **Components Used:** SpiralDAO enables nested decision-making from neighborhood to city level, BloomKernel simulates impacts, PSI Nodes protect privacy\n\n"
        
        markdown += "**2. Global Commons Management**\n"
        markdown += "- **Challenge:** Resources like oceans and atmosphere lack effective governance mechanisms\n"
        markdown += "- **Genesis Bloom Solution:** Transparent, participatory system for governing shared resources across jurisdictions\n"
        markdown += "- **Components Used:** Ouroboros Layer provides ethical frameworks, NovaChain tracks agreements, Sentinel Layer monitors compliance\n\n"
    
    # Add impact assessment based on simulation metrics
    markdown += "### Impact Assessment\n\n"
    markdown += f"Based on simulation metrics, these applications would likely achieve:\n\n"
    
    if health_percent > 80:
        markdown += "✓ **High System Reliability:** {0:.1f}% uptime even under adverse conditions\n".format(health_percent)
    elif health_percent > 60:
        markdown += "✓ **Moderate System Reliability:** {0:.1f}% functionality maintained during challenges\n".format(health_percent)
    else:
        markdown += "⚠ **Resilient but Degraded Performance:** System maintains {0:.1f}% functionality during severe disruptions\n".format(health_percent)
    
    if information_flow > 70:
        markdown += "✓ **Excellent Information Sharing:** Fast, efficient coordination across components\n"
    elif information_flow > 50:
        markdown += "✓ **Good Information Sharing:** Effective communication with occasional delays\n"
    else:
        markdown += "⚠ **Basic Information Sharing:** Critical information preserved despite significant constraints\n"
    
    if governance_consensus > 70:
        markdown += "✓ **Strong Consensus Building:** Rapidly converges on effective decisions even with diverse stakeholders\n"
    elif governance_consensus > 50:
        markdown += "✓ **Effective Governance:** Reaches acceptable compromises on most issues\n"
    else:
        markdown += "⚠ **Challenging Governance Conditions:** Basic decision-making maintained in difficult circumstances\n"
    
    # Add implementation considerations
    markdown += "\n### Implementation Considerations\n\n"
    markdown += "To implement these use cases, consider:\n\n"
    markdown += "1. **Start Small:** Begin with limited-scope pilots before scaling\n"
    markdown += "2. **Community Engagement:** Involve stakeholders from the beginning to ensure adoption\n"
    markdown += "3. **Technical Infrastructure:** Evaluate local connectivity and hardware requirements\n"
    markdown += "4. **Governance Design:** Carefully structure initial decision-making processes\n"
    markdown += "5. **Phased Deployment:** Implement core components first, then add advanced features\n"
    
    return markdown
