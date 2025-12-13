#!/usr/bin/env python3
"""Generate questions.json with metadata for all 1000 practice questions"""

import json
import os

# Question templates for each difficulty level
templates = {
    'beginner': [
        {"title": "Hello World", "desc": "Print 'Hello World' to console", "tags": ["basics", "print"], "time": 2},
        {"title": "Print Name", "desc": "Print your name to console", "tags": ["basics", "print"], "time": 2},
        {"title": "Add Numbers", "desc": "Add two numbers and print result", "tags": ["arithmetic", "operators"], "time": 3},
        {"title": "Age Calculator", "desc": "Calculate age from birth year", "tags": ["input", "arithmetic"], "time": 5},
        {"title": "Rectangle Area", "desc": "Calculate area of rectangle", "tags": ["arithmetic", "variables"], "time": 4},
        {"title": "Temperature Converter", "desc": "Convert Celsius to Fahrenheit", "tags": ["arithmetic", "formulas"], "time": 5},
        {"title": "Circle Area", "desc": "Calculate area of circle", "tags": ["arithmetic", "math"], "time": 4},
        {"title": "Even or Odd", "desc": "Check if number is even or odd", "tags": ["conditionals", "modulo"], "time": 5},
        {"title": "Max of Two", "desc": "Find maximum of two numbers", "tags": ["conditionals", "comparison"], "time": 4},
        {"title": "Absolute Value", "desc": "Calculate absolute value of number", "tags": ["conditionals", "math"], "time": 4},
    ],
    'intermediate': [
        {"title": "List Operations", "desc": "Perform operations on lists", "tags": ["lists", "data-structures"], "time": 10},
        {"title": "String Manipulation", "desc": "Manipulate and transform strings", "tags": ["strings", "methods"], "time": 8},
        {"title": "Dictionary Tasks", "desc": "Work with Python dictionaries", "tags": ["dictionaries", "data-structures"], "time": 10},
        {"title": "Function Design", "desc": "Create reusable functions", "tags": ["functions", "design"], "time": 12},
        {"title": "Loop Patterns", "desc": "Implement various loop patterns", "tags": ["loops", "iteration"], "time": 10},
        {"title": "File Operations", "desc": "Read and write files", "tags": ["files", "io"], "time": 15},
        {"title": "Error Handling", "desc": "Handle exceptions properly", "tags": ["exceptions", "error-handling"], "time": 12},
        {"title": "List Comprehension", "desc": "Use list comprehensions", "tags": ["lists", "comprehensions"], "time": 10},
        {"title": "Class Design", "desc": "Design basic classes", "tags": ["oop", "classes"], "time": 15},
        {"title": "Recursion", "desc": "Solve problems recursively", "tags": ["recursion", "algorithms"], "time": 12},
    ],
    'advanced': [
        {"title": "Algorithm Design", "desc": "Design efficient algorithms", "tags": ["algorithms", "optimization"], "time": 20},
        {"title": "Data Structure Implementation", "desc": "Implement custom data structures", "tags": ["data-structures", "algorithms"], "time": 25},
        {"title": "Decorators", "desc": "Create and use decorators", "tags": ["decorators", "functions"], "time": 15},
        {"title": "Generators", "desc": "Work with generators and iterators", "tags": ["generators", "iteration"], "time": 15},
        {"title": "Context Managers", "desc": "Implement context managers", "tags": ["context-managers", "with"], "time": 18},
        {"title": "Metaclasses", "desc": "Work with metaclasses", "tags": ["metaclasses", "oop"], "time": 20},
        {"title": "Async Programming", "desc": "Write asynchronous code", "tags": ["async", "concurrency"], "time": 25},
        {"title": "Design Patterns", "desc": "Implement design patterns", "tags": ["patterns", "design"], "time": 20},
        {"title": "Graph Algorithms", "desc": "Solve graph problems", "tags": ["graphs", "algorithms"], "time": 25},
        {"title": "Dynamic Programming", "desc": "Apply dynamic programming", "tags": ["dp", "algorithms"], "time": 30},
    ],
    'expert': [
        {"title": "System Design", "desc": "Design scalable systems", "tags": ["system-design", "architecture"], "time": 40},
        {"title": "Advanced Algorithms", "desc": "Implement complex algorithms", "tags": ["algorithms", "optimization"], "time": 35},
        {"title": "Distributed Systems", "desc": "Design distributed systems", "tags": ["distributed", "systems"], "time": 45},
        {"title": "Database Design", "desc": "Design database schemas", "tags": ["database", "design"], "time": 30},
        {"title": "API Design", "desc": "Design RESTful APIs", "tags": ["api", "design"], "time": 35},
        {"title": "Caching Strategies", "desc": "Implement caching systems", "tags": ["caching", "performance"], "time": 30},
        {"title": "Load Balancing", "desc": "Implement load balancing", "tags": ["load-balancing", "systems"], "time": 35},
        {"title": "Message Queues", "desc": "Work with message queues", "tags": ["queues", "async"], "time": 35},
        {"title": "Microservices", "desc": "Design microservices", "tags": ["microservices", "architecture"], "time": 40},
        {"title": "Cryptography", "desc": "Implement cryptographic algorithms", "tags": ["crypto", "security"], "time": 40},
    ],
    'master': [
        {"title": "Compiler Design", "desc": "Design language compilers", "tags": ["compilers", "parsers"], "time": 60},
        {"title": "OS Internals", "desc": "Understand OS internals", "tags": ["os", "systems"], "time": 50},
        {"title": "Network Protocols", "desc": "Implement network protocols", "tags": ["networking", "protocols"], "time": 45},
        {"title": "Database Internals", "desc": "Understand database internals", "tags": ["database", "internals"], "time": 55},
        {"title": "Quantum Computing", "desc": "Quantum algorithms", "tags": ["quantum", "algorithms"], "time": 60},
        {"title": "Machine Learning", "desc": "ML algorithm implementation", "tags": ["ml", "ai"], "time": 50},
        {"title": "Blockchain", "desc": "Blockchain implementation", "tags": ["blockchain", "crypto"], "time": 55},
        {"title": "Search Engines", "desc": "Build search engines", "tags": ["search", "algorithms"], "time": 50},
        {"title": "Code Optimization", "desc": "Advanced code optimization", "tags": ["optimization", "performance"], "time": 45},
        {"title": "Security Systems", "desc": "Design security systems", "tags": ["security", "systems"], "time": 55},
    ],
    'challenge': [
        {"title": "Competitive Programming", "desc": "Solve competitive programming challenges", "tags": ["competitive", "algorithms"], "time": 45},
        {"title": "Code Golf", "desc": "Solve problems in minimal code", "tags": ["golf", "optimization"], "time": 30},
        {"title": "Algorithm Challenges", "desc": "Solve complex algorithm challenges", "tags": ["algorithms", "challenges"], "time": 40},
        {"title": "System Optimization", "desc": "Optimize complex systems", "tags": ["optimization", "systems"], "time": 50},
        {"title": "Brain Teasers", "desc": "Solve programming brain teasers", "tags": ["puzzles", "logic"], "time": 35},
    ],
}

