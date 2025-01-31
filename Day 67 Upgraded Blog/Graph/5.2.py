import matplotlib.pyplot as plt
import matplotlib.ticker as mtick

# Survey data
categories = ['Discounts', 'Loyalty Programs', 'Bundled Offers']
preferences = [0.45, 0.30, 0.25]  # 45%, 30%, 25%
colors = ['#3498db', '#9b59b6', '#2ecc71']  # Blue, Purple, Green

# Create figure
fig, ax = plt.subplots(figsize=(10, 6))

# Create bar chart
bars = ax.bar(categories, preferences, color=colors, width=0.7)

# Formatting
ax.set_title("Effectiveness of Sales Promotion Techniques",
             pad=20, fontsize=14, fontweight='bold')
ax.set_ylabel("Percentage of Respondents", labelpad=15, fontsize=12)
ax.yaxis.set_major_formatter(mtick.PercentFormatter(1.0))  # Format as percentages
ax.set_ylim(0, 0.5)  # Set y-axis limit to 50%
ax.grid(True, axis='y', linestyle='--', alpha=0.6)

# Remove unnecessary spines
for spine in ['top', 'right']:
    ax.spines[spine].set_visible(False)

# Add data labels
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2,  # X-position centered
            height + 0.01,  # Y-position slightly above bar
            f'{height:.0%}',  # Format as percentage
            ha='center', 
            va='bottom',
            fontsize=12,
            fontweight='bold')

# Add annotation about overall likelihood
ax.text(0.5, -0.15, 
        "*68% of consumers are more likely to purchase when exposed to sales promotions",
        ha='center', va='center', 
        transform=ax.transAxes,  # Uses axis coordinates
        fontsize=10, 
        color='#666666')

plt.tight_layout()
plt.show()