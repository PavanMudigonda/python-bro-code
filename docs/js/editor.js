// Editor functionality
let currentQuestion = 1;
let currentLevel = 'beginner';
let startTime = null;
let questionsData = {}; // Will hold all 1000 questions

// Load questions data
async function initializeEditor() {
    try {
        const response = await fetch('data/questions.json');
        questionsData = await response.json();
        console.log('Loaded', Object.keys(questionsData).length, 'questions');
        
        // Now load the first question
        loadQuestion(currentQuestion);
    } catch (error) {
        console.error('Error loading questions:', error);
        // Fallback to default
        questionsData = {};
        // Still load the question with fallback data
        loadQuestion(currentQuestion);
    }
}

document.addEventListener('DOMContentLoaded', function() {
    // Get level and question from URL parameters
    const urlParams = new URLSearchParams(window.location.search);
    if (urlParams.has('level')) {
        currentLevel = urlParams.get('level');
    }
    if (urlParams.has('question')) {
        const questionParam = parseInt(urlParams.get('question'));
        if (questionParam >= 1 && questionParam <= 1000) {
            currentQuestion = questionParam;
        }
    }
    
    // Initialize editor and load questions
    initializeEditor();
    
    // Event listeners
    document.getElementById('run-code').addEventListener('click', runCode);
    document.getElementById('clear-code').addEventListener('click', clearCode);
    document.getElementById('save-code').addEventListener('click', saveCode);
    document.getElementById('mark-complete').addEventListener('click', markComplete);
    document.getElementById('prev-question').addEventListener('click', prevQuestion);
    document.getElementById('next-question').addEventListener('click', nextQuestion);
    document.getElementById('random-question').addEventListener('click', randomQuestion);
    document.getElementById('goto-question').addEventListener('click', gotoQuestion);
    document.getElementById('show-hints').addEventListener('click', toggleHints);
    document.getElementById('clear-output').addEventListener('click', clearOutput);
    
    // Enter key on question input
    document.getElementById('question-input').addEventListener('keypress', function(e) {
        if (e.key === 'Enter') {
            gotoQuestion();
        }
    });
    
    // Track start time
    startTime = Date.now();
});

function runCode() {
    const code = document.getElementById('code-editor').value.trim();
    const outputDiv = document.getElementById('output');
    const loadingDiv = document.getElementById('loading');
    const testResultsSection = document.getElementById('test-results');
    const testResultsContent = document.getElementById('test-results-content');
    
    if (!code) {
        outputDiv.innerHTML = '<div class="output-info">Please write some code first</div>';
        return;
    }
    
    // Check if Skulpt is loaded
    if (typeof Sk === 'undefined') {
        outputDiv.innerHTML = '<div class="output-info">⏳ Python runtime is loading... Please wait a moment and try again.</div>';
        return;
    }
    
    // Get current question data
    const questionData = questionsData[currentQuestion];
    
    if (questionData && questionData.testCases && questionData.testCases.length > 0) {
        // Run with test cases
        loadingDiv.style.display = 'block';
        outputDiv.innerHTML = '';
        testResultsSection.style.display = 'none';
        
        window.runPythonWithTests(code, questionData.testCases, questionData.functionName)
            .then(results => {
                loadingDiv.style.display = 'none';
                
                // Display test results
                displayTestResults(results);
                
                // Check if all tests passed
                const allPassed = results.every(r => r.passed);
                const markCompleteBtn = document.getElementById('mark-complete');
                
                if (allPassed) {
                    markCompleteBtn.disabled = false;
                    markCompleteBtn.title = 'All tests passed! Click to mark complete';
                } else {
                    markCompleteBtn.disabled = true;
                    markCompleteBtn.title = 'Pass all tests to enable';
                }
            })
            .catch(error => {
                loadingDiv.style.display = 'none';
                outputDiv.innerHTML = '<pre class="output-error"><strong>Error:</strong>\n' + error.toString() + '</pre>';
            });
    } else {
        // No test cases - run normally for output
        window.runPythonCode(code);
        // Enable mark complete button for questions without tests
        document.getElementById('mark-complete').disabled = false;
    }
}

