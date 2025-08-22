from tradingagents.graph.trading_graph import TradingAgentsGraph
from tradingagents.default_config import DEFAULT_CONFIG
from config import API_KEYS, TRADING_CONFIG

# Create a custom config
config = DEFAULT_CONFIG.copy()
config.update(TRADING_CONFIG)

# Set API keys in environment variables so the trading agents can access them
import os
for key, value in API_KEYS.items():
    if value != f"your_actual_{key}_here":  # Only set if not placeholder
        os.environ[key.upper()] = value

# Initialize with custom config
ta = TradingAgentsGraph(debug=True, config=config)

# forward propagate
_, decision = ta.propagate("NVDA", "2024-05-10")
print(decision)

# Memorize mistakes and reflect
# ta.reflect_and_remember(1000) # parameter is the position returns
