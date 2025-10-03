# Installation

## Prerequisites

- Python 3.12+
- OpenSearch (for Similarity Pipeline)
- OpenAI API key (for LLM Pipeline)

## Quick Start

1. **Clone the repository**
   ```bash
   git clone https://github.com/0xAIDR/AIDR-Bastion.git
   cd AIDR-Bastion
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp env.example .env
   # Edit .env with your configuration
   ```

5. **Run the application**
   ```bash
   python server.py
   ```

By default, the API will be available at `http://localhost:8000`. You can customize the host and port using the HOST and PORT environment variables.