function displayTestResults(results) {
    const testResultsSection = document.getElementById('test-results');
    const testResultsContent = document.getElementById('test-results-content');
    
    // Count results
    const passedCount = results.filter(r => r.passed).length;
    const totalCount = results.length;
    const visibleCount = results.filter(r => r.visible).length;
    const hiddenCount = totalCount - visibleCount;
    
    let html = '';
    
    // Summary
    if (passedCount === totalCount) {
        html += `<div class="test-summary all-passed">
            <i class="fas fa-check-circle"></i> All ${totalCount} tests passed! 🎉
        </div>`;
    } else {
        html += `<div class="test-summary some-failed">
            <i class="fas fa-times-circle"></i> ${passedCount}/${totalCount} tests passed
        </div>`;
    }
    
    // Individual test cases (only visible ones with details)
    results.forEach((result, index) => {
        if (result.visible) {
            const status = result.passed ? 'passed' : 'failed';
            const icon = result.passed ? 'fa-check' : 'fa-times';
            
            html += `<div class="test-case ${status}">
                <div class="test-case-header">
                    <span>Test Case ${index + 1}</span>
                    <span class="status ${status}">
                        <i class="fas ${icon}"></i>
                        ${result.passed ? 'Passed' : 'Failed'}
                    </span>
                </div>
                <div class="test-case-details">
                    <div><strong>Input:</strong> ${formatValue(result.input)}</div>
                    <div><strong>Expected:</strong> ${formatValue(result.expected)}</div>
                    ${!result.passed ? `<div><strong>Got:</strong> ${formatValue(result.actual)}</div>` : ''}
                    ${result.error ? `<div><strong>Error:</strong> ${result.error}</div>` : ''}
                </div>
            </div>`;
        }
    });
    
    // Hidden tests info
    if (hiddenCount > 0) {
        const hiddenPassed = results.filter((r, i) => !r.visible && r.passed).length;
        html += `<div class="hidden-test-info">
            <i class="fas fa-lock"></i> ${hiddenPassed}/${hiddenCount} hidden test(s) passed
        </div>`;
    }
    
    testResultsContent.innerHTML = html;
    testResultsSection.style.display = 'block';
}

function formatValue(value) {
    if (Array.isArray(value)) {
        return '[' + value.join(', ') + ']';
    } else if (typeof value === 'string') {
        return '"' + value + '"';
    } else if (value === null || value === undefined) {
        return String(value);
    } else {
        return String(value);
    }
}

function clearCode() {
    if (confirm('Clear all code? This cannot be undone.')) {
        document.getElementById('code-editor').value = '# Write your Python code here\n';
    }
}

function saveCode() {
    const code = document.getElementById('code-editor').value;
    const key = `code-${currentLevel}-${currentQuestion}`;
    localStorage.setItem(key, code);
    
    // Show success message
    const btn = document.getElementById('save-code');
    const originalText = btn.innerHTML;
    btn.innerHTML = '<i class="fas fa-check"></i> Saved!';
    btn.style.background = '#28a745';
    
    setTimeout(() => {
        btn.innerHTML = originalText;
        btn.style.background = '';
    }, 2000);
}

function markComplete() {
    const endTime = Date.now();
    const timeTaken = Math.floor((endTime - startTime) / 1000); // seconds
    
    const success = progressTracker.markQuestionComplete(
        currentQuestion, 
        currentLevel, 
        timeTaken
    );
    
    if (success) {
        const message = document.getElementById('completion-message');
        message.style.display = 'block';
        
        setTimeout(() => {
            message.style.display = 'none';
            nextQuestion();
        }, 2000);
    } else {
        alert('Question already completed!');
    }
}

