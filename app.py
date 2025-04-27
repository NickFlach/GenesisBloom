import streamlit as st
from streamlit_extras.switch_page_button import switch_page
import core_principles
import system_components
import network_architecture
import risk_mitigation
import simulation
import utils

# Set page configuration
st.set_page_config(
    page_title="Genesis Bloom",
    page_icon="🌱",
    layout="wide",
    initial_sidebar_state="expanded",
)

def main():
    # Sidebar navigation
    st.sidebar.title("Genesis Bloom")
    st.sidebar.image("assets/genesis_bloom_logo.svg", use_column_width=True)
    
    st.sidebar.markdown("## Navigation")
    page = st.sidebar.radio(
        "Select a section:",
        [
            "Home",
            "Core Principles",
            "System Components",
            "Network Architecture",
            "Risk Mitigation",
            "Interactive Simulation"
        ],
        index=0
    )
    
    st.sidebar.markdown("---")
    st.sidebar.markdown("An open-source architecture for the flourishing of all life.")
    
    # Main content based on selected page
    if page == "Home":
        display_home()
    elif page == "Core Principles":
        core_principles.display()
    elif page == "System Components":
        system_components.display()
    elif page == "Network Architecture":
        network_architecture.display()
    elif page == "Risk Mitigation":
        risk_mitigation.display()
    elif page == "Interactive Simulation":
        simulation.display()

def display_home():
    # Header
    col1, col2 = st.columns([1, 3])
    with col1:
        st.image("assets/genesis_bloom_logo.svg", width=200)
    with col2:
        st.title("Genesis Bloom")
        st.markdown("### An open-source architecture for the flourishing of all life")
    
    st.markdown("---")
    
    # Introduction
    st.markdown("""
    ## About Genesis Bloom
    
    Genesis Bloom is a visionary decentralized architecture designed to create a more equitable, compassionate, and 
    resilient global system. By distributing power, minimizing suffering, fostering collective intelligence, 
    balancing privacy with transparency, and adapting to chaos, Genesis Bloom aims to nurture a flourishing ecosystem 
    for all life on Earth.
    
    This platform provides an educational exploration of the Genesis Bloom concepts, components, and architecture.
    """)
    
    # Overview of sections
    st.markdown("## Explore the Architecture")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown("### Core Principles")
        st.markdown("The five foundational principles that guide Genesis Bloom's design and operation.")
        if st.button("Explore Principles", key="principles_btn"):
            core_principles.display()
    
    with col2:
        st.markdown("### System Components")
        st.markdown("The six main components that make up the Genesis Bloom architecture.")
        if st.button("Explore Components", key="components_btn"):
            system_components.display()
    
    with col3:
        st.markdown("### Network Architecture")
        st.markdown("The three-layer network structure that enables Genesis Bloom's resilience and functionality.")
        if st.button("Explore Architecture", key="architecture_btn"):
            network_architecture.display()
    
    st.markdown("---")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("### Risk Mitigation")
        st.markdown("Strategies employed to ensure Genesis Bloom remains robust, secure, and resistant to corruption.")
        if st.button("Explore Risk Mitigation", key="risk_btn"):
            risk_mitigation.display()
    
    with col2:
        st.markdown("### Interactive Simulation")
        st.markdown("Visualize how the components of Genesis Bloom interact in a simplified simulation.")
        if st.button("Try Simulation", key="simulation_btn"):
            simulation.display()

if __name__ == "__main__":
    main()
