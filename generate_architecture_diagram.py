import matplotlib
matplotlib.use('Agg')  # Use non-interactive backend
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_architecture_diagram():
    # Create figure and axis
    fig, ax = plt.subplots(1, 1, figsize=(16, 12))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Define colors for different layers
    colors = {
        'frontend': '#E3F2FD',
        'backend': '#FFF3E0', 
        'data': '#F3E5F5',
        'external': '#E8F5E8'
    }
    
    # Layer positions and heights
    layers = [
        {'name': 'PRESENTATION LAYER\n(Frontend)', 'y': 9, 'height': 2.5, 'color': colors['frontend']},
        {'name': 'APPLICATION LAYER\n(Backend)', 'y': 6, 'height': 2.5, 'color': colors['backend']},
        {'name': 'DATA LAYER\n(Database)', 'y': 3.5, 'height': 2, 'color': colors['data']},
        {'name': 'EXTERNAL SERVICES\n(Third Party)', 'y': 0.5, 'height': 2.5, 'color': colors['external']}
    ]
    
    # Frontend components
    frontend_components = [
        'Login with\nGoogle', 'Dashboard\nUI', 'Chat with AI\nUI',
        'Financial Goals\nUI', 'Export Data\nUI', 'Net Worth\nVisualizer',
        'Simulations\nUI', 'Alerts & Nudges\nUI'
    ]
    
    # Backend components
    backend_components = [
        'Authentication\nService', 'Dashboard\nService', 'AI Chat\nService',
        'Financial Goals\nService', 'Data Export\nService', 'Net Worth\nCalculator',
        'Simulation\nEngine', 'Notification\nService', 'Insights\nGenerator'
    ]
    
    # Data layer components
    data_components = [
        'User Data\nRepository', 'Financial\nAccounts', 'Investment\nPortfolio',
        'Goals &\nPreferences', 'Transaction\nHistory', 'AI Chat\nHistory'
    ]
    
    # External services components
    external_components = [
        'Google OAuth\nService', 'Financial\nData Providers', 'AI/ML\nModels',
        'Credit Score\nServices', 'Market Data\nProviders'
    ]
    
    # Draw layer backgrounds
    for layer in layers:
        rect = FancyBboxPatch(
            (0.2, layer['y']), 9.6, layer['height'],
            boxstyle="round,pad=0.1",
            facecolor=layer['color'],
            edgecolor='#666666',
            linewidth=2
        )
        ax.add_patch(rect)
        
        # Add layer title
        ax.text(5, layer['y'] + layer['height'] - 0.3, layer['name'], 
                ha='center', va='center', fontsize=14, fontweight='bold')
    
    # Function to draw components in a layer
    def draw_components(components, y_base, y_height, max_per_row=3):
        rows = (len(components) + max_per_row - 1) // max_per_row
        component_height = 0.6
        component_width = 2.8
        
        for i, component in enumerate(components):
            row = i // max_per_row
            col = i % max_per_row
            
            # Calculate position
            x = 0.5 + col * 3.2
            y = y_base + y_height - 0.8 - (row * 0.8)
            
            # Draw component box
            comp_rect = FancyBboxPatch(
                (x, y), component_width, component_height,
                boxstyle="round,pad=0.05",
                facecolor='white',
                edgecolor='#333333',
                linewidth=1
            )
            ax.add_patch(comp_rect)
            
            # Add component text
            ax.text(x + component_width/2, y + component_height/2, component,
                   ha='center', va='center', fontsize=9, fontweight='normal')
    
    # Draw components for each layer
    draw_components(frontend_components, 9, 2.5, 3)
    draw_components(backend_components, 6, 2.5, 3)
    draw_components(data_components, 3.5, 2, 3)
    draw_components(external_components, 0.5, 2.5, 3)
    
    # Add arrows to show data flow between layers
    arrow_props = dict(arrowstyle='->', connectionstyle='arc3', color='#555555', lw=2)
    
    # Frontend to Backend arrows
    for i in range(3):
        ax.annotate('', xy=(1.5 + i*3.2, 8.5), xytext=(1.5 + i*3.2, 9),
                   arrowprops=arrow_props)
    
    # Backend to Data arrows
    for i in range(3):
        ax.annotate('', xy=(1.5 + i*3.2, 5.2), xytext=(1.5 + i*3.2, 6),
                   arrowprops=arrow_props)
    
    # Backend to External arrows
    for i in range(2):
        ax.annotate('', xy=(1.5 + i*3.2, 3), xytext=(1.5 + i*3.2, 6),
                   arrowprops=dict(arrowstyle='->', connectionstyle='arc3,rad=0.3', 
                                 color='#555555', lw=2))
    
    # Add title
    ax.text(5, 11.5, 'Financial Application - Layered Architecture', 
            ha='center', va='center', fontsize=18, fontweight='bold')
    
    # Add legend
    legend_elements = [
        patches.Patch(color=colors['frontend'], label='Frontend Layer'),
        patches.Patch(color=colors['backend'], label='Backend Layer'),
        patches.Patch(color=colors['data'], label='Data Layer'),
        patches.Patch(color=colors['external'], label='External Services')
    ]
    ax.legend(handles=legend_elements, loc='upper right', bbox_to_anchor=(1, 1))
    
    plt.tight_layout()
    plt.savefig('financial_app_architecture.png', dpi=300, bbox_inches='tight')
    plt.savefig('financial_app_architecture.pdf', bbox_inches='tight')
    print("Architecture diagram saved as 'financial_app_architecture.png' and 'financial_app_architecture.pdf'")
    plt.close()

if __name__ == "__main__":
    create_architecture_diagram()