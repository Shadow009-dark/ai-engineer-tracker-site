"""Phase 6 - NLP and LLMs: prompts, RAG, agents, fine-tuning (days 113-140, 24 study days)."""

from helpers import day, doc, gq, phase, yt

PROMPTING = "https://www.promptingguide.ai/"
OAI_PROMPT = "https://platform.openai.com/docs/guides/prompt-engineering"
OAI_COOKBOOK = "https://github.com/openai/openai-cookbook"
ANTHROPIC = "https://docs.anthropic.com/"
MCP = "https://modelcontextprotocol.io/"
HF_LLM = "https://huggingface.co/learn/llm-course/chapter1/1"
HF_BLOG = "https://huggingface.co/blog"
HF_PEFT = "https://huggingface.co/docs/peft/index"
LANGCHAIN = "https://python.langchain.com/"
LLAMAINDEX = "https://docs.llamaindex.ai/"
FAISS = "https://github.com/facebookresearch/faiss"
CHROMA = "https://docs.trychroma.com/"
QDRANT = "https://qdrant.tech/documentation/"
VLLM = "https://docs.vllm.ai/"
OLLAMA = "https://github.com/ollama/ollama"
RAG_PAPER = "https://arxiv.org/abs/2005.11401"
COT_PAPER = "https://arxiv.org/abs/2201.11903"
REACT_PAPER = "https://arxiv.org/abs/2210.03629"
LILIAN_AGENT = "https://lilianweng.github.io/posts/2023-06-23-agent/"
SIMON = "https://simonwillison.net/"
RAGAS = "https://docs.ragas.io/"
FUNCTION_CALLING = "https://platform.openai.com/docs/guides/function-calling"
WHISPER = "https://github.com/openai/whisper"
CLIP = "https://arxiv.org/abs/2103.00020"

