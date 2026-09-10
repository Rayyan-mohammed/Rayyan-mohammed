<div align="center">

# Md Rayyan

**Machine Learning Engineer in training** — Applied ML Systems · Deep Learning · MLOps

Building ML systems that hold up past the notebook: a retrieval pipeline that checks its own claims, training infrastructure that survives cloud interruptions, and a diagnostic ML pipeline built specifically to avoid the data-leakage mistakes that inflate most student results.

[LinkedIn](https://www.linkedin.com/in/md-rayyan/) · [GitHub](https://github.com/Rayyan-mohammed) · [Email](mailto:rayyan1652@gmail.com) · Hyderabad, India

</div>

<br/>

## About

Final-year B.Tech CSE (Data Science) student at NMIMS University, Hyderabad (2023–2027). I spend more time in `model.py` and `docker-compose.yml` than in lecture slides.

My focus is applied ML engineering — not just training a model that scores well offline, but building the retrieval, evaluation, and serving layer around it that makes it trustworthy somewhere other than a notebook. Recent work spans retrieval-augmented generation with claim-level faithfulness checking, ML training infrastructure that survives AWS Spot interruptions, and a diagnostic pipeline built around getting cross-validation right.

I lead the **Code IT Club at NMIMS**, serve as a **Google Cloud Student Ambassador**, and was part of the winning team at **TechFest 2025**.

---

## Stack

| | |
|---|---|
| **AI / ML** | PyTorch · TensorFlow/Keras · scikit-learn · XGBoost · SHAP · HuggingFace Transformers |
| **LLM / RAG** | LangGraph · FAISS · ChromaDB · Claude API · claim verification pipelines |
| **Backend & Serving** | FastAPI · Flask · Streamlit · Next.js |
| **Cloud & Infrastructure** | AWS (EKS, EC2, Lambda, S3, IAM) · Kubernetes · Terraform · Docker · Google Cloud |
| **MLOps & Tooling** | GitHub Actions · Prometheus/Grafana · Git |

---

## Featured Projects

### 1. CodeSwitch-Verify — Faithfulness-Checked RAG
**[Repository](https://github.com/Rayyan-mohammed/HinglishRAG-Faith)**

RAG chatbots that answer Hinglish (Hindi-English) questions about Indian government welfare schemes generate fluent answers — but nothing checks whether each individual claim in that answer is actually supported by the source document. In a domain where a wrong eligibility condition or deadline has real consequences, that gap matters.

**What it does:** every generated answer is decomposed into atomic claims; each claim is independently re-retrieved against the source corpus and judged — supported / contradicted / unverifiable — by an LLM-as-judge using majority vote over 3 samples, instead of being trusted outright.

**Engineering:** `bge-m3` embeddings + FAISS retrieval · Claude Haiku 4.5 for generation, decomposition, and verification · scheme data pulled live from official `.gov.in` sources · design decisions tracked in ADRs.

`Python` `FAISS` `Claude API` `RAG`

---

### 2. BharatHealth Analyst — LLM Agent over National Health Survey Data
**[Repository](https://github.com/Rayyan-mohammed/aarogya-lens)**

India's NFHS-5 district health survey (706 districts × 448 indicators) is the kind of dataset that normally needs SQL and an analyst to query. Questions like *"which districts have the worst child anaemia"* shouldn't require that.

**What it does:** a LangGraph ReAct agent with 7 tools (semantic search, pandas/SQL query, charting, trend and correlation analysis) sits over a pipeline that merges NFHS-5 with historical NFHS-4 trend data for 62 indicators, indexed in ChromaDB.

**Engineering:** FastAPI backend (11 endpoints, rate limiting, request logging) · Next.js frontend · CI test suite at 93% API coverage.

**Where it honestly stands:** all 7 tools are verified end-to-end against a live LLM and the full stack runs. The one thing not yet proven is a complete accuracy benchmark — blocked twice by free-tier rate limits. Stating that plainly beats rounding it up.

`Python` `LangGraph` `FastAPI` `Next.js` `ChromaDB`

---

### 3. Parkinson's Detection via Acoustic Biomarkers
**[Repository](https://github.com/Rayyan-mohammed/Parkinson)**

Most student ML projects on medical audio data report inflated accuracy because of subject-level data leakage — recordings from the same patient end up on both sides of the train/test split.

**What it does:** strict subject-level `GroupKFold` cross-validation so no patient crosses the split, hyperparameter search bounded inside inner folds, and SMOTE balancing applied only within training folds.

**Engineering:** `wav2vec2` transformer embeddings (768-dim) alongside hand-crafted acoustic features · SHAP for global (beeswarm) and per-patient (waterfall) explainability · built for cross-corpus evaluation against a second, independent dataset.

**Result** (subject-isolated CV, reported with confidence intervals rather than one rounded number):

| Model | Accuracy | ROC-AUC |
|---|---|---|
| MLP | 0.756 ± 0.057 | 0.851 ± 0.116 |
| XGBoost | 0.760 ± 0.114 | 0.793 ± 0.204 |

`Python` `scikit-learn` `XGBoost` `SHAP` `HuggingFace`

---

### 4. Argus — Spot-Resilient ML Training Orchestrator *(team project)*
**[Repository](https://github.com/Rayyan-mohammed/Argus-Spot_Resilient_ML_Training_Orchestrator)**

AWS Spot instances are 70–90% cheaper than on-demand but can be reclaimed on 2 minutes' notice — a long training job that ignores this loses everything since its last checkpoint.

**What it does:** a Transformer predicts interruption risk from Spot price history; a Kubernetes operator (`kopf`) acts on that prediction to checkpoint and reschedule the training pod before the interruption lands; the job resumes automatically.

**Result:** validated on a real AWS EKS cluster — a live Spot drain was survived with a ~75-second recovery. A controlled 80-trial benchmark showed the predictive approach hit **zero wasted compute** vs. 202s with no protection, and recovered **~12× faster** than a purely reactive approach. Every claimed result ships with a documented "honest limitations" note rather than being oversold. Targeting a NeurIPS ML4Sys 2026 workshop poster.

**My part:** built with a teammate — I worked the orchestration/deployment side: Helm chart deployment, concurrent load/stress testing and cost analysis, and fixes to the risk-threshold logic.

`Kubernetes` `PyTorch` `FastAPI` `Terraform` `AWS EKS` `Prometheus/Grafana`

---

### 5. OptiPrice — Dynamic Pricing Engine
**[Repository](https://github.com/Rayyan-mohammed/OptiPrice)** · **[Live](https://optiprice-dynamic-pricing-agent.streamlit.app/)**

Retail pricing decisions are often static or purely rule-based, ignoring price elasticity, competitor movement, and margin trade-offs.

**What it does:** a constrained optimization engine (SciPy) that maximizes profit or revenue depending on objective, a Monte Carlo simulator modeling a 30-day forward A/B test under realistic demand volatility, and SHAP-based explainability so a pricing recommendation isn't a black box.

**Engineering:** live competitor pricing via the Mercado Libre API · batch CSV pipeline for pricing thousands of SKUs at once · deployed and publicly reachable.

`Python` `scikit-learn` `SciPy` `SHAP` `Streamlit`

---

## Additional Work

| Project | What it is | Stack |
|---|---|---|
| [ApplyForge](https://github.com/Rayyan-mohammed/ApplyForge) | Human-in-the-loop AI agent that discovers internships, ranks them against a resume, and drafts applications for review over Telegram. Deployed on EC2, running continuously. | Python · LLM agents |
| [DNA Sequence Compression](https://github.com/Rayyan-mohammed/DNA-sequence-compression) ([live](https://dna-sequence-compression.streamlit.app/)) | Genomic data compression via LZ77, Burrows-Wheeler Transform, and suffix trees, with live NCBI data pulls and 3D protein structure rendering. | Python · Streamlit |
| [Route Resilience](https://github.com/Rayyan-mohammed/Urban-Route-Resilience) *(team, ISRO hackathon)* | Occlusion-robust road extraction from satellite imagery (SegFormer) plus graph-theoretic network resilience analysis. | Python · PyTorch · NetworkX |
| [Traffic Sign Recognition](https://github.com/Rayyan-mohammed/Traffic-Sign-Recognition-System) | Real-time 43-class CNN traffic sign classifier with webcam inference. | TensorFlow/Keras · OpenCV · Streamlit |
| [Phishing URL Detector](https://github.com/Rayyan-mohammed/Phishing-Attack-Detection-System) | Random Forest classifier over 15+ URL features, served via Flask. | scikit-learn · Flask |

---

## How I approach ML problems

- **Leakage is the default failure mode.** The Parkinson's project exists specifically to get subject-level cross-validation right, because most student medical-ML projects don't.
- **An unverified result isn't a result.** Argus documents its limitations next to its wins. aarogya-lens says plainly which benchmark isn't finished instead of skipping it.
- **Explainability isn't optional.** SHAP shows up wherever a model makes a decision that needs to be justified — diagnosis, pricing.
- **Decisions get written down.** ADRs in CodeSwitch-Verify and Argus record *why* a design changed, not just what it is now.

---

## Currently exploring

- Production ML infrastructure — extending Argus toward real (not injected) Spot interruption testing
- Evaluation methodology for RAG and multi-agent LLM systems
- PyTorch and deep learning beyond transfer learning

---

<div align="center">

[LinkedIn](https://www.linkedin.com/in/md-rayyan/) · [GitHub](https://github.com/Rayyan-mohammed) · [Email](mailto:rayyan1652@gmail.com)

<br/>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/Rayyan-mohammed/Rayyan-mohammed/output/github-contribution-grid-snake-dark.svg" />
  <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/Rayyan-mohammed/Rayyan-mohammed/output/github-contribution-grid-snake.svg" />
  <img alt="" src="https://raw.githubusercontent.com/Rayyan-mohammed/Rayyan-mohammed/output/github-contribution-grid-snake.svg" width="80%" />
</picture>

</div>
