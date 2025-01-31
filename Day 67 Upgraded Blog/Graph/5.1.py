import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Data
scenarios = ['Digital Advertising', 'Traditional Advertising']
sales_increase = [0.25, 0.15]  # 40% and 25%
colors = ['#2ecc71', '#e74c3c']  # Green for discount, red for no discount

# Create plot
fig, ax = plt.subplots(figsize=(8, 5))

# Create vertical bars (using bar instead of barh)
bars = ax.bar(scenarios, sales_increase, color=colors, width=0.6)

# Formatting
ax.set_title('Advertising Expenditure vs Sales Volume', 
             pad=20, fontsize=14, fontweight='bold')
ax.set_ylabel('Sales Increase', labelpad=15, fontsize=12)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))  # Format Y-axis as percentages
ax.set_ylim(0, 0.5)  # Cap Y-axis at 50%
ax.grid(True, axis='y', linestyle='--', alpha=0.6)

# Remove spines
for spine in ['top', 'right', 'bottom']:
    ax.spines[spine].set_visible(False)

# Add percentage labels on top of bars
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2,  # Center text horizontally
            height + 0.01,  # Position text slightly above bar
            f'{height:.0%}',
            va='bottom',
            ha='center',
            color='black',
            fontsize=12,
            fontweight='bold')

plt.tight_layout()
plt.show()