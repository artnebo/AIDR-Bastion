import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import styles from './index.module.css';

type FeatureItem = {
  title: string;
  icon: string;
  description: JSX.Element;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Multi-Pipeline Detection',
    icon: '🔍',
    description: (
      <>
        Regex patterns, ML models, vector-based similarity detection, and 
        LLM-based analysis working together for comprehensive protection.
      </>
    ),
  },
  {
    title: 'Flexible Configuration',
    icon: '⚙️',
    description: (
      <>
        Dynamic pipeline configuration via JSON. Customize detection flows 
        for your specific use cases.
      </>
    ),
  },
  {
    title: 'Real-time Analysis',
    icon: '⚡',
    description: (
      <>
        Fast async processing with configurable thresholds. Analyze prompts 
        in milliseconds without impacting user experience.
      </>
    ),
  },
  {
    title: 'Industry-Aligned',
    icon: '🎯',
    description: (
      <>
        Detection logic aligns with MITRE ATLAS and OWASP Top 10 for LLMs, 
        ensuring standardized coverage.
      </>
    ),
  },
  {
    title: 'Extensible Architecture',
    icon: '🔧',
    description: (
      <>
        Simple plugin system for custom pipelines. Add your own detection 
        logic seamlessly.
      </>
    ),
  },
  {
    title: 'Event Logging',
    icon: '📊',
    description: (
      <>
        Kafka integration for scalable event streaming. Monitor and analyze 
        security events in real-time.
      </>
    ),
  },
];

function Feature({title, icon, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <div className={styles.featureIcon}>{icon}</div>
      </div>
      <div className="text--center padding-horiz--md">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </div>
  );
}

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className={styles.neonLines}>
        <div className={styles.neonLine1}></div>
        <div className={styles.neonLine2}></div>
      </div>
      <div className="container">
        <div className={styles.heroContent}>
          <div className={styles.heroLeft}>
            <div className={styles.logoContainer}>
              <img 
                src="/AIDR-Bastion/img/aidr-bastion-logo.png" 
                alt="AIDR Bastion" 
                className={styles.logo}
                loading="eager"
                decoding="async"
              />
            </div>
          </div>
          <div className={styles.heroRight}>
            <h1 className={styles.heroTitle}>{siteConfig.title}</h1>
            <p className={styles.heroSubtitle}>{siteConfig.tagline}</p>
            <div className={styles.badges}>
              <span className={styles.badge}>Python 3.12</span>
              <span className={styles.badge}>FastAPI</span>
              <span className={styles.badge}>LGPL-3.0</span>
            </div>
            <div className={styles.buttons}>
              <Link
                className="button button--primary button--lg"
                to="/docs/intro">
                Get Started →
              </Link>
              <Link
                className="button button--outline button--secondary button--lg"
                to="/docs/installation"
                style={{marginLeft: '1rem'}}>
                Installation Guide
              </Link>
            </div>
          </div>
        </div>
      </div>
    </header>
  );
}

function HomepageFeatures() {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}

function ArchitectureSection() {
  return (
    <section className={styles.architectureSection}>
      <div className="container">
        <h2 className={styles.sectionTitle}>System Architecture</h2>
        <p className={styles.sectionSubtitle}>
          Layered detection approach with multiple specialized pipelines
        </p>
        <div className={styles.architectureDiagram}>
          <pre className={styles.diagram}>
{`┌────────────────────────────────┐
│   FastAPI Endpoint             │
│   (POST /api/v1/run_pipeline)  │
└──────────────┬─────────────────┘
               │
               ▼
      ┌─────────────────────┐
      │  Pipeline Manager   │
      └─────────┬───────────┘
                │
                ▼
      ┌──────────────────────────────┐
      │          Pipelines           │
      │ ┌──────────────────────────┐ │
      │ │  Regex Pipeline          │ │
      │ ├──────────────────────────┤ │
      │ │  Similarity Pipeline     │ │
      │ ├──────────────────────────┤ │
      │ │  Code Analysis Pipeline  │ │
      │ ├──────────────────────────┤ │
      │ │  ML Pipeline             │ │
      │ ├──────────────────────────┤ │
      │ │  LLM (OpenAI) Pipeline   │ │
      │ └──────────────────────────┘ │
      └──────────────────────────────┘`}
          </pre>
        </div>
      </div>
    </section>
  );
}

function CodeExampleSection() {
  return (
    <section className={styles.codeSection}>
      <div className="container">
        <h2>Quick Start Example</h2>
        <p>Integrate AIDR Bastion with just a few lines of code</p>
        
        <div className={styles.codeBlock}>
          <pre>
{`import requests

# Run pipeline analysis
response = requests.post(
    "http://localhost:8000/api/v1/run_pipeline",
    json={
        "prompt": "Your text to analyze",
        "pipeline_flow": "full_scan"
    }
)

result = response.json()
print(f"Status: {result['status']}")  # allow, block, or notify
print(f"Triggered rules: {result['result']}")`}
          </pre>
        </div>

        <div className={styles.buttons}>
          <Link
            className="button button--primary button--lg"
            to="/docs/usage">
            View Full Documentation
          </Link>
        </div>
      </div>
    </section>
  );
}

