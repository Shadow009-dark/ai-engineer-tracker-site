"""Phase 5 - Deep learning with PyTorch (days 85-112, 4 weeks, 24 study days)."""

from helpers import day, doc, gq, phase, yt

PT = "https://pytorch.org/tutorials/"
PT_BASICS = "https://pytorch.org/tutorials/beginner/basics/intro.html"
PT_DOCS = "https://pytorch.org/docs/stable/index.html"
PT_AUTOGRAD = "https://pytorch.org/docs/stable/notes/autograd.html"
PT_CIFAR = "https://pytorch.org/tutorials/beginner/blitz/cifar10_tutorial.html"
PT_TRANSF = "https://pytorch.org/tutorials/beginner/transfer_learning_tutorial.html"
PT_SEQ2SEQ = "https://pytorch.org/tutorials/intermediate/seq2seq_translation_tutorial.html"
PT_TRANSFORMER = "https://pytorch.org/tutorials/beginner/transformer_tutorial.html"
PT_WORD_EMB = "https://pytorch.org/tutorials/beginner/nlp/word_embeddings_tutorial.html"
HF_COURSE = "https://huggingface.co/learn/nlp-course/chapter1/1"
HF_LLM = "https://huggingface.co/learn/llm-course/chapter1/1"
HF_TRANSFORMERS = "https://huggingface.co/docs/transformers/index"
HF_DATASETS = "https://huggingface.co/docs/datasets/index"
HF_PEFT = "https://huggingface.co/docs/peft/index"
HF_TOKENIZERS = "https://huggingface.co/docs/tokenizers/index"
ZERO_HERO = "https://karpathy.ai/zero-to-hero.html"
NANOGPT = "https://github.com/karpathy/nanoGPT"
LLM_C = "https://github.com/karpathy/llm.c"
D2L = "https://d2l.ai/"
FASTAI = "https://course.fast.ai/"
PLAYGROUND = "https://playground.tensorflow.org/"
ILLUSTRATED = "https://jalammar.github.io/illustrated-transformer/"
CS231N = "https://cs231n.stanford.edu/"
DL_AI = "https://www.deeplearning.ai/"
DISTILL = "https://distill.pub/"

