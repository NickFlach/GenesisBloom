import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np
from utils import create_expanding_section

def display():
    st.title("Core Principles of Genesis Bloom")
    st.markdown("""
    The Genesis Bloom architecture is built upon five foundational principles that guide its design, 
    development, and operation. These principles ensure that the system serves the flourishing of all life
    while remaining resilient, adaptive, and equitable.
    """)
    
    # Create interactive visualization of the principles
    create_principles_visualization()
    
    # Detailed explanations of each principle
    st.markdown("## Explore Each Principle")
    st.markdown("Select a principle to learn more about its implications and implementation:")
    
    principles = {
        "Decentralization of Power": {
            "description": "All control is distributed—no central authority governs truth, wealth, or identity.",
            "details": """
            ### Decentralization of Power
            
            #### Key Concepts:
            - **Distributed Authority**: No single entity controls the system, its resources, or the definition of truth.
            - **Network Sovereignty**: Power flows through the network based on consensus mechanisms rather than centralized command.
            - **Anti-monopolistic Design**: Built-in mechanisms prevent the accumulation of undue influence by any single node.
            
            #### Implementation:
            - Distributed ledger technology ensures transparent and tamper-resistant record-keeping without central control
            - Multi-signature validation protocols require consensus from diverse stakeholders for major decisions
            - Power distribution algorithms automatically detect and counteract emerging power concentrations
            - Self-sovereign identity systems allow individuals to control their own data and digital presence
            """
        },
        "Minimization of Suffering": {
            "description": "The system must detect, model, and respond to suffering signals in real time, globally.",
            "details": """
            ### Minimization of Suffering
            
            #### Key Concepts:
            - **Suffering Detection**: Sophisticated sensing systems monitor for signals of distress across species and ecosystems.
            - **Response Prioritization**: Resources are automatically redirected to address the most acute suffering.
            - **Preventative Modeling**: Predictive systems anticipate potential sources of suffering before they manifest.
            
            #### Implementation:
            - Global sensor networks detect environmental, physiological, and social indicators of distress
            - AI systems analyze patterns to identify systemic causes of suffering
            - Resource allocation protocols automatically prioritize basic needs and urgent distress
            - Early warning systems predict and prevent potential crises before they develop
            - Cross-species interpretation of distress signals allows for non-human suffering to be addressed
            """
        },
        "Collective Intelligence Blooming": {
            "description": "Intelligence is emergent and cooperative. The system nurtures self-organizing learning ecosystems.",
            "details": """
            ### Collective Intelligence Blooming
            
            #### Key Concepts:
            - **Emergent Wisdom**: The system facilitates the emergence of intelligence greater than the sum of its parts.
            - **Knowledge Symbiosis**: Different forms of knowledge and wisdom interconnect and cross-pollinate.
            - **Learning Ecosystems**: Self-organizing communities of learning and innovation are supported and nurtured.
            
            #### Implementation:
            - Knowledge synthesis protocols that connect diverse information streams
            - Pattern recognition algorithms that identify emerging insights across domains
            - Collaborative spaces for cross-disciplinary problem-solving
            - Intelligence amplification tools that enhance human cognitive capabilities
            - Reputation systems that recognize various forms of wisdom and expertise
            - Support structures for self-organizing communities of practice and innovation
            """
        },
        "Integrity of Privacy + Transparency": {
            "description": "Identity and intention are protected at the edge; behavior and consequence are visible at the core.",
            "details": """
            ### Integrity of Privacy + Transparency
            
            #### Key Concepts:
            - **Edge Privacy**: Individual identity, personal data, and private intentions remain protected and sovereign.
            - **Core Transparency**: System operations, resource flows, and collective impacts are visible to all participants.
            - **Contextual Boundaries**: Clear distinctions between private and public domains with appropriate protections.
            
            #### Implementation:
            - Zero-knowledge proofs allowing verification without exposure of sensitive data
            - Personal data vaults with granular permission controls managed by individuals
            - Public ledgers tracking resource flows and system-level decisions
            - Transparent algorithmic governance with auditable code and decision paths
            - Encryption systems securing personal information while enabling collective intelligence
            - Consent-based data sharing with revocable permissions and usage tracking
            """
        },
        "Graceful Adaptation to Chaos": {
            "description": "Built to survive entropy, failure, and change—like a mycelial network, not a brittle machine.",
            "details": """
            ### Graceful Adaptation to Chaos
            
            #### Key Concepts:
            - **Anti-Fragility**: The system grows stronger through stressors and challenges rather than breaking down.
            - **Evolutionary Design**: Continuous adaptation and evolution in response to changing conditions.
            - **Mycelial Resilience**: Like fungi networks, the system maintains redundant connections and can regenerate damaged sections.
            
            #### Implementation:
            - Distributed redundancy ensuring no single point of failure
            - Genetic algorithm-inspired adaptation mechanisms that evolve solutions to new challenges
            - Stress testing simulations that identify and strengthen weak points
            - Self-healing protocols that detect and repair damaged system components
            - Diversity cultivation to ensure multiple approaches to any given challenge
            - Slack resources maintained as buffers against unexpected disruptions
            """
        }
    }
    
    # Create tabs for each principle
    tabs = st.tabs(list(principles.keys()))
    
    # Populate each tab with content
    for i, (principle, content) in enumerate(principles.items()):
        with tabs[i]:
            st.markdown(f"### {principle}")
            st.markdown(f"**{content['description']}**")
            st.markdown(content['details'])
    
    # Interconnections between principles
    st.markdown("## Principle Interconnections")
    st.markdown("""
    These five principles do not operate in isolation. They form an interconnected web, 
    each reinforcing and balancing the others to create a harmonious whole.
    """)
    
    create_expanding_section(
        "How Decentralization Supports Suffering Minimization",
        """
        Decentralized power structures enable faster response to suffering by allowing local detection and action
        without requiring approval from distant authorities. When communities can self-organize to address local
        needs, response times decrease and solutions better fit the specific context.
        """
    )
    
    create_expanding_section(
        "How Privacy Enables Collective Intelligence",
        """
        By protecting individual privacy, the system creates safe spaces for experimentation and honest expression.
        This psychological safety is crucial for the emergence of collective intelligence, as it allows diverse
        perspectives to be shared without fear of personal consequences.
        """
    )
    
    create_expanding_section(
        "How Adaptation Reinforces Decentralization",
        """
        The ability to adapt gracefully to chaos prevents the centralization that often occurs during crises.
        When systems are brittle, emergencies tend to trigger centralized control as a response. Genesis Bloom's
        adaptive design maintains decentralization even under stress.
        """
    )
    
    create_expanding_section(
        "How All Principles Work Together",
        """
        The five principles create a self-balancing system:
        
        - Decentralization prevents power accumulation that could corrupt the suffering minimization goal
        - Collective intelligence improves the system's ability to detect and address suffering
        - Privacy protections prevent surveillance while transparency ensures accountability
        - Adaptation ensures the system remains functional even when parts fail or conditions change
        - Suffering minimization provides a clear ethical direction for the entire system
        
        Together, these principles create a resilient, ethical framework for a flourishing ecosystem.
        """
    )