days = [
    day(
        "Prompt engineering I: əsaslar",
        [
            "Prompt strukturu: system, user, assistant rolları",
            "Zero-shot, few-shot və nümunə seçimi",
            "Rol vermə, ton və format təlimatı",
            "Prompt-ların versiyalanması",
        ],
        [
            yt("Prompt Engineering Full Course", "DeepLearning.AI", "1s 30d", "chatgpt prompt engineering for developers"),
            yt("Prompt engineering ən yaxşı təcrübələri", "Andrej Karpathy", "25 d", "karpathy prompt engineering tips"),
        ],
        [
            doc("Prompt Engineering Guide", "promptingguide.ai", PROMPTING),
            doc("OpenAI prompt bələdçisi", "platform.openai.com", OAI_PROMPT),
        ],
        [
            "Eyni tapşırıq üçün 5 fərqli prompt yaz",
            "Nəticələri müqayisə cədvəlində göstər",
            "System prompt-un təsirini ölç",
            "Few-shot nümunələrin keyfiyyətinin rolunu yoxla",
        ],
        "5 prompt variantının müqayisəsi (nəticələrlə)",
        [
            "System prompt nə edir?",
            "Few-shot nə vaxt kömək edir?",
            "Prompt niyə versiyalanmalıdır?",
        ],
    ),
    day(
        "Prompt engineering II: reasoning və struktur çıxış",
        [
            "Chain-of-Thought (CoT) prompting",
            "ReAct: reasoning + acting",
            "Structured output (JSON schema)",
            "Guardrails və output validasiyası",
        ],
        [
            yt("Chain of Thought izahı", "Yannic Kilcher", "20 d", "chain of thought paper explained"),
            yt("Structured output və function calling", "OpenAI", "25 d", "structured outputs json mode openai"),
        ],
        [
            doc("Paper: Chain-of-Thought", "arxiv.org", COT_PAPER),
            doc("Paper: ReAct", "arxiv.org", REACT_PAPER),
        ],
        [
            "CoT ilə və olmadan eyni riyaziyyat sualını həll et",
            "Prompt-dan JSON çıxışı al və sxemə uyğunluğu yoxla",
            "ReAct dövrünü kağızda modelləşdir",
            "Uğursuz JSON çıxışı üçün retry məntiqi yaz",
        ],
        "Struktur JSON çıxışı verən, validasiya olunan prompt sistemi",
        [
            "CoT nə vaxt kömək edir, nə vaxt zərərlidir?",
            "ReAct-in fərqi nədir?",
            "JSON validasiyası niyə zəruridir?",
        ],
    ),
    day(
        "LLM API-ləri ilə işləmək",
        [
            "API-lər: OpenAI, Anthropic, Groq, HF Inference",
            "Token, kontekst, xərc hesablaması",
            "Retry, timeout, rate limit idarəsi",
            "Streaming cavablar",
        ],
        [
            yt("LLM API ilə işləmək", "AssemblyAI", "40 d", "openai api python tutorial"),
            yt("API xərcini azaltmaq", "Trelis Research", "25 d", "reduce llm api cost tokens"),
        ],
        [
            doc("OpenAI Cookbook", "github.com/openai", OAI_COOKBOOK),
            doc("Anthropic sənədləri", "docs.anthropic.com", ANTHROPIC),
        ],
        [
            "Kiçik Python skripti yaz: API-yə sorğu göndər və cavabı çap et",
            "Retry və timeout məntiqi əlavə et",
            "Streaming cavabı terminalda göstər",
            "10 sorğunun token xərcini hesabla",
        ],
        "Xəta idarəsi və streaming olan LLM API klienti",
        [
            "Token xərci necə hesablanır?",
            "Rate limit olanda nə etmək lazımdır?",
            "Streaming istifadəçi təcrübəsini necə dəyişir?",
        ],
    ),
    day(
        "Embedding-lər və semantik axtarış",
        [
            "Mətn embedding modelləri",
            "Cosine similarity ilə semantik axtarış",
            "Chunking strategiyaları",
            "Embedding-lərin saxlanması və yenilənməsi",
        ],
        [
            yt("Vector embedding və semantik axtarış", "AssemblyAI", "35 d", "vector embeddings semantic search tutorial"),
            yt("Chunking strategiyaları RAG üçün", "LlamaIndex", "25 d", "chunking strategies rag llamaindex"),
        ],
        [
            doc("Sentence Transformers", "sbert.net", "https://www.sbert.net/"),
            doc("Hugging Face: embedding modelləri", "huggingface.co", "https://huggingface.co/models?pipeline_tag=feature-extraction"),
        ],
        [
            "Sənədlər toplusunu chunk-lara böl",
            "Embedding hesabla və saxla (npy/json)",
            "Sabit axtarış funksiyası yaz (cosine)",
            "Chunk ölçüsünün nəticəyə təsirini ölç",
        ],
        "Semantik axtarış prototipi (chunk + embedding + axtarış)",
        [
            "Embedding nə üçün vektorlaşdırma adlanır?",
            "Chunk ölçüsü necə seçilir?",
            "Keyword axtarışı ilə semantik axtarış fərqi nədir?",
        ],
    ),
    day(
        "Vektor bazaları: FAISS, Chroma, Qdrant",
        [
            "Vektor indeksləri: flat, IVF, HNSW",
            "FAISS, Chroma, Qdrant müqayisəsi",
            "Metadata filtrləmə",
            "Yenilənmə/silinmə strategiyaları",
        ],
        [
            yt("Vektor bazaları izahı", "Fireship / IBM", "20 d", "what is a vector database explained"),
            yt("FAISS tutorial", "James Briggs", "35 d", "faiss tutorial vector search"),
        ],
        [
            doc("FAISS repo", "github.com", FAISS),
            doc("Chroma sənədləri", "docs.trychroma.com", CHROMA),
            doc("Qdrant sənədləri", "qdrant.tech", QDRANT),
        ],
        [
            "FAISS ilə indeks qur və axtarış et",
            "Chroma ilə eyni işi et və müqayisə et",
            "Metadata ilə filtrlə",
            "Axtarış vaxtını ölç (100, 1000, 10000 vektor)",
        ],
        "İki vektor bazası ilə semantik axtarış müqayisəsi",
        [
            "HNSW indeksi nə üçün sürətlidir?",
            "Metadata filtrasiyası nə vaxt lazımdır?",
            "Kiçik data üçün hansı yanaşma sadədir?",
        ],
    ),
    day(
        "RAG I: arxitektura və əsas implementasiya",
        [
            "RAG nədir və niyə lazımdır (hallucination, bilik yeniliyi)",
            "Retrieval -> kontekst qurma -> generasiya",
            "Prompt-da kontekstin verilməsi",
            "Sitat mənbələri və cavabın əsaslandırılması",
        ],
        [
            yt("RAG izahı", "IBM Technology", "15 d", "what is rag retrieval augmented generation"),
            yt("RAG from scratch", "LangChain", "1s", "rag from scratch langchain tutorial"),
        ],
        [
            doc("Paper: RAG", "arxiv.org", RAG_PAPER),
            doc("LangChain sənədləri", "python.langchain.com", LANGCHAIN),
        ],
        [
            "Sənəd kolleksiyasını indekslə (5-10 sənəd)",
            "Sual -> retrieval -> cavab axınını qur",
            "Cavabda mənbə sitatı göstər",
            "RAG-sız və RAG-lı cavabı müqayisə et",
        ],
        "İşləyən minimal RAG prototipi (sitat göstərən)",
        [
            "RAG hansı problemi həll edir?",
            "Retrieval keyfiyyəti cavaba necə təsir edir?",
            "Hallucination necə azaldılır?",
        ],
    ),
    day(
        "RAG II: təkmil retrieval",
        [
            "Hybrid search (BM25 + vektor)",
            "Reranking modelləri (cross-encoder)",
            "Chunking strategiyaları: fixed, semantic, hierarchical",
            "Query transformation (HyDE, multi-query)",
        ],
        [
            yt("Advanced RAG üsulları", "LlamaIndex", "40 d", "advanced rag techniques reranking hybrid search"),
            yt("Reranking izahı", "Cohere", "20 d", "reranking cross encoder rag"),
        ],
        [
            doc("LlamaIndex sənədləri", "docs.llamaindex.ai", LLAMAINDEX),
            gq("Advanced RAG texnikaları", "huggingface.co", "advanced rag techniques survey"),
        ],
        [
            "BM25 və vektor axtarışını birləşdir (hybrid)",
            "Reranker əlavə et və nəticəni müqayisə et",
            "2 fərqli chunking strategiyasını sına",
            "Nəticələri cədvəldə göstər",
        ],
        "Hybrid + reranking ilə təkmilləşdirilmiş RAG (müqayisə cədvəli ilə)",
        [
            "Hybrid search nə qazandırır?",
            "Reranker nə üçün lazımdır?",
            "Semantic chunking nə vaxt üstündür?",
        ],
    ),
    day(
        "RAG III: qiymətləndirmə və test dəsti",
        [
            "RAG-ın qiymətləndirmə ölçüləri (context recall, faithfulness)",
            "Test sual dəsti yaratmaq",
            "RAGAS və LLM-as-judge",
            "Regressiya testləri",
        ],
        [
            yt("RAG qiymətləndirmə", "LlamaIndex / RAGAS", "35 d", "evaluating rag pipelines ragas"),
            yt("LLM-as-judge qiymətləndirmə", "DeepLearning.AI", "25 d", "llm as a judge evaluation"),
        ],
        [
            doc("RAGAS sənədləri", "docs.ragas.io", RAGAS),
            gq("RAG evaluation metrikaları", "arxiv.org", "rag evaluation metrics faithfulness context"),
        ],
        [
            "20 sualdan ibarət test dəsti hazırla",
            "Hər cavabı 1-5 bal ilə qiymətləndir",
            "Prompt dəyişikliyinin təsirini ölç",
            "Qiymətləndirməni skriptə çevir (təkrar işlədilə bilən)",
        ],
        "Avtomatlaşdırılmış RAG qiymətləndirmə skripti + nəticələr",
        [
            "Faithfulness nə deməkdir?",
            "Retrieval metrikaları hansılardır?",
            "Regressiya testi niyə vacibdir?",
        ],
    ),
    day(
        "RAG tətbiqini API kimi qurmaq",
        [
            "RAG servisinin arxitekturası",
            "Endpoint dizaynı və sxemalar",
            "Kontekst və sessiya idarəsi",
            "Loglama və xərclərin izlənməsi",
        ],
        [
            yt("FastAPI ilə LLM servisi", "AssemblyAI", "40 d", "fastapi llm api tutorial rag"),
            yt("RAG API dizaynı", "James Briggs", "30 d", "building rag api service design"),
        ],
        [
            doc("FastAPI sənədləri", "fastapi.tiangolo.com", "https://fastapi.tiangolo.com/"),
            doc("Hugging Face Spaces", "huggingface.co", "https://huggingface.co/docs/hub/spaces"),
        ],
        [
            "RAG axınını FastAPI endpoint-inə çevir",
            "Sorğu/cavab sxemalarını Pydantic ilə yaz",
            "Loglama əlavə et (sual, retrieval nəticələri, xərc)",
            "Lokal olaraq servisi test et (curl / Swagger UI)",
        ],
        "İşləyən RAG API-si (Swagger UI ilə test edilmiş)",
        [
            "API sxeması nə üçün vacibdir?",
            "Sessiya necə saxlanılır?",
            "Nəyi loglamaq lazımdır?",
        ],
    ),
    day(
        "Agents I: tool use və function calling",
        [
            "Agent nədir (plan -> act -> observe dövrü)",
            "Tool/function calling mexanizmi",
            "Tool dizaynı və təsvirləri",
            "Xəta halları və fallback",
        ],
        [
            yt("AI agents izahı", "Andrej Karpathy / DeepLearning.AI", "35 d", "ai agents explained tool use"),
            yt("Function calling tutorial", "OpenAI", "30 d", "openai function calling tutorial"),
        ],
        [
            doc("Function calling sənədləri", "platform.openai.com", FUNCTION_CALLING),
            doc("Lilian Weng: LLM Agents", "lilianweng.github.io", LILIAN_AGENT),
        ],
        [
            "3 tool təyin et (kalkulyator, axtarış, vaxt)",
            "Agent dövrünü sıfırdan yaz (döngü + tool seçimi)",
            "Tool xətalarını idarə et",
            "Agent loglarını yaz və analiz et",
        ],
        "Sıfırdan yazılmış minimal agent (3 tool ilə)",
        [
            "Agent və adi LLM çağırışı fərqi nədir?",
            "Tool təsviri nə üçün kritikdir?",
            "Sonsuz döngüdən necə qorunmaq olar?",
        ],
    ),
    day(
        "Agents II: framework-lər, memory, multi-agent",
        [
            "LangChain və LlamaIndex agent abstraksiyaları",
            "Memory: qısa və uzunmüddətli yaddaş",
            "Multi-agent sistemlər (planner, worker, critic)",
            "Agent təhlükəsizliyi və insan nəzarəti",
        ],
        [
            yt("LangChain agents", "LangChain", "45 d", "langchain agents tutorial tools memory"),
            yt("Multi-agent sistemlər", "DeepLearning.AI", "40 d", "multi agent systems llm tutorial"),
        ],
        [
            doc("LangChain agents sənədləri", "python.langchain.com", LANGCHAIN + "docs/concepts/agents/"),
            doc("Model Context Protocol", "modelcontextprotocol.io", MCP),
        ],
        [
            "LangChain ilə eyni agenti qur və müqayisə et",
            "Memory əlavə et (söhbət tarixçəsi)",
            "2 agentli (planner + executor) nümunə qur",
            "İnsan təsdiqi (human-in-the-loop) addımı əlavə et",
        ],
        "Memory-li agent + qısa framework müqayisəsi",
        [
            "Memory olmadan agent nə edə bilmir?",
            "Multi-agent nə vaxt artıq mürəkkəblikdir?",
            "Framework nə qazandırır, nə itirir?",
        ],
    ),
    day(
        "Agents III: real layihə və izləmə",
        [
            "Araşdırma köməkçisi agentin dizaynı",
            "Observability (trace, latency, xərc)",
            "Qiymətləndirmə və regressiya testləri",
            "Deploy-a hazırlıq",
        ],
        [
            yt("Agent observability", "LangChain", "30 d", "langsmith agent observability tracing"),
            yt("Agent layihəsi nümunəsi", "Sam Witteveen", "40 d", "build research agent tutorial"),
        ],
        [
            doc("LangSmith sənədləri", "docs.smith.langchain.com", "https://docs.smith.langchain.com/"),
            doc("Simon Willison bloqu (LLM praktika)", "simonwillison.net", SIMON),
        ],
        [
            "Araşdırma agenti qur (veb axtarış + xülasə + sitat)",
            "Trace-ləri qeyd et və latency-ni ölç",
            "10 test sualı ilə agenti qiymətləndir",
            "Nəticələri README-də yaz",
        ],
        "İşləyən araşdırma agenti + trace-lər və qiymətləndirmə",
        [
            "Agent uğursuzluğunun 3 səbəbi nədir?",
            "Latency-ni necə azaltmaq olar?",
            "Nəyi test etmək lazımdır?",
        ],
    ),
    day(
        "LLM fine-tuning: təlimat dataseti",
        [
            "Instruction tuning anlayışı",
            "Dataset formatı (prompt-completion cütləri)",
            "LoRA/QLoRA ilə LLM fine-tuning",
            "Fine-tuning vs RAG vs prompt engineering qərarı",
        ],
        [
            yt("LLM fine-tuning əsasları", "Krish Naik", "40 d", "fine tuning llm lora tutorial"),
            yt("LoRA və QLoRA praktikada", "Trelis Research", "45 d", "lora qlora fine tuning practical"),
        ],
        [
            doc("PEFT sənədləri", "huggingface.co", HF_PEFT),
            doc("Hugging Face LLM kursu (fine-tuning fəsli)", "huggingface.co", HF_LLM),
        ],
        [
            "50 nümunəlik təlimat dataseti yarat",
            "Kiçik modeli QLoRA ilə fine-tune et",
            "Əvvəl/sonra cavablarını müqayisə et",
            "Yaddaş və vaxt xərclərini qeyd et",
        ],
        "Öz datasetində fine-tuned model + müqayisə hesabatı",
        [
            "Nə vaxt RAG, nə vaxt fine-tuning?",
            "Dataset keyfiyyəti nəticəyə necə təsir edir?",
            "QLoRA nəyi qənaət edir?",
        ],
    ),
    day(
        "Open-source LLM-lər və lokal inference",
        [
            "Açıq modellər (Llama, Mistral, Qwen, Gemma)",
            "Ollama ilə lokal işləmə",
            "vLLM ilə sürətli servis",
            "Kvantizasiya formatları (GGUF, GPTQ, AWQ)",
        ],
        [
            yt("Ollama ilə lokal LLM", "Matthew Berman", "25 d", "ollama local llm tutorial"),
            yt("vLLM ilə servis", "vLLM", "30 d", "vllm serving tutorial"),
        ],
        [
            doc("Ollama repo", "github.com", OLLAMA),
            doc("vLLM sənədləri", "docs.vllm.ai", VLLM),
        ],
        [
            "Ollama quraşdır və 2 modeli sına",
            "Python-dan lokal modelə sorğu göndər",
            "Kiçik və böyük modelin sürətini müqayisə et",
            "Nəticələri cədvəldə yaz",
        ],
        "Lokal LLM işləyən mühit + sürət/keyfiyyət müqayisəsi",
        [
            "Lokal model nə vaxt bulud API-dən üstündür?",
            "Kvantizasiya nəyi dəyişir?",
            "Hansı hardware lazımdır?",
        ],
    ),
    day(
        "LLM qiymətləndirmə və benchmark-lar",
        [
            "Benchmark-lar (MMLU və s.) və məhdudiyyətləri",
            "Öz tapşırığınız üçün eval dəsti",
            "LLM-as-judge və insan qiymətləndirməsi",
            "Metrikaların seçilməsi",
        ],
        [
            yt("LLM evaluation", "DeepLearning.AI", "35 d", "llm evaluation benchmarks best practices"),
            yt("Benchmark-ların problemi", "Yannic Kilcher", "25 d", "llm benchmarks criticism"),
        ],
        [
            doc("Hugging Face Open LLM Leaderboard", "huggingface.co", "https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard"),
            doc("Hugging Face Papers", "huggingface.co", "https://huggingface.co/papers"),
        ],
        [
            "Öz eval dəstini yarat (30 sual)",
            "3 modeli eyni dəst üzərində müqayisə et",
            "Skriptlə avtomatik qiymətləndir",
            "Nəticələri cədvəl və qrafiklə göstər",
        ],
        "Öz eval dəsti + 3 modelin müqayisə hesabatı",
        [
            "Benchmark nəticələri niyə həmişə real performansı göstərmir?",
            "LLM-as-judge-un riski nədir?",
            "Eval dəsti necə genişləndirilir?",
        ],
    ),
    day(
        "Təhlükəsizlik, hallucination və guardrails",
        [
            "Hallucination səbəbləri və azaldılması",
            "Prompt injection və data exfiltration",
            "Guardrails: input/output yoxlaması",
            "Məsuliyyətli AI prinsipləri",
        ],
        [
            yt("Prompt injection izahı", "Simon Willison / IBM", "30 d", "prompt injection explained"),
            yt("LLM guardrails", "DeepLearning.AI", "30 d", "llm guardrails safety tutorial"),
        ],
        [
            doc("OWASP LLM Top 10", "genai.owasp.org", "https://genai.owasp.org/llm-top-10/"),
            doc("Simon Willison: prompt injection", "simonwillison.net", SIMON + "/2022/Sep/12/prompt-injection/"),
        ],
        [
            "Sisteminizə qarşı 5 injection cəhdi yaz və nəticələri qeyd et",
            "Input/output filter əlavə et",
            "Sitat məcburiyyəti (citation-only) sına",
            "Nəticələri təhlükəsizlik qeydində yaz",
        ],
        "Təhlükəsizlik testi hesabatı + guardrail implementasiyası",
        [
            "Prompt injection niyə fundamental problemdir?",
            "Output validasiyası nəyi tutur?",
            "İstifadəçi datasını necə qorumalı?",
        ],
    ),
    day(
        "LLM məhsulu: UX, latency, xərc",
        [
            "Streaming UX və gözləmə hissi",
            "Latency optimallaşdırması (kvantizasiya, keş, daha kiçik model)",
            "Xərc hesablaması və limitlər",
            "İstifadəçi rəyi və iterasiya",
        ],
        [
            yt("LLM tətbiqi UX-i", "LangChain / AI Engineer", "30 d", "llm app user experience streaming latency"),
            yt("LLM xərcini azaltmaq", "Trelis Research", "30 d", "reduce llm cost production optimization"),
        ],
        [
            doc("Hugging Face blog", "huggingface.co", HF_BLOG),
            gq("LLM tətbiqi best practices", "eugeneyan.com", "llm application best practices production"),
        ],
        [
            "Tətbiqinizə keş (caching) əlavə et",
            "P95 latency-ni ölç",
            "Kiçik model ilə böyük modeli xərc/keyfiyyət baxımından müqayisə et",
            "3 optimallaşdırma qərarını yaz",
        ],
        "Latency və xərc optimallaşdırma hesabatı",
        [
            "Latency-ni ən sürətli azaldan 2 addım nədir?",
            "Keş nə vaxt yanlış nəticə verir?",
            "Kiçik modeli nə vaxt seçmək lazımdır?",
        ],
    ),
    day(
        "Multimodal və səs modelləri",
        [
            "CLIP: şəkil-mətn əlaqəsi",
            "Vision-language modellər",
            "Whisper ilə nitq mətnə çevirmə",
            "Multimodal tətbiq nümunələri",
        ],
        [
            yt("CLIP izahı", "Yannic Kilcher", "25 d", "clip paper explained"),
            yt("Whisper ilə transkripsiya", "AssemblyAI", "30 d", "whisper transcription tutorial"),
        ],
        [
            doc("Paper: CLIP", "arxiv.org", CLIP),
            doc("Whisper repo", "github.com", WHISPER),
        ],
        [
            "Whisper ilə bir audio faylı mətnə çevir",
            "CLIP ilə şəkil-klassifikasiya et",
            "Multimodal kiçik tətbiq qur (şəkil + sual)",
            "Nəticələri qiymətləndir",
        ],
        "Multimodal mini tətbiq (səs + şəkil + mətn)",
        [
            "CLIP necə öyrədilir?",
            "Whisper-in məhdudiyyətləri nədir?",
            "Multimodal model nə vaxt lazımdır?",
        ],
    ),
    day(
        "LLM layihəsini deploy etmək",
        [
            "Hugging Face Spaces ilə yayımlama",
            "Docker ilə paketləmə (sonra ətraflı)",
            "Sirrlərin idarəsi (API keys)",
            "Demo-nun sabit işləməsi (xəta idarəsi, limitlər)",
        ],
        [
            yt("Hugging Face Spaces deploy", "Hugging Face", "30 d", "deploy app hugging face spaces tutorial"),
            yt("Gradio ilə UI qurmaq", "Hugging Face", "35 d", "gradio interface tutorial"),
        ],
        [
            doc("Hugging Face Spaces sənədləri", "huggingface.co", "https://huggingface.co/docs/hub/spaces-overview"),
            doc("Gradio sənədləri", "gradio.app", "https://www.gradio.app/docs"),
        ],
        [
            "RAG/agent tətbiqinə Gradio UI yaz",
            "Spaces-ə deploy et",
            "API açarlarını secret kimi əlavə et",
            "Xəta hallarını ekranda göstər",
        ],
        "Canlı demo (Hugging Face Spaces) linki",
        [
            "Sirrləri necə təhlükəsiz saxlamaq olar?",
            "Demo-da ən çox hansı xəta olur?",
            "Demo-nu necə stabil saxlamaq olar?",
        ],
    ),
    day(
        "Portfolio: LLM layihəsini sənədləşdirmək",
        [
            "README strukturu (problem, yanaşma, nəticə, demo)",
            "Arxitektura diaqramı",
            "Demo videosu və skrinşotlar",
            "Nəticələrin rəqəmlərlə ifadəsi",
        ],
        [
            yt("Layihə README necə yazılır", "Krish Naik", "25 d", "how to write project readme machine learning"),
            yt("Portfolio layihəsi təqdimatı", "Ken Jee", "30 d", "data science portfolio project presentation"),
        ],
        [
            doc("GitHub README bələdçisi", "docs.github.com", "https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes"),
            doc("Make a README", "makeareadme.com", "https://www.makeareadme.com/"),
        ],
        [
            "Layihə README-ni problem-yanaşma-nəticə strukturunda yenidən yaz",
            "Arxitektura diaqramı çək (draw.io)",
            "2 dəqiqəlik demo videosu çək",
            "Nəticələri rəqəmlərlə cədvəldə ver",
        ],
        "Peşəkar README + diaqram + demo videosu olan LLM layihəsi",
        [
            "README-də ilk 5 sətir nə olmalıdır?",
            "Demo video nə üçün lazımdır?",
            "Hansı rəqəmlər təsir edicidir?",
        ],
    ),
    day(
        "İstifadəçi rəyi və iterasiya dövrü (feedback loop)",
        [
            "İstifadəçi rəyinin toplanması (like/dislike, şərhlər)",
            "Uğursuzluq hallarının kateqoriyalaşdırılması",
            "Eval dəstinin rəylər əsasında böyüdülməsi",
            "A/B testləri və təkmilləşdirmə prioritetləri",
        ],
        [
            yt("LLM tətbiqində feedback loop", "LangChain / AI Engineer", "30 d", "llm app feedback loop user feedback evaluation"),
            yt("A/B testi məhsulda", "StatQuest", "25 d", "ab testing product metrics statistics"),
        ],
        [
            doc("Hugging Face blog (praktika yazıları)", "huggingface.co", HF_BLOG),
            gq("LLM tətbiqi təkmilləşdirmə dövrü", "eugeneyan.com", "improving llm applications feedback loop"),
        ],
        [
            "Tətbiqə rəy toplama mexanizmi əlavə et (UI-da 2 düymə)",
            "20 uğursuzluq halını kateqoriyalara böl",
            "Eval dəstinə 10 yeni sual əlavə et",
            "Növbəti 3 təkmilləşdirməni prioritetləşdir",
        ],
        "Rəy toplama mexanizmi + uğursuzluq analizi hesabatı",
        [
            "Uğursuzluqları necə kateqoriyalaşdırırsan?",
            "Rəy necə eval dəstinə çevrilir?",
            "Hansı təkmilləşdirməni ilk edərdin?",
        ],
    ),
    day(
        "Model Context Protocol (MCP) və tool ekosistemi",
        [
            "MCP nədir və hansı problemi həll edir",
            "Server/client arxitekturası",
            "Tool, resource və prompt primitivləri",
            "Agenti xarici sistemlərə qoşmaq",
        ],
        [
            yt("Model Context Protocol izahı", "Anthropic / AI Engineer", "25 d", "model context protocol explained mcp"),
            yt("MCP server qurmaq", "Sam Witteveen", "30 d", "build mcp server tutorial"),
        ],
        [
            doc("MCP sənədləri", "modelcontextprotocol.io", MCP),
            doc("Anthropic sənədləri", "docs.anthropic.com", ANTHROPIC),
        ],
        [
            "MCP-nin 3 primitivini yaz və izah et",
            "Mövcud MCP server-lərdən birini istifadə et",
            "Öz tool-unu (fayl oxuma) MCP server kimi paketlə",
            "Agentini MCP üzərindən qoş və test et",
        ],
        "Kiçik MCP server + agent inteqrasiyası",
        [
            "MCP hansı problemi həll edir?",
            "Tool ilə resource fərqi nədir?",
            "MCP olmadan eyni işi necə edərdin?",
        ],
    ),
    day(
        "Müsahibə hazırlığı I: NLP və LLM sualları",
        [
            "Transformer detal sualları",
            "Embedding və RAG sualları",
            "Fine-tuning qərarları",
            "Tipik səhv cavablar",
        ],
        [
            yt("NLP müsahibə sualları", "Krish Naik", "40 d", "nlp interview questions answers"),
            yt("LLM müsahibə sualları", "AI Engineer / DeepLearning.AI", "35 d", "llm interview questions generative ai"),
        ],
        [
            doc("Hugging Face LLM kursu (təkrar)", "huggingface.co", HF_LLM),
            gq("NLP müsahibə sualları toplu", "github.com", "nlp interview questions github"),
        ],
        [
            "30 NLP/LLM sualına yazılı cavab hazırla",
            "Self-attention-ı ağ vərəqdə yaz",
            "RAG arxitekturasını izah et (2 dəqiqə)",
            "Zəif mövzuları qeyd et və planla",
        ],
        "30 sual-cavabdan ibarət NLP/LLM müsahibə qeydi",
        [
            "Transformer-i 2 dəqiqədə necə izah edərdin?",
            "RAG ilə fine-tuning fərqini necə izah edərdin?",
            "Hansı mövzu hələ zəifdir?",
        ],
    ),
    day(
        "Faza 6 layihəsi: tam RAG + agent tətbiqi",
        [
            "Layihə birləşdirilməsi: RAG + agent + UI",
            "Qiymətləndirmə və optimallaşdırma",
            "Deploy və sənədləşdirmə",
            "Portfolio-ya əlavə",
        ],
        [
            yt("Full stack AI app", "AI Jason / Smith", "45 d", "build full stack llm app rag agent"),
            yt("RAG tətbiqini optimallaşdırmaq", "LlamaIndex", "30 d", "optimize rag application production"),
        ],
        [
            doc("LangChain sənədləri (təkrar)", "python.langchain.com", LANGCHAIN),
            doc("Streamlit sənədləri", "docs.streamlit.io", "https://docs.streamlit.io/"),
        ],
        [
            "RAG + agent funksiyalarını bir tətbiqdə birləşdir",
            "20 suallıq test dəsti ilə qiymətləndir",
            "UI əlavə et (Gradio/Streamlit)",
            "Deploy et və README-də nəticələri yaz",
        ],
        "Canlı demo + kod + hesabat: `llm-rag-agent` layihəsi",
        [
            "Sistemin arxitekturası necədir?",
            "Hansı metrikaları ölçdün?",
            "Nəyi fərqli edərdin?",
        ],
    ),
]

