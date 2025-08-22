# API Keys Configuration
# Replace the placeholder values with your actual API keys

API_KEYS = {
    "google_api_key": "your_actual_google_api_key_here",
    "openai_api_key": "your_actual_openai_api_key_here", 
    "finnhub_api_key": "your_actual_finnhub_api_key_here",
    "eodhd_api_key": "your_actual_eodhd_api_key_here",
    "reddit_client_id": "your_actual_reddit_client_id_here",
    "reddit_client_secret": "your_actual_reddit_client_secret_here",
    "reddit_user_agent": "your_actual_reddit_user_agent_here",
}

# Trading configuration - OpenAI as default
TRADING_CONFIG = {
    "llm_provider": "openai",  # Default to OpenAI
    "deep_think_llm": "gpt-4o-mini",  # Use gpt-4o-mini for deep thinking
    "quick_think_llm": "gpt-4o-mini",  # Use gpt-4o-mini for quick thinking
    "max_debate_rounds": 1,
    "online_tools": True,
}