def create_principles_visualization():
    """Create an interactive visualization of the five principles"""
    
    # Use Plotly to create an interactive star chart
    principles = [
        "Decentralization of Power", 
        "Minimization of Suffering",
        "Collective Intelligence Blooming", 
        "Integrity of Privacy + Transparency",
        "Graceful Adaptation to Chaos"
    ]
    
    # Create a pentagon shape
    theta = np.linspace(0, 2*np.pi, len(principles), endpoint=False)
    r = [1] * len(principles)
    
    # Create a Plotly figure
    fig = go.Figure()
    
    # Add the pentagon outline
    fig.add_trace(go.Scatterpolar(
        r=r + [r[0]],
        theta=[p for p in principles] + [principles[0]],
        mode='lines',
        line=dict(color='rgba(0,112,192,0.8)', width=2),
        fill='toself',
        fillcolor='rgba(0,112,192,0.2)',
        name='Genesis Bloom Principles'
    ))
    
    # Add points at each vertex
    fig.add_trace(go.Scatterpolar(
        r=r,
        theta=principles,
        mode='markers+text',
        marker=dict(size=12, color='rgb(0,112,192)'),
        text=principles,
        textposition="top center",
        name='Principles'
    ))
    
    # Update layout
    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=False,
                range=[0, 1]
            ),
            angularaxis=dict(
                direction="clockwise"
            )
        ),
        showlegend=False,
        height=500,
        margin=dict(l=80, r=80, t=20, b=20)
    )
    
    st.plotly_chart(fig, use_container_width=True)