weeks = [
    {
        "focus": "Prompt engineering və LLM API-ləri",
        "project": "Prompt kitabçası: 20 prompt nümunəsi, nəticələrin müqayisəsi və xərc hesablaması",
        "quiz": "Prompting, structured output, API idarəsi və token xərci üzrə 10 sual",
    },
    {
        "focus": "Embedding, vektor bazaları və RAG",
        "project": "RAG prototipi: sənəd toplusu üzərində sual-cavab, retrieval metrikaları ilə qiymətləndirmə",
        "quiz": "Embedding, vektor indeksləri, RAG arxitekturası və qiymətləndirmə üzrə 10 sual",
    },
    {
        "focus": "Agents, fine-tuning və açıq modellər",
        "project": "Agent layihəsi: tool-lar istifadə edən araşdırma köməkçisi + trace-lər və eval dəsti",
        "quiz": "Agents, function calling, LoRA, kvantizasiya və benchmark-lar üzrə 10 sual",
    },
    {
        "focus": "Təhlükəsizlik, multimodal və deploy",
        "project": "Portfolio demo: RAG/agent tətbiqini deploy edib GitHub-da sənədləşdirmək (demo videosu ilə)",
        "quiz": "Təhlükəsizlik, guardrails, multimodal modellər və deploy üzrə 10 sual",
    },
]

PHASE = phase(
    6,
    "NLP və Böyük Dil Modelləri (LLM)",
    "Prompt engineering, embedding, RAG, agentlər, fine-tuning və LLM tətbiqini deploy etmək.",
    "72-82 saat",
    weeks,
    days,
)