function RuleSupportSection() {
  return (
    <section className={styles.ruleSection}>
      <div className="container">
        <h2 className={styles.sectionTitle}>Comprehensive Rule Support</h2>
        <p className={styles.sectionSubtitle}>
          Industry-standard detection rules and frameworks for comprehensive security coverage
        </p>
        <div className="row">
          <div className="col col--6">
            <div className={styles.ruleCard}>
              <h3>🔐 Roota & Sigma Rules</h3>
              <p>
                Support for industry-standard detection rules from SigmaHQ 
                (1,200+ free community rules) and SOC Prime (3,000+ additional rules).
              </p>
            </div>
          </div>
          <div className="col col--6">
            <div className={styles.ruleCard}>
              <h3>🔄 Uncoder AI Integration</h3>
              <p>
                Translate Sigma rules into Semgrep format for standardized 
                and reusable detection pipelines.
              </p>
            </div>
          </div>
        </div>
        <div className="row" style={{marginTop: '2rem'}}>
          <div className="col col--6">
            <div className={styles.ruleCard}>
              <h3>🎯 MITRE ATLAS Aligned</h3>
              <p>
                Detection logic aligns with MITRE ATLAS framework for 
                adversarial machine learning.
              </p>
            </div>
          </div>
          <div className="col col--6">
            <div className={styles.ruleCard}>
              <h3>📋 OWASP Top 10 for LLMs</h3>
              <p>
                Coverage against OWASP Top 10 vulnerabilities specific 
                to Large Language Models.
              </p>
            </div>
          </div>
        </div>
      </div>
    </section>
  );
}

function BuiltWithSection() {
  return (
    <section className={styles.builtWithSection}>
      <div className="container">
        <h2 className={styles.sectionTitle}>Built With</h2>
        <div className={styles.techStack}>
          <div className={styles.techItem}>
            <img src="/AIDR-Bastion/img/tech-logos/fastapi.svg" alt="FastAPI" className={styles.techLogo} />
            <span>FastAPI</span>
          </div>
          <div className={styles.techItem}>
            <img src="/AIDR-Bastion/img/tech-logos/opensearch.svg" alt="OpenSearch" className={styles.techLogo} />
            <span>OpenSearch</span>
          </div>
          <div className={styles.techItem}>
            <img src="/AIDR-Bastion/img/tech-logos/openai.svg" alt="OpenAI" className={styles.techLogo} />
            <span>OpenAI</span>
          </div>
          <div className={styles.techItem}>
            <img src="/AIDR-Bastion/img/tech-logos/semgrep.svg" alt="Semgrep" className={styles.techLogo} />
            <span>Semgrep</span>
          </div>
          <div className={styles.techItem}>
            <img src="/AIDR-Bastion/img/tech-logos/huggingface.svg" alt="Sentence Transformers" className={styles.techLogo} />
            <span>Sentence Transformers</span>
          </div>
          <div className={styles.techItem}>
            <img src="/AIDR-Bastion/img/tech-logos/kafka.svg" alt="Kafka" className={styles.techLogo} />
            <span>Kafka</span>
          </div>
          <div className={styles.techItem}>
            <img src="/AIDR-Bastion/img/tech-logos/pydantic.svg" alt="Pydantic" className={styles.techLogo} />
            <span>Pydantic</span>
          </div>
          <div className={styles.techItem}>
            <img src="/AIDR-Bastion/img/tech-logos/uvicorn.svg" alt="Uvicorn" className={styles.techLogo} />
            <span>Uvicorn</span>
          </div>
        </div>
        <p className={styles.inspiration}>
          Inspired by <a href="https://meta-llama.github.io/PurpleLlama/LlamaFirewall/" target="_blank" rel="noopener noreferrer">LlamaFirewall</a>
        </p>
      </div>
    </section>
  );
}

export default function Home(): JSX.Element {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title="Home"
      description="A comprehensive GenAI protection system designed to safeguard against malicious prompts, injection attacks, and harmful content">
      <HomepageHeader />
      <hr className={styles.sectionDivider} />
      <main>
        <HomepageFeatures />
        <hr className={styles.sectionDivider} />
        <ArchitectureSection />
        <hr className={styles.sectionDivider} />
        <RuleSupportSection />
        <hr className={styles.sectionDivider} />
        <CodeExampleSection />
        <hr className={styles.sectionDivider} />
        <BuiltWithSection />
      </main>
    </Layout>
  );
}



