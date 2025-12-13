#!/usr/bin/env python3
"""Generate questions.json with metadata for all 1000 practice questions"""

import json
import os

# Question templates for each difficulty level with test cases
templates = {
    'beginner': [
        {
            "title": "Hello World", 
            "desc": "Write a function that returns 'Hello World'", 
            "tags": ["basics", "functions"], 
            "time": 2,
            "function": "hello_world",
            "tests": [
                {"input": [], "output": "Hello World", "visible": True},
            ]
        },
        {
            "title": "Print Name", 
            "desc": "Write a function that takes a name and returns 'Hello, [name]!'", 
            "tags": ["basics", "strings"], 
            "time": 2,
            "function": "greet",
            "tests": [
                {"input": ["Alice"], "output": "Hello, Alice!", "visible": True},
                {"input": ["Bob"], "output": "Hello, Bob!", "visible": True},
                {"input": [""], "output": "Hello, !", "visible": False},
            ]
        },
        {
            "title": "Add Numbers", 
            "desc": "Write a function that adds two numbers", 
            "tags": ["arithmetic", "operators"], 
            "time": 3,
            "function": "add",
            "tests": [
                {"input": [2, 3], "output": 5, "visible": True},
                {"input": [10, 20], "output": 30, "visible": True},
                {"input": [-5, 5], "output": 0, "visible": False},
                {"input": [0, 0], "output": 0, "visible": False},
            ]
        },
        {
            "title": "Age Calculator", 
            "desc": "Write a function that calculates age given birth year", 
            "tags": ["arithmetic"], 
            "time": 5,
            "function": "calculate_age",
            "tests": [
                {"input": [2000], "output": 25, "visible": True},
                {"input": [1990], "output": 35, "visible": True},
                {"input": [2020], "output": 5, "visible": False},
            ]
        },
        {
            "title": "Rectangle Area", 
            "desc": "Write a function that calculates rectangle area", 
            "tags": ["arithmetic", "geometry"], 
            "time": 4,
            "function": "rectangle_area",
            "tests": [
                {"input": [5, 3], "output": 15, "visible": True},
                {"input": [10, 10], "output": 100, "visible": True},
                {"input": [7, 2], "output": 14, "visible": False},
            ]
        },
        {
            "title": "Temperature Converter", 
            "desc": "Write a function to convert Celsius to Fahrenheit", 
            "tags": ["arithmetic", "formulas"], 
            "time": 5,
            "function": "celsius_to_fahrenheit",
            "tests": [
                {"input": [0], "output": 32, "visible": True},
                {"input": [100], "output": 212, "visible": True},
                {"input": [-40], "output": -40, "visible": False},
            ]
        },
        {
            "title": "Circle Area", 
            "desc": "Write a function to calculate circle area (use 3.14159 for pi)", 
            "tags": ["arithmetic", "math"], 
            "time": 4,
            "function": "circle_area",
            "tests": [
                {"input": [1], "output": 3.14159, "visible": True},
                {"input": [5], "output": 78.53975, "visible": True},
                {"input": [10], "output": 314.159, "visible": False},
            ]
        },
        {
            "title": "Even or Odd", 
            "desc": "Write a function that returns 'even' or 'odd'", 
            "tags": ["conditionals", "modulo"], 
            "time": 5,
            "function": "even_or_odd",
            "tests": [
                {"input": [4], "output": "even", "visible": True},
                {"input": [7], "output": "odd", "visible": True},
                {"input": [0], "output": "even", "visible": False},
                {"input": [-3], "output": "odd", "visible": False},
            ]
        },
        {
            "title": "Max of Two", 
            "desc": "Write a function that returns the maximum of two numbers", 
            "tags": ["conditionals", "comparison"], 
            "time": 4,
            "function": "max_of_two",
            "tests": [
                {"input": [5, 10], "output": 10, "visible": True},
                {"input": [20, 15], "output": 20, "visible": True},
                {"input": [7, 7], "output": 7, "visible": False},
            ]
        },
        {
            "title": "Absolute Value", 
            "desc": "Write a function that returns absolute value", 
            "tags": ["conditionals", "math"], 
            "time": 4,
            "function": "absolute",
            "tests": [
                {"input": [5], "output": 5, "visible": True},
                {"input": [-5], "output": 5, "visible": True},
                {"input": [0], "output": 0, "visible": False},
            ]
        },
    ],
    'intermediate': [
        {"title": "List Sum", "desc": "Write a function that returns sum of all numbers in a list", "tags": ["lists", "loops"], "time": 10,
         "function": "list_sum", "tests": [{"input": [[1,2,3]], "output": 6, "visible": True}, {"input": [[10,20,30]], "output": 60, "visible": True}, {"input": [[]], "output": 0, "visible": False}]},
        {"title": "Reverse String", "desc": "Write a function that reverses a string", "tags": ["strings", "methods"], "time": 8,
         "function": "reverse_string", "tests": [{"input": ["hello"], "output": "olleh", "visible": True}, {"input": ["Python"], "output": "nohtyP", "visible": True}, {"input": [""], "output": "", "visible": False}]},
        {"title": "Count Vowels", "desc": "Write a function that counts vowels in a string", "tags": ["strings", "loops"], "time": 10,
         "function": "count_vowels", "tests": [{"input": ["hello"], "output": 2, "visible": True}, {"input": ["aeiou"], "output": 5, "visible": True}, {"input": ["xyz"], "output": 0, "visible": False}]},
        {"title": "Factorial", "desc": "Write a function that calculates factorial", "tags": ["recursion", "math"], "time": 12,
         "function": "factorial", "tests": [{"input": [5], "output": 120, "visible": True}, {"input": [0], "output": 1, "visible": True}, {"input": [10], "output": 3628800, "visible": False}]},
        {"title": "Fibonacci", "desc": "Write a function that returns nth Fibonacci number", "tags": ["recursion", "algorithms"], "time": 10,
         "function": "fibonacci", "tests": [{"input": [5], "output": 5, "visible": True}, {"input": [10], "output": 55, "visible": True}, {"input": [15], "output": 610, "visible": False}]},
        {"title": "Is Palindrome", "desc": "Write a function that checks if a string is a palindrome", "tags": ["strings", "algorithms"], "time": 15,
         "function": "is_palindrome", "tests": [{"input": ["radar"], "output": True, "visible": True}, {"input": ["hello"], "output": False, "visible": True}, {"input": ["A man a plan a canal Panama"], "output": False, "visible": False}]},
        {"title": "Prime Check", "desc": "Write a function that checks if a number is prime", "tags": ["math", "algorithms"], "time": 12,
         "function": "is_prime", "tests": [{"input": [7], "output": True, "visible": True}, {"input": [10], "output": False, "visible": True}, {"input": [2], "output": True, "visible": False}]},
        {"title": "List Max", "desc": "Write a function that finds maximum in a list", "tags": ["lists", "algorithms"], "time": 10,
         "function": "find_max", "tests": [{"input": [[1,5,3]], "output": 5, "visible": True}, {"input": [[10,2,8]], "output": 10, "visible": True}, {"input": [[-5,-1,-10]], "output": -1, "visible": False}]},
        {"title": "Remove Duplicates", "desc": "Write a function that removes duplicates from a list", "tags": ["lists", "sets"], "time": 15,
         "function": "remove_duplicates", "tests": [{"input": [[1,2,2,3]], "output": [1,2,3], "visible": True}, {"input": [[5,5,5]], "output": [5], "visible": True}, {"input": [[]], "output": [], "visible": False}]},
        {"title": "Word Count", "desc": "Write a function that counts words in a string", "tags": ["strings", "dictionaries"], "time": 12,
         "function": "word_count", "tests": [{"input": ["hello world"], "output": 2, "visible": True}, {"input": ["one"], "output": 1, "visible": True}, {"input": [""], "output": 0, "visible": False}]},
    ],
    'advanced': [
        {"title": "Binary Search", "desc": "Implement binary search algorithm", "tags": ["algorithms", "search"], "time": 20,
         "function": "binary_search", "tests": [{"input": [[1,2,3,4,5], 3], "output": 2, "visible": True}, {"input": [[1,2,3,4,5], 6], "output": -1, "visible": True}, {"input": [[], 1], "output": -1, "visible": False}]},
        {"title": "Merge Sort", "desc": "Implement merge sort algorithm", "tags": ["algorithms", "sorting"], "time": 25,
         "function": "merge_sort", "tests": [{"input": [[3,1,4,1,5]], "output": [1,1,3,4,5], "visible": True}, {"input": [[5,4,3,2,1]], "output": [1,2,3,4,5], "visible": True}, {"input": [[]], "output": [], "visible": False}]},
        {"title": "LCS Length", "desc": "Find longest common subsequence length", "tags": ["dp", "algorithms"], "time": 15,
         "function": "lcs_length", "tests": [{"input": ["ABCD", "ACDF"], "output": 3, "visible": True}, {"input": ["ABC", "XYZ"], "output": 0, "visible": True}, {"input": ["", "ABC"], "output": 0, "visible": False}]},
        {"title": "Valid Parentheses", "desc": "Check if parentheses are balanced", "tags": ["stack", "strings"], "time": 15,
         "function": "valid_parentheses", "tests": [{"input": ["()"], "output": True, "visible": True}, {"input": ["()[]{}" ], "output": True, "visible": True}, {"input": ["(]"], "output": False, "visible": False}]},
        {"title": "Two Sum", "desc": "Find two numbers that add up to target", "tags": ["arrays", "hash-table"], "time": 18,
         "function": "two_sum", "tests": [{"input": [[2,7,11,15], 9], "output": [0,1], "visible": True}, {"input": [[3,2,4], 6], "output": [1,2], "visible": True}, {"input": [[3,3], 6], "output": [0,1], "visible": False}]},
        {"title": "Max Subarray Sum", "desc": "Find maximum subarray sum (Kadane's algorithm)", "tags": ["dp", "arrays"], "time": 20,
         "function": "max_subarray_sum", "tests": [{"input": [[-2,1,-3,4,-1,2,1,-5,4]], "output": 6, "visible": True}, {"input": [[1]], "output": 1, "visible": True}, {"input": [[5,4,-1,7,8]], "output": 23, "visible": False}]},
        {"title": "Coin Change", "desc": "Find minimum coins needed for amount", "tags": ["dp", "greedy"], "time": 25,
         "function": "coin_change", "tests": [{"input": [[1,2,5], 11], "output": 3, "visible": True}, {"input": [[2], 3], "output": -1, "visible": True}, {"input": [[1], 0], "output": 0, "visible": False}]},
        {"title": "Longest Palindrome", "desc": "Find longest palindromic substring", "tags": ["strings", "dp"], "time": 20,
         "function": "longest_palindrome", "tests": [{"input": ["babad"], "output": "bab", "visible": True}, {"input": ["cbbd"], "output": "bb", "visible": True}, {"input": ["a"], "output": "a", "visible": False}]},
        {"title": "DFS Graph", "desc": "Implement depth-first search", "tags": ["graphs", "dfs"], "time": 25,
         "function": "dfs", "tests": [{"input": [{0:[1,2], 1:[2], 2:[0,3], 3:[3]}, 2], "output": [2,0,1,3], "visible": True}]},
        {"title": "BFS Graph", "desc": "Implement breadth-first search", "tags": ["graphs", "bfs"], "time": 30,
         "function": "bfs", "tests": [{"input": [{0:[1,2], 1:[2], 2:[0,3], 3:[3]}, 2], "output": [2,0,3,1], "visible": True}]},
    ],
    'expert': [
        {"title": "LRU Cache", "desc": "Implement LRU cache with O(1) operations", "tags": ["data-structures", "design"], "time": 40,
         "function": "LRUCache", "tests": [{"input": ["put", 1, 1], "output": None, "visible": True}]},
        {"title": "Trie Implementation", "desc": "Implement a Trie (prefix tree)", "tags": ["data-structures", "trees"], "time": 35,
         "function": "Trie", "tests": [{"input": ["insert", "apple"], "output": None, "visible": True}]},
        {"title": "Dijkstra's Algorithm", "desc": "Find shortest path in weighted graph", "tags": ["graphs", "algorithms"], "time": 45,
         "function": "dijkstra", "tests": [{"input": [{0:{1:4,2:1}, 1:{3:1}, 2:{1:2,3:5}, 3:{}}, 0, 3], "output": 4, "visible": True}]},
        {"title": "Regex Matcher", "desc": "Implement regex pattern matching", "tags": ["strings", "algorithms"], "time": 30,
         "function": "is_match", "tests": [{"input": ["aa", "a"], "output": False, "visible": True}, {"input": ["aa", "a*"], "output": True, "visible": True}]},
        {"title": "Serialize Binary Tree", "desc": "Serialize and deserialize binary tree", "tags": ["trees", "serialization"], "time": 35,
         "function": "serialize", "tests": []},
        {"title": "Word Ladder", "desc": "Find shortest transformation sequence", "tags": ["bfs", "strings"], "time": 30,
         "function": "ladder_length", "tests": [{"input": ["hit", "cog", ["hot","dot","dog","lot","log","cog"]], "output": 5, "visible": True}]},
        {"title": "Median Finder", "desc": "Find median from data stream", "tags": ["heaps", "design"], "time": 35,
         "function": "MedianFinder", "tests": []},
        {"title": "N-Queens", "desc": "Solve N-Queens problem", "tags": ["backtracking", "algorithms"], "time": 35,
         "function": "solve_n_queens", "tests": [{"input": [4], "output": 2, "visible": True}]},
        {"title": "Edit Distance", "desc": "Calculate minimum edit distance", "tags": ["dp", "strings"], "time": 40,
         "function": "min_distance", "tests": [{"input": ["horse", "ros"], "output": 3, "visible": True}]},
        {"title": "Sudoku Solver", "desc": "Solve Sudoku puzzle", "tags": ["backtracking", "algorithms"], "time": 40,
         "function": "solve_sudoku", "tests": []},
    ],
    'master': [
        {"title": "Expression Evaluator", "desc": "Build mathematical expression evaluator", "tags": ["parsers", "algorithms"], "time": 60,
         "function": "evaluate", "tests": [{"input": ["2+3*4"], "output": 14, "visible": True}]},
        {"title": "Memory Allocator", "desc": "Implement custom memory allocator", "tags": ["memory", "systems"], "time": 50,
         "function": "malloc", "tests": []},
        {"title": "Task Scheduler", "desc": "Implement CPU task scheduler", "tags": ["scheduling", "algorithms"], "time": 45,
         "function": "schedule", "tests": []},
        {"title": "B-Tree", "desc": "Implement B-tree data structure", "tags": ["trees", "databases"], "time": 55,
         "function": "BTree", "tests": []},
        {"title": "PageRank", "desc": "Implement PageRank algorithm", "tags": ["graphs", "algorithms"], "time": 60,
         "function": "page_rank", "tests": []},
        {"title": "Neural Network", "desc": "Implement basic neural network", "tags": ["ml", "ai"], "time": 50,
         "function": "NeuralNetwork", "tests": []},
        {"title": "SHA-256", "desc": "Implement SHA-256 hash function", "tags": ["crypto", "algorithms"], "time": 55,
         "function": "sha256", "tests": []},
        {"title": "Inverted Index", "desc": "Build inverted index for search", "tags": ["search", "data-structures"], "time": 50,
         "function": "InvertedIndex", "tests": []},
        {"title": "JIT Compiler", "desc": "Build simple JIT compiler", "tags": ["compilers", "optimization"], "time": 45,
         "function": "compile_and_run", "tests": []},
        {"title": "Garbage Collector", "desc": "Implement mark-and-sweep GC", "tags": ["memory", "systems"], "time": 55,
         "function": "gc_collect", "tests": []},
    ],
    'challenge': [
        {"title": "Traveling Salesman", "desc": "Solve TSP with dynamic programming", "tags": ["dp", "graphs"], "time": 45,
         "function": "tsp", "tests": [{"input": [[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]], "output": 80, "visible": True}]},
        {"title": "Shortest Code", "desc": "Solve FizzBuzz in under 50 characters", "tags": ["golf", "optimization"], "time": 30,
         "function": "fizzbuzz", "tests": [{"input": [15], "output": "FizzBuzz", "visible": True}]},
        {"title": "Alien Dictionary", "desc": "Derive order from alien language", "tags": ["graphs", "topological-sort"], "time": 40,
         "function": "alien_order", "tests": [{"input": [["wrt","wrf","er","ett","rftt"]], "output": "wertf", "visible": True}]},
        {"title": "Skyline Problem", "desc": "Find city skyline from buildings", "tags": ["heaps", "algorithms"], "time": 50,
         "function": "get_skyline", "tests": []},
        {"title": "Palindrome Partitioning", "desc": "Minimum cuts for palindrome partitioning", "tags": ["dp", "strings"], "time": 35,
         "function": "min_cut", "tests": [{"input": ["aab"], "output": 1, "visible": True}]},
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
            "description": f"{template['desc']}. Write a function named `{template['function']}` that solves this problem.",
            "functionName": template['function'],
            "testCases": template['tests'],
            "hints": [
                "Break down the problem into smaller steps",
                "Test your code with different inputs",
                "Make sure to name your function correctly"
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
            "description": f"{template['desc']}. Write a function named `{template['function']}` that solves this problem.",
            "functionName": template['function'],
            "testCases": template['tests'],
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
            "description": f"{template['desc']}. Write a function named `{template['function']}` that solves this problem.",
            "functionName": template['function'],
            "testCases": template['tests'],
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
            "description": f"{template['desc']}. Write a function or class named `{template['function']}` that solves this problem.",
            "functionName": template['function'],
            "testCases": template['tests'],
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
            "description": f"{template['desc']}. Write a function or class named `{template['function']}` that solves this problem.",
            "functionName": template['function'],
            "testCases": template['tests'],
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
            "description": f"{template['desc']}. Write a function named `{template['function']}` that solves this problem.",
            "functionName": template['function'],
            "testCases": template['tests'],
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