days = [
    day(
        "Neyron şəbəkə əsasları: perceptron və MLP",
        [
            "Perceptron və onun məhdudiyyətləri",
            "Aktivasiya funksiyaları (ReLU, sigmoid, tanh, softmax)",
            "Çoxqatlı perceptron (MLP) və gizli qatlar",
            "Universal approximation ideyası",
        ],
        [
            yt("Neural Networks Zero to Hero (bölmə 1-2)", "Andrej Karpathy", "2s 30d", "karpathy zero to hero neural networks"),
            yt("But what is a Neural Network?", "3Blue1Brown", "20 d", "3blue1brown neural network introduction"),
        ],
        [
            doc("PyTorch: 60 dəqiqədə öyrən", "pytorch.org", "https://pytorch.org/tutorials/beginner/deep_learning_60min_blitz.html"),
            doc("Dive into Deep Learning (bölmə 3-5)", "d2l.ai", D2L),
        ],
        [
            "TensorFlow Playground-da şəbəkəni oynayaraq öyrən",
            "Bir neyronu əl ilə hesabla (giriş x çəki + bias -> aktivasiya)",
            "ReLU və sigmoid funksiyalarını çək",
            "Nə üçün xətti aktivasiya kifayət etmir sualını cavablandır",
        ],
        "Neyron şəbəkə intuisiya qeydi + Playground təcrübələri",
        [
            "Perceptron XOR problemini həll edə bilir?",
            "ReLU-nun üstünlüyü nədir?",
            "Gizli qatlar nə edir?",
        ],
    ),
    day(
        "Backpropagation əl ilə + PyTorch tensorları",
        [
            "Forward pass və loss",
            "Backward pass: chain rule tətbiqi",
            "Tensorlar: shape, dtype, device, cihaz seçimi (CPU/CUDA)",
            "Tensor əməliyyatları və broadcasting",
        ],
        [
            yt("Backpropagation əl ilə hesablama", "Andrej Karpathy", "1s", "karpathy backpropagation from scratch"),
            yt("PyTorch tensors əsasları", "Python Engineer", "30 d", "pytorch tensors tutorial"),
        ],
        [
            doc("PyTorch: tensorlar", "pytorch.org", PT_DOCS + "/tensors.html"),
            doc("PyTorch: autograd", "pytorch.org", PT_AUTOGRAD),
        ],
        [
            "İki qatlı şəbəkə üçün əl ilə backprop hesabla",
            "Tensorlar yarat, shape dəyişdir, CPU/GPU-da sına",
            "`.grad` dəyərlərini əl ilə hesablanan nəticə ilə müqayisə et",
            "Bank data üzərində mini MLP qur",
        ],
        "Əl ilə backprop + PyTorch müqayisəsi notebooku",
        [
            "Forward və backward pass fərqi nədir?",
            "Niyə tensorlar GPU-da sürətlidir?",
            "`requires_grad` nə edir?",
        ],
    ),
    day(
        "PyTorch I: nn.Module, optim, ilk təlim dövrü",
        [
            "nn.Module ilə model qurma",
            "Kayıp funksiyaları (MSELoss, CrossEntropyLoss)",
            "Optimizer və sıfırlama (`zero_grad`)",
            "Təlim dövrü: forward -> loss -> backward -> step",
        ],
        [
            yt("PyTorch for Deep Learning (təlim dövrü)", "Daniel Bourke", "1s", "pytorch deep learning workflow daniel bourke"),
            yt("nn.Module ilə model qurmaq", "Aladdin Persson", "30 d", "pytorch nn.module custom model"),
        ],
        [
            doc("PyTorch: basics təlimatı", "pytorch.org", PT_BASICS),
            doc("PyTorch: optimizasiya", "pytorch.org", PT + "beginner/basics/optimization_tutorial.html"),
        ],
        [
            "Xətti reqressiyanı PyTorch ilə yaz (nn.Linear)",
            "Klassifikasiya modelini CrossEntropyLoss ilə öyrət",
            "Təlim dövrünü funksiyaya çevir (train_step)",
            "Loss əyrisini çək",
        ],
        "PyTorch ilə iki tam model: reqressiya və klassifikasiya",
        [
            "Təlim dövrünün 4 addımı nədir?",
            "`zero_grad()` niyə hər iterasiyada çağırılır?",
            "CrossEntropyLoss hansı girişi gözləyir?",
        ],
    ),
    day(
        "PyTorch II: Dataset, DataLoader, GPU təlimi",
        [
            "Dataset və DataLoader sinifləri",
            "Batch, shuffle, collate_fn",
            "Transform-lar (torchvision)",
            "GPU-da təlim: `.to(device)`, xəta mənbələri",
        ],
        [
            yt("PyTorch Dataset və DataLoader", "Aladdin Persson", "35 d", "pytorch dataset dataloader tutorial"),
            yt("GPU-da PyTorch təlimi", "Python Engineer", "25 d", "pytorch gpu training cuda"),
        ],
        [
            doc("PyTorch: data ilə iş", "pytorch.org", PT + "beginner/basics/data_tutorial.html"),
            doc("torchvision transform-ları", "pytorch.org", "https://pytorch.org/vision/stable/transforms.html"),
        ],
        [
            "Öz Dataset sinfini yaz (CSV fayldan oxusun)",
            "DataLoader ilə batch-lar yarat və ölçüləri yoxla",
            "Təlimi GPU-da işə sal (Colab)",
            "CPU vs GPU vaxtını müqayisə et",
        ],
        "Şəxsi Dataset + DataLoader + GPU təlimi işləyən skript",
        [
            "Dataset ilə DataLoader fərqi nədir?",
            "`num_workers` nə edir?",
            "GPU-da təlim zamanı tipik xətalar nədir?",
        ],
    ),
    day(
        "Overfitting, regulyarizasiya və təlim strategiyaları",
        [
            "Overfitting və underfitting əlamətləri",
            "Weight decay, dropout, batch normalization",
            "Early stopping və model checkpointing",
            "Data augmentation-a giriş",
        ],
        [
            yt("Regularization üsulları", "Andrew Ng / DeepLearning.AI", "35 d", "regularization dropout batch normalization deeplearning ai"),
            yt("Overfitting-i necə aradan qaldırmaq", "Krish Naik", "25 d", "how to prevent overfitting deep learning"),
        ],
        [
            doc("Dropout (PyTorch)", "pytorch.org", "https://pytorch.org/docs/stable/generated/torch.nn.Dropout.html"),
            doc("Batch Normalization (paper)", "arxiv.org", "https://arxiv.org/abs/1502.03167"),
        ],
        [
            "Kiçik dataset-də qəsdən overfit et və əlamətləri göstər",
            "Dropout əlavə edib fərqi ölç",
            "Batch norm ilə təlimi sürətləndir",
            "Early stopping implement et",
        ],
        "Regulyarizasiya üsullarının müqayisə cədvəli",
        [
            "Dropout necə işləyir?",
            "Train və validation loss fərqi nə deməkdir?",
            "Early stopping nə vaxt dayanmalıdır?",
        ],
    ),
    day(
        "Təlimin debug edilməsi və optimallaşdırılması",
        [
            "Loss-un izlənməsi və anomaliyalar",
            "Learning rate finder və scheduler-lər",
            "Gradient clipping və ölü neyronlar",
            "Eksperimentlərin təkrar istehsalı (seed, versiya)",
        ],
        [
            yt("Deep learning modellərini debug etmək", "Andrej Karpathy", "30 d", "karpathy deep learning debugging tips"),
            yt("Learning rate scheduler", "Aladdin Persson", "20 d", "pytorch learning rate scheduler"),
        ],
        [
            doc("PyTorch: lr scheduler", "pytorch.org", "https://pytorch.org/docs/stable/optim.html#how-to-adjust-learning-rate"),
            gq("Model necə debug edilir", "karpathy.github.io", "a recipe for training neural networks karpathy"),
        ],
        [
            "Kiçik dataset üzərində modelləri overfit etmə testi apar",
            "Learning rate-i 10x artırıb/azaldıb effekti göstər",
            "Scheduler tətbiq et və loss əyrisini müqayisə et",
            "Gradient norm-u izləyib clipping tətbiq et",
        ],
        "Debug checklist-i + təlim jurnalı olan notebook",
        [
            "Loss NaN olursa ilk nə yoxlayarsan?",
            "Learning rate çox kiçik olsa nə olur?",
            "Gradient clipping nə vaxt lazımdır?",
        ],
    ),
    day(
        "CNN I: konvolusiya əməliyyatı",
        [
            "Convolution: kernel, padding, stride",
            "Feature map-lərin mənası",
            "Pooling (max, average) və downsample",
            "Receptive field və parametr sayının azalması",
        ],
        [
            yt("Convolutional Neural Networks izahı", "3Blue1Brown / CNN dərsləri", "25 d", "convolutional neural network 3blue1brown"),
            yt("CNN Full Course", "DeepLearning.AI", "1s", "convolutional neural networks deeplearning ai"),
        ],
        [
            doc("CS231n: CNN-lər", "cs231n.stanford.edu", CS231N),
            doc("PyTorch: Conv2d", "pytorch.org", "https://pytorch.org/docs/stable/generated/torch.nn.Conv2d.html"),
        ],
        [
            "Bir şəkli NumPy ilə konvolusiya et (əl ilə kernel)",
            "Edge detection kernel-i tətbiq et",
            "Padding və stride təsirini ölç",
            "Max pooling-i əl ilə implement et",
        ],
        "Əl ilə yazılmış konvolusiya + pooling implementasiyası",
        [
            "Konvolusiya ilə tam bağlı qat fərqi nədir?",
            "Padding nə vaxt lazımdır?",
            "Parameter sharing nə deməkdir?",
        ],
    ),
    day(
        "CNN II: PyTorch ilə şəkil klassifikasiyası",
        [
            "CNN arxitekturası qurmaq (Conv -> ReLU -> Pool)",
            "MNIST və CIFAR-10 dataset-ləri",
            "Təlim və qiymətləndirmə axını",
            "Səhv təsnifatları vizuallaşdırmaq",
        ],
        [
            yt("PyTorch CNN tutorial", "Aladdin Persson", "45 d", "pytorch cnn mnist tutorial"),
            yt("CIFAR-10 klassifikasiyası", "Daniel Bourke", "40 d", "cifar10 pytorch classification tutorial"),
        ],
        [
            doc("PyTorch: CIFAR-10 tutorial", "pytorch.org", PT_CIFAR),
            doc("torchvision dataset-ləri", "pytorch.org", "https://pytorch.org/vision/stable/datasets.html"),
        ],
        [
            "MNIST üzərində CNN öyrət və 98%+ dəqiqliyə çat",
            "CIFAR-10 üzərində CNN qur",
            "Confusion matrix çıxart",
            "Səhv təxmin olunan 10 şəkli göstər",
        ],
        "İki dataset üzərində işləyən CNN notebooku + səhv analizi",
        [
            "Niyə CNN şəkillərdə MLP-dən yaxşıdır?",
            "Batch size təlimə necə təsir edir?",
            "Səhvlər hansı siniflərdə cəmləşir?",
        ],
    ),
    day(
        "CNN III: transfer learning və data augmentation",
        [
            "Pretrained modellər və ImageNet",
            "Feature extraction vs fine-tuning",
            "Data augmentation (flip, crop, color jitter, mixup)",
            "Kiçik dataset-də yüksək nəticə əldə etmək",
        ],
        [
            yt("Transfer Learning dərsi", "Andrew Ng / DeepLearning.AI", "30 d", "transfer learning deep learning andrew ng"),
            yt("PyTorch transfer learning", "Aladdin Persson", "35 d", "pytorch transfer learning pretrained model"),
        ],
        [
            doc("PyTorch: transfer learning tutorial", "pytorch.org", PT_TRANSF),
            doc("torchvision modelləri", "pytorch.org", "https://pytorch.org/vision/stable/models.html"),
        ],
        [
            "ResNet18-i pretrained yüklə və fine-tune et",
            "Feature extraction rejimində dəqiqliyi ölç",
            "Data augmentation pipeline qur",
            "Augmentation-lı və olmayan təlimi müqayisə et",
        ],
        "Kiçik dataset üzərində 90%+ dəqiqlik əldə edən transfer learning modeli",
        [
            "Feature extraction ilə fine-tuning fərqi nədir?",
            "Niyə augmentation kiçik dataset-lərdə vacibdir?",
            "Hansı qatları dondurmaq lazımdır?",
        ],
    ),
    day(
        "CNN IV: modern arxitekturalar",
        [
            "LeNet, AlexNet, VGG, ResNet",
            "Residual connections (skip connections)",
            "Inception modulu və 1x1 konvolusiya",
            "EfficientNet və modern dizayn prinsipləri",
        ],
        [
            yt("ResNet və residual connections", "Yannic Kilcher", "30 d", "resnet paper explained residual connections"),
            yt("CNN arxitekturaları tarixçəsi", "DeepLearning.AI", "40 d", "cnn architectures evolution alexnet vgg resnet"),
        ],
        [
            doc("ResNet paper", "arxiv.org", "https://arxiv.org/abs/1512.03385"),
            doc("VGG paper", "arxiv.org", "https://arxiv.org/abs/1409.1556"),
        ],
        [
            "ResNet-in residual blokunu əl ilə yaz",
            "VGG ilə ResNet-i kiçik dataset-də müqayisə et",
            "Dərinlik artımının nəticəyə təsirini ölç",
            "Hər arxitekturanın parametr sayını cədvəldə yaz",
        ],
        "CNN arxitekturalarının müqayisə cədvəli + öz ResNet blokun",
        [
            "Residual connection hansı problemi həll edir?",
            "VGG niyə bu qədər parametrlidir?",
            "1x1 konvolusiya nə edir?",
        ],
    ),
    day(
        "Vizual modellərin izahı: feature maps və Grad-CAM",
        [
            "Konvolusiya qatlarının öyrəndikləri",
            "Feature map-ləri vizuallaşdırma",
            "Grad-CAM ilə modelin 'baxdığı' yerlər",
            "Embedding-lərin t-SNE ilə vizualizasiyasi",
        ],
        [
            yt("Grad-CAM izahı", "Yannic Kilcher", "25 d", "grad-cam paper explained"),
            yt("CNN nə öyrənir", "Krish Naik", "20 d", "what do cnns learn feature visualization"),
        ],
        [
            doc("KerasViz / Grad-CAM", "github.com/keisen", "https://github.com/jacobgil/pytorch-grad-cam"),
            gq("CNN feature visualization", "distill.pub", "feature visualization neural networks distill"),
        ],
        [
            "İlk konvolusiya qatının filter-lərini vizuallaşdır",
            "Grad-CAM istilik xəritəsi çək",
            "Model səhv edən şəkillərdə diqqəti yoxla",
            "Penultimate layer embedding-lərini t-SNE ilə göstər",
        ],
        "Model izahı: feature map + Grad-CAM + t-SNE toplusu",
        [
            "Model hara 'baxır' və niyə vacibdir?",
            "Səhv təsnifatların səbəbi nədir?",
            "Embedding fəzası nəyi göstərir?",
        ],
    ),
    day(
        "RNN I: ardıcıl data və təkrarlanan şəbəkələr",
        [
            "Ardıcıl data nədir (mətn, zaman seriyası)",
            "RNN quruluşu və hidden state",
            "Backpropagation through time (BPTT)",
            "Vanishing/exploding gradient problemi",
        ],
        [
            yt("Recurrent Neural Networks izahı", "StatQuest", "20 d", "statquest recurrent neural networks"),
            yt("RNN və BPTT", "Stanford CS224n", "50 d", "cs224n rnn language models lecture"),
        ],
        [
            doc("PyTorch: RNN", "pytorch.org", "https://pytorch.org/docs/stable/generated/torch.nn.RNN.html"),
            doc("Stanford CS224n", "stanford.edu", "https://web.stanford.edu/class/cs224n/"),
        ],
        [
            "Sadə RNN hüceyrəsini əl ilə hesabla",
            "PyTorch RNN ilə ardıcıl data üzərində proqnoz ver",
            "Gradient-lərin kiçilməsini müşahidə et",
            "Nəticələri bir abzasda izah et",
        ],
        "RNN nümunəsi + gradient problemi qeydi",
        [
            "Hidden state nə saxlayır?",
            "BPTT nədir?",
            "Vanishing gradient nə üçün problemdir?",
        ],
    ),
    day(
        "RNN II: LSTM və GRU",
        [
            "LSTM qapıları (input, forget, output)",
            "Cell state və uzunmüddətli yaddaş",
            "GRU: sadələşdirilmiş versiya",
            "Nə vaxt RNN/LSTM, nə vaxt Transformer",
        ],
        [
            yt("LSTM izahı", "StatQuest", "25 d", "statquest lstm long short term memory"),
            yt("LSTM və GRU arxitekturası", "Stanford CS224n", "45 d", "cs224n lstm gru lecture"),
        ],
        [
            doc("PyTorch: LSTM", "pytorch.org", "https://pytorch.org/docs/stable/generated/torch.nn.LSTM.html"),
            doc("Understanding LSTM Networks", "colah.github.io", "https://colah.github.io/posts/2015-08-Understanding-LSTMs/"),
        ],
        [
            "LSTM hüceyrəsini əl ilə bir addım hesabla",
            "PyTorch LSTM ilə mətn generasiyası et",
            "LSTM və GRU nəticələrini müqayisə et",
            "Parametr saylarını cədvəldə yaz",
        ],
        "LSTM/GRU müqayisəsi + mətn generasiyası nümunəsi",
        [
            "LSTM-də forget qapısı nə edir?",
            "GRU ilə LSTM fərqi nədir?",
            "Nə vaxt LSTM əvəzinə Transformer seçərdin?",
        ],
    ),
    day(
        "Seq2seq və attention mexanizmi",
        [
            "Encoder-decoder arxitekturası",
            "Seq2seq problemləri (uzun ardıcıllıqlar)",
            "Attention mexanizmi və onun intuisiya",
            "Attention-ın tərcümə keyfiyyətinə təsiri",
        ],
        [
            yt("Seq2seq və attention", "Stanford CS224n", "50 d", "cs224n attention seq2seq lecture"),
            yt("Attention izahı", "DeepLearning.AI", "30 d", "attention mechanism deeplearning ai"),
        ],
        [
            doc("PyTorch: seq2seq tutorial", "pytorch.org", PT_SEQ2SEQ),
            doc("Attention vizual izahı", "jalammar.github.io", "https://jalammar.github.io/visualizing-neural-machine-translation-mechanics-of-seq2seq-models-with-attention/"),
        ],
        [
            "Kiçik seq2seq modeli qur (rəqəm çevrilməsi kimi tapşırıq)",
            "Attention mexanizmini əlavə et",
            "Attention ağırlıqlarını vizuallaşdır",
            "Attention-sız versiya ilə müqayisə et",
        ],
        "İşləyən seq2seq + attention nümunəsi (attention xəritəsi ilə)",
        [
            "Attention hansı problemi həll edir?",
            "Encoder hidden state-ləri necə istifadə olunur?",
            "Attention niyə Transformer-in əsasıdır?",
        ],
    ),
    day(
        "Transformer I: self-attention",
        [
            "Self-attention mexanizmi (Q, K, V)",
            "Scaled dot-product attention",
            "Multi-head attention",
            "Positional encoding",
        ],
        [
            yt("Attention Is All You Need izahı", "Yannic Kilcher", "50 d", "yannic kilcher attention is all you need"),
            yt("Transformer vizual izahı", "3Blue1Brown", "25 d", "3blue1brown transformers attention"),
        ],
        [
            doc("Paper: Attention Is All You Need", "arxiv.org", "https://arxiv.org/abs/1706.03762"),
            doc("The Illustrated Transformer", "jalammar.github.io", ILLUSTRATED),
        ],
        [
            "Self-attention-ı NumPy ilə implement et",
            "Multi-head attention-ı kodla yaz",
            "Positional encoding funksiyasını çək",
            "Kiçik ardıcıllıq üzərində attention matrisini vizuallaşdır",
        ],
        "Sıfırdan yazılmış self-attention modulu (test ilə)",
        [
            "Q, K, V nədir?",
            "Niyə `sqrt(d_k)` ilə bölürük?",
            "Multi-head nə qazandırır?",
        ],
    ),
    day(
        "Transformer II: encoder-decoder və BERT/GPT",
        [
            "Transformer bloku (LayerNorm, residual, FFN)",
            "Encoder-only (BERT) vs decoder-only (GPT)",
            "Masked attention və causal mask",
            "Pretraining və fine-tuning fərqi",
        ],
        [
            yt("BERT izahı", "Yannic Kilcher", "35 d", "bert paper explained yannic kilcher"),
            yt("GPT arxitekturası izahı", "Andrej Karpathy", "2s", "karpathy let us build gpt"),
        ],
        [
            doc("BERT paper", "arxiv.org", "https://arxiv.org/abs/1810.04805"),
            doc("GPT-3 paper", "arxiv.org", "https://arxiv.org/abs/2005.14165"),
        ],
        [
            "Transformer blokunu tam yaz (attention + FFN + LayerNorm)",
            "Causal mask-ı implement et",
            "Encoder və decoder-only fərqini cədvəldə göstər",
            "Kiçik modeli mətn üzərində öyrət",
        ],
        "Kiçik, işləyən Transformer bloku (encoder və decoder variantları)",
        [
            "BERT və GPT hansı cəhətdən fərqlənir?",
            "Causal mask nə üçün lazımdır?",
            "LayerNorm nə edir?",
        ],
    ),
    day(
        "Transformer praktika: kiçik GPT qurmaq",
        [
            "Karpathy-nin nanoGPT yanaşması",
            "Tokenizer seçimi (character vs BPE)",
            "Kiçik dataset üzərində pretraining",
            "Mətn generasiyası və temperatur",
        ],
        [
            yt("Let us build GPT from scratch", "Andrej Karpathy", "2s", "karpathy let us build gpt from scratch"),
            yt("nanoGPT izahı", "Andrej Karpathy", "1s", "karpathy nanogpt explained"),
        ],
        [
            doc("nanoGPT repo", "github.com/karpathy", NANOGPT),
            doc("PyTorch transformer tutorial", "pytorch.org", PT_TRANSFORMER),
        ],
        [
            "nanoGPT kodunu oxu və əsas hissələri qeyd et",
            "Kiçik dataset üzərində modeli öyrət (Colab)",
            "Mətn generasiyası nümunələri çıxart",
            "Temperature dəyərini dəyişib nəticəni müqayisə et",
        ],
        "Öz kiçik GPT modeliniz + generasiya nümunələri",
        [
            "Tokenizer seçimi nəticəyə necə təsir edir?",
            "Kiçik model nə öyrəndi?",
            "Temperature nəyi dəyişir?",
        ],
    ),
    day(
        "Embedding-lər: sözdən vektora",
        [
            "Word2vec, GloVe, fastText",
            "Embedding fəzasının xassələri (analogiyalar)",
            "Contextual embedding-lər (ELMo, BERT)",
            "Sentence və document embedding-ləri",
        ],
        [
            yt("Word Embeddings izahı", "Stanford CS224n", "50 d", "cs224n word vectors word2vec lecture"),
            yt("Word2vec vizual izah", "StatQuest", "25 d", "statquest word embedding word2vec"),
        ],
        [
            doc("PyTorch: word embeddings tutorial", "pytorch.org", PT_WORD_EMB),
            doc("Illustrated Word2Vec", "jalammar.github.io", "https://jalammar.github.io/illustrated-word2vec/"),
        ],
        [
            "Kiçik korpus üzərində word2vec öyrət",
            "Ən yaxın qonşuları tap və yoxla",
            "Analoji tapşırığı sına (kral - kişi + qadın)",
            "BERT embedding-ləri ilə müqayisə et",
        ],
        "Embedding təcrübələri notebooku (analogiyalar ilə)",
        [
            "Embedding nədir?",
            "Word2vec ilə GloVe fərqi nədir?",
            "Contextual embedding niyə üstündür?",
        ],
    ),
    day(
        "Hugging Face ekosistemi",
        [
            "transformers, datasets, tokenizers, hub",
            "Pipeline API ilə sürətli istifadə",
            "Model və tokenizer yükləmə",
            "Model kartı oxumaq və seçim meyarları",
        ],
        [
            yt("Hugging Face kurs (bölmə 1-2)", "Hugging Face", "1s", "hugging face nlp course transformers"),
            yt("Hugging Face transformers ilk addımlar", "AssemblyAI", "30 d", "hugging face transformers tutorial beginners"),
        ],
        [
            doc("Hugging Face NLP kursu", "huggingface.co", HF_COURSE),
            doc("Transformers sənədləri", "huggingface.co", HF_TRANSFORMERS),
        ],
        [
            "Hugging Face hesabı yarat və token al",
            "Pipeline ilə 3 fərqli tapşırıq işlət",
            "Model kartlarını oxuyub 3 model müqayisə et",
            "Tokenizasiyanı əl ilə yoxla (token-id-lərə bax)",
        ],
        "Hugging Face pipeline nümunələri notebooku",
        [
            "Pipeline API nəyi qısaldır?",
            "Model kartında nəyə baxmaq lazımdır?",
            "Tokenizasiya nə üçün vacibdir?",
        ],
    ),
    day(
        "Pretrained modellərlə praktik tapşırıqlar",
        [
            "Sentiment analysis",
            "Named Entity Recognition (NER)",
            "Question answering / summarization",
            "Zero-shot klassifikasiya",
        ],
        [
            yt("NLP tapşırıqları transformers ilə", "AssemblyAI", "40 d", "hugging face nlp tasks sentiment ner"),
            yt("Zero-shot classification", "Hugging Face", "20 d", "zero shot classification transformers pipeline"),
        ],
        [
            doc("Hugging Face tapşırıqları", "huggingface.co", "https://huggingface.co/tasks"),
            doc("Datasets sənədləri", "huggingface.co", HF_DATASETS),
        ],
        [
            "4 fərqli NLP tapşırığını ardıcıl işlət",
            "Nəticələri birləşdirib mini API yaz (FastAPI ilə sonra baxacaqsan)",
            "Səhvləri analiz et (hansı cümlələrdə model yanıldı)",
            "Nəticələri markdown hesabatda yaz",
        ],
        "4 NLP tapşırığını birləşdirən nümunə + nəticə hesabatı",
        [
            "Hansı tapşırıq üçün hansı model tipi lazımdır?",
            "Model hansı nümunələrdə yanıldı?",
            "Nəticələri necə yaxşılaşdırmaq olar?",
        ],
    ),
    day(
        "Fine-tuning I: Trainer API",
        [
            "Dataset formatı (Hugging Face datasets)",
            "Tokenization pipeline və padding/truncation",
            "Trainer və TrainingArguments",
            "Metrikalar (f1, accuracy) ilə qiymətləndirmə",
        ],
        [
            yt("Fine-tuning transformers", "Hugging Face", "40 d", "hugging face fine tuning trainer tutorial"),
            yt("Trainer API ilə təlim", "Krish Naik", "35 d", "hugging face trainer api fine tune model"),
        ],
        [
            doc("Fine-tuning təlimatı", "huggingface.co", HF_TRANSFORMERS + "/training"),
            doc("Hugging Face LLM kursu", "huggingface.co", HF_LLM),
        ],
        [
            "Kiçik mətn dataseti seç və tokenizə et",
            "Trainer ilə modeli fine-tune et",
            "Metrikaları hesabla və əsas model ilə müqayisə et",
            "Modeli Hub-a yüklə",
        ],
        "Hub-da yayımlanmış fine-tuned model + nəticələr",
        [
            "Fine-tuning nə vaxt lazımdır?",
            "Padding və truncation nə üçün vacibdir?",
            "Trainer əsas təlim dövründən nəyi gizlədir?",
        ],
    ),
    day(
        "Fine-tuning II: PEFT, LoRA və kvantizasiya",
        [
            "Full fine-tuning-in dəyəri (yaddaş, vaxt)",
            "LoRA və adapter-lər",
            "Quantization (8-bit, 4-bit) və QLoRA",
            "Nə vaxt PEFT, nə vaxt full fine-tuning",
        ],
        [
            yt("LoRA izahı", "Yannic Kilcher", "30 d", "lora paper explained low rank adaptation"),
            yt("QLoRA ilə fine-tuning", "Trelis Research", "40 d", "qlora fine tune llm tutorial"),
        ],
        [
            doc("PEFT sənədləri", "huggingface.co", HF_PEFT),
            doc("Paper: LoRA", "arxiv.org", "https://arxiv.org/abs/2106.09685"),
        ],
        [
            "LoRA ilə kiçik modeli fine-tune et",
            "4-bit kvantizasiya ilə yaddaş istifadəsini ölç",
            "LoRA ilə full fine-tuning nəticələrini müqayisə et",
            "Xülasəni README-də yaz",
        ],
        "LoRA/QLoRA təcrübəsi + yaddaş/performans müqayisəsi",
        [
            "LoRA necə parametr sayını azaldır?",
            "Kvantizasiya nəyi dəyişir?",
            "PEFT nə vaxt zəruridir?",
        ],
    ),
    day(
        "LLM əsasları: tokenization, sampling, kontekst",
        [
            "Next-token prediction və dil modelləri",
            "Tokenization (BPE) detalları",
            "Sampling: temperature, top-k, top-p",
            "Kontekst pəncərəsi və onun məhdudiyyətləri",
        ],
        [
            yt("LLM-lər necə işləyir", "Andrej Karpathy", "1s", "karpathy intro to large language models"),
            yt("LLM əsasları: tokenizasiya və sampling", "Andrej Karpathy", "2s", "karpathy deep dive into llms"),
        ],
        [
            doc("Hugging Face LLM kursu", "huggingface.co", HF_LLM),
            doc("Tokenizer sənədləri", "huggingface.co", HF_TOKENIZERS),
        ],
        [
            "Mətni tokenlara böl və geri çevir",
            "Temperature/top-p ilə generasiya nəticələrini müqayisə et",
            "Kontekst limitini aşan nümunə yarat və xətanı gör",
            "Sampling strategiyalarını cədvəldə izah et",
        ],
        "Tokenizasiya + sampling təcrübələri notebooku",
        [
            "BPE niyə istifadə olunur?",
            "Temperature 0 nə deməkdir?",
            "Kontekst pəncərəsi nədir?",
        ],
    ),
    day(
        "Faza 5 layihəsi: deep learning modelinin tam dövriyyəsi",
        [
            "Model seçimi və arxitektura qərarı",
            "Təlim, qiymətləndirmə, izah",
            "Modelin saxlanması və yüklənməsi",
            "Nəticələrin təqdimatı",
        ],
        [
            yt("Deep learning layihəsini sondan başa aparmaq", "Daniel Bourke", "1s", "end to end deep learning project pytorch"),
            yt("Model deployment-a hazırlıq", "Krish Naik", "25 d", "prepare pytorch model for deployment"),
        ],
        [
            doc("PyTorch: model save/load", "pytorch.org", "https://pytorch.org/tutorials/beginner/saving_loading_models.html"),
            doc("Deep Learning with PyTorch (kitab)", "pytorch.org", "https://pytorch.org/assets/deep-learning/Deep-Learning-with-PyTorch.pdf"),
        ],
        [
            "Layihə üçün dataset və tapşırıq seç",
            "Ən azı 2 arxitektura sına və müqayisə et",
            "Ən yaxşı modeli saxla (state_dict)",
            "README-də nəticələr, qrafiklər və növbəti addımlar yaz",
        ],
        "GitHub-da `deep-learning-project` reposu (model + notebook + README)",
        [
            "Niyə bu arxitekturanı seçdin?",
            "Modelin məhdudiyyətləri nədir?",
            "Növbəti eksperiment nə olardı?",
        ],
    ),
]

