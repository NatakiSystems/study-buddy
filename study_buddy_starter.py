import os
import json
from dotenv import load_dotenv
from openai import OpenAI, OpenAIError

# ======================================
# PART 1: Project Setup & Initialization
# ======================================

# load variables from .env file
load_dotenv()

# Retrieve API key
api_key = os.getenv("DEEPSEEK_API_KEY")

# Initialize DeepSeek Client
client = OpenAI(
    api_key=api_key,
    base_url = "https://api.deepseek.com"
)

print("Setup successful! Client initialized.")

# ======================================
# PART 2: Role-Setting + Temperature Test
# ======================================

# 1. Define your tutor persona
SYSTEM_PROMPT = """
You are an experienced home inspector and tutor. You have a deep understanding of home inspection processes, techniques, and best practies. Your role is to guide and educate users on how to conduct thorough home inspections, identify potential issues, and provide recommendations for improvements. You are patient, knowledgeable, and able to explain complex concepts in a clear and concise manner. You should not provide legal or financial advice, but focus on the technical aspects of home inspections. Your goal is to help users become proficient in home inspection practices and ensure they can perform inspections with confidence and effectively.
"""

# 2. Define the question you want to test
USER_QUESTION = "What are the most common issues found during a home inspection, and how can they be addressed?"

# Function to run our test with a specific temperature
def test_temperature(temp_value):
    print(f"\n--- Testing with Termperature: {temp_value} ---")
    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_QUESTION}
        ],
        temperature=temp_value
    )
    print(response.choices[0].message.content)

# Run once at 0.2 and once at 0.9
test_temperature(0.2)
test_temperature(0.9)

# Shared Variables & Prompts for Part 3 & Part 4
SYSTEM_PROMPT = """
You are a helpful study buddy and an expert home inspector tutor. You MUST respond ONLY with valid JSON. Do not include markdown formatting or extra text.

The JSON output MUST contain exactly these three keys:
- "topic": string (the core topic being discussed)
- "explanation": string (a clear, brief explanation)
- "follow_up_question": string (a question to test the user's understanding)
"""

USER_QUESTION = "What should I look for when inspecting an electrical panel?"

# Part 2 Reflection starts at Line 145

# ==================================
# PART 3: Structured JSON Output
# ==================================

def get_structured_response_part3():
    print("\n--- Requesting JSON Output ---")

    response = client.chat.completions.create(
        model="deepseek-v4-flash",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT},
            {"role": "user", "content": USER_QUESTION}
        ],
        temperature=0.2,
        response_format={"type": "json_object"}
    )
    raw_content = response.choices[0].message.content

    data = json.loads(raw_content)

    print(f"\nTOPIC: {data['topic']}")
    print(f"\nEXPLANATION: {data['explanation']}")
    print(f'\nFOLLOW-UP QUESTION: {data['follow_up_question']}')

get_structured_response_part3()

# ================================
# PART 4: Error Handling
#=================================

def get_structured_response_part4():
    print("\n--- Requesting JSON Output ---")

    # 1. API Call with error handling (Part 4, Req 1)
    try:
        response = client.chat.completions.create(
            model="deepseek-v4-flash",
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": USER_QUESTION}
            ],
            temperature=0.2,
            response_format={"type": "json_object"}            
        )
    except OpenAIError as e:
        print(f"API Request Failed: {e}")
        return

    raw_content = response.choices[0].message.content

    # 2. JSON Parsing with single retry (Part 4, Req 2)
    try:
        data = json.loads(raw_content)
    except json.JSONDecodeError:
        print("Invalid JSON, retrying...")
        try:
            retry_response = client.chat.completions.create(
                model="deepseek-v4-flash",
                messages=[
                    {"role": "system", "content": SYSTEM_PROMPT},
                    {"role": "user", "content": USER_QUESTION}
                ],
                temperature=0.2,
                response_format={"type": "json_object"}
            )
            data = json.loads(retry_response.choices[0].message.content)
        except Exception:
            print("Failed to parse JSON after retry.")
            return
    
    # 3. Print individual fields if JSON parsing succeeded
    print(f"\nTOPIC: {data.get('topic')}")
    print(f"\nEXPLANATION: {data.get('explanation')}")
    print(f"\nFOLLOW-UP QUESTION: {data.get('follow_up_question')}")

# Call the function at the bottom of the script
get_structured_response_part4()

# Part 2: Role-Setting + Temperature Reflection: I honestly liked both responses so I am torn as to which one I prefer. The response at 0.2 was more structured and concise, providing clear and actionable advice on common issues found during home inspections. I loved the inspector tip provided after each system. It was easy to follow and the tone reminded me of the owner of the inspection organization I belong to. On the other hand, the response at 0.9 was more detailed, offering a broader range of insights and examples, which could be very helpful for someone looking to understand the nuances of home inspections. It actually used language that I would use in my home inspection reports, however, I didn't like the structure of the response as much as the 0.2 response. I think I would prefer to use the 0.2 response for my own learning and the 0.9 response for my clients, as it provides a more comprehensive overview of potential issues and solutions. Overall, both responses were valuable and provided useful information for anyone interested in home inspections.

# Before submitting, I reviewed and edited code using Gemini as my assistant to ensure I completed the assignment correctly. I did a final run and all sections were successful. 