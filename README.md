# 🧠 Python MCP (Model Context Protocol) Agent

Bu proje, **Python tabanlı bir MCP (Model Context Protocol) agent** örneğidir.  
Amaç, bir LLM’in (OpenAI) **kontrollü ve güvenli şekilde** bilgisayar kaynaklarını
(tool'lar aracılığıyla) kullanabilmesini sağlamaktır.

Bu agent:
- Tool calling kullanır
- Dosya oluşturabilir
- MCP uyumlu agent loop içerir
- Sandbox (izole dosya alanı) mantığına sahiptir

---

## 📁 Proje Yapısı

MCP_Project/
│
├── main.py                 # Agent loop (MCP akışı)
├── client.py               # OpenAI API adapter
├── tools.py                # Gerçek sistem işlemleri
├── tool_registry.py        # Tool → function eşleştirme
├── schemas.py              # Tool JSON schema'ları
├── config.py               # Ayarlar & güvenlik
│
├── mcp_workspace/          # 🔒 Sandbox (AI erişimi)
│   └── (oluşturulan dosyalar)
│
├── requirements.txt        # Python bağımlılıkları
├── README.md               # Proje dokümantasyonu
│
└── .gitignore              # (önerilir)


---

## 🧩 MCP Mimarisi (Özet)


> 🔐 Model **hiçbir zaman** doğrudan dosya sistemine erişmez.  
> Tüm yetki MCP server (Python) tarafındadır.

---

## ⚙️ Kurulum

### 1️⃣ Sanal ortam (önerilir)

```bash
python -m venv venv
source venv/bin/activate   # Linux / macOS
venv\Scripts\activate      # Windows