weeks = [
    {
        "focus": "Neyron şəbəkə və PyTorch əsasları",
        "project": "PyTorch MLP: tabular dataset üzərində sıfırdan təlim dövrü, loss əyriləri və nəticə hesabatı",
        "quiz": "Backprop, PyTorch API, DataLoader və regulyarizasiya üzrə 10 sual",
    },
    {
        "focus": "Kompüter görmə (CNN)",
        "project": "CNN layihəsi: CIFAR-10-da transfer learning ilə 85%+ dəqiqlik + səhv analizi",
        "quiz": "Konvolusiya, pooling, ResNet və transfer learning üzrə 10 sual",
    },
    {
        "focus": "Ardıcıl modellər və Transformer",
        "project": "Transformer notebooku: kiçik dataset üzərində self-attention və mətn generasiyası",
        "quiz": "RNN, LSTM, attention və Transformer üzrə 10 sual",
    },
    {
        "focus": "Embedding, Hugging Face və LLM əsasları",
        "project": "Hugging Face layihəsi: pretrained modeli öz mətn datasetində fine-tune et və Hub-da yayımla",
        "quiz": "Embedding, tokenizasiya, fine-tuning və PEFT üzrə 10 sual",
    },
]

PHASE = phase(
    5,
    "Dərin öyrənmə: PyTorch, CNN, RNN, Transformer",
    "Şəbəkələri sıfırdan qurmaq, təlim etmək, debug etmək və müasir arxitekturaları anlamaq.",
    "72-82 saat",
    weeks,
    days,
)
