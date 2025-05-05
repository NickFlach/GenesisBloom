import os
import streamlit as st
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, Text, Float, DateTime, JSON
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime
import json

# Create SQLAlchemy engine and session
db_url = os.getenv("DATABASE_URL")
engine = create_engine(db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Create a base class for declarative models
Base = declarative_base()

# Define the SimulationResult model
class SimulationResult(Base):
    __tablename__ = "simulation_results"
    
    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    scenario_type = Column(String, index=True)
    simulation_steps = Column(Integer)
    final_healthy_nodes = Column(Float)
    final_total_resources = Column(Float)
    final_information_flow = Column(Float)
    final_governance_consensus = Column(Float)
    metrics_history = Column(JSON)
    use_cases = Column(Text)

# Create all tables in the database
Base.metadata.create_all(bind=engine)

# Initialize database tables if needed
def init_db():
    Base.metadata.create_all(bind=engine)

# Store simulation result and use cases
def store_simulation_result(scenario, steps, metrics_history, use_cases_markdown):
    """
    Store simulation results and use cases in the database
    
    Args:
        scenario (str): The simulation scenario (e.g., "Normal Operation")
        steps (int): Number of simulation steps completed
        metrics_history (dict): Metrics data collected during simulation
        use_cases_markdown (str): Generated use cases in markdown format
    
    Returns:
        int: ID of the saved simulation result
    """
    try:
        # Create a database session
        db = SessionLocal()
        
        # Get final metrics
        final_step_idx = len(metrics_history["steps"]) - 1 if metrics_history["steps"] else 0
        
        # Simplify metrics history to reduce size - just keep every 5th data point
        simplified_metrics = {
            "steps": [],
            "healthy_nodes": [],
            "total_resources": [],
            "information_flow": [],
            "governance_consensus": []
        }
        
        # Sample the metrics data to reduce size
        for i in range(0, len(metrics_history["steps"]), 5):  # Sample every 5th data point
            if i < len(metrics_history["steps"]):
                simplified_metrics["steps"].append(metrics_history["steps"][i])
                simplified_metrics["healthy_nodes"].append(metrics_history["healthy_nodes"][i])
                simplified_metrics["total_resources"].append(metrics_history["total_resources"][i])
                simplified_metrics["information_flow"].append(metrics_history["information_flow"][i])
                simplified_metrics["governance_consensus"].append(metrics_history["governance_consensus"][i])
        
        # Create a new record
        simulation_result = SimulationResult(
            scenario_type=scenario,
            simulation_steps=steps,
            final_healthy_nodes=metrics_history["healthy_nodes"][final_step_idx] if metrics_history["healthy_nodes"] else 0,
            final_total_resources=metrics_history["total_resources"][final_step_idx] if metrics_history["total_resources"] else 0,
            final_information_flow=metrics_history["information_flow"][final_step_idx] if metrics_history["information_flow"] else 0,
            final_governance_consensus=metrics_history["governance_consensus"][final_step_idx] if metrics_history["governance_consensus"] else 0,
            metrics_history=simplified_metrics,  # Use the simplified metrics
            use_cases=use_cases_markdown
        )
        
        # Add and commit to database
        db.add(simulation_result)
        db.commit()
        db.refresh(simulation_result)
        
        result_id = simulation_result.id
        
        # Close session
        db.close()
        
        return result_id
    
    except Exception as e:
        st.error(f"Database error: {str(e)}")
        # Log the full error for debugging
        import traceback
        st.error(f"Error details: {traceback.format_exc()}")
        return None

# Get all simulation results
def get_all_simulation_results():
    """
    Retrieve all simulation results from the database
    
    Returns:
        pd.DataFrame: DataFrame containing simulation results
    """
    try:
        # Create a database session
        db = SessionLocal()
        
        # Query all results
        results = db.query(SimulationResult).all()
        
        # Convert to DataFrame for easier display in Streamlit
        data = [{
            "id": r.id,
            "timestamp": r.timestamp,
            "scenario": r.scenario_type,
            "steps": r.simulation_steps,
            "healthy_nodes": r.final_healthy_nodes,
            "total_resources": r.final_total_resources,
            "information_flow": r.final_information_flow,
            "governance_consensus": r.final_governance_consensus
        } for r in results]
        
        # Close session
        db.close()
        
        return pd.DataFrame(data)
    
    except Exception as e:
        st.error(f"Database error: {str(e)}")
        return pd.DataFrame()

# Get a specific simulation result by ID
def get_simulation_result(simulation_id):
    """
    Retrieve a specific simulation result by ID
    
    Args:
        simulation_id (int): ID of the simulation result to retrieve
    
    Returns:
        SimulationResult: The simulation result object
    """
    try:
        # Create a database session
        db = SessionLocal()
        
        # Query the specific result
        result = db.query(SimulationResult).filter(SimulationResult.id == simulation_id).first()
        
        # Close session
        db.close()
        
        return result
    
    except Exception as e:
        st.error(f"Database error: {str(e)}")
        return None
