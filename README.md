# MCP Agent Project (PostgreSQL, Slack, Git)

Bu proje, **GPT-5 tabanlı bir AI agent** kullanarak MCP (Model Context Protocol) serverlarına bağlanır ve PostgreSQL, Git ve Slack araçlarını kullanır. LLM, hangi tool’u kullanacağına kendi karar verir. Docker Compose ile sürekli çalışan MCP serverları sağlanmıştır.


## Özellikler

* PostgreSQL MCP server ile **veritabanı sorgulama ve şema inceleme**.
* Slack MCP server ile **kanal mesajları, threadler ve emoji reaksiyonları**.
* Git MCP server ile **dosya sistemi ve repository işlemleri**.
* GPT-5 agent ile araçlar arası **otomatik seçim ve işlem yürütme**.
* Docker Compose ile **sürekli çalışan servisler**.



## Gereksinimler

* Docker & Docker Compose
* Python 3.11+
* GPT-5 API erişimi



## Kurulum

### 1. Repository’yi klonlayın

```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Ortam değişkenlerini ayarlayın

`.env` dosyası oluşturun:

```env
SLACK_BOT_TOKEN=xoxb-your-bot-token
SLACK_TEAM_ID=T01234567
SLACK_CHANNEL_IDS=C01234567,C76543210

POSTGRES_URL=postgresql://postgres:password@localhost:5432/mydb
```

> Git MCP için host dosya yollarını docker-compose.yml’de güncelleyin.

---

### 3. Docker Compose ile servisleri başlatın

```bash
docker-compose up -d
```

* PostgreSQL MCP server: `mcp_postgres`
* Slack MCP server: `mcp_slack`
* Git MCP server: `mcp_git`

> `-d` ile arka planda çalışır.



## GPT-5 Agent Kullanımı

`agent.py` ile LLM, MCP serverlarına bağlanır:

```bash
python agent.py
```

* Agent, PostgreSQL, Slack ve Git MCP serverlarını otomatik olarak kullanır.
* Tool seçimleri ve sorgular GPT-5 tarafından yürütülür.
* Slack mesaj gönderme, PostgreSQL sorgulama ve Git dosya yönetimi yapılabilir.



## Config Dosyaları

### `config.json`

```json
{
  "mcpServers": {
    "postgres": {
      "command": "docker",
      "args": ["exec", "-i", "mcp_postgres", "server"]
    },
    "slack": {
      "command": "docker",
      "args": ["exec", "-i", "mcp_slack", "server"]
    },
    "git": {
      "command": "docker",
      "args": ["exec", "-i", "mcp_git", "server"]
    }
  }
}
```

> `docker exec` ile sürekli çalışan containerlara bağlanılır.

### `docker-compose.yml`

```yaml
version: "3.9"

services:
  postgres:
    image: mcp/postgres
    container_name: mcp_postgres
    restart: unless-stopped
    environment:
      POSTGRES_URL: "${POSTGRES_URL}"
    ports:
      - "5432:5432"

  slack:
    image: mcp/slack
    container_name: mcp_slack
    restart: unless-stopped
    environment:
      SLACK_BOT_TOKEN: "${SLACK_BOT_TOKEN}"
      SLACK_TEAM_ID: "${SLACK_TEAM_ID}"
      SLACK_CHANNEL_IDS: "${SLACK_CHANNEL_IDS}"

  git:
    image: mcp/git
    container_name: mcp_git
    restart: unless-stopped
    volumes:
      - /Users/username/Desktop:/projects/Desktop
      - /path/to/other/allowed/dir:/projects/other/allowed/dir:ro
      - /path/to/file.txt:/projects/path/to/file.txt
```



## Troubleshooting

* MCP serverlara erişilemiyorsa containerlar çalışıyor mu kontrol edin:

  ```bash
  docker ps
  ```
* Slack hatası → Token ve kanal ID’lerini `.env` ile güncelleyin.
* PostgreSQL hatası → URL, kullanıcı ve şifreyi doğrulayın.
* Git MCP → Host dosya yolları doğru mount edilmiş olmalı.

## Lisans

MIT License

## Kaynakça

Bu proje, Model Context Protocol (MCP) üzerine inşa edilmiştir ve aşağıdaki kaynaklardan yararlanılarak geliştirilmiştir:

* **MCP Resmi Sunucu Entegrasyonları:** [MCP Servers GitHub](https://github.com/modelcontextprotocol/servers?tab=readme-ov-file#%EF%B8%8F-official-integrations)
* **Git Tool Entegrasyonu:** [MCP Git Server](https://github.com/modelcontextprotocol/servers/tree/main/src/git)
* **Slack Tool Entegrasyonu:** [MCP Slack Server (archived)](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/slack)
* **PostgreSQL Tool Entegrasyonu:** [MCP Postgres Server (archived)](https://github.com/modelcontextprotocol/servers-archived/tree/main/src/postgres)
* **MCP Örnek Projeler ve Kullanıcı Dokümantasyonu:** [MCP Examples](https://modelcontextprotocol.io/examples), [MCP Clients](https://modelcontextprotocol.io/clients)