def generate_questions():
    questions = {}
    q_num = 1
    
    # Beginner (1-100)
    for i in range(100):
        template = templates['beginner'][i % len(templates['beginner'])]
        questions[str(q_num)] = {
            "title": f"{template['title']} #{i+1}",
            "description": f"{template['desc']}. Practice problem {i+1} at beginner level.",
            "example": "Check the question file for examples and test cases.",
            "hints": [
                "Break down the problem into smaller steps",
                "Test your code with different inputs",
                "Use print statements to debug"
            ],
            "tags": template['tags'],
            "difficulty": "beginner",
            "estimatedTime": template['time']
        }
        q_num += 1
    
    # Intermediate (101-300)
    for i in range(200):
        template = templates['intermediate'][i % len(templates['intermediate'])]
        questions[str(q_num)] = {
            "title": f"{template['title']} #{i+1}",
            "description": f"{template['desc']}. Practice problem {i+1} at intermediate level.",
            "example": "Check the question file for examples and test cases.",
            "hints": [
                "Consider edge cases",
                "Think about time and space complexity",
                "Write clean, readable code"
            ],
            "tags": template['tags'],
            "difficulty": "intermediate",
            "estimatedTime": template['time']
        }
        q_num += 1
    
    # Advanced (301-500)
    for i in range(200):
        template = templates['advanced'][i % len(templates['advanced'])]
        questions[str(q_num)] = {
            "title": f"{template['title']} #{i+1}",
            "description": f"{template['desc']}. Practice problem {i+1} at advanced level.",
            "example": "Check the question file for examples and test cases.",
            "hints": [
                "Analyze the problem thoroughly",
                "Consider algorithmic optimization",
                "Write comprehensive tests"
            ],
            "tags": template['tags'],
            "difficulty": "advanced",
            "estimatedTime": template['time']
        }
        q_num += 1
    
    # Expert (501-700)
    for i in range(200):
        template = templates['expert'][i % len(templates['expert'])]
        questions[str(q_num)] = {
            "title": f"{template['title']} #{i+1}",
            "description": f"{template['desc']}. Practice problem {i+1} at expert level.",
            "example": "Check the question file for examples and test cases.",
            "hints": [
                "Think about scalability and performance",
                "Consider distributed systems concepts",
                "Design for fault tolerance"
            ],
            "tags": template['tags'],
            "difficulty": "expert",
            "estimatedTime": template['time']
        }
        q_num += 1
    
    # Master (701-900)
    for i in range(200):
        template = templates['master'][i % len(templates['master'])]
        questions[str(q_num)] = {
            "title": f"{template['title']} #{i+1}",
            "description": f"{template['desc']}. Practice problem {i+1} at master level.",
            "example": "Check the question file for examples and test cases.",
            "hints": [
                "Deep dive into system internals",
                "Consider low-level optimizations",
                "Study academic papers if needed"
            ],
            "tags": template['tags'],
            "difficulty": "master",
            "estimatedTime": template['time']
        }
        q_num += 1
    
    # Challenge (901-1000)
    for i in range(100):
        template = templates['challenge'][i % len(templates['challenge'])]
        questions[str(q_num)] = {
            "title": f"{template['title']} #{i+1}",
            "description": f"{template['desc']}. Practice problem {i+1} at challenge level.",
            "example": "Check the question file for examples and test cases.",
            "hints": [
                "Think creatively and outside the box",
                "Try multiple approaches",
                "Learn from failed attempts"
            ],
            "tags": template['tags'],
            "difficulty": "challenge",
            "estimatedTime": template['time']
        }
        q_num += 1
    
    return questions

if __name__ == "__main__":
    print("Generating questions.json with 1000 questions...")
    questions = generate_questions()
    
    # Save to docs/data/questions.json
    output_path = os.path.join(os.path.dirname(__file__), "docs", "data", "questions.json")
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    
    with open(output_path, 'w') as f:
        json.dump(questions, f, indent=2)
    
    print(f"✅ Generated {len(questions)} questions!")
    print(f"📝 Saved to {output_path}")
