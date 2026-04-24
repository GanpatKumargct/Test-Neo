from langgraph.graph import StateGraph, END
from app.ai.graph.state import LeadProcessingState
from app.ai.nodes.score_node import score_lead_node
from app.ai.nodes.enrich_node import enrich_node
from app.ai.nodes.message_node import message_node

def build_graph():
    workflow = StateGraph(LeadProcessingState)
    
    workflow.add_node("score", score_lead_node)
    workflow.add_node("enrich", enrich_node)
    workflow.add_node("message", message_node)
    
    workflow.set_entry_point("score")
    workflow.add_edge("score", "enrich")
    workflow.add_edge("enrich", "message")
    workflow.add_edge("message", END)
    
    return workflow.compile()

# Instantiate the graph
lead_processing_graph = build_graph()