function loadQuestion(questionNum) {
    currentQuestion = questionNum;
    
    // Update UI
    document.getElementById('question-number').textContent = `Question ${String(questionNum).padStart(3, '0')}`;
    
    // Set difficulty badge
    const badge = document.getElementById('question-difficulty');
    if (questionNum <= 100) {
        currentLevel = 'beginner';
        badge.textContent = 'Beginner';
        badge.className = 'badge badge-beginner';
    } else if (questionNum <= 300) {
        currentLevel = 'intermediate';
        badge.textContent = 'Intermediate';
        badge.className = 'badge badge-intermediate';
    } else if (questionNum <= 500) {
        currentLevel = 'advanced';
        badge.textContent = 'Advanced';
        badge.className = 'badge badge-advanced';
    } else if (questionNum <= 700) {
        currentLevel = 'expert';
        badge.textContent = 'Expert';
        badge.className = 'badge badge-expert';
    } else if (questionNum <= 900) {
        currentLevel = 'master';
        badge.textContent = 'Master';
        badge.className = 'badge badge-master';
    } else {
        currentLevel = 'challenge';
        badge.textContent = 'Challenge';
        badge.className = 'badge badge-challenge';
    }
    
    // Load question content from JSON
    const questionData = questionsData[questionNum];
    if (questionData) {
        document.getElementById('question-title').textContent = questionData.title;
        
        // Build description HTML
        let descriptionHTML = `<p>${questionData.description}</p>`;
        
        // Show visible test cases as examples
        if (questionData.testCases && questionData.testCases.length > 0) {
            const visibleTests = questionData.testCases.filter(t => t.visible);
            if (visibleTests.length > 0) {
                descriptionHTML += `<p><strong>Example Test Cases:</strong></p>`;
                visibleTests.forEach((test, idx) => {
                    descriptionHTML += `<pre><strong>Input:</strong> ${formatValue(test.input)}\n<strong>Output:</strong> ${formatValue(test.output)}</pre>`;
                });
                
                const hiddenCount = questionData.testCases.filter(t => !t.visible).length;
                if (hiddenCount > 0) {
                    descriptionHTML += `<p class="hidden-test-info"><i class="fas fa-lock"></i> Plus ${hiddenCount} hidden test case(s)</p>`;
                }
            }
        }
        
        document.getElementById('question-description').innerHTML = descriptionHTML;
        
        // Update hints
        if (questionData.hints && questionData.hints.length > 0) {
            let hintsHTML = '<ul>';
            questionData.hints.forEach(hint => {
                hintsHTML += `<li>${hint}</li>`;
            });
            hintsHTML += '</ul>';
            document.getElementById('hints-content').innerHTML = hintsHTML;
        }
        
        // Update meta info
        const metaHTML = `
            <div class="meta-item">
                <i class="fas fa-clock"></i>
                <span>Estimated: ${questionData.estimatedTime || 5} min</span>
            </div>
            <div class="meta-item">
                <i class="fas fa-tag"></i>
                <span>Tags: ${questionData.tags ? questionData.tags.join(', ') : 'practice'}</span>
            </div>
        `;
        document.querySelector('.question-meta').innerHTML = metaHTML;
    } else {
        // Fallback if question data not loaded
        document.getElementById('question-title').textContent = `Practice Question ${questionNum}`;
        document.getElementById('question-description').innerHTML = 
            `<p>Loading question details... If this persists, please refresh the page.</p>`;
    }
    
    // Load saved code if exists
    const savedCode = localStorage.getItem(`code-${currentLevel}-${questionNum}`);
    if (savedCode) {
        document.getElementById('code-editor').value = savedCode;
    } else {
        document.getElementById('code-editor').value = '# Write your Python code here\n';
    }
    
    // Clear output and test results
    clearOutput();
    document.getElementById('test-results').style.display = 'none';
    
    // Reset mark complete button
    document.getElementById('mark-complete').disabled = true;
    document.getElementById('mark-complete').title = 'Pass all tests to enable';
    
    // Reset start time
    startTime = Date.now();
    
    // Hide completion message
    document.getElementById('completion-message').style.display = 'none';
    
    // Reset hints to hidden
    const hints = document.getElementById('hints-content');
    hints.classList.remove('visible');
    document.getElementById('show-hints').innerHTML = '<i class="fas fa-lightbulb"></i> Show Hints';
}

function prevQuestion() {
    if (currentQuestion > 1) {
        loadQuestion(currentQuestion - 1);
    }
}

function nextQuestion() {
    if (currentQuestion < 1000) {
        loadQuestion(currentQuestion + 1);
    }
}

function gotoQuestion() {
    const input = document.getElementById('question-input');
    const questionNum = parseInt(input.value);
    
    console.log('Goto question:', questionNum, 'Questions loaded:', Object.keys(questionsData).length); // Debug log
    
    if (!questionNum || isNaN(questionNum)) {
        // No valid input
        return;
    }
    
    if (questionNum >= 1 && questionNum <= 1000) {
        // Check if questions are loaded
        if (Object.keys(questionsData).length === 0) {
            alert('Questions are still loading... Please wait a moment and try again.');
            return;
        }
        
        loadQuestion(questionNum);
        input.value = ''; // Clear input after loading
    } else {
        alert('Please enter a question number between 1 and 1000');
    }
}

function randomQuestion() {
    const random = Math.floor(Math.random() * 1000) + 1;
    loadQuestion(random);
}

function toggleHints() {
    const hints = document.getElementById('hints-content');
    hints.classList.toggle('visible');
    
    const btn = document.getElementById('show-hints');
    if (hints.classList.contains('visible')) {
        btn.innerHTML = '<i class="fas fa-eye-slash"></i> Hide Hints';
    } else {
        btn.innerHTML = '<i class="fas fa-lightbulb"></i> Show Hints';
    }
}

function clearOutput() {
    document.getElementById('output').innerHTML = 
        '<div class="output-placeholder">Click "Run Code" to see output here...</div>';
}
