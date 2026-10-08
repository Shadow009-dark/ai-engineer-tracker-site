"""Phase 8 - MLOps and deployment (days 155-168, 2 weeks, 12 study days)."""

from helpers import day, doc, gq, phase, yt

FASTAPI = "https://fastapi.tiangolo.com/"
DOCKER = "https://docs.docker.com/get-started/"
DOCKER_COMPOSE = "https://docs.docker.com/compose/"
K8S = "https://kubernetes.io/docs/tutorials/"
GH_ACTIONS = "https://docs.github.com/en/actions"
MLFLOW = "https://mlflow.org/docs/latest/"
MLFLOW_TRACK = "https://mlflow.org/docs/latest/tracking.html"
EVIDENTLY = "https://docs.evidentlyai.com/"
DVC = "https://dvc.org/"
MLOPS_ZC = "https://github.com/DataTalksClub/mlops-zoomcamp"
MADEWITHML = "https://madewithml.com/"
MLOPS_ORG = "https://ml-ops.org/"
FSDL = "https://fullstackdeeplearning.com/course/"
WANDB = "https://docs.wandb.ai/"
HF_SPACES = "https://huggingface.co/docs/hub/spaces"
GCRASH = "https://developers.google.com/machine-learning/crash-course"

days = [
    day(
        "MLOps nədir: lifecycle və olgunluq",
        [
            "ML lifecycle: data -> model -> deploy -> monitorinq",
            "CI/CD/CT anlayışları",
            "MLOps olgunluq səviyyələri (0-2)",
            "Rollar: data scientist, ML engineer, MLOps engineer",
        ],
        [
            yt("MLOps Full Course", "DataTalksClub (MLOps Zoomcamp)", "1s 30d", "mlops zoomcamp introduction"),
            yt("MLOps nədir", "Krish Naik", "25 d", "what is mlops explained"),
        ],
        [
            doc("MLOps Zoomcamp", "github.com/DataTalksClub", MLOPS_ZC),
            doc("MLOps principles", "ml-ops.org", MLOPS_ORG),
        ],
        [
            "ML lifecycle diaqramını çək",
            "Öz layihəniz üçün olgunluq səviyyəsini qiymətləndir",
            "CI/CD/CT fərqini yaz",
            "Növbəti addımları prioritetləşdir",
        ],
        "Şəxsi ML lifecycle diaqramı + olgunluq qiymətləndirməsi",
        [
            "MLOps hansı problemi həll edir?",
            "CT (continuous training) nədir?",
            "Olgunluq səviyyələri nə ilə fərqlənir?",
        ],
    ),
    day(
        "FastAPI ilə model servisi",
        [
            "FastAPI əsasları: endpoint, router, status kodları",
            "Pydantic ilə sxema və validasiya",
            "Modelin yüklənməsi və tək instance (startup)",
            "Xəta idarəsi və sağlamlıq endpoint-i",
        ],
        [
            yt("FastAPI Full Course", "freeCodeCamp", "4s", "fastapi full course freecodecamp"),
            yt("ML modelini FastAPI ilə deploy etmək", "Krish Naik", "35 d", "deploy machine learning model fastapi"),
        ],
        [
            doc("FastAPI sənədləri", "fastapi.tiangolo.com", FASTAPI),
            doc("Pydantic sənədləri", "docs.pydantic.dev", "https://docs.pydantic.dev/latest/"),
        ],
        [
            "Model yükləyən FastAPI tətbiqi yaz",
            "Pydantic ilə giriş/çıxış sxemaları təyin et",
            "Sağlamlıq endpoint-i əlavə et (/health)",
            "Swagger UI-da test et və xəta hallarını sına",
        ],
        "İşləyən model API-si (validasiya + xəta idarəsi ilə)",
        [
            "Niyə sxemalar vacibdir?",
            "Model niyə bir dəfə yüklənməlidir?",
            "Status kodları necə seçilir?",
        ],
    ),
    day(
        "Docker əsasları",
        [
            "Image, container, registry anlayışları",
            "Dockerfile: FROM, COPY, RUN, CMD",
            "Layer keşi və build sürəti",
            "Volume və port mapping",
        ],
        [
            yt("Docker Full Course", "TechWorld with Nana", "3s", "docker tutorial techworld with nana"),
            yt("Docker 30 dəqiqədə", "Fireship", "30 d", "docker in 30 minutes fireship"),
        ],
        [
            doc("Docker get started", "docs.docker.com", DOCKER),
            doc("Dockerfile reference", "docs.docker.com", "https://docs.docker.com/reference/dockerfile/"),
        ],
        [
            "Python skripti üçün Dockerfile yaz",
            "Image build et və container işə sal",
            "Layer keşini müşahidə et (RUN sırasını dəyiş)",
            "Volume ilə fayl paylaşımını göstər",
        ],
        "İşləyən Docker image + Dockerfile izahı",
        [
            "Image ilə container fərqi nədir?",
            "Layer keşi necə işləyir?",
            "Volume nə üçün lazımdır?",
        ],
    ),
    day(
        "Docker + ML: model image-ı",
        [
            "ML üçün Docker image dizaynı",
            "Multi-stage build ilə ölçü azaltma",
            "Base image seçimi (python-slim, CUDA image-ları)",
            "Modelin image-a daxil edilməsi",
        ],
        [
            yt("Docker for machine learning", "Krish Naik", "40 d", "docker for machine learning projects"),
            yt("Multi-stage Docker builds", "TechWorld with Nana", "25 d", "docker multi stage build tutorial"),
        ],
        [
            doc("Docker best practices", "docs.docker.com", "https://docs.docker.com/build/building/best-practices/"),
            doc("Made With ML (deploy bölməsi)", "madewithml.com", MADEWITHML),
        ],
        [
            "Model API-si üçün Dockerfile yaz",
            "Multi-stage build ilə ölçünü azalt",
            "Image ölçüsünü müqayisə et (əvvəl/sonra)",
            "`.dockerignore` faylı əlavə et",
        ],
        "Kiçildilmiş, işləyən ML image-ı + ölçü müqayisəsi",
        [
            "Multi-stage build nə qazandırır?",
            "`.dockerignore` nə üçün vacibdir?",
            "CUDA image-ları nə vaxt lazımdır?",
        ],
    ),
    day(
        "docker compose, konfiqurasiya və sirrlər",
        [
            "docker compose ilə çoxservisli tətbiq",
            "Environment dəyişənləri və .env faylları",
            "Sirrlərin idarəsi (Docker secrets, cloud secret manager)",
            "Servislər arasında şəbəkə (network)",
        ],
        [
            yt("Docker Compose tutorial", "TechWorld with Nana", "40 d", "docker compose tutorial multi container"),
            yt("Sirrlərin idarəsi", "Krish Naik", "20 d", "managing secrets docker environment variables"),
        ],
        [
            doc("Docker Compose sənədləri", "docs.docker.com", DOCKER_COMPOSE),
            doc("12-Factor: konfiqurasiya", "12factor.net", "https://12factor.net/config"),
        ],
        [
            "API + verilənlər bazası üçün compose faylı yaz",
            "Konfiqurasiyanı .env ilə idarə et",
            "Sirri birbaşa fayla yazma (image-a daxil etmə)",
            "Servisləri bir əmrlə işə sal və test et",
        ],
        "docker compose ilə işləyən çoxservisli ML tətbiqi",
        [
            "Compose nə vaxt faydalıdır?",
            "Sirrləri necə təhlükəsiz saxlamaq olar?",
            "Servislər bir-birini necə tapır?",
        ],
    ),
    day(
        "Cloud əsasları: GPU, storage, xərc",
        [
            "IaaS/PaaS/FaaS fərqi",
            "GPU instansları və seçim meyarları",
            "Object storage və maşın öyrənməsi üçün data saxlama",
            "Xərc idarəsi strategiyaları",
        ],
        [
            yt("Cloud computing əsasları", "TechWorld with Nana", "40 d", "cloud computing explained aws azure gcp"),
            yt("GPU cloud xərclərini azaltmaq", "Yannic Kilcher / hobbyist", "25 d", "cheap gpu cloud training llm cost tips"),
        ],
        [
            doc("AWS SageMaker", "aws.amazon.com", "https://aws.amazon.com/sagemaker/"),
            doc("Google Cloud ML", "cloud.google.com", "https://cloud.google.com/vertex-ai"),
        ],
        [
            "3 provayderin GPU qiymətlərini müqayisə et",
            "Öz layihəsi üçün xərc təxmini hesabla",
            "Storage siniflərini müqayisə et",
            "Xərci azaltmağın 3 yolunu yaz",
        ],
        "Xərc müqayisəsi cədvəli + seçim əsaslandırması",
        [
            "On-demand ilə spot instans fərqi nədir?",
            "Object storage nə vaxt lazımdır?",
            "Xərc ən çox hansı addımda artır?",
        ],
    ),
    day(
        "Deployment variantları",
        [
            "Real-time, batch, streaming, edge deployment",
            "Serverless inference (Lambda, Cloud Run, HF Inference Endpoints)",
            "Modelin versiyalanması və rollback",
            "Trafik idarəsi (canary, blue-green)",
        ],
        [
            yt("ML model deployment üsulları", "Krish Naik", "40 d", "machine learning model deployment strategies"),
            yt("Serverless ML inference", "Made With ML", "25 d", "serverless machine learning inference"),
        ],
        [
            doc("HF Inference Endpoints", "huggingface.co", "https://huggingface.co/docs/inference-endpoints/index"),
            doc("Full Stack Deep Learning", "fullstackdeeplearning.com", FSDL),
        ],
        [
            "Layihəniz üçün 3 deployment variantını müqayisə et",
            "Bir variantı seç və səbəbini yaz",
            "Rollback planı hazırla",
            "Canary deployment-i diaqramla izah et",
        ],
        "Deployment strategiyası sənədi (seçim + rollback planı)",
        [
            "Batch ilə real-time fərqi nədir?",
            "Canary deployment niyə lazımdır?",
            "Model versiyası necə idarə olunur?",
        ],
    ),
    day(
        "CI/CD for ML: GitHub Actions ilə avtomatlaşdırma",
        [
            "Test -> build -> deploy pipeline-ı",
            "Docker image-ının CI-da build edilməsi",
            "Registry-yə push və deploy addımı",
            "Model keyfiyyət qapıları (testlər keçməzsə deploy yox)",
        ],
        [
            yt("GitHub Actions ilə CI/CD", "TechWorld with Nana", "1s", "github actions docker build push ci cd"),
            yt("ML üçün CI/CD", "Made With ML", "30 d", "ci cd machine learning pipeline github actions"),
        ],
        [
            doc("GitHub Actions sənədləri", "docs.github.com", GH_ACTIONS),
            doc("Made With ML kursu", "madewithml.com", MADEWITHML),
        ],
        [
            "Workflow yaz: testlər -> docker build -> registry push",
            "Model metrikası həddən aşağı olsa pipeline-ı dayandır",
            "Deploy addımını əlavə et",
            "Pipeline-ın işlədiyini sübut et (yaşıl badge)",
        ],
        "Tam işləyən CI/CD pipeline-ı (test + build + deploy)",
        [
            "Keyfiyyət qapısı nədir?",
            "Image registry nə üçün lazımdır?",
            "Deploy uğursuz olsa nə edilməlidir?",
        ],
    ),
    day(
        "Monitorinq və drift aşkarlanması",
        [
            "Data drift, concept drift, model drift",
            "Monitorinq metrikaları (latency, xəta, paylanma)",
            "Evidently ilə drift hesabatı",
            "Alerting və insident idarəsi",
        ],
        [
            yt("Data drift və monitorinq", "Evidently AI", "35 d", "data drift monitoring machine learning"),
            yt("ML model monitorinqi", "Krish Naik", "25 d", "machine learning model monitoring production"),
        ],
        [
            doc("Evidently sənədləri", "docs.evidentlyai.com", EVIDENTLY),
            doc("Weights & Biases sənədləri", "docs.wandb.ai", WANDB),
        ],
        [
            "İki dataset arasında drift hesabla (Evidently)",
            "Drift hesabatını HTML kimi çıxart",
            "Monitorinq panosu üçün 5 metriki seç",
            "Alert qaydası yaz (hansı həddə nə edilsin)",
        ],
        "Drift hesabatı + monitorinq planı",
        [
            "Data drift ilə concept drift fərqi nədir?",
            "Drift aşkarlandıqda ilk addım nədir?",
            "Hansı metrikləri izləmək lazımdır?",
        ],
    ),
    day(
        "Experiment tracking və model registry",
        [
            "MLflow tracking: run, parameter, metric, artifact",
            "Model registry və versiya idarəsi",
            "Modelin staging -> production keçidi",
            "Reproduksiya üçün minimum məlumat dəsti",
        ],
        [
            yt("MLflow tam kurs", "Krish Naik", "45 d", "mlflow tutorial tracking model registry"),
            yt("Model registry nədir", "Made With ML", "20 d", "model registry versioning production"),
        ],
        [
            doc("MLflow tracking", "mlflow.org", MLFLOW_TRACK),
            doc("MLflow model registry", "mlflow.org", "https://mlflow.org/docs/latest/model-registry.html"),
        ],
        [
            "Layihədə MLflow serveri işə sal",
            "5 eksperimenti log et (parametr, metrik, artifact)",
            "Ən yaxşı modeli registry-yə qeyd et",
            "REPLACE-yə keçid prosesini yaz",
        ],
        "MLflow ilə izlənən eksperimentlər + registry-də model",
        [
            "Run ilə experiment fərqi nədir?",
            "Registry nə üçün lazımdır?",
            "Artifact nədir?",
        ],
    ),
    day(
        "Data versiyalama və pipeline orkestrasiyası",
        [
            "Data versiyalama (DVC) prinsipləri",
            "Pipeline-lar: Airflow, Prefect, Dagster (tanışlıq)",
            "Təkrarlanan təlim iş axını",
            "Feature store anlayışı",
        ],
        [
            yt("DVC tutorial", "DVC (rəsmi)", "30 d", "dvc data version control tutorial"),
            yt("Airflow əsasları", "TechWorld with Nana", "35 d", "airflow tutorial beginners dag"),
        ],
        [
            doc("DVC sənədləri", "dvc.org", DVC),
            doc("Airflow sənədləri", "airflow.apache.org", "https://airflow.apache.org/docs/"),
        ],
        [
            "DVC quraşdır və dataset-i versiyala",
            "Kiçik pipeline yaz (data -> təlim -> metrikalar)",
            "DVC ilə pipeline-ı təkrar işlədə bilən et",
            "Nəticələri qeyd et",
        ],
        "DVC ilə versiyalanmış dataset + təkrar işləyən pipeline",
        [
            "Data versiyalama nə üçün lazımdır?",
            "DAG nədir?",
            "Feature store nə problemi həll edir?",
        ],
    ),
    day(
        "MLOps layihəsi: modeldən monitorinqə",
        [
            "Bütün MLOps biliklərinin birləşdirilməsi",
            "Avtomatlaşdırılmış pipeline-ın qurulması",
            "Monitorinq və alerting",
            "Sənədləşdirmə və nəticələrin təqdimatı",
        ],
        [
            yt("Tam MLOps layihəsi", "DataTalksClub", "1s", "end to end mlops project example"),
            yt("ML modelini production-a çıxarmaq", "Made With ML", "40 d", "deploy ml model production end to end"),
        ],
        [
            doc("MLOps Zoomcamp (təkrar)", "github.com/DataTalksClub", MLOPS_ZC),
            doc("Full Stack Deep Learning", "fullstackdeeplearning.com", FSDL),
        ],
        [
            "Modeli FastAPI + Docker ilə paketlə",
            "CI/CD pipeline-ı qur",
            "MLflow ilə izlə və registry-dən yüklə",
            "Monitorinq + drift hesabatı əlavə et və README yaz",
        ],
        "GitHub-da `mlops-deployment` reposu (API + Docker + CI/CD + monitoring)",
        [
            "Arxitektura necədir (diaqramla)?",
            "Hansson zaman model yenilənir?",
            "Hansı metrikalar izlənir?",
        ],
    ),
]

weeks = [
    {
        "focus": "Servis, Docker və cloud",
        "project": "Docker + FastAPI: öz modelinizi microservice kimi qablaşdırın (docker compose ilə) və xərc hesablaması çıxarın",
        "quiz": "FastAPI, Docker, compose, cloud sitayişi və deployment variantları üzrə 10 sual",
    },
    {
        "focus": "CI/CD, monitorinq və registry",
        "project": "MLOps pipeline: GitHub Actions ilə test -> build -> deploy + drift monitorinqi və MLflow registry",
        "quiz": "CI/CD, drift, monitorinq, MLflow və data versiyalama üzrə 10 sual",
    },
]

PHASE = phase(
    8,
    "MLOps və deployment",
    "Modeli API, Docker, bulud və monitorinq ilə istehsal mühitinə çıxarmaq.",
    "36-41 saat",
    weeks,
    days,
)
