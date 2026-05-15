# TO-BE Architecture — PM AI Agent

## Overview

The PM AI Agent is designed as a modular AI-assisted project management system that supports project managers with task analysis, prioritization, risk detection, reporting, and Jira integration.

The system follows a layered architecture to ensure scalability, maintainability, and future AI expansion.

---

# Architecture Layers

## 1. Input Layer

Responsible for collecting project management data.

### Supported Inputs

- CSV task files
- Manual text input
- Jira tasks (via Jira REST API)

### Example Input Fields

- task name
- deadline
- owner
- dependency
- impact

---

## 2. LLM Layer

Handles AI-assisted processing.

### Responsibilities

- task understanding
- task generation from text
- prompt-based reasoning
- future OpenAI integration

The current MVP uses lightweight prompt-based logic and rule-based analysis.

---

## 3. Logic Layer

Core analytical layer of the system.

### Responsibilities

- task parsing
- priority scoring
- dependency analysis
- risk detection
- overload analysis

### Prioritization Rules

Priority is calculated based on:

- deadline proximity
- dependency existence
- task impact

### Risk Detection Rules

The system identifies:

- deadline risks
- blocked dependencies
- workload overload risks

---

## 4. Output Layer

Responsible for generating structured outputs.

### Outputs

- prioritized task lists
- risk summaries
- JSON reports
- CLI visualizations

Generated reports are exported into the REPORTS directory.

---

## 5. Jira Integration Layer

The system integrates with Jira Cloud using Jira REST API.

### Current Capabilities

- automatic Jira issue creation
- Jira task fetching
- project synchronization support

### Future Capabilities

- automatic comments
- automatic task assignment
- sprint automation
- semi-autonomous workflow execution

---

# Human vs AI Model

The system follows a human-in-the-loop model.

## AI Responsibilities

- analyze tasks
- detect risks
- prioritize work
- generate reports
- suggest actions

## Human Responsibilities

- validate outputs
- approve decisions
- manage execution

---

# Future Improvements

Planned future enhancements include:

- ML-based risk prediction
- Streamlit web interface
- Slack integration
- advanced analytics
- semi-autonomous Jira workflows

---

# Conclusion

The PM AI Agent MVP successfully demonstrates a working AI-assisted project management prototype with real Jira integration, risk analysis, prioritization, and reporting capabilities.