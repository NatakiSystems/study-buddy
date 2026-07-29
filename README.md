# AI Study Buddy: Home Inspection Tutor

An interactive Python application that leverages large language models (LLMs) to serve as an intelligent, dynamic study buddy for home inspection processes and best practices.

## Overview

This project was built to explore core AI engineering concepts, including system prompt engineering, temperature tuning, structured JSON outputs, robust error handling, and secure API key management.

The application acts as an expert home inspector tutor designed to guide users through inspection techniques, structural evaluation, electrical panels, and safety protocols-delivering concise, structured learning experiences.

___

## Features & Learning Milestones

* **Part 1: Secure Setup & Environment Management**
  * Environment configuration using 'python-dotenv' to isolate sensitive API credentials.
  * Local virtual environment isolation ('.venv').
  * '.gitignore' implementation to protect private keys from source control.

* **Part 2: Role-Setting & Temperature Reflections**
  * System prompt engineering defining an expert Home Inspector Tutor persona.
  * Temperature comparative testing (evaluating model behavior at '0.2' vs. '0.9').
  * Empirical reflection on response consistency versus creative variability for educational tools.

* **Part 3: Structured JSON**
  * Enforcing valid JSON output formatting directly from the API.
  * Key extraction and parsing for programmatic fields: 'topic', 'explanation', and 'follow_up_question'.
 
* **Part 4: Error Handling & Resilience**
  * Exception handling ('try/except') for network and API connection issues ('OpenAIError').
  * Single-retry parsing fallback on 'JSONDecodeError' to guarantee output integrity.
 
___

## Project Structure

'''text

study-buddy/
|-- .gitignore              # Ignores .env and virtual environment folders

|-- study_buddy_starty.py   # Main Python pipeline execution script

|-- README.md


The Knowledge House - AI Business Solutions Fellowship - Phase 2 Week 7 TLAB: Creating a Study Buddy using LLM
Author: Nataki Boykin IF 2026 
